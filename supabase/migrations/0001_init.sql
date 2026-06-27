-- Code Quest — schema inicial (perfis, currículo, progresso, widgets) + RLS + RPCs
-- ===== Enums =====
create type tool_kind as enum ('scratch','piskel','magicvoxel','roblox');
create type lesson_status as enum ('not_started','in_progress','completed');
create type user_role as enum ('student','tutor');

-- ===== profiles (1:1 com auth.users) =====
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null default '',
  avatar text not null default U&'\2665',
  role user_role not null default 'student',
  theme text default 'comfy',
  coins integer not null default 0,
  streak integer not null default 0,
  last_active date,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- ===== currículo =====
create table public.modules (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  description text default '',
  tool tool_kind,
  position integer not null default 0,
  is_published boolean not null default true,
  created_at timestamptz not null default now()
);

create table public.lessons (
  id uuid primary key default gen_random_uuid(),
  module_id uuid not null references public.modules(id) on delete cascade,
  title text not null,
  description text default '',
  tool tool_kind,
  position integer not null default 0,
  content text default '',
  external_url text,
  reward_coins integer not null default 20,
  is_published boolean not null default true,
  created_at timestamptz not null default now()
);

create table public.lesson_progress (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  lesson_id uuid not null references public.lessons(id) on delete cascade,
  status lesson_status not null default 'not_started',
  completed_at timestamptz,
  updated_at timestamptz not null default now(),
  unique (student_id, lesson_id)
);

-- ===== widgets do hub migrados pra nuvem =====
create table public.missions (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  text text not null,
  done boolean not null default false,
  rewarded boolean not null default false,
  day date not null default ((now() at time zone 'America/Fortaleza')::date),
  created_at timestamptz not null default now()
);

create table public.projects (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  title text not null,
  description text default '',
  color integer not null default 0,
  created_at timestamptz not null default now()
);

create index on public.lessons(module_id, position);
create index on public.lesson_progress(student_id);
create index on public.missions(student_id, day);
create index on public.projects(student_id);

-- ===== helpers / triggers =====
create or replace function public.is_tutor() returns boolean
  language sql security definer stable set search_path = public as
$$ select exists(select 1 from public.profiles where id = auth.uid() and role = 'tutor') $$;

create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, role)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'display_name',''),
    coalesce((new.raw_user_meta_data->>'role')::user_role,'student')
  );
  return new;
end $$;

create trigger on_auth_user_created
  after insert on auth.users for each row execute function public.handle_new_user();

-- ===== RPCs (autoridade das moedas) =====
create or replace function public.complete_lesson(p_lesson_id uuid)
returns void language plpgsql security definer set search_path = public as $$
declare v_reward integer; v_already boolean;
begin
  select status = 'completed' into v_already
    from public.lesson_progress where student_id = auth.uid() and lesson_id = p_lesson_id;
  insert into public.lesson_progress (student_id, lesson_id, status, completed_at)
    values (auth.uid(), p_lesson_id, 'completed', now())
  on conflict (student_id, lesson_id)
    do update set status='completed', completed_at=now(), updated_at=now();
  if v_already is distinct from true then
    select reward_coins into v_reward from public.lessons where id = p_lesson_id;
    update public.profiles set coins = coins + coalesce(v_reward,0), updated_at = now() where id = auth.uid();
  end if;
end $$;

create or replace function public.complete_mission(p_id uuid, p_done boolean default true)
returns void language plpgsql security definer set search_path = public as $$
declare v_owner uuid; v_rewarded boolean;
begin
  select student_id, rewarded into v_owner, v_rewarded from public.missions where id = p_id;
  if v_owner is distinct from auth.uid() then raise exception 'not allowed'; end if;
  update public.missions set done = p_done where id = p_id;
  if p_done and v_rewarded is distinct from true then
    update public.missions set rewarded = true where id = p_id;
    update public.profiles set coins = coins + 10, updated_at = now() where id = auth.uid();
  end if;
end $$;

create or replace function public.award_focus_coins()
returns integer language plpgsql security definer set search_path = public as $$
begin
  update public.profiles set coins = coins + 20, updated_at = now() where id = auth.uid();
  return (select coins from public.profiles where id = auth.uid());
end $$;

-- ===== RLS =====
alter table public.profiles        enable row level security;
alter table public.modules         enable row level security;
alter table public.lessons         enable row level security;
alter table public.lesson_progress enable row level security;
alter table public.missions        enable row level security;
alter table public.projects        enable row level security;

create policy "profiles_select" on public.profiles for select using (id = auth.uid() or public.is_tutor());
create policy "profiles_tutor_update" on public.profiles for update using (public.is_tutor()) with check (public.is_tutor());

create policy "modules_read" on public.modules for select using (is_published or public.is_tutor());
create policy "modules_tutor_all" on public.modules for all using (public.is_tutor()) with check (public.is_tutor());
create policy "lessons_read" on public.lessons for select using (is_published or public.is_tutor());
create policy "lessons_tutor_all" on public.lessons for all using (public.is_tutor()) with check (public.is_tutor());

create policy "progress_select" on public.lesson_progress for select using (student_id = auth.uid() or public.is_tutor());
create policy "progress_write_own" on public.lesson_progress for all using (student_id = auth.uid()) with check (student_id = auth.uid());

create policy "missions_own" on public.missions for all using (student_id = auth.uid()) with check (student_id = auth.uid());
create policy "missions_tutor_read" on public.missions for select using (public.is_tutor());
create policy "projects_own" on public.projects for all using (student_id = auth.uid()) with check (student_id = auth.uid());
create policy "projects_tutor_read" on public.projects for select using (public.is_tutor());

-- ===== grants (RLS continua valendo) =====
grant usage on schema public to anon, authenticated;
grant select, insert, update, delete on all tables in schema public to authenticated;
grant execute on all functions in schema public to authenticated;
