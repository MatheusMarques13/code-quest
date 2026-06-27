-- Tira a trigger function da API e bloqueia as funções de moeda para anon.
revoke execute on function public.handle_new_user() from anon, authenticated;
revoke execute on function public.complete_lesson(uuid) from anon;
revoke execute on function public.complete_mission(uuid, boolean) from anon;
revoke execute on function public.award_focus_coins() from anon;
