-- 0012_seed_loja.sql
-- Itens iniciais da loja (ícones SVG em assets/shop/). Idempotente por nome.

create unique index if not exists shop_items_name_uniq on public.shop_items (name);

insert into public.shop_items (name, description, category, rarity, price_coins, price_gems, icon, position) values
  ('Cubo Voxel', 'Um voxel de estimação, direto do MagicaVoxel.', 'colecionavel', 'comum', 20, 0, 'assets/shop/cubo_voxel.svg', 1),
  ('Poção de XP', 'Borbulha conhecimento puro. Não beber de verdade.', 'colecionavel', 'comum', 18, 0, 'assets/shop/pocao_xp.svg', 2),
  ('Disquete Dourado', 'O botão de salvar dos tempos antigos, banhado a ouro.', 'colecionavel', 'raro', 60, 0, 'assets/shop/disquete_dourado.svg', 3),
  ('Troféu do Obby', 'Para quem zerou o próprio obby sem cair (quase).', 'colecionavel', 'raro', 65, 0, 'assets/shop/trofeu_obby.svg', 4),
  ('Gato do Código', 'Ronrona quando o seu código compila de primeira.', 'colecionavel', 'epico', 150, 0, 'assets/shop/gato_do_codigo.svg', 5),
  ('Dragão Pixel', 'Guardião lendário dos repositórios. Cospe fogo em bugs.', 'colecionavel', 'lendario', 0, 15, 'assets/shop/dragao_pixel.svg', 6),
  ('Capuz do Dev', 'Modo focado ativado. Café não incluso.', 'roupa', 'comum', 25, 0, 'assets/shop/capuz_do_dev.svg', 7),
  ('Óculos Pixel', 'Enxergue o mundo em 8 bits.', 'roupa', 'raro', 70, 0, 'assets/shop/oculos_pixel.svg', 8),
  ('Luvas de Neon', 'Digitam 20% mais rápido (cientificamente duvidoso).', 'roupa', 'epico', 160, 0, 'assets/shop/luvas_de_neon.svg', 9),
  ('Capa do Fundador', 'Reservada aos primeiros heróis do Code Quest.', 'roupa', 'lendario', 0, 18, 'assets/shop/capa_do_fundador.svg', 10),
  ('Emblema HTML', 'Provou que domina as tags. <br> de respeito.', 'emblema', 'comum', 15, 0, 'assets/shop/emblema_html.svg', 11),
  ('Emblema do Studio', 'Scripts em Lua? Touched! Emblema de quem programa no Roblox.', 'emblema', 'raro', 50, 0, 'assets/shop/emblema_lua.svg', 12),
  ('Emblema Caça-Bugs', 'Nenhum bug escapa do seu Console.', 'emblema', 'epico', 120, 0, 'assets/shop/emblema_caca_bugs.svg', 13),
  ('Emblema Mestre da Web', 'HTML + CSS + JS: a tríplice coroa da web.', 'emblema', 'lendario', 0, 12, 'assets/shop/emblema_mestre_web.svg', 14),
  ('Coroa das Gems', 'Só para quem acumulou um tesouro de CodeGems.', 'colecionavel', 'lendario', 0, 20, 'assets/shop/coroa_das_gems.svg', 15),
  ('Espada do Código', 'Corta qualquer problema em funções menores.', 'colecionavel', 'lendario', 0, 16, 'assets/shop/espada_do_codigo.svg', 16)
on conflict (name) do update set
  description = excluded.description, category = excluded.category, rarity = excluded.rarity,
  price_coins = excluded.price_coins, price_gems = excluded.price_gems,
  icon = excluded.icon, position = excluded.position;
