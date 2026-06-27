-- Guarda o email no perfil (pra listar alunos no painel do tutor)
alter table public.profiles add column if not exists email text;
update public.profiles p set email = u.email from auth.users u where u.id = p.id and (p.email is null or p.email = '');

create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, display_name, role, email)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'display_name',''),
    coalesce((new.raw_user_meta_data->>'role')::user_role,'student'),
    new.email
  );
  return new;
end $$;
revoke execute on function public.handle_new_user() from anon, authenticated;
