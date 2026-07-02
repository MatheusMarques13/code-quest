# -*- coding: utf-8 -*-
from reportlab.lib.colors import HexColor
import engine, sys

theme = {
    "primary":  HexColor("#FF6B4A"),
    "secondary":HexColor("#12B5A5"),
    "accent":   HexColor("#FFC531"),
    "ink":      HexColor("#2C2340"),
    "paper":    HexColor("#FFF6F0"),
    "confetti":[HexColor("#FFC531"),HexColor("#12B5A5"),HexColor("#FF6B4A"),
                HexColor("#7C5CFF"),HexColor("#4ECDC4"),HexColor("#FF8FB1")],
}

course = {
 "slug":"01_KIDS_MagicaVoxel",
 "audience":"KIDS",
 "age":"6 a 9 anos",
 "platform":"MagicaVoxel",
 "title":"Construtores de Mundos 3D",
 "subtitle":"Crie o seu bichinho e o mundinho dele — tudo feito de cubos mágicos!",
 "day_len":"2 HORAS",
 "theme":theme,
 "seal":("COORDENAÇÃO PEDAGÓGICA","CNA Via Sul","★ ★ ★"),
 "source_note":"Fontes: magicavoxel.net • ephtracy.github.io",
 "sources":[
   "MagicaVoxel — página oficial do autor (ephtracy): ephtracy.github.io e magicavoxel.net. Programa gratuito, sem necessidade de conta (verificado em jul/2026).",
 ],
 "overview":("Um curso de férias 100% prático e lúdico para crianças de 6 a 9 anos. Em 4 encontros, "
   "cada criança aprende a modelar em 3D usando o MagicaVoxel — um programa onde tudo é construído com "
   "cubinhos (voxels), como peças de montar digitais. O projeto final é um personagem 3D com o seu próprio "
   "mini-cenário, transformado numa imagem renderizada bonita que a criança apresenta para a turma. O curso mistura "
   "construção livre, pequenas doses de teoria contadas como história e uma 'English Lab' diária com os termos em "
   "inglês que aparecem na tela do programa."),
 "teacher_intro":{
   "project_goal":("Ao final, cada aluno entrega UMA imagem renderizada (PNG) do seu personagem 3D dentro de um "
      "pequeno cenário, e faz uma apresentação de 1 minuto contando quem é o personagem e como o construiu."),
   "setup":[
     "Baixe o MagicaVoxel ANTES da aula em magicavoxel.net (ou ephtracy.github.io). É um .zip: basta descompactar e abrir — não precisa instalar nem criar conta.",
     "Deixe o programa já aberto em cada máquina e uma cópia aberta na TV para você demonstrar.",
     "Crie uma pasta 'MEUS MUNDOS' na área de trabalho de cada computador para salvar os arquivos .vox e as imagens.",
     "Teste o mouse: modelar em 3D exige girar a câmera. Mouse com rodinha facilita muito para as crianças.",
   ],
   "materials":[
     "Computador Windows ou Mac (MagicaVoxel roda nos dois e tem menos de 20 MB).",
     "Mouse com rodinha (altamente recomendado para girar e dar zoom).",
     "MagicaVoxel — sem conta e sem anúncio (magicavoxel.net).",
     "TV ou projetor para o aluno acompanhar o passo a passo.",
   ],
   "management":[
     "Nesta idade, demonstre 1 passo na TV e espere todos repetirem antes de seguir. Nunca acumule 2 passos.",
     "Use a regra do 'polegar para cima': só avance quando todos os polegares subirem.",
     "Elogie tentativas, não só acertos. Errar e apagar (erase) faz parte — mostre o Undo (Ctrl+Z) no 1º dia.",
     "Combine um 'gesto de silêncio' para reunir a atenção na TV durante as demonstrações.",
   ],
 },
 "closing":("Você construiu um personagem em 3D e um mundinho inteiro só com cubos — e ainda transformou tudo "
   "numa imagem de verdade! Continue criando em casa — o MagicaVoxel fica no seu computador."),
 "assessment_intro":("A avaliação é leve e comemorativa. O foco do Dia 4 é finalizar, renderizar a imagem e "
   "apresentar. Todos terminam com um projeto pronto — o objetivo é a alegria de criar e a coragem de mostrar."),
 "rubric":[
   "Construiu um personagem reconhecível (cabeça, corpo, detalhes)? — Sim / Quase / Vamos ajudar",
   "Montou um mini-cenário com pelo menos 2 objetos (chão + algo)? — Sim / Quase / Vamos ajudar",
   "Gerou a imagem renderizada (PNG) e salvou na pasta? — Sim / Quase / Vamos ajudar",
   "Apresentou em ~1 minuto contando sobre o personagem? — Sim / Quase / Vamos ajudar",
 ],
 "presentation":[
   "Monte um 'cinema': projete cada imagem renderizada na TV, uma por vez.",
   "Cada criança fala 3 coisas: o nome do personagem, o que ele faz e a parte mais difícil de construir.",
   "A turma responde com o 'aplauso de chuva' (bater palmas devagar e ir acelerando).",
   "Entregue um 'Diploma de Construtor de Mundos 3D' para cada aluno.",
 ],
 "days":[
  # ---------------- DIA 1
  {"n":1,"title":"Bem-vindo ao mundo dos cubos!","theme_line":"Primeiro contato",
   "focus":"Abrir o MagicaVoxel, girar a câmera em 3D, escolher cores e colocar/apagar os primeiros cubos.",
   "english":[
     ("Voxel","VÓK-sel","Um cubo 3D. É o 'pixel' do mundo em 3 dimensões."),
     ("Attach","a-TÉTCH","Encaixar / adicionar um cubo novo."),
     ("Erase","i-RÊIS","Apagar um cubo."),
     ("Palette","PÁ-let","A caixinha com todas as cores."),
     ("Model","MÓ-del","O seu desenho em 3D."),
     ("Undo","ân-DÚ","Desfazer o último erro."),
   ],
   "agenda":[
     ("15 min","Boas-vindas + English Lab","Combinados da turma e os termos em inglês do dia."),
     ("15 min","História: o que é 3D?","Demonstração na TV: 2D é chapado, 3D a gente gira em volta."),
     ("55 min","Mão na massa","Girar a câmera, escolher cor, attach e erase. Construir uma torre."),
     ("25 min","Desafio livre","Cada um cria uma forma simples só com cubos."),
     ("10 min","Salvar + rodada final","Salvar o arquivo e mostrar 1 criação na TV."),
   ],
   "notes":[
     {"kind":"teoria","title":"2D x 3D: qual é a diferença?","big":"3D",
      "body":"No 2D o desenho é chapado, como no papel. No 3D a gente pode GIRAR em volta e ver por cima, por baixo e por trás. Cada cubinho do nosso 3D tem um nome: voxel!"},
     {"kind":"cultura","title":"Você já joga com voxels!","big":"CUBOS",
      "body":"Muitos jogos e desenhos são feitos de cubos, como o mundo do Minecraft. Hoje você vai ser a pessoa que CONSTRÓI esse tipo de mundo, e não só quem joga."},
   ],
   "steps":[
     {"title":"Abra o programa","body":"Abra o MagicaVoxel. Vai aparecer um modelo pronto na tela. Esse é o nosso 'palco' 3D.",
      "tip":"Não precisa instalar nada nem fazer login. É só abrir e criar!"},
     {"title":"Gire a câmera","body":"Segure o botão esquerdo do mouse e arraste no espaço vazio para GIRAR em volta. Role a rodinha para aproximar (zoom).",
      "tip":"Brinque de olhar o modelo por cima, por baixo e por trás."},
     {"title":"Escolha uma cor","body":"Do lado da tela fica a Palette (caixa de cores). Clique na cor que você quiser usar."},
     {"title":"Attach: coloque cubos","body":"Com o modo Attach ligado, clique no modelo para colar um voxel. Segure e arraste para colocar vários de uma vez!"},
     {"title":"Erase: apague os erros","body":"Clique no botão Erase e depois clique nos cubos que quer tirar. Errou? Use o Undo (Ctrl+Z) para voltar.",
      "tip":"Errar faz parte! Todo construtor apaga e tenta de novo."},
     {"title":"Construa uma torre colorida","body":"Empilhe cubos de cores diferentes e faça uma torre ou um docinho. Gire para ver de todos os lados."},
   ],
   "challenge":{"title":"Desafio: A Torre Arco-Íris","items":[
      "Construa uma torre usando pelo menos 4 cores diferentes.",
      "Ela precisa ter uma parte que 'sai para o lado' (não pode ser só reta!).",
      "Gire a câmera e mostre sua torre por 3 lados diferentes.",
   ],"closing":"Terminou? Ajude um colega a girar a câmera dele. :)"},
   "teacher":{
     "objectives":["Abrir e navegar no MagicaVoxel com autonomia (girar e dar zoom).",
        "Diferenciar 2D de 3D com as próprias palavras.",
        "Usar Attach, Erase e Undo para construir e corrigir.",
        "Reconhecer o termo 'voxel' e associá-lo a um cubo 3D."],
     "pitfalls":[
        "Câmera 'sumiu' / modelo fora da tela: role o zoom para trás e gire. Ensine a não ter medo de girar.",
        "A criança clica e move sem querer: mostre a diferença entre arrastar no VAZIO (gira a câmera) e clicar NO modelo (cola voxel).",
        "Mouse sem rodinha: configure antes; sem rodinha, use as teclas de zoom.",
        "Frustração ao errar: normalize o erro e ensine o Ctrl+Z logo no início."],
     "checks":["Todos conseguem girar a câmera 360º?","Todos colocaram e apagaram pelo menos 1 voxel?",
        "Todos salvaram o arquivo na pasta MEUS MUNDOS?"],
     "differ":["Mais rápidos: pedir uma torre com um 'telhado' inclinado.",
        "Precisam de apoio: dar uma forma-alvo simples (um coração ou uma casinha 5x5) para copiar."],
   }},
  # ---------------- DIA 2
  {"n":2,"title":"Meu personagem 3D","theme_line":"Criar o herói","focus":"Construir um personagem com cabeça, corpo, braços e pernas usando o espelho (mirror) para ficar simétrico.",
   "english":[
     ("Character","KÉ-rak-ter","Personagem."),
     ("Mirror","MÍ-ror","Espelho: copia igual dos dois lados."),
     ("Box","BÓKS","Ferramenta caixa: cria vários cubos de uma vez."),
     ("Head","RÉD","Cabeça."),
     ("Body","BÓ-di","Corpo."),
     ("Eyes","ÁIS","Olhos."),
   ],
   "agenda":[
     ("15 min","English Lab + revisão","Termos do dia e relembrar attach/erase."),
     ("15 min","Demo: o espelho mágico","Mostrar na TV como o Mirror copia dos dois lados."),
     ("60 min","Construir o personagem","Corpo, cabeça, braços e pernas passo a passo."),
     ("20 min","Rosto e cores","Olhos, boca e pintar o personagem."),
     ("10 min","Salvar + mostrar","Salvar o .vox e apresentar na TV."),
   ],
   "notes":[
     {"kind":"teoria","title":"Simetria: os dois lados iguais","big":"=",
      "body":"Nosso corpo é simétrico: o lado direito parece o esquerdo. O Mirror (espelho) do programa faz isso sozinho — você constrói um olho e o outro aparece do outro lado, igualzinho!"},
     {"kind":"dica","title":"Planeje antes de colar","body":"Grandes criadores pensam primeiro. Imagine o seu personagem: é um bicho? um robô? um monstrinho fofo? Decida a forma da cabeça e do corpo antes de empilhar os cubos."},
   ],
   "steps":[
     {"title":"Faça o corpo","body":"Comece por um bloco para o corpo. Use a ferramenta Box para criar vários cubos de uma vez e ganhar tempo.",
      "tip":"Box = você clica e arrasta para 'puxar' uma caixa inteira."},
     {"title":"Ligue o espelho (Mirror)","body":"Ative o Mirror no eixo X. Agora tudo que você fizer de um lado aparece igual do outro lado."},
     {"title":"Cabeça e pescoço","body":"Coloque a cabeça em cima do corpo. Deixe um pescocinho de 1 cubo, se quiser."},
     {"title":"Braços e pernas","body":"Com o espelho ligado, construa 1 braço e 1 perna — o outro lado aparece sozinho, simétrico!"},
     {"title":"Rosto e cores","body":"Escolha cores novas na Palette e faça olhos e boca. Pinte a roupa e a pele do seu jeito."},
   ],
   "challenge":{"title":"Desafio: Dê um superpoder a ele!","items":[
      "Adicione UM detalhe especial: chapéu, antena, asa, rabo ou coroa.",
      "Use o espelho para deixar esse detalhe simétrico (quando fizer sentido).",
      "Dê um nome ao seu personagem — vamos usar no Dia 4!",
   ],"closing":"Guarde bem o nome: ele vai na sua apresentação final."},
   "teacher":{
     "objectives":["Planejar uma figura antes de construir.",
       "Usar a ferramenta Box para ganhar eficiência.",
       "Aplicar o Mirror para criar simetria.",
       "Compor um personagem com partes (cabeça/corpo/membros) e cores."],
     "pitfalls":[
       "Mirror faz o dobro sem querer: explique que, com o espelho ligado, apagar de um lado apaga do outro.",
       "Personagem gigante/minúsculo: oriente ~15 a 20 cubos de altura para caber no cenário do Dia 3.",
       "Braços 'flutuando': mostre que precisa haver cubos conectando ao corpo.",
       "A cor 'some': lembre de reclicar a cor na Palette antes de continuar."],
     "checks":["O personagem tem cabeça, corpo e membros?","Usou o Mirror pelo menos uma vez?",
       "Deu um nome e salvou o .vox?"],
     "differ":["Mais rápidos: adicionar textura de roupa (listras, bolsos) cubo a cubo.",
       "Apoio: oferecer um molde de boneco simples (formato 'biscoito') para preencher."],
   }},
  # ---------------- DIA 3
  {"n":3,"title":"O mundinho do meu personagem","theme_line":"Construir o cenário","focus":"Montar um mini-cenário ao redor do personagem: chão, uma árvore, uma casa ou objetos.",
   "english":[
     ("Scene","SÍN","Cenário / cena."),
     ("Ground","GRÁUND","Chão."),
     ("Tree","TRÍ","Árvore."),
     ("House","RÁUS","Casa."),
     ("World","UÓRLD","Mundo."),
     ("Save","SÊIV","Salvar."),
   ],
   "agenda":[
     ("15 min","English Lab + ideia do mundo","Termos do dia e escolher o tema do cenário."),
     ("15 min","Demo: montando um chão","Como criar uma base grande e um objeto (árvore)."),
     ("60 min","Construir o cenário","Chão + 2 ou 3 objetos ao redor do personagem."),
     ("20 min","Detalhes e cores","Flores, nuvens, pedras, caminho..."),
     ("10 min","Salvar + revisar","Salvar tudo e conferir se o personagem está no cenário."),
   ],
   "notes":[
     {"kind":"cultura","title":"Todo jogo tem um mapa","big":"MAPA",
      "body":"O lugar onde o personagem vive se chama cenário (scene). Nos jogos, é o mapa ou a fase. Um bom cenário conta uma história: floresta, espaço, cidade, fundo do mar..."},
     {"kind":"curiosidade","title":"Escala: grande e pequeno","big":"TAM",
      "body":"Uma árvore deve ser MAIOR que o personagem; uma flor, menor. Cuidar do tamanho (escala) faz o mundo parecer de verdade."},
   ],
   "steps":[
     {"title":"Crie o chão (ground)","body":"Faça uma base plana embaixo do personagem usando a ferramenta Box. Esse é o chão do mundo.",
      "tip":"Chão verde vira grama; marrom vira terra; azul vira água."},
     {"title":"Plante uma árvore","body":"Faça um tronco (marrom) e uma copa (verde) por cima. Lembre: a árvore é maior que o personagem."},
     {"title":"Construa uma casa ou objeto","body":"Monte uma casinha simples (paredes + telhado) OU objetos do seu tema: foguete, castelo, cogumelo gigante..."},
     {"title":"Espalhe detalhes","body":"Adicione 3 detalhes pequenos: flores, pedras, nuvens ou um caminho de cubos."},
     {"title":"Salve e exporte","body":"Salve o arquivo .vox na pasta MEUS MUNDOS. Esse arquivo guarda TUDO para o Dia 4.",
      "tip":"Salvar sempre! Assim nada se perde de um dia para o outro."},
   ],
   "challenge":{"title":"Desafio: Conte uma história","items":[
      "O seu cenário precisa deixar claro ONDE o personagem vive.",
      "Inclua pelo menos 3 tipos de objeto diferentes.",
      "Esconda um 'segredo' no mapa (um item escondido atrás de algo).",
   ],"closing":"No Dia 4 vamos deixar tudo lindo com luz e sombra!"},
   "teacher":{
     "objectives":["Compreender cenário/scene como o 'mundo' do personagem.",
       "Aplicar a noção de escala (objetos maiores/menores).",
       "Construir uma base e múltiplos objetos numa mesma cena.",
       "Salvar/exportar o projeto com segurança."],
     "pitfalls":[
       "Personagem 'afundado' no chão: reposicione para ficar EM CIMA da base.",
       "Cena gigante e lenta: limite o tamanho do chão (ex.: 30x30) para não pesar.",
       "Aluno esquece de salvar: faça um 'momento salvar' coletivo a cada 20 minutos.",
       "Objetos todos do mesmo tamanho: reforce a escala com exemplos na TV."],
     "checks":["Há um chão e o personagem está sobre ele?","Existem pelo menos 3 objetos?",
       "O arquivo .vox foi salvo na pasta?"],
     "differ":["Mais rápidos: criar relevo (morrinhos), água ou uma ponte.",
       "Apoio: fornecer um 'kit' de formas prontas (tronco, copa, telhado) para copiar."],
   }},
  # ---------------- DIA 4
  {"n":4,"title":"Luz, câmera, render!","theme_line":"Finalizar e apresentar","focus":"Ajustes finais, ligar o modo Render com luz e sombra, exportar a imagem e apresentar para a turma.",
   "english":[
     ("Render","RÊN-der","Transformar o modelo numa imagem bonita com luz."),
     ("Light","LÁIT","Luz."),
     ("Shadow","XÁ-dou","Sombra."),
     ("Camera","KÉ-me-ra","Câmera (o ponto de vista)."),
     ("Export","ÉKS-port","Salvar a imagem final."),
     ("Present","pri-ZÉNT","Apresentar."),
   ],
   "agenda":[
     ("10 min","English Lab + aquecer","Termos do dia e revisão rápida."),
     ("30 min","Retoques finais","Últimos ajustes no personagem e no cenário."),
     ("25 min","Render + exportar imagem","Ligar o Render, ajustar a luz e salvar o PNG."),
     ("35 min","Preparar a apresentação","Ensaiar as 3 frases e organizar quem fala quando."),
     ("20 min","Apresentações + diplomas","Cada um mostra a imagem na TV. Aplausos e diploma!"),
   ],
   "notes":[
     {"kind":"teoria","title":"O que é 'render'?","big":"LUZ",
      "body":"Render é quando o computador calcula a LUZ e a SOMBRA e transforma os seus cubos numa imagem de verdade, bonita e brilhante. É como tirar uma foto profissional do seu mundo!"},
     {"kind":"dica","title":"Apresentar dá um friozinho — e tudo bem","body":"Respire fundo e lembre das suas 3 frases: (1) o nome do personagem, (2) o que ele faz e (3) a parte mais difícil de construir. Você criou isso — pode se orgulhar!"},
   ],
   "steps":[
     {"title":"Retoques finais","body":"Abra o seu arquivo salvo. Conserte o que faltou: uma cor, um detalhe, deixar tudo no lugar."},
     {"title":"Ligue o modo Render","body":"No topo, troque para o modo Render. O seu mundo vai ganhar luz e sombra automaticamente. Uau!",
      "tip":"Gire a câmera para achar o ângulo mais bonito do seu personagem."},
     {"title":"Ajuste a luz","body":"Mexa na luz (sol) e no fundo até o seu personagem ficar bem iluminado e com uma sombra legal."},
     {"title":"Exporte a imagem","body":"Salve a imagem (Export / PNG) na pasta MEUS MUNDOS. Essa é a sua obra final!"},
     {"title":"Apresente","body":"Mostre a sua imagem na TV e diga as suas 3 frases. Sorria: você é um Construtor de Mundos 3D!"},
   ],
   "challenge":{"title":"Missão final: A foto perfeita","items":[
      "Ache um ângulo de câmera onde dê para ver o personagem E o cenário.",
      "Deixe a luz batendo de um lado para criar sombra.",
      "Exporte a imagem e escolha um título para a sua obra.",
   ],"closing":"Pronto! Hora de apresentar e comemorar!"},
   "teacher":{
     "objectives":["Entender render como o cálculo de luz/sombra que gera a imagem final.",
       "Enquadrar a câmera para uma boa composição.",
       "Exportar um PNG do projeto.",
       "Apresentar o trabalho com uma estrutura simples de 3 frases."],
     "pitfalls":[
       "Render escuro demais: aumente a luz/sol ou clareie o fundo.",
       "Aluno não acha o Export: circule e faça junto; salve sempre na mesma pasta.",
       "Timidez na apresentação: permita apresentar em dupla ou ler as 3 frases de um cartão.",
       "Falta de tempo: priorize EXPORTAR a imagem de todos antes de começar as falas."],
     "checks":["Todos geraram e salvaram o PNG?","Todos têm as 3 frases prontas?",
       "A imagem mostra personagem + cenário?"],
     "differ":["Mais rápidos: exportar 2 ângulos diferentes e escolher o melhor.",
       "Apoio: ajudar no enquadramento e apresentar junto do professor."],
   }},
 ],
}

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv)>1 else "."
    a,b = engine.build_all(course, outdir)
    print("OK", a, b)
