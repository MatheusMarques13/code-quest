-- Conteúdo estruturado da aula (material / recursos / desafio / inglês) em JSONB
alter table public.lessons add column if not exists body jsonb not null default '{}'::jsonb;
