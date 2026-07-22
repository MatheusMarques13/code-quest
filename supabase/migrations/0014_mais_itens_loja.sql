-- 0014_mais_itens_loja.sql
-- Segunda leva de itens da loja (novas roupas com camadas do avatar na casa,
-- colecionáveis e emblemas dos cursos). Idempotente por nome (índice único de 0012).

insert into public.shop_items (name, description, category, rarity, price_coins, price_gems, icon, position) values
  ('Foguete de Mesa', 'Decolagem em 3, 2, 1… direto da sua escrivaninha.', 'colecionavel', 'comum', 18, 0, 'assets/shop/foguete_de_mesa.svg', 17),
  ('Console Retrô', 'Roda jogos de 8 bits e memórias de 1988.', 'colecionavel', 'raro', 58, 0, 'assets/shop/console_retro.svg', 18),
  ('Robô de Estimação', 'Bipa feliz toda vez que você termina uma aula.', 'colecionavel', 'epico', 150, 0, 'assets/shop/robo_de_estimacao.svg', 19),
  ('Fênix do Deploy', 'Renasce das cinzas de todo código que quebrou.', 'colecionavel', 'lendario', 0, 18, 'assets/shop/fenix_do_deploy.svg', 20),
  ('Orbe do Infinito', 'Gira para sempre, como um loop bem feito.', 'colecionavel', 'lendario', 0, 17, 'assets/shop/orbe_do_infinito.svg', 21),
  ('Camiseta Pixel', 'Coração de 8 bits para programar com estilo.', 'roupa', 'comum', 22, 0, 'assets/shop/camiseta_pixel.svg', 22),
  ('Tênis Turbo', 'Corre mais que bug em sexta-feira.', 'roupa', 'comum', 28, 0, 'assets/shop/tenis_turbo.svg', 23),
  ('Fones Gamer', 'Modo imersão total: só você e o código.', 'roupa', 'raro', 60, 0, 'assets/shop/fones_gamer.svg', 24),
  ('Elmo do Cavaleiro', 'Proteção máxima contra erros de digitação.', 'roupa', 'raro', 75, 0, 'assets/shop/elmo_do_cavaleiro.svg', 25),
  ('Chapéu de Mago', 'Transforma café em código (magia avançada).', 'roupa', 'epico', 140, 0, 'assets/shop/chapeu_de_mago.svg', 26),
  ('Mochila a Jato', 'Voa direto para o topo do ranking.', 'roupa', 'lendario', 0, 16, 'assets/shop/mochila_a_jato.svg', 27),
  ('Emblema Voxel 3D', 'Mestre dos cubos! Construiu mundos no MagicaVoxel.', 'emblema', 'comum', 15, 0, 'assets/shop/emblema_voxel.svg', 28),
  ('Emblema Criador de Jogos', 'Fez o próprio jogo no Construct. Respeito.', 'emblema', 'raro', 55, 0, 'assets/shop/emblema_construct.svg', 29),
  ('Emblema English Pro', 'Fala os termos de programação like a pro.', 'emblema', 'epico', 125, 0, 'assets/shop/emblema_ingles.svg', 30)
on conflict (name) do update set
  description = excluded.description, category = excluded.category, rarity = excluded.rarity,
  price_coins = excluded.price_coins, price_gems = excluded.price_gems,
  icon = excluded.icon, position = excluded.position;
