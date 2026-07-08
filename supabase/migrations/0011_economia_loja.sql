-- 0011_economia_loja.sql
-- Economia do Code Quest: CodeCoin (coins, já existente) + CodeGem (gems).
-- Loja (shop_items), inventário (inventory) e extrato auditável (wallet_tx).
-- Prêmios idempotentes por RPC security definer (ref único por aluno):
--   página do material -> +1 coin | material 100% -> +1 gem
--   atividade prática  -> +5 coins | atividade de inglês -> +5 coins
--   desafio concluído  -> +2 gems (e marca a aula como concluída)
-- Admin (tutor): presentear/retirar coins e gems com motivo registrado.

alter table public.profiles add column if not exists gems integer not null default 0;

create table if not exists public.shop_items (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  description text not null default '',
  category text not null check (category in ('colecionavel','roupa','emblema')),
  rarity text not null default 'comum' check (rarity in ('comum','raro','epico','lendario')),
  price_coins integer not null default 0 check (price_coins >= 0),
  price_gems integer not null default 0 check (price_gems >= 0),
  icon text not null default '',
  is_active boolean not null default true,
  position integer not null default 0,
  created_at timestamptz not null default now()
);

create table if not exists public.inventory (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  item_id uuid not null references public.shop_items(id) on delete cascade,
  equipped boolean not null default false,
  acquired_at timestamptz not null default now(),
  unique (student_id, item_id)
);

create table if not exists public.wallet_tx (
  id uuid primary key default gen_random_uuid(),
  student_id uuid not null references auth.users(id) on delete cascade,
  delta_coins integer not null default 0,
  delta_gems integer not null default 0,
  reason text not null default '',
  ref text,
  created_by uuid,
  created_at timestamptz not null default now()
);
create unique index if not exists wallet_tx_ref_uniq on public.wallet_tx (student_id, ref) where ref is not null;
create index if not exists wallet_tx_student on public.wallet_tx (student_id, created_at desc);

-- ---------- núcleo idempotente (não exposto ao cliente) ----------
create or replace function public.cq_award(p_ref text, p_coins int, p_gems int, p_reason text)
returns boolean language plpgsql security definer set search_path = public as $$
declare v_new boolean := false;
begin
  insert into public.wallet_tx (student_id, delta_coins, delta_gems, reason, ref, created_by)
    values (auth.uid(), p_coins, p_gems, p_reason, p_ref, auth.uid())
  on conflict (student_id, ref) where ref is not null do nothing;
  if found then
    v_new := true;
    update public.profiles
       set coins = coins + p_coins, gems = gems + p_gems, updated_at = now()
     where id = auth.uid();
  end if;
  return v_new;
end $$;
revoke execute on function public.cq_award(text,int,int,text) from public, anon, authenticated;

-- ---------- prêmios do aluno ----------
create or replace function public.award_page(p_lesson_id uuid, p_page int)
returns boolean language plpgsql security definer set search_path = public as $$
begin
  if p_page is null or p_page < 0 or p_page > 80 then return false; end if;
  if not exists (select 1 from public.lessons where id = p_lesson_id and is_published) then return false; end if;
  return public.cq_award('page:'||p_lesson_id||':'||p_page, 1, 0, 'Página do material');
end $$;

create or replace function public.award_material(p_lesson_id uuid)
returns boolean language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from public.lessons where id = p_lesson_id and is_published) then return false; end if;
  return public.cq_award('material:'||p_lesson_id, 0, 1, 'Material 100% concluído');
end $$;

create or replace function public.award_activity(p_lesson_id uuid, p_kind text)
returns boolean language plpgsql security definer set search_path = public as $$
begin
  if p_kind not in ('pratica','english') then return false; end if;
  if not exists (select 1 from public.lessons where id = p_lesson_id and is_published) then return false; end if;
  return public.cq_award(p_kind||':'||p_lesson_id, 5, 0,
    case p_kind when 'pratica' then 'Atividade prática' else 'Atividade de inglês' end);
end $$;

create or replace function public.finish_challenge(p_lesson_id uuid)
returns boolean language plpgsql security definer set search_path = public as $$
declare v_new boolean;
begin
  if not exists (select 1 from public.lessons where id = p_lesson_id and is_published) then return false; end if;
  insert into public.lesson_progress (student_id, lesson_id, status, completed_at)
    values (auth.uid(), p_lesson_id, 'completed', now())
  on conflict (student_id, lesson_id)
    do update set status='completed', completed_at=now(), updated_at=now();
  v_new := public.cq_award('desafio:'||p_lesson_id, 0, 2, 'Desafio concluído');
  return v_new;
end $$;

-- ---------- loja ----------
create or replace function public.buy_item(p_item_id uuid)
returns text language plpgsql security definer set search_path = public as $$
declare v_item public.shop_items; v_coins int; v_gems int;
begin
  select * into v_item from public.shop_items where id = p_item_id and is_active;
  if v_item.id is null then return 'item_indisponivel'; end if;
  if exists (select 1 from public.inventory where student_id = auth.uid() and item_id = p_item_id) then
    return 'ja_possui';
  end if;
  select coins, gems into v_coins, v_gems from public.profiles where id = auth.uid();
  if v_coins < v_item.price_coins or v_gems < v_item.price_gems then return 'saldo_insuficiente'; end if;
  update public.profiles
     set coins = coins - v_item.price_coins, gems = gems - v_item.price_gems, updated_at = now()
   where id = auth.uid();
  insert into public.wallet_tx (student_id, delta_coins, delta_gems, reason, ref, created_by)
    values (auth.uid(), -v_item.price_coins, -v_item.price_gems, 'Compra: '||v_item.name, 'buy:'||p_item_id, auth.uid());
  insert into public.inventory (student_id, item_id) values (auth.uid(), p_item_id);
  return 'ok';
end $$;

create or replace function public.set_equipped(p_item_id uuid, p_on boolean)
returns void language plpgsql security definer set search_path = public as $$
begin
  update public.inventory set equipped = p_on
   where student_id = auth.uid() and item_id = p_item_id;
end $$;

-- ---------- admin (tutor): presentear / retirar ----------
create or replace function public.admin_adjust_wallet(p_student uuid, p_coins int, p_gems int, p_reason text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not public.is_tutor() then raise exception 'apenas_tutor'; end if;
  if coalesce(p_coins,0) = 0 and coalesce(p_gems,0) = 0 then return; end if;
  update public.profiles
     set coins = greatest(0, coins + coalesce(p_coins,0)),
         gems  = greatest(0, gems + coalesce(p_gems,0)),
         updated_at = now()
   where id = p_student and role = 'student';
  if found then
    insert into public.wallet_tx (student_id, delta_coins, delta_gems, reason, ref, created_by)
      values (p_student, coalesce(p_coins,0), coalesce(p_gems,0),
              coalesce(nullif(trim(p_reason),''),'Ajuste do professor'), null, auth.uid());
  end if;
end $$;

-- ---------- permissões ----------
revoke execute on function public.award_page(uuid,int) from public, anon;
revoke execute on function public.award_material(uuid) from public, anon;
revoke execute on function public.award_activity(uuid,text) from public, anon;
revoke execute on function public.finish_challenge(uuid) from public, anon;
revoke execute on function public.buy_item(uuid) from public, anon;
revoke execute on function public.set_equipped(uuid,boolean) from public, anon;
revoke execute on function public.admin_adjust_wallet(uuid,int,int,text) from public, anon;

grant execute on function public.award_page(uuid,int) to authenticated;
grant execute on function public.award_material(uuid) to authenticated;
grant execute on function public.award_activity(uuid,text) to authenticated;
grant execute on function public.finish_challenge(uuid) to authenticated;
grant execute on function public.buy_item(uuid) to authenticated;
grant execute on function public.set_equipped(uuid,boolean) to authenticated;
grant execute on function public.admin_adjust_wallet(uuid,int,int,text) to authenticated;

-- ---------- RLS ----------
alter table public.shop_items enable row level security;
alter table public.inventory enable row level security;
alter table public.wallet_tx enable row level security;

drop policy if exists "shop_read" on public.shop_items;
create policy "shop_read" on public.shop_items for select using (is_active or public.is_tutor());
drop policy if exists "shop_tutor_all" on public.shop_items;
create policy "shop_tutor_all" on public.shop_items for all using (public.is_tutor()) with check (public.is_tutor());

drop policy if exists "inv_read" on public.inventory;
create policy "inv_read" on public.inventory for select using (student_id = auth.uid() or public.is_tutor());

drop policy if exists "tx_read" on public.wallet_tx;
create policy "tx_read" on public.wallet_tx for select using (student_id = auth.uid() or public.is_tutor());

grant select on public.shop_items, public.inventory, public.wallet_tx to authenticated;
