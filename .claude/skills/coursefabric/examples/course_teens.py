# -*- coding: utf-8 -*-
from reportlab.lib.colors import HexColor
import engine, sys

theme = {
    "primary":  HexColor("#2D6CDF"),
    "secondary":HexColor("#21B573"),
    "accent":   HexColor("#FFC93C"),
    "ink":      HexColor("#16233B"),
    "paper":    HexColor("#EEF3FB"),
    "confetti":[HexColor("#2D6CDF"),HexColor("#21B573"),HexColor("#FFC93C"),
                HexColor("#4ECDC4"),HexColor("#FF7A59"),HexColor("#9B7CFF")],
}

course = {
 "slug":"02_TEENS_RobloxStudio",
 "audience":"TEENS",
 "age":"10 a 13 anos",
 "platform":"Roblox Studio",
 "title":"Crie o seu Jogo: Obby!",
 "subtitle":"Construa um obby (corrida de obstáculos) jogável, com checkpoints, lava e um final épico.",
 "day_len":"2 HORAS",
 "theme":theme,
 "seal":("COORDENAÇÃO PEDAGÓGICA","CNA Via Sul","★ ★ ★"),
 "source_note":"Fonte: create.roblox.com/docs",
 "sources":[
   "Roblox Studio — documentação oficial: create.roblox.com/docs/studio/setup. Download gratuito; requer conta Roblox gratuita (verificado em jul/2026).",
 ],
 "overview":("Curso de férias para pré-adolescentes de 10 a 13 anos que amam jogar e agora vão APRENDER A CRIAR. "
   "Em 4 encontros, cada aluno constrói um obby (obstacle course) jogável no Roblox Studio — a mesma "
   "ferramenta usada por criadores profissionais do Roblox. Ao longo do curso eles montam o percurso, "
   "escrevem o primeiro script (a lava que 'mata' o jogador), adicionam checkpoints e um final vitorioso, e "
   "publicam o jogo. O curso equilibra construção livre, noções de lógica/programação e uma 'English Lab' diária "
   "com os termos em inglês que aparecem na tela do Studio."),
 "teacher_intro":{
   "project_goal":("Ao final, cada aluno entrega um obby jogável e publicado no Roblox, com pelo menos 6 obstáculos, "
      "2 checkpoints, uma zona de lava funcional e um bloco de vitória. Apresenta jogando o próprio percurso na TV."),
   "setup":[
     "Instale o Roblox Studio ANTES da aula: acesse create.roblox.com e clique em 'Start Creating' para baixar.",
     "Cada aluno precisa de uma conta Roblox. Oriente as famílias a criarem antes (use o e-mail de um responsável para menores).",
     "Abra o Studio na TV com o template 'Baseplate' para as demonstrações.",
     "Ative os painéis Explorer e Properties (aba View) em todas as máquinas — são essenciais.",
   ],
   "materials":[
     "Computador Windows ou Mac (o Studio roda nos dois).",
     "Conta Roblox (criar em roblox.com).",
     "Roblox Studio (create.roblox.com).",
     "Internet (o Studio salva e publica na nuvem) + TV/projetor.",
   ],
   "management":[
     "Regra de ouro: construir 10 minutos, TESTAR (Play) 2 minutos. Testar sempre evita frustração no fim.",
     "Antes de escrever o script, explique 'evento' com uma analogia: 'QUANDO tocar na lava, ENTÃO perde vida'.",
     "Combine que ninguém baixa itens do Toolbox sem você ver — há conteúdo de terceiros. Fale de segurança online.",
     "Incentive testar o obby do colega: feedback entre pares melhora muito os jogos.",
   ],
 },
 "closing":("Você não só jogou — você CRIOU e PUBLICOU um jogo de verdade no Roblox! Continue evoluindo o seu obby "
   "em casa, adicionando fases, cores e desafios. O Roblox Studio fica instalado no seu computador."),
 "assessment_intro":("A avaliação acontece jogando. No Dia 4 cada aluno testa, corrige, publica e apresenta o obby "
   "rodando na TV. O foco é ter um jogo COMPLETO e jogável do início ao fim, mesmo que simples."),
 "rubric":[
   "O obby tem começo, meio e fim jogáveis (dá para zerar)? — Sim / Parcial / Revisar",
   "Tem pelo menos 2 checkpoints funcionando (respawn correto)? — Sim / Parcial / Revisar",
   "A lava (script Touched) tira a vida do jogador corretamente? — Sim / Parcial / Revisar",
   "Foi publicado no Roblox e apresentado jogando? — Sim / Parcial / Revisar",
 ],
 "presentation":[
   "Cada aluno joga o próprio obby na TV, do início ao fim (ou até onde chegar).",
   "Fala 3 coisas: a parte mais difícil de construir, o obstáculo favorito e o que mudaria.",
   "A turma dá um 'desafio-relâmpago': tentar zerar o obby do colega em 60 segundos.",
   "Troca de 'gamertags' para jogar os jogos depois (com autorização dos responsáveis).",
 ],
 "days":[
  # -------- DIA 1
  {"n":1,"title":"Entrando no Roblox Studio","theme_line":"Primeiros blocos",
   "focus":"Conhecer a interface, inserir Parts, travar com Anchored, colorir e montar a plataforma inicial do obby.",
   "english":[
     ("Studio","STÚ-di-o","O programa onde criamos jogos do Roblox."),
     ("Baseplate","BÊIS-pleit","O 'chão' cinza inicial do projeto novo."),
     ("Part","PART","Uma peça/bloco — o tijolo dos nossos jogos."),
     ("Explorer","eks-PLÓ-rer","O painel que lista tudo que existe no jogo."),
     ("Properties","PRÓ-per-tis","Painel de propriedades (cor, tamanho...)."),
     ("Anchor","ÊN-kor","Ancorar: travar a peça para ela não cair."),
   ],
   "agenda":[
     ("15 min","Boas-vindas + English Lab","Combinados e termos do dia."),
     ("20 min","Tour pelo Studio (na TV)","Explorer, Properties, Toolbox e as ferramentas Move/Scale/Rotate."),
     ("55 min","Mão na massa","Inserir Parts, ancorar, colorir e montar a largada + 3 pulos."),
     ("20 min","Testar (Play)","Jogar o começo do obby e ajustar as distâncias dos pulos."),
     ("10 min","Salvar","Salvar o projeto no Studio (File > Save)."),
   ],
   "notes":[
     {"kind":"teoria","title":"Tudo é uma 'Part'","big":"PART",
      "body":"No Roblox, quase tudo que você vê é feito de Parts (peças). Você muda tamanho, cor, material e posição de cada uma. Um obby é só um monte de Parts bem colocadas!"},
     {"kind":"dica","title":"Ancore ou o mundo cai","body":"Toda peça tem uma propriedade Anchored (ancorada). Se estiver desligada, a peça cai com a gravidade quando você testar. Plataformas de obby precisam estar ANCORADAS."},
   ],
   "steps":[
     {"title":"Abra um Baseplate","body":"No Studio, crie um New > Baseplate. Aquele chão cinza é a sua base para construir.",
      "tip":"Ative Explorer e Properties na aba View — vamos usar o tempo todo."},
     {"title":"Insira uma Part","body":"Na aba Home, clique em Part para inserir um bloco. Ele aparece no Explorer, dentro de Workspace."},
     {"title":"Mova, gire e redimensione","body":"Use as ferramentas Move, Scale e Rotate (aba Home) para posicionar e esticar a peça como plataforma."},
     {"title":"Ancore a peça","body":"Selecione a Part, vá em Properties e marque Anchored. Agora ela não cai quando você testar.",
      "tip":"Sem Anchored = plataforma despencando. Marque sempre!"},
     {"title":"Dê cor e material","body":"Em Properties, mude Color e Material (tente Neon, Wood, Grass) para o obby ficar com a sua cara."},
     {"title":"Monte a largada + 3 pulos","body":"Duplique a peça (Ctrl+D) e crie a plataforma inicial e os 3 primeiros pulos, com espaços entre elas."},
   ],
   "challenge":{"title":"Desafio: A largada perfeita","items":[
      "Crie uma plataforma de largada bem visível (cor diferente).",
      "Faça 3 pulos com distâncias que dá para vencer sem cair sempre.",
      "Teste (Play) e ajuste: nem fácil demais, nem impossível.",
   ],"closing":"Guarde: amanhã transformamos isso num percurso de verdade."},
   "teacher":{
     "objectives":["Navegar no Studio usando Explorer e Properties.",
       "Inserir, mover, escalar e ancorar Parts.",
       "Alterar cor e material de peças.",
       "Testar (Play) e iterar sobre o design dos pulos."],
     "pitfalls":[
       "Plataformas caindo ao testar: faltou marcar Anchored.",
       "Aluno 'perde' a peça: ensine a clicar no nome dela no Explorer para selecionar.",
       "Pulos impossíveis: mostre o padrão de altura de pulo do avatar (ajuste distâncias no Play).",
       "Studio não abre/loga: confirme a conta Roblox e a conexão antes da aula."],
     "checks":["Todos criaram e ancoraram pelo menos 4 Parts?","Todos conseguiram testar com Play?",
       "Todos salvaram o projeto?"],
     "differ":["Mais rápidos: criar plataformas de tamanhos variados e rampas.",
       "Apoio: fornecer um Baseplate com a largada já pronta para eles continuarem."],
   }},
  # -------- DIA 2
  {"n":2,"title":"Montando o percurso (o obby)","theme_line":"Obstáculos + 1º script",
   "focus":"Construir o percurso completo de obstáculos e escrever o primeiro script: a lava que elimina o jogador.",
   "english":[
     ("Obby","Ó-bi","Obstacle course: corrida de obstáculos."),
     ("Platform","PLÁT-form","Plataforma."),
     ("Lava","LÁ-va","Lava (a peça que 'mata' o jogador)."),
     ("Script","SCRIPT","Um conjunto de instruções (código) para o jogo."),
     ("Touched","TÂTCHT","Evento 'foi tocado' — quando algo encosta na peça."),
     ("Humanoid","RIU-ma-noid","A 'parte viva' do avatar (tem vida/Health)."),
   ],
   "agenda":[
     ("15 min","English Lab + revisão","Termos do dia e relembrar Anchored."),
     ("15 min","Teoria: o que é um script?","Evento = 'QUANDO isto acontece, FAÇA aquilo'."),
     ("50 min","Construir o percurso","Montar 6+ obstáculos com dificuldade crescente."),
     ("30 min","Criar a lava (script)","Inserir Part de lava + Script Touched que zera a vida."),
     ("10 min","Testar + salvar","Cair na lava deve reiniciar o jogador. Salvar."),
   ],
   "notes":[
     {"kind":"teoria","title":"Programar é reagir a eventos","big":"EVENTO",
      "body":"Um script escuta EVENTOS. O evento Touched acontece quando algo encosta na peça. Aí o jogo executa uma ação — no nosso caso, tirar a vida do jogador. É a base de quase todo jogo!"},
     {"kind":"cultura","title":"Coordenadas: X, Y, Z","big":"XYZ",
      "body":"Toda peça tem uma posição em 3 números: X (esquerda/direita), Y (altura) e Z (frente/trás). Entender isso ajuda a alinhar plataformas com precisão."},
   ],
   "steps":[
     {"title":"Estenda o percurso","body":"Continue a partir do Dia 1. Crie 6 ou mais obstáculos com dificuldade crescente: pulos, cantos, peças finas."},
     {"title":"Crie a peça de lava","body":"Insira uma Part, cor vermelha, material Neon, e ANCORE. Renomeie para 'Lava' no Explorer."},
     {"title":"Adicione um Script na lava","body":"No Explorer, passe o mouse na Lava, clique no + e escolha Script. Uma janela de código abre."},
     {"title":"Escreva o código da lava","body":"Digite o script do próximo slide. Ele detecta o toque e zera a vida do jogador (respawn)."},
     {"title":"Teste a lava","body":"Play. Encoste na lava: você deve 'morrer' e voltar à largada. Se não, revise o script.",
      "tip":"Erros de código aparecem em vermelho na aba Output. Leia a linha indicada."},
   ],
   "code_slides":[
     {"title":"O script da lava","lang":"Luau (Roblox)","lines":[
        "-- coloque este Script DENTRO da peça de lava",
        "local parte = script.Parent",
        "",
        "parte.Touched:Connect(function(outro)",
        "  local h = outro.Parent:FindFirstChildWhichIsA(\"Humanoid\")",
        "  if h then",
        "    h.Health = 0   -- tira toda a vida = respawn",
        "  end",
        "end)",
     ],"caption":"Touched é o evento; quando um Humanoid encosta, a vida vira 0 e o jogador renasce."},
   ],
   "challenge":{"title":"Desafio: Um obstáculo assinatura","items":[
      "Crie 1 obstáculo único e criativo (ponte fina, zigue-zague, salto duplo).",
      "Coloque lava embaixo dele para aumentar a tensão.",
      "Teste e garanta que é DIFÍCIL, mas possível.",
   ],"closing":"Amanhã: checkpoints para o jogador não recomeçar do zero!"},
   "teacher":{
     "objectives":["Compreender script e evento (Touched) na prática.",
       "Inserir um Script dentro de uma Part pelo Explorer.",
       "Ler e digitar um script curto em Luau.",
       "Depurar usando a aba Output."],
     "pitfalls":[
       "Script no lugar errado: deve ficar DENTRO da peça de lava (filho dela no Explorer).",
       "Aspas 'curvas' quebram o código: digite aspas retas \" \" no editor do Studio.",
       "Lava não mata: confira se a peça pode ser tocada (CanCollide/CanTouch ligado) e se o script está na peça certa.",
       "Erro em vermelho no Output: leia o número da linha e compare caractere a caractere."],
     "checks":["O percurso tem 6+ obstáculos?","A lava zera a vida ao toque?",
       "Todos leram pelo menos um erro no Output e corrigiram?"],
     "differ":["Mais rápidos: criar 2 tipos de lava (uma fina 'laser').",
       "Apoio: fornecer o script pronto para colar e focar em posicionar a lava."],
   }},
  # -------- DIA 3
  {"n":3,"title":"Checkpoints, vitória e decoração","theme_line":"Justiça + estilo",
   "focus":"Adicionar checkpoints com SpawnLocation, criar o bloco de vitória e decorar o mundo com segurança.",
   "english":[
     ("Checkpoint","TCHÉK-point","Ponto de salvamento no meio do percurso."),
     ("Spawn","SPÓN","Nascer/aparecer — onde o jogador surge."),
     ("Respawn","ri-SPÓN","Renascer após 'morrer'."),
     ("Win","UÍN","Vencer / vitória."),
     ("Toolbox","TÚL-boks","Caixa de recursos com modelos prontos."),
     ("Publish","PÁ-blish","Publicar o jogo na nuvem do Roblox."),
   ],
   "agenda":[
     ("15 min","English Lab + plano do dia","Termos e onde colocar cada checkpoint."),
     ("20 min","Demo: SpawnLocation","Como um spawn neutro vira checkpoint automático."),
     ("45 min","Colocar checkpoints + vitória","Spawns ao longo do percurso + bloco final dourado."),
     ("30 min","Decorar (com segurança)","Cores, luzes e itens do Toolbox revisados pelo professor."),
     ("10 min","Publicar (1ª vez)","File > Publish to Roblox. Salvar na nuvem."),
   ],
   "notes":[
     {"kind":"teoria","title":"Checkpoint = respawn mais justo","big":"SAVE",
      "body":"Um SpawnLocation 'neutro' (Neutral = true) vira um checkpoint: quando o jogador toca nele, é ali que vai renascer. Assim, cair não significa recomeçar tudo — só voltar ao último checkpoint."},
     {"kind":"seguranca","title":"Cuidado com o Toolbox","big":"!",
      "body":"O Toolbox tem itens criados por outras pessoas. Alguns podem ter scripts ruins. Use só modelos simples, com o professor por perto, e nunca compartilhe senha ou dados pessoais no Roblox."},
   ],
   "steps":[
     {"title":"Coloque o 1º SpawnLocation","body":"Insira um SpawnLocation na largada (Explorer > +). É onde o jogo começa."},
     {"title":"Crie checkpoints","body":"Insira mais SpawnLocations ao longo do percurso. Em cada um, marque Neutral = true em Properties.",
      "tip":"Neutral ligado = tocar nele vira o seu novo ponto de respawn."},
     {"title":"Bloco de vitória","body":"No fim, crie uma Part dourada (Neon), ancore e renomeie para 'Win'. É o troféu do obby."},
     {"title":"Decore o mundo","body":"Adicione cores, luzes (SpotLight) e 1 ou 2 itens simples do Toolbox — sempre com o professor revisando."},
     {"title":"Publique o jogo","body":"File > Publish to Roblox As... Dê um nome e salve. Seu obby agora vive na nuvem!"},
   ],
   "code_slides":[
     {"title":"(Opcional) Mensagem de vitória","lang":"Luau (Roblox)","lines":[
        "-- Script DENTRO da peça 'Win'",
        "local win = script.Parent",
        "",
        "win.Touched:Connect(function(outro)",
        "  local h = outro.Parent:FindFirstChildWhichIsA(\"Humanoid\")",
        "  if h then",
        "    print(outro.Parent.Name .. \" venceu o obby!\")",
        "  end",
        "end)",
     ],"caption":"Mesma ideia da lava, mas agora comemoramos: imprime o nome de quem venceu no Output."},
   ],
   "challenge":{"title":"Desafio: Zona temática","items":[
      "Escolha um tema (gelo, vulcão, espaço) e decore uma parte do obby com ele.",
      "Garanta que há um checkpoint ANTES da parte mais difícil.",
      "Publique e jogue do início para conferir os respawns.",
   ],"closing":"Amanhã: testar de verdade, corrigir bugs e apresentar!"},
   "teacher":{
     "objectives":["Usar SpawnLocation como início e como checkpoint (Neutral).",
       "Criar um objetivo final (bloco de vitória).",
       "Avaliar segurança e adequação de itens do Toolbox.",
       "Publicar o jogo no Roblox."],
     "pitfalls":[
       "Respawn sempre na largada: os checkpoints precisam de Neutral = true e estar habilitados.",
       "Vários spawns 'brigando': espace-os bem; teste tocando um a um.",
       "Itens pesados do Toolbox travam o jogo: prefira modelos simples e revise antes.",
       "Falha ao publicar: verifique login e conexão; tente novamente em File > Publish."],
     "checks":["Há largada + pelo menos 2 checkpoints funcionando?","Existe um bloco de vitória?",
       "O jogo foi publicado?"],
     "differ":["Mais rápidos: criar leaderboard de tempo (extensão) ou plataformas móveis.",
       "Apoio: dar checkpoints prontos para posicionar."],
   }},
  # -------- DIA 4
  {"n":4,"title":"Testar, publicar e apresentar","theme_line":"Lançamento",
   "focus":"Playtest completo, corrigir bugs, publicar a versão final e apresentar o obby jogando na TV.",
   "english":[
     ("Playtest","PLÊI-test","Testar o jogo jogando de verdade."),
     ("Bug","BÂG","Um erro/defeito no jogo."),
     ("Fix","FÍKS","Consertar."),
     ("Publish","PÁ-blish","Publicar a versão final."),
     ("Player","PLÊI-er","Jogador."),
     ("Feedback","FÍD-bek","Retorno/opinião de quem jogou."),
   ],
   "agenda":[
     ("10 min","English Lab + aquecer","Termos do dia e checklist de bugs."),
     ("30 min","Playtest + corrigir","Zerar o próprio obby e anotar/consertar bugs."),
     ("25 min","Testar o do colega","Jogar em dupla e dar feedback (o que melhorar)."),
     ("35 min","Retoques finais + publicar","Últimos ajustes, nome caprichado e Publish final."),
     ("20 min","Apresentações","Cada um joga o obby na TV. Desafio-relâmpago e aplausos."),
   ],
   "notes":[
     {"kind":"teoria","title":"O que é um 'bug'?","big":"BUG",
      "body":"Bug é qualquer coisa que não funciona como deveria: um pulo impossível, uma lava que não mata, um checkpoint que não salva. Testar (playtest) serve para caçar e consertar (fix) esses bugs."},
     {"kind":"dica","title":"Feedback é presente","body":"Quando um colega joga o seu obby e trava, isso é OURO: mostra exatamente o que melhorar. Ouça sem se ofender e anote. Depois, retribua testando o dele com carinho."},
   ],
   "steps":[
     {"title":"Zere o próprio obby","body":"Jogue do início ao fim. Anote tudo que travar, for injusto ou não funcionar."},
     {"title":"Corrija os bugs","body":"Volte ao Studio e conserte: distâncias, Anchored, lava, checkpoints. Teste de novo."},
     {"title":"Teste com um colega","body":"Troquem de cadeira e joguem o obby um do outro. Dê 2 elogios e 1 sugestão."},
     {"title":"Capriche e publique","body":"Ajuste cores, dê um nome legal e faça o Publish final. Seu jogo está pronto para o mundo!"},
     {"title":"Apresente jogando","body":"Mostre o obby na TV jogando ao vivo. Conte a parte mais difícil de criar."},
   ],
   "challenge":{"title":"Missão final: Lançamento oficial","items":[
      "Seu obby precisa ser 'zerável' do início ao fim.",
      "Nome + cor de largada + bloco de vitória bem visíveis.",
      "Publicado e apresentado ao vivo na TV.",
   ],"closing":"Parabéns, criador(a) de jogos! O mundo já pode jogar o seu obby."},
   "teacher":{
     "objectives":["Realizar playtest sistemático e registrar bugs.",
       "Corrigir problemas de jogabilidade e scripts.",
       "Dar e receber feedback construtivo.",
       "Publicar e apresentar o produto final."],
     "pitfalls":[
       "Obby 'inzerável': teste você mesmo cada trecho; ajuste distâncias.",
       "Aluno leva feedback para o pessoal: reforce a regra '2 elogios + 1 sugestão'.",
       "Tempo curto: garanta que TODOS publiquem antes das falas começarem.",
       "Timidez: permita apresentar em dupla, um joga e o outro narra."],
     "checks":["O obby é zerável do início ao fim?","Foi publicado na versão final?",
       "Cada aluno deu e recebeu feedback?"],
     "differ":["Mais rápidos: criar uma 2ª fase ou um atalho secreto.",
       "Apoio: focar em deixar 1 percurso curto 100% funcional e publicado."],
   }},
 ],
}

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv)>1 else "."
    a,b = engine.build_all(course, outdir)
    print("OK", a, b)
