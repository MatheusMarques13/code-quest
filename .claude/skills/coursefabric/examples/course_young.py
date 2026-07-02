# -*- coding: utf-8 -*-
from reportlab.lib.colors import HexColor
import engine, sys

theme = {
    "primary":  HexColor("#6C4CE0"),
    "secondary":HexColor("#17B8C4"),
    "accent":   HexColor("#C4E24A"),
    "ink":      HexColor("#1C1533"),
    "paper":    HexColor("#F2F0FB"),
    "confetti":[HexColor("#6C4CE0"),HexColor("#17B8C4"),HexColor("#C4E24A"),
                HexColor("#FF7AC6"),HexColor("#FFB020"),HexColor("#4ECDC4")],
}

course = {
 "slug":"03_YOUNG_Construct3",
 "audience":"YOUNG",
 "age":"14+ anos",
 "platform":"Construct 3",
 "title":"Game Dev: seu Plataforma 2D",
 "subtitle":"Programe um jogo de plataforma completo — moedas, espinhos e a bandeira final — no navegador.",
 "day_len":"2 HORAS",
 "theme":theme,
 "seal":("COORDENAÇÃO PEDAGÓGICA","CNA Via Sul","★ ★ ★"),
 "source_note":"Fontes: construct.net • editor.construct.net",
 "sources":[
   "Construct 3 — site oficial: construct.net e editor.construct.net. O plano Free permite 50 eventos e 2 camadas por projeto (verificado em jul/2026).",
 ],
 "overview":("Curso de férias para jovens de 14+ que querem realmente PROGRAMAR um jogo. Em 4 encontros, "
   "cada aluno cria um jogo de plataforma 2D completo no Construct 3 — uma ferramenta profissional que roda no "
   "navegador, sem instalar nada. Usando o sistema de eventos (condição → ação), eles programam movimento, coleta "
   "de moedas, obstáculos que fazem perder e uma bandeira de vitória. O curso trabalha lógica de programação de "
   "forma visual, pensamento de game design e uma 'English Lab' diária com os termos técnicos em inglês da "
   "interface. Tudo dentro dos limites do plano Free (uma ótima lição de otimização)."),
 "teacher_intro":{
   "project_goal":("Ao final, cada aluno entrega um jogo de plataforma 2D jogável com: personagem que anda e pula, "
      "moedas com placar, um obstáculo que reinicia a fase e uma bandeira de vitória — tudo em 2 camadas e menos de "
      "50 eventos (limites do plano Free). Apresenta jogando no Preview, na TV."),
   "setup":[
     "Não precisa instalar: abra editor.construct.net no Google Chrome (recomendado) em todas as máquinas.",
     "Peça que cada aluno crie uma conta em construct.net para salvar o projeto na nuvem (ou salve o arquivo .c3p localmente).",
     "O plano Free do Construct = 50 eventos e 2 camadas por projeto. Projete o jogo dentro desses limites (usaremos ~10 eventos).",
     "Tenha o editor aberto na TV. Deixe uns sprites simples (personagem, moeda, espinho) prontos para agilizar.",
   ],
   "materials":[
     "Qualquer computador com navegador moderno (Chrome de preferência) — funciona até em Chromebook.",
     "Conta no Construct (construct.net) para salvar na nuvem.",
     "Construct 3 — plano Free (editor.construct.net), sem instalação.",
     "Internet + TV/projetor.",
   ],
   "management":[
     "Sempre nomeie os objetos (Player, Coin, Spike, Goal). Eventos ficam ilegíveis com 'Sprite2, Sprite3...'.",
     "Ensine o ciclo: adicionar 1 evento → dar Preview → verificar. Nunca 5 eventos sem testar.",
     "O limite de 50 eventos é pedagógico: force reuso e clareza. Mostre o contador de eventos.",
     "Incentive arte própria (editor de sprite embutido) ou assets livres — bom gancho para falar de licenças.",
   ],
 },
 "closing":("Você programou um jogo de plataforma completo, do zero, usando lógica de eventos de verdade — e ainda "
   "respeitando limites técnicos, como um dev profissional. Continue: adicione fases, inimigos e sons. O Construct "
   "roda no navegador. Continue criando!"),
 "assessment_intro":("A avaliação é por demonstração jogável. No Dia 4 cada aluno testa, ajusta dentro dos limites do "
   "plano Free e apresenta o jogo no Preview. O foco é um jogo COMPLETO: começar, jogar, perder e vencer."),
 "rubric":[
   "O personagem anda e pula corretamente (behavior Platform)? — Sim / Parcial / Revisar",
   "Coletar moedas aumenta o placar (variável + texto)? — Sim / Parcial / Revisar",
   "Há um jeito de PERDER (espinho reinicia) e de VENCER (bandeira)? — Sim / Parcial / Revisar",
   "Ficou dentro dos limites (2 camadas, < 50 eventos) e foi apresentado? — Sim / Parcial / Revisar",
 ],
 "presentation":[
   "Cada aluno joga o próprio jogo no Preview, na TV: mostra andar, coletar, perder e vencer.",
   "Explica 1 evento que programou (condição → ação) com as próprias palavras.",
   "Conta quantos eventos usou e uma decisão de otimização que tomou.",
   "A turma sugere 1 melhoria (novo obstáculo, power-up, fase 2).",
 ],
 "days":[
  # -------- DIA 1
  {"n":1,"title":"Conhecendo o Construct 3","theme_line":"Layout, camadas e o herói",
   "focus":"Abrir o editor no navegador, entender Layout x Event Sheet, criar as 2 camadas e um personagem que já anda.",
   "english":[
     ("Layout","LÊI-aut","A 'tela'/fase do jogo (onde ficam os objetos)."),
     ("Event Sheet","i-VÊNT XIT","A folha de eventos: onde fica a lógica do jogo."),
     ("Sprite","SPRÁIT","Uma imagem/objeto do jogo (personagem, moeda...)."),
     ("Layer","LÊI-er","Camada (o plano Free permite 2)."),
     ("Behavior","bi-RÊI-vior","Comportamento pronto (ex.: Platform, Solid)."),
     ("Preview","PRÍ-viu","Rodar o jogo para testar."),
   ],
   "agenda":[
     ("15 min","Boas-vindas + English Lab","Combinados e termos técnicos do dia."),
     ("20 min","Tour do Construct (na TV)","Layout x Event Sheet, painel de camadas e de objetos."),
     ("50 min","Criar cena + personagem","2 camadas (Background/Game), Sprite do Player + behavior Platform."),
     ("25 min","Chão sólido + Preview","Tiled Background como chão com Solid; testar o pulo."),
     ("10 min","Salvar","Salvar na nuvem ou baixar o .c3p."),
   ],
   "notes":[
     {"kind":"teoria","title":"Layout x Event Sheet","big":"2x",
      "body":"O Layout é o PALCO (onde você posiciona os objetos). O Event Sheet é o ROTEIRO (a lógica: o que acontece e quando). Todo jogo no Construct é essa dupla: cena + eventos."},
     {"kind":"cultura","title":"Behaviors: superpoderes prontos","big":"⚙",
      "body":"Um Behavior é um comportamento pré-programado. 'Platform' já dá gravidade, andar e pular ao personagem; 'Solid' faz o chão bloquear. Você ganha tempo e foca na parte criativa."},
   ],
   "steps":[
     {"title":"Abra o editor","body":"No Chrome, acesse editor.construct.net e clique em New project. Não precisa instalar nada.",
      "tip":"Crie uma conta em construct.net para salvar seu projeto na nuvem."},
     {"title":"Crie 2 camadas","body":"No painel Layers, deixe duas: 'Background' (fundo) e 'Game' (jogo). O plano Free permite 2 — perfeito."},
     {"title":"Desenhe o Player","body":"Insira um Sprite na camada Game, desenhe/importe o personagem e renomeie o objeto para 'Player'."},
     {"title":"Adicione o behavior Platform","body":"Com o Player selecionado, em Behaviors clique em Add e escolha Platform. Agora ele anda e pula."},
     {"title":"Crie o chão sólido","body":"Insira um Tiled Background como chão, na camada Game, e adicione o behavior Solid para o Player pisar."},
     {"title":"Dê Preview","body":"Clique em Preview (▶) e teste com as setas do teclado. O personagem deve andar e pular sobre o chão.",
      "tip":"O behavior Platform já usa Setas + Seta para cima (pulo) por padrão."},
   ],
   "challenge":{"title":"Desafio: Um palco com estilo","items":[
      "Deixe o Background com uma cor/fundo (céu) diferente do chão.",
      "Ajuste o tamanho do Player e do chão para ficar agradável.",
      "Garanta no Preview que ele anda e pula sem atravessar o chão.",
   ],"closing":"Amanhã: plataformas, teclado e as primeiras MOEDAS com placar."},
   "teacher":{
     "objectives":["Diferenciar Layout (cena) de Event Sheet (lógica).",
       "Trabalhar com 2 camadas (limite do plano Free).",
       "Criar um Sprite e aplicar behaviors Platform e Solid.",
       "Executar e testar com Preview."],
     "pitfalls":[
       "Player atravessa o chão: o chão precisa do behavior Solid; o Player, do Platform.",
       "Player cai infinitamente: coloque-o ACIMA do chão no layout.",
       "Objetos sem nome: renomeie tudo agora (Player, Chao) para os eventos ficarem legíveis.",
       "Não salvou: mostre salvar na nuvem OU baixar o .c3p; combine sempre salvar ao fim."],
     "checks":["Todos têm 2 camadas nomeadas?","O Player anda e pula no Preview?",
       "Todos salvaram (nuvem ou .c3p)?"],
     "differ":["Mais rápidos: desenhar um sprite mais caprichado no editor embutido.",
       "Apoio: fornecer um projeto-base com Player e chão prontos."],
   }},
  # -------- DIA 2
  {"n":2,"title":"Movimento, moedas e placar","theme_line":"Primeiros eventos","focus":"Montar as plataformas, controlar pelo teclado e programar o primeiro evento: coletar moedas e somar pontos.",
   "english":[
     ("Solid","SÓ-lid","Comportamento que bloqueia (chão/parede)."),
     ("Collision","co-LÍ-jon","Colisão: quando dois objetos se encostam."),
     ("Event","i-VÊNT","Evento = uma condição que dispara ações."),
     ("Action","ÁK-shon","Ação executada quando a condição é verdadeira."),
     ("Variable","VÉ-ri-a-bol","Variável: uma 'caixinha' que guarda um valor (ex.: Score)."),
     ("Keyboard","KÍ-bord","Teclado (objeto que lê as teclas)."),
   ],
   "agenda":[
     ("15 min","English Lab + revisão","Termos do dia e relembrar behaviors."),
     ("20 min","Teoria: condição → ação","O que é um evento e como o Construct pensa."),
     ("45 min","Plataformas + teclado","Montar a fase com plataformas Solid e testar o percurso."),
     ("30 min","Moedas + placar","Variável Score, objeto Text e o evento de coletar moeda."),
     ("10 min","Preview + salvar","Coletar moeda deve somar no placar. Salvar."),
   ],
   "notes":[
     {"kind":"teoria","title":"Evento = condição → ação","big":"IF",
      "body":"No Event Sheet, cada evento tem uma CONDIÇÃO (ex.: 'Player colidiu com Coin') e uma ou mais AÇÕES (ex.: 'destruir a moeda', 'somar 1 ponto'). É o 'SE isto, ENTÃO faça aquilo' de toda programação."},
     {"kind":"cultura","title":"Variáveis guardam o estado","big":"Score",
      "body":"Uma variável global 'Score' guarda quantas moedas você pegou. O jogo lê e atualiza esse número o tempo todo. Sem variáveis, o jogo não teria memória — nem placar, nem vidas, nem fases."},
   ],
   "steps":[
     {"title":"Monte as plataformas","body":"Duplique o chão para criar plataformas em alturas diferentes. Todas com behavior Solid."},
     {"title":"Adicione o Keyboard","body":"Insira o objeto Keyboard (uma vez no projeto). Ele permite que os eventos leiam as teclas."},
     {"title":"Crie a variável Score","body":"No Event Sheet, crie uma Global variable chamada Score, tipo número, começando em 0."},
     {"title":"Desenhe as moedas","body":"Crie um Sprite 'Coin' e espalhe várias cópias pela fase, em cima das plataformas."},
     {"title":"Mostre o placar","body":"Insira um objeto Text 'PlacarTxt' na camada Game e posicione no canto da tela."},
     {"title":"Programe coletar moeda","body":"No Event Sheet, adicione o evento do próximo slide: colidir com a moeda a destrói e soma 1 ponto.",
      "tip":"Add event → Player → On collision with Coin. Depois Add action."},
   ],
   "code_slides":[
     {"title":"Evento: coletar moeda","lang":"Eventos (Construct 3)","lines":[
        "-- Global variable:  Score = 0",
        "",
        "QUANDO  Player  ->  On collision with  Coin",
        "FAÇA    Coin       ->  Destroy",
        "        System     ->  Add 1 to Score",
        "        PlacarTxt  ->  Set text: \"Moedas: \" & Score",
     ],"caption":"Uma condição (colisão) e três ações. Assim funciona quase toda regra de jogo no Construct."},
   ],
   "challenge":{"title":"Desafio: Circuito de moedas","items":[
      "Posicione pelo menos 6 moedas exigindo pulos para pegar.",
      "Garanta que o placar sobe certinho a cada moeda.",
      "Equilibre: alcançável, mas que dê vontade de arriscar.",
   ],"closing":"Amanhã: como PERDER (espinhos) e como VENCER (a bandeira)."},
   "teacher":{
     "objectives":["Construir um nível com plataformas Solid.",
       "Adicionar o objeto Keyboard e entender seu papel.",
       "Criar e usar uma variável global (Score).",
       "Escrever o primeiro evento colisão → ações."],
     "pitfalls":[
       "Placar não atualiza: a ação Set text precisa concatenar com & Score.",
       "Moeda não some: confirme a condição 'On collision with Coin' no objeto certo.",
       "Muitos objetos sem nome: mantenha Player/Coin/PlacarTxt nomeados.",
       "Plataformas sem Solid: o Player as atravessa."],
     "checks":["O nível tem plataformas navegáveis?","Coletar moeda soma no placar?",
       "A variável Score existe e começa em 0?"],
     "differ":["Mais rápidos: som ao coletar (objeto Audio) — cuidado com o nº de eventos.",
       "Apoio: dar o evento da moeda pronto para eles replicarem."],
   }},
  # -------- DIA 3
  {"n":3,"title":"As regras: perder e vencer","theme_line":"Game design","focus":"Adicionar o obstáculo que reinicia a fase (perder) e a bandeira de vitória (vencer) — o jogo fica completo.",
   "english":[
     ("Variable","VÉ-ri-a-bol","Variável (valor guardado, ex.: Score)."),
     ("Restart","ri-STÁRT","Reiniciar a fase."),
     ("Win","UÍN","Vencer."),
     ("Lose","LÚZ","Perder."),
     ("Layout","LÊI-aut","Cena/fase (usaremos uma de vitória)."),
     ("Text","TÉKST","Objeto de texto na tela."),
   ],
   "agenda":[
     ("15 min","English Lab + plano","Termos e desenhar as regras de vitória/derrota."),
     ("20 min","Teoria: o loop do jogo","Começar, jogar, perder/vencer, repetir."),
     ("45 min","Espinhos (perder)","Sprite Spike + evento que reinicia a fase ao tocar."),
     ("30 min","Bandeira (vencer)","Sprite Goal + layout de Vitória com Text."),
     ("10 min","Preview completo + salvar","Testar perder E vencer. Salvar."),
   ],
   "notes":[
     {"kind":"teoria","title":"O loop do jogo","big":"LOOP",
      "body":"Todo jogo tem um ciclo: um estado inicial, uma jogabilidade, e condições de FIM (vitória ou derrota) que reiniciam o ciclo. Hoje você fecha esse loop: dá um jeito de perder e um de vencer."},
     {"kind":"cultura","title":"Otimização: menos é mais","big":"< 50",
      "body":"O plano Free limita a 50 eventos. Isso não é problema — é treino de dev! Reaproveite eventos, use variáveis e evite repetição. Jogos incríveis já foram feitos com pouquíssimos eventos."},
   ],
   "steps":[
     {"title":"Crie o espinho (Spike)","body":"Desenhe um Sprite 'Spike' e coloque em pontos perigosos da fase, entre plataformas."},
     {"title":"Programe a derrota","body":"Evento: Player colide com Spike → System: Restart layout. Encostar no espinho reinicia a fase."},
     {"title":"Crie a bandeira (Goal)","body":"Desenhe um Sprite 'Goal' no fim do percurso — o objetivo a alcançar."},
     {"title":"Crie o layout de Vitória","body":"Adicione um novo Layout 'Vitoria' com um Text grande: 'VOCÊ VENCEU!' e o placar."},
     {"title":"Programe a vitória","body":"Evento: Player colide com Goal → System: Go to layout 'Vitoria'. Fim feliz!",
      "tip":"Veja o contador de eventos: dá para fazer tudo isso com poucos!"},
   ],
   "code_slides":[
     {"title":"Eventos: perder e vencer","lang":"Eventos (Construct 3)","lines":[
        "QUANDO  Player  ->  On collision with  Spike",
        "FAÇA    System  ->  Restart layout          -- perdeu",
        "",
        "QUANDO  Player  ->  On collision with  Goal",
        "FAÇA    System  ->  Go to layout \"Vitoria\"   -- venceu",
     ],"caption":"Duas regras fecham o loop do jogo: uma para perder, outra para vencer."},
   ],
   "challenge":{"title":"Desafio: Dificuldade justa","items":[
      "Coloque espinhos que exijam cuidado, mas nunca 'impossíveis'.",
      "Garanta um caminho claro até a bandeira (Goal).",
      "Teste perder e vencer pelo menos 1 vez cada.",
   ],"closing":"Amanhã: polir, checar os limites do plano Free e apresentar!"},
   "teacher":{
     "objectives":["Modelar condições de derrota e vitória.",
       "Usar System: Restart layout e Go to layout.",
       "Compreender o loop de jogo.",
       "Aplicar otimização dentro do limite de 50 eventos."],
     "pitfalls":[
       "Restart não funciona: a ação correta é System > Restart layout.",
       "Layout de vitória em branco: adicione um Text visível.",
       "Goal reiniciando em vez de vencer: confira se a colisão é com Goal, não Spike.",
       "Estouro de eventos: revise duplicações; combine condições."],
     "checks":["Encostar no espinho reinicia a fase?","Encostar na bandeira leva à vitória?",
       "O projeto está com 2 camadas e < 50 eventos?"],
     "differ":["Mais rápidos: sistema de vidas (variável Lives) em vez de restart imediato.",
       "Apoio: fornecer os 2 eventos prontos para posicionar os sprites."],
   }},
  # -------- DIA 4
  {"n":4,"title":"Polir, testar e apresentar","theme_line":"Release","focus":"Ajustes finais dentro dos limites do plano Free, caça a bugs, tela de instruções e apresentação no Preview.",
   "english":[
     ("Debug","di-BÂG","Encontrar e corrigir erros."),
     ("Playtest","PLÊI-test","Testar jogando de verdade."),
     ("Preview","PRÍ-viu","Rodar o jogo (como apresentamos)."),
     ("Bug","BÂG","Erro/defeito no jogo."),
     ("Polish","PÓ-lish","Polir: dar acabamento e capricho."),
     ("Feedback","FÍD-bek","Opinião de quem jogou."),
   ],
   "agenda":[
     ("10 min","English Lab + checklist","Termos e lista de bugs a caçar."),
     ("30 min","Playtest + corrigir","Jogar do início ao fim; anotar e consertar bugs."),
     ("25 min","Polir + tela de início","Texto de instruções, cores, som opcional (dentro dos limites)."),
     ("35 min","Testar do colega + ajustes","Feedback em dupla e últimos retoques."),
     ("20 min","Apresentações","Cada um joga no Preview na TV e explica 1 evento."),
   ],
   "notes":[
     {"kind":"teoria","title":"Debugar é ler o próprio jogo","big":"BUG",
      "body":"Debugar é investigar por que algo não funciona: um evento na ordem errada, um objeto sem nome, uma variável não atualizada. O painel de eventos é o seu mapa — leia de cima para baixo."},
     {"kind":"dica","title":"Apresente como um dev","body":"Ao mostrar seu jogo, explique UMA regra que você programou (condição → ação) e uma decisão de otimização. Isso mostra que você entende o que construiu, não só que 'funcionou'."},
   ],
   "steps":[
     {"title":"Playtest completo","body":"Jogue do início ao fim várias vezes. Anote todo bug: pulo, colisão, placar, vitória."},
     {"title":"Corrija os bugs","body":"Volte ao Event Sheet e conserte. Teste no Preview a cada correção."},
     {"title":"Tela de instruções","body":"Adicione um Text de início explicando os controles e o objetivo (pegar moedas, evitar espinhos)."},
     {"title":"Polir dentro dos limites","body":"Ajuste cores, posições e (opcional) um som. Confira: 2 camadas e menos de 50 eventos."},
     {"title":"Apresente no Preview","body":"Rode o jogo na TV. Mostre andar, coletar, perder e vencer. Explique 1 evento que você criou."},
   ],
   "challenge":{"title":"Missão final: Build jogável","items":[
      "O jogo precisa começar, jogar, PERDER e VENCER sem travar.",
      "Instruções na tela + placar funcionando.",
      "Dentro do plano Free (2 camadas, < 50 eventos) e apresentado no Preview.",
   ],"closing":"Parabéns, game dev! Você programou um jogo completo respeitando limites reais."},
   "teacher":{
     "objectives":["Realizar playtest e depuração sistemática.",
       "Adicionar UX básica (instruções na tela).",
       "Validar o projeto dentro dos limites do plano Free.",
       "Apresentar explicando a lógica (condição → ação)."],
     "pitfalls":[
       "Bug 'fantasma': cheque a ordem dos eventos (executam de cima para baixo).",
       "Estouro de 50 eventos ao polir: priorize; remova eventos redundantes.",
       "Preview não abre: verifique o navegador (Chrome) e pop-ups bloqueados.",
       "Tempo curto: garanta que todos tenham um build jogável antes das falas."],
     "checks":["O jogo tem começo, perder e vencer sem travar?","Há instruções e placar na tela?",
       "Está dentro de 2 camadas e < 50 eventos?"],
     "differ":["Mais rápidos: adicionar 2ª fase (novo layout) ou inimigo simples.",
       "Apoio: focar em deixar 1 fase curta 100% jogável e apresentável."],
   }},
 ],
}

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv)>1 else "."
    a,b = engine.build_all(course, outdir)
    print("OK", a, b)
