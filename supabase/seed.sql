-- Conteúdo de exemplo: módulo Piskel + Scratch com 3 aulas.
-- Substitua/adicione com o material real da Ctrl+Play.
with m as (
  insert into public.modules (title, description, tool, position)
  values ('Piskel + Scratch — Primeiros sprites', 'Crie seus personagens no Piskel e dê vida a eles no Scratch.', 'piskel', 1)
  returning id
)
insert into public.lessons (module_id, title, description, tool, position, reward_coins, body)
select m.id, t.title, t.descr, t.tool::tool_kind, t.pos, t.reward, t.body::jsonb
from m, (values
  ('Aula 1 — Meu primeiro sprite', 'Desenhe um sprite no Piskel e prepare pro Scratch.', 'scratch', 1, 20,
   $json${
     "intro":"Hoje você vai criar o personagem do seu jogo no Piskel e deixar tudo pronto pra programar no Scratch!",
     "material":[
       {"t":"h","x":"O que é um sprite?"},
       {"t":"p","x":"Um sprite é o desenho do personagem ou objeto do seu jogo. No Piskel a gente desenha quadradinho por quadradinho (pixel art) e depois usa ele no Scratch pra dar vida ao jogo."},
       {"t":"img","svg":"<svg viewBox='0 0 112 96' width='112' height='96' xmlns='http://www.w3.org/2000/svg'><rect x='16' y='0' width='16' height='16' fill='#FF6B9D'/><rect x='80' y='0' width='16' height='16' fill='#FF6B9D'/><rect x='16' y='16' width='80' height='64' rx='6' fill='#FF6B9D'/><rect x='32' y='34' width='14' height='16' fill='#1E293B'/><rect x='66' y='34' width='14' height='16' fill='#1E293B'/><rect x='50' y='58' width='12' height='10' fill='#1E293B'/></svg>","cap":"Exemplo: sprite de gato (pixel art)"},
       {"t":"anim","cap":"Como um sprite é desenhado, pixel a pixel"},
       {"t":"embed","url":"","cap":"Vídeo curto (YouTube/TikTok/Insta) — adicione o link depois"},
       {"t":"tip","x":"Comece pequeno: 8x8 ou 16x16 pixels. Menos quadrados = mais fácil de fazer!"}
     ],
     "resources":[
       {"label":"Abrir o Piskel","url":"https://www.piskelapp.com","kind":"piskel","note":"desenhar o sprite"},
       {"label":"Abrir o Scratch","url":"https://scratch.mit.edu","kind":"scratch","note":"programar o jogo"},
       {"label":"Paletas de cores","url":"https://lospec.com/palette-list","kind":"link","note":"escolher cores bonitas"},
       {"label":"Galeria pra inspiração","url":"https://www.piskelapp.com/explore","kind":"image","note":"ver outros sprites"}
     ],
     "challenge":{"x":"Crie o seu próprio sprite de um gato (ou outro bicho!) no Piskel e exporte como imagem PNG.","steps":["Abra o Piskel e crie um quadro de 16x16","Desenhe o seu personagem com as cores que quiser","Clique em Export e salve como PNG","Guarde o arquivo pra usar no Scratch na próxima aula"]},
     "english":{"intro":"Palavras que aparecem no Piskel e no Scratch:","pairs":[["cat","gato"],["color","cor"],["frame","quadro"],["export","exportar"],["sprite","personagem"]]}
   }$json$),
  ('Aula 2 — Animação do sprite', 'Faça seu personagem se mexer com vários quadros.', 'piskel', 2, 20,
   $json${
     "intro":"Vamos fazer seu sprite ganhar vida com vários quadros!",
     "material":[
       {"t":"h","x":"Animação = vários quadros"},
       {"t":"p","x":"No Piskel você cria vários frames (quadros) e o programa mostra um atrás do outro, bem rápido, criando o movimento."},
       {"t":"anim","cap":"Vários quadros viram movimento"},
       {"t":"tip","x":"2 ou 3 quadros já fazem uma animação simples, tipo um gato andando."}
     ],
     "resources":[{"label":"Abrir o Piskel","url":"https://www.piskelapp.com","kind":"piskel","note":"criar os frames"}],
     "challenge":{"x":"Faça seu gato piscar os olhos usando 2 quadros.","steps":["Duplique o seu sprite (novo frame)","No 2 quadro, feche os olhos do gato","Use o Preview pra ver a animação"]},
     "english":{"intro":"Palavras de animação:","pairs":[["frame","quadro"],["play","tocar"],["loop","repetir"],["speed","velocidade"]]}
   }$json$),
  ('Aula 3 — Movimento no Scratch', 'Programe o personagem pra andar com as setas.', 'scratch', 3, 20,
   $json${
     "intro":"Hora de programar: faça o personagem se mexer com as setas!",
     "material":[
       {"t":"h","x":"Blocos de movimento"},
       {"t":"p","x":"No Scratch a gente junta blocos como peças de Lego. Pra mexer o personagem, usamos os blocos de quando tecla pressionada e mude x/y."},
       {"t":"tip","x":"Teste sempre clicando na bandeira verde!"}
     ],
     "resources":[{"label":"Abrir o Scratch","url":"https://scratch.mit.edu","kind":"scratch","note":"montar os blocos"}],
     "challenge":{"x":"Faça seu sprite andar para os 4 lados com as setas do teclado.","steps":["Importe seu sprite do Piskel","Use quando seta pressionada","Mude a posição x e y do personagem"]},
     "english":{"intro":"Palavras de programação:","pairs":[["move","mover"],["key","tecla"],["sprite","personagem"],["start","começar"]]}
   }$json$)
) as t(title, descr, tool, pos, reward, body);
