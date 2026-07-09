-- 0013_quiz_aulas.sql
-- Adiciona um quiz (perguntas de múltipla escolha sobre o conteúdo do dia) a
-- cada aula reformulada. NÃO destrutivo: jsonb_set só cria/atualiza body.quiz.
-- Chaveado por (tool, position) e, para Web, por título do módulo + position.

do $mig$
declare
  v_mod uuid;
  v_ids uuid[];
  n int;
begin

  -- ===== magicvoxel =====
  select id into v_mod from public.modules where tool = 'magicvoxel' order by position, created_at limit 1;
  if v_mod is not null then
    select array_agg(id order by position, created_at) into v_ids from public.lessons where module_id = v_mod;
    n := coalesce(array_length(v_ids,1),0);
    if n >= 1 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qmag1$[{"q":"O que é um 'voxel'?","options":["Um pincel mágico","Um cubo 3D — o 'pixel' do mundo em 3 dimensões","Um tipo de som","Um botão de salvar"],"answer":1,"explain":"Voxel é o cubinho 3D. É o 'pixel' do mundo em três dimensões."},{"q":"Qual é a grande diferença entre 2D e 3D?","options":["O 3D é sempre colorido","No 3D dá para girar em volta e ver por todos os lados","O 2D não tem cor","Não existe diferença"],"answer":1,"explain":"No 2D o desenho é chapado; no 3D você gira e vê por cima, por baixo e por trás."},{"q":"Para que serve a ferramenta Erase?","options":["Pintar cubos","Apagar cubos","Girar a câmera","Salvar o arquivo"],"answer":1,"explain":"Erase apaga os cubos. Se errar, use o Undo (Ctrl+Z)."},{"q":"Como você desfaz um erro rapidinho?","options":["Fechando o programa","Com o Undo (Ctrl+Z)","Apagando tudo","Trocando a cor"],"answer":1,"explain":"O Undo (Ctrl+Z) volta o último passo. Errar faz parte!"}]$qmag1$::jsonb) where id = v_ids[1];
    end if;
    if n >= 2 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qmag2$[{"q":"O que o Mirror (espelho) faz?","options":["Deixa tudo colorido","Copia igual dos dois lados (simetria)","Apaga o modelo","Gira a câmera"],"answer":1,"explain":"O Mirror espelha no eixo X: o que você faz de um lado aparece igual do outro."},{"q":"Qual ferramenta cria vários cubos de uma vez?","options":["Erase","Undo","Box","Palette"],"answer":2,"explain":"A ferramenta Box cria uma caixa inteira de cubos de uma vez."},{"q":"Com o espelho ligado, se você APAGAR de um lado...","options":["Nada acontece","Apaga do outro lado também","O programa fecha","Muda a cor"],"answer":1,"explain":"O Mirror também espelha o apagar: tirou de um lado, some do outro."},{"q":"Por que é bom planejar o personagem antes de colar cubos?","options":["Para gastar mais cubos","Para decidir a forma e não se perder","Porque o programa exige","Não é bom planejar"],"answer":1,"explain":"Grandes criadores pensam primeiro: decida a forma da cabeça e do corpo antes."}]$qmag2$::jsonb) where id = v_ids[2];
    end if;
    if n >= 3 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qmag3$[{"q":"Como se chama o lugar onde o personagem vive?","options":["Palette","Cenário (scene)","Voxel","Render"],"answer":1,"explain":"O cenário (scene) é o 'mundo' do personagem — floresta, cidade, espaço..."},{"q":"Pensando em escala, a árvore deve ser...","options":["Menor que o personagem","Do mesmo tamanho","Maior que o personagem","Invisível"],"answer":2,"explain":"Cuidar da escala faz o mundo parecer de verdade: a árvore é maior que o personagem."},{"q":"'Ground' em português é...","options":["Céu","Chão","Casa","Árvore"],"answer":1,"explain":"Ground = chão. É a base plana embaixo do personagem."},{"q":"Por que salvar o arquivo .vox no fim da aula?","options":["Para deixar o computador rápido","Para guardar TUDO para a próxima aula","Para apagar o projeto","Não precisa salvar"],"answer":1,"explain":"Salvar sempre! O .vox guarda o personagem e o cenário para o próximo dia."}]$qmag3$::jsonb) where id = v_ids[3];
    end if;
    if n >= 4 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qmag4$[{"q":"O que o 'render' faz?","options":["Apaga o modelo","Calcula a luz e a sombra e transforma tudo numa imagem bonita","Cria cubos","Gira a câmera"],"answer":1,"explain":"Render é o computador calculando luz e sombra para virar uma foto profissional do seu mundo."},{"q":"Como salvar a imagem final?","options":["Undo","Export (PNG)","Attach","Mirror"],"answer":1,"explain":"Export salva a imagem em PNG na sua pasta."},{"q":"Quantas frases combinamos para a apresentação?","options":["1 frase","3 frases","10 frases","Nenhuma"],"answer":1,"explain":"3 frases: o nome do personagem, o que ele faz e a parte mais difícil de construir."},{"q":"'Shadow' em português é...","options":["Luz","Sombra","Câmera","Cor"],"answer":1,"explain":"Shadow = sombra. É ela que dá o toque realista no render."}]$qmag4$::jsonb) where id = v_ids[4];
    end if;
  end if;

  -- ===== roblox =====
  select id into v_mod from public.modules where tool = 'roblox' order by position, created_at limit 1;
  if v_mod is not null then
    select array_agg(id order by position, created_at) into v_ids from public.lessons where module_id = v_mod;
    n := coalesce(array_length(v_ids,1),0);
    if n >= 1 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qrob1$[{"q":"No Roblox, quase tudo que você vê é feito de...","options":["Scripts","Parts (peças)","Sons","Textos"],"answer":1,"explain":"Um obby é só um monte de Parts (peças) bem colocadas."},{"q":"Para a plataforma NÃO cair quando você testar, você marca...","options":["Neon","Anchored","Explorer","Play"],"answer":1,"explain":"Anchored trava a peça no lugar. Sem isso, ela despenca com a gravidade."},{"q":"Qual painel lista tudo que existe no jogo?","options":["Properties","Explorer","Toolbox","Output"],"answer":1,"explain":"O Explorer mostra a árvore de tudo — Workspace, Parts, Scripts..."},{"q":"Onde você muda a cor e o tamanho de uma peça?","options":["No Explorer","Em Properties","No Toolbox","No Baseplate"],"answer":1,"explain":"Properties é o painel de propriedades: Color, Material, Anchored..."}]$qrob1$::jsonb) where id = v_ids[1];
    end if;
    if n >= 2 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qrob2$[{"q":"Qual evento acontece quando algo encosta na peça?","options":["Clicked","Touched","Jump","Died"],"answer":1,"explain":"Touched dispara quando um objeto encosta na peça — a base da lava."},{"q":"No script da lava, o que faz o jogador 'morrer'?","options":["Mudar a cor","Zerar a vida (Health = 0)","Ancorar a peça","Publicar o jogo"],"answer":1,"explain":"Ao encostar, o script coloca Health = 0 e o jogador renasce (respawn)."},{"q":"As três coordenadas de posição de uma peça são...","options":["A, B e C","X, Y e Z","1, 2 e 3","Cima, meio e baixo"],"answer":1,"explain":"X (lados), Y (altura) e Z (frente/trás) posicionam qualquer peça."},{"q":"A peça de lava precisa estar...","options":["Sem cor","Ancorada (Anchored)","Invisível","No Toolbox"],"answer":1,"explain":"Como toda plataforma, a lava deve estar Anchored para ficar no lugar."}]$qrob2$::jsonb) where id = v_ids[2];
    end if;
    if n >= 3 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qrob3$[{"q":"O que transforma um SpawnLocation em checkpoint?","options":["Deixá-lo vermelho","Marcar Neutral = true","Ancorá-lo","Publicá-lo"],"answer":1,"explain":"Com Neutral = true, tocar nele vira o novo ponto de respawn."},{"q":"Por que ter cuidado com o Toolbox?","options":["Ele é pago","Alguns modelos de outras pessoas têm scripts ruins","Ele apaga o jogo","Ele é lento"],"answer":1,"explain":"Use só modelos simples e com o professor por perto — alguns têm scripts perigosos."},{"q":"O que o 'Publish' faz com o seu jogo?","options":["Apaga o jogo","Sobe o jogo para a nuvem do Roblox","Fecha o Studio","Tira a lava"],"answer":1,"explain":"Publish to Roblox coloca o obby na nuvem, pronto para jogar."},{"q":"'Win' significa...","options":["Perder","Vencer","Cair","Pular"],"answer":1,"explain":"Win = vencer. É o bloco de vitória, o troféu do obby."}]$qrob3$::jsonb) where id = v_ids[3];
    end if;
    if n >= 4 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qrob4$[{"q":"O que é um 'bug'?","options":["Um inseto do jogo","Algo que não funciona como deveria","Um tipo de peça","Uma cor"],"answer":1,"explain":"Bug é qualquer coisa errada: um pulo impossível, uma lava que não mata..."},{"q":"Para que serve o 'playtest'?","options":["Publicar o jogo","Jogar para caçar e consertar bugs","Mudar de conta","Criar peças"],"answer":1,"explain":"Playtest é jogar do início ao fim para achar o que precisa consertar (fix)."},{"q":"Quando um colega trava jogando o seu obby, isso é...","options":["Um problema dele","Feedback valioso (ouro!)","Motivo para desistir","Um bug do Roblox"],"answer":1,"explain":"Feedback mostra exatamente o que melhorar. Ouça e anote."},{"q":"'Fix' quer dizer...","options":["Fixar na tela","Consertar","Publicar","Testar"],"answer":1,"explain":"Fix = consertar. É o que você faz depois de achar um bug."}]$qrob4$::jsonb) where id = v_ids[4];
    end if;
  end if;

  -- ===== construct =====
  select id into v_mod from public.modules where tool = 'construct' order by position, created_at limit 1;
  if v_mod is not null then
    select array_agg(id order by position, created_at) into v_ids from public.lessons where module_id = v_mod;
    n := coalesce(array_length(v_ids,1),0);
    if n >= 1 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qcon1$[{"q":"No Construct, o Layout é o... e o Event Sheet é o...","options":["Som / imagem","Palco (cena) / Roteiro (a lógica)","Menu / botão","Nada disso"],"answer":1,"explain":"Layout = onde você posiciona os objetos; Event Sheet = a lógica do jogo."},{"q":"O que um Behavior faz?","options":["Muda a cor","Dá um comportamento pronto ao objeto","Salva o jogo","Cria camadas"],"answer":1,"explain":"Behavior é um superpoder pré-programado (Platform, Solid...)."},{"q":"Qual behavior faz o personagem andar e pular?","options":["Solid","Platform","Keyboard","Text"],"answer":1,"explain":"Platform já dá gravidade, andar e pular ao personagem."},{"q":"Quantas camadas (layers) o plano Free permite?","options":["1","2","10","Ilimitadas"],"answer":1,"explain":"O plano Free permite 2 camadas — Background e Game, perfeito para começar."}]$qcon1$::jsonb) where id = v_ids[1];
    end if;
    if n >= 2 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qcon2$[{"q":"Um evento é formado por...","options":["Só uma imagem","Uma condição e uma ou mais ações","Duas cores","Um som"],"answer":1,"explain":"É o 'SE isto (condição), ENTÃO faça aquilo (ações)' da programação."},{"q":"Para que serve a variável Score?","options":["Mudar o fundo","Guardar quantas moedas você pegou","Criar camadas","Pular"],"answer":1,"explain":"A variável Score é a memória do placar — sem ela, não há pontuação."},{"q":"Ao colidir com a moeda (Coin), o que acontece?","options":["Nada","A moeda é destruída e soma 1 ponto","O jogo reinicia","Você perde"],"answer":1,"explain":"On collision with Coin → Destroy a moeda + Add 1 to Score."},{"q":"'Collision' significa...","options":["Camada","Colisão (dois objetos se encostam)","Comportamento","Câmera"],"answer":1,"explain":"Collision é quando dois objetos se encostam — o gatilho do evento."}]$qcon2$::jsonb) where id = v_ids[2];
    end if;
    if n >= 3 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qcon3$[{"q":"Ao encostar no espinho (Spike), o evento faz...","options":["Você vencer","Restart layout (reinicia a fase)","Somar pontos","Nada"],"answer":1,"explain":"Spike → Restart layout: encostar no espinho reinicia a fase (perder)."},{"q":"Ao encostar na bandeira (Goal)...","options":["A fase reinicia","Vai para o layout de Vitória","Perde uma vida","Some a moeda"],"answer":1,"explain":"Goal → Go to layout 'Vitoria': o fim feliz do jogo (vencer)."},{"q":"Quantos eventos o plano Free permite?","options":["10","50","500","Ilimitados"],"answer":1,"explain":"50 eventos — um ótimo treino de otimização de dev!"},{"q":"Fechar o 'loop do jogo' significa ter...","options":["Muitas cores","Um jeito de perder E um de vencer","Só o começo","Apenas o placar"],"answer":1,"explain":"Todo jogo tem início, jogabilidade e condições de fim (vitória/derrota)."}]$qcon3$::jsonb) where id = v_ids[3];
    end if;
    if n >= 4 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qcon4$[{"q":"O que é 'debugar'?","options":["Publicar o jogo","Investigar por que algo não funciona e corrigir","Adicionar cores","Criar variáveis"],"answer":1,"explain":"Debugar é caçar o motivo do erro: evento fora de ordem, objeto sem nome..."},{"q":"Como se lê o painel de eventos?","options":["De baixo para cima","De cima para baixo","Da direita para a esquerda","Em qualquer ordem"],"answer":1,"explain":"O painel roda de cima para baixo — leia nessa ordem para achar bugs."},{"q":"Ao apresentar como dev, o que é legal explicar?","options":["Nada","Uma regra (condição → ação) que você programou","O preço do Construct","A cor do fundo"],"answer":1,"explain":"Mostrar que você entende o que construiu vale mais que só 'funcionou'."},{"q":"'Playtest' é...","options":["Um behavior","Testar o jogo jogando de verdade","Uma variável","Um layout"],"answer":1,"explain":"Playtest é jogar do início ao fim várias vezes para achar bugs."}]$qcon4$::jsonb) where id = v_ids[4];
    end if;
  end if;

  -- ===== Crie a Web: sua Página Interativa =====
  select id into v_mod from public.modules where title = $mt$Crie a Web: sua Página Interativa$mt$ limit 1;
  if v_mod is not null then
    select array_agg(id order by position, created_at) into v_ids from public.lessons where module_id = v_mod;
    n := coalesce(array_length(v_ids,1),0);
    if n >= 1 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qCri1$[{"q":"Para que serve o HTML?","options":["Deixar a página bonita","Descrever a ESTRUTURA da página","Sortear números","Tocar sons"],"answer":1,"explain":"HTML diz o que é título, parágrafo, imagem... o navegador lê e desenha."},{"q":"Como quase toda tag funciona?","options":["Só abre","Abre e fecha: <p></p>","Só fecha","Não usa símbolos"],"answer":1,"explain":"Quase toda tag vem em par. Esquecer de fechar é o erro nº 1."},{"q":"O que vai dentro do <body>?","options":["Dados invisíveis","O conteúdo que aparece na tela","O nome do arquivo","O CSS apenas"],"answer":1,"explain":"O body guarda o conteúdo visível; o head guarda os dados invisíveis."},{"q":"Qual arquivo é a página inicial de um site?","options":["home.txt","index.html","start.css","pagina.js"],"answer":1,"explain":"index.html é o nome especial da página inicial de qualquer site."}]$qCri1$::jsonb) where id = v_ids[1];
    end if;
    if n >= 2 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qCri2$[{"q":"Enquanto o HTML estrutura, o CSS...","options":["Sorteia números","Embeleza (define a aparência)","Guarda dados","Cria eventos"],"answer":1,"explain":"HTML diz O QUE é cada coisa; CSS diz COMO ela aparece (cor, fonte, posição)."},{"q":"Quais partes formam o 'box model'?","options":["Só a borda","Conteúdo, padding, border e margin","Apenas cor e fonte","Linhas e colunas"],"answer":1,"explain":"Todo elemento é uma caixa: conteúdo + padding + border + margin."},{"q":"Como é a estrutura de uma regra CSS?","options":["função(argumento)","seletor { propriedade: valor; }","<tag>valor</tag>","if (condição)"],"answer":1,"explain":"Ex.: button { color: white; } — seletor, propriedade e valor."},{"q":"Para alinhar e centralizar elementos usamos...","options":["o box model","o Flexbox (display: flex)","o Console","o index.html"],"answer":1,"explain":"display:flex com justify-content/align-items alinha os elementos."}]$qCri2$::jsonb) where id = v_ids[2];
    end if;
    if n >= 3 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qCri3$[{"q":"No trio da web, o JavaScript é o...","options":["Estrutura","Estilo","Comportamento (a página reage e muda)","Nome do arquivo"],"answer":2,"explain":"HTML=estrutura, CSS=estilo, JS=comportamento. Ele reage a eventos como cliques."},{"q":"Qual tecla abre o Console do navegador?","options":["F1","F12","Esc","Enter"],"answer":1,"explain":"F12 abre as ferramentas do dev; o Console mostra erros e console.log."},{"q":"O que Math.random faz no mini-jogo?","options":["Salva o jogo","Sorteia a jogada do computador","Muda a cor","Fecha a página"],"answer":1,"explain":"Math.random gera o sorteio — a jogada do PC no Pedra/Papel/Tesoura."},{"q":"O que classList.toggle('claro') faz?","options":["Apaga a página","Liga/desliga a classe 'claro' (troca o tema) num clique","Cria um botão","Recarrega o site"],"answer":1,"explain":"toggle liga se estiver desligado e desliga se estiver ligado — alterna o tema."}]$qCri3$::jsonb) where id = v_ids[3];
    end if;
    if n >= 4 then
      update public.lessons set body = jsonb_set(body, '{quiz}', $qCri4$[{"q":"Onde o navegador mostra o erro e a LINHA do problema?","options":["No título","No Console (F12)","No CSS","No nome do arquivo"],"answer":1,"explain":"Ler o recado do Console (F12) é meio caminho para consertar o bug."},{"q":"O que deixa a página boa no celular?","options":["Mais cores","A meta viewport + tamanhos flexíveis (responsividade)","Mais botões","Um arquivo maior"],"answer":1,"explain":"A meta viewport faz o navegador respeitar o tamanho da tela."},{"q":"'Deploy' significa...","options":["Apagar o site","Publicar o site na internet","Testar no Console","Trocar a fonte"],"answer":1,"explain":"Deploy é publicar (ex.: Netlify Drop ou GitHub Pages) e receber um link."},{"q":"Depurar (debug) é...","options":["Criar bugs","Encontrar e corrigir o erro","Publicar","Deixar responsivo"],"answer":1,"explain":"Debug é caçar o erro e consertar — habilidade valiosa de todo dev."}]$qCri4$::jsonb) where id = v_ids[4];
    end if;
  end if;

  raise notice 'quiz aplicado';
end
$mig$;