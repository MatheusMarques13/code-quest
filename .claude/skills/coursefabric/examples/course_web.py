# -*- coding: utf-8 -*-
from reportlab.lib.colors import HexColor
import engine, sys

theme = {
    "primary":  HexColor("#0EA5A9"),
    "secondary":HexColor("#F59E0B"),
    "accent":   HexColor("#FDE047"),
    "ink":      HexColor("#0B2E2E"),
    "paper":    HexColor("#E9F7F6"),
    "confetti":[HexColor("#0EA5A9"),HexColor("#F59E0B"),HexColor("#FDE047"),
                HexColor("#8B5CF6"),HexColor("#EF476F"),HexColor("#22D3EE")],
}

course = {
 "slug":"04_YOUNG_HTML_CSS_JS",
 "audience":"YOUNG WEB",
 "age":"14+ anos",
 "platform":"HTML · CSS · JS",
 "title":"Crie a Web: sua Página Interativa",
 "subtitle":"Programe do zero uma página com HTML, CSS e JavaScript — incluindo um mini-jogo que funciona de verdade.",
 "day_len":"2 HORAS",
 "theme":theme,
 "seal":("COORDENAÇÃO PEDAGÓGICA","CNA Via Sul","★ ★ ★"),
 "source_note":"Fontes: code.visualstudio.com • developer.mozilla.org",
 "sources":[
   "VS Code — site oficial: code.visualstudio.com. Editor de código gratuito, sem conta (verificado em jul/2026).",
   "MDN Web Docs (Mozilla): developer.mozilla.org. Referência oficial de HTML, CSS e JavaScript.",
 ],
 "overview":("Curso de férias para jovens de 14+ que querem entender a linguagem por trás de todo site. Em 4 encontros "
   "cada aluno constrói do zero uma página web interativa usando as três tecnologias fundamentais da web: "
   "HTML (estrutura), CSS (design) e JavaScript (interatividade). O projeto final é uma página pessoal estilizada com "
   "um mini-jogo de Pedra, Papel e Tesoura funcionando e um botão que troca o tema (claro/escuro). O curso usa apenas "
   "um editor de código e o navegador. Cada dia abre com uma 'English Lab' dos termos técnicos, já "
   "que a programação é toda em inglês."),
 "teacher_intro":{
   "project_goal":("Ao final, cada aluno entrega um arquivo index.html (página pessoal) com: estrutura em HTML, "
      "estilo em CSS (cores, fontes, layout com flexbox), um mini-jogo de Pedra/Papel/Tesoura em JavaScript e um "
      "botão de trocar tema. Apresenta a página aberta no navegador, na TV."),
   "setup":[
     "Instale um editor antes: VS Code (code.visualstudio.com) é o recomendado, sem conta.",
     "Alternativa sem instalar nada: use o Bloco de Notas / TextEdit e abra o arquivo no navegador. Também funciona.",
     "Crie uma pasta 'minha-pagina' por aluno com um index.html dentro. Ensine a abrir esse arquivo no navegador (duplo clique).",
     "Fluxo do curso: editar → salvar (Ctrl+S) → atualizar o navegador (F5) para ver a mudança.",
   ],
   "materials":[
     "Qualquer computador (Windows, Mac ou Linux) com um navegador.",
     "Editor de código: VS Code (ou até o Bloco de Notas), sem conta.",
     "Navegador (Chrome, Edge, Firefox) — já vem no computador.",
     "(Opcional) Conta no Netlify ou GitHub para publicar no Dia 4.",
   ],
   "management":[
     "Erro mais comum é esquecer de SALVAR ou de ATUALIZAR (F5). Repita esse ciclo até virar hábito.",
     "Programação diferencia maiúsculas de minúsculas e exige fechar tags/chaves. Mostre a indentação desde o Dia 1.",
     "Use o Console do navegador (F12) desde cedo — é onde os erros de JavaScript aparecem.",
     "Incentive personalização (nome, cores, textos): a página é de cada um. Copiar sem entender não vale.",
   ],
 },
 "closing":("Você aprendeu as três linguagens que sustentam TODA a web — HTML, CSS e JavaScript — e construiu uma "
   "página interativa de verdade, com um jogo que funciona. Esse conhecimento abre a porta para sites, apps e muito "
   "mais. Continue criando!"),
 "assessment_intro":("A avaliação é por demonstração no navegador. No Dia 4 cada aluno testa, corrige com ajuda do "
   "Console, deixa a página responsiva e apresenta. O foco é uma página COMPLETA e interativa: estrutura + estilo + "
   "um recurso em JavaScript funcionando."),
 "rubric":[
   "A página tem estrutura HTML válida (título, textos, botões)? — Sim / Parcial / Revisar",
   "Tem estilo em CSS (cores, fontes, layout com flexbox)? — Sim / Parcial / Revisar",
   "O mini-jogo em JavaScript funciona (responde ao clique)? — Sim / Parcial / Revisar",
   "Foi testada, ficou responsiva e foi apresentada no navegador? — Sim / Parcial / Revisar",
 ],
 "presentation":[
   "Cada aluno abre a própria página no navegador, na TV, e joga o mini-jogo ao vivo.",
   "Mostra o código e explica 1 trecho de cada linguagem (uma tag, uma regra CSS, uma função JS).",
   "Conta o bug mais difícil que resolveu e como o Console ajudou.",
   "A turma sugere 1 recurso novo (placar, som, nova cor de tema).",
 ],
 "days":[
  # -------- DIA 1  HTML
  {"n":1,"title":"HTML: a estrutura da página","theme_line":"O esqueleto","focus":"Montar a estrutura da página em HTML: o esqueleto do documento, títulos, textos, imagem, link e um botão.",
   "english":[
     ("Tag","TÉG","Marcação como <p>. Quase sempre abre e fecha: <p></p>."),
     ("Element","É-le-ment","Uma tag + seu conteúdo (o 'bloco' completo)."),
     ("Attribute","Á-tri-biut","Info extra dentro da tag (ex.: src, href)."),
     ("Head","RÉD","Cabeçalho do documento (dados invisíveis)."),
     ("Body","BÓ-di","Corpo: o conteúdo que aparece na tela."),
     ("Heading","RÉ-ding","Título (<h1> é o maior)."),
   ],
   "agenda":[
     ("15 min","Boas-vindas + English Lab","Combinados e termos do dia."),
     ("15 min","Como a web funciona","O navegador lê HTML e desenha a página."),
     ("20 min","Setup: editor + navegador","Criar index.html e abrir no navegador."),
     ("55 min","Construir a estrutura","Esqueleto, títulos, texto, imagem, link e botão."),
     ("15 min","Salvar + atualizar","Ciclo salvar (Ctrl+S) e atualizar (F5)."),
   ],
   "notes":[
     {"kind":"teoria","title":"O que é HTML?","big":"HTML",
      "body":"HTML é a linguagem que descreve a ESTRUTURA da página: o que é título, o que é parágrafo, o que é imagem. O navegador lê esse texto e desenha a página. Sem HTML, não há página."},
     {"kind":"cultura","title":"Tags vêm em pares","big":"</>",
      "body":"Quase toda tag abre e fecha: <p>texto</p>. O que fica entre elas é o conteúdo. Esquecer de fechar uma tag é o erro nº 1 de quem começa — cuidado com isso!"},
   ],
   "steps":[
     {"title":"Abra o editor e crie o arquivo","body":"No VS Code (ou Bloco de Notas), crie um arquivo chamado index.html numa pasta sua.",
      "tip":"O nome index.html é especial: é a página inicial de qualquer site."},
     {"title":"Escreva o esqueleto","body":"Digite a estrutura básica do próximo slide: DOCTYPE, html, head e body. É a base de toda página."},
     {"title":"Abra no navegador","body":"Salve (Ctrl+S) e dê duplo clique no arquivo para abrir no navegador. Você verá seu título aparecer."},
     {"title":"Adicione conteúdo","body":"Dentro do body, coloque um <h1>, um <p>, uma <img>, um <a> (link) e um <button> (2º slide de código)."},
     {"title":"Salve e atualize","body":"A cada mudança: Ctrl+S no editor e F5 no navegador. Assim você vê a página evoluindo.",
      "tip":"Sempre que 'nada mudou', você provavelmente esqueceu de salvar ou de atualizar."},
   ],
   "code_slides":[
     {"title":"O esqueleto HTML","lang":"HTML","lines":[
        "<!DOCTYPE html>",
        "<html lang=\"pt-br\">",
        "<head>",
        "  <meta charset=\"utf-8\">",
        "  <title>Minha Página</title>",
        "</head>",
        "<body>",
        "  <h1>Oi! Eu sou o(a) [seu nome]</h1>",
        "</body>",
        "</html>",
     ],"caption":"Salve como index.html e abra no navegador. Todo documento HTML tem head (dados) e body (conteúdo)."},
     {"title":"Conteúdo da página","lang":"HTML","lines":[
        "<h1>Meu Perfil</h1>",
        "<img src=\"foto.png\" alt=\"minha foto\" width=\"150\">",
        "<p>Eu gosto de games e tecnologia.</p>",
        "<a href=\"https://exemplo.com\">Meu link</a>",
        "<button id=\"btnJogar\">Jogar!</button>",
     ],"caption":"Título, imagem, texto, link e um botão. O id do botão será usado pelo JavaScript no Dia 3."},
   ],
   "challenge":{"title":"Desafio: Sua página, sua cara","items":[
      "Troque os textos pelos seus (nome, o que você gosta).",
      "Adicione uma lista (<ul><li>) com 3 hobbies.",
      "Garanta que TODAS as tags estão fechadas corretamente.",
   ],"closing":"Amanhã: deixar tudo bonito com CSS."},
   "teacher":{
     "objectives":["Entender o papel do HTML (estrutura) e como o navegador o lê.",
       "Criar e abrir um index.html.",
       "Usar as tags essenciais: h1, p, img, a, button, ul/li.",
       "Adotar o ciclo salvar (Ctrl+S) → atualizar (F5)."],
     "pitfalls":[
       "Tag não fechada: a página 'quebra'. Revise pares de abertura/fechamento.",
       "Imagem não aparece: o arquivo foto.png precisa estar NA MESMA pasta (ou ajuste o src).",
       "Abriram o arquivo errado: confirme extensão .html (não .txt).",
       "'Não mudou nada': faltou salvar ou atualizar."],
     "checks":["Todos abriram um index.html no navegador?","Há h1, p, img, a e button na página?",
       "Todos praticaram salvar + atualizar?"],
     "differ":["Mais rápidos: adicionar seções com <h2> e mais listas.",
       "Apoio: fornecer o esqueleto pronto para colar e personalizar."],
   }},
  # -------- DIA 2  CSS
  {"n":2,"title":"CSS: o design da página","theme_line":"Estilo e layout","focus":"Estilizar a página com CSS: cores, fontes, o box model e um layout centralizado com flexbox.",
   "english":[
     ("Selector","se-LÉK-tor","O que o CSS mira (ex.: body, button, .classe)."),
     ("Class","CLÁS","Um 'apelido' (.container) para estilizar vários elementos."),
     ("Property","PRÓ-per-ti","O que muda (color, font-size, margin...)."),
     ("Color","CÂ-lor","Cor (ex.: #0EA5A9)."),
     ("Margin","MÁR-jin","Espaço POR FORA do elemento."),
     ("Flexbox","FLÉKS-boks","Sistema para alinhar elementos em linha/coluna."),
   ],
   "agenda":[
     ("15 min","English Lab + revisão","Termos do dia e conferir o HTML de ontem."),
     ("15 min","HTML x CSS","Conteúdo (HTML) vs aparência (CSS)."),
     ("20 min","Ligar o CSS","Adicionar <style> e o primeiro seletor."),
     ("55 min","Estilizar tudo","Cores, fontes, box model, botão e flexbox."),
     ("15 min","Ajustes + salvar","Refinar espaçamentos e cores. Salvar."),
   ],
   "notes":[
     {"kind":"teoria","title":"HTML estrutura, CSS embeleza","big":"CSS",
      "body":"O HTML diz O QUE é cada coisa; o CSS diz COMO cada coisa aparece: cor, tamanho, fonte, posição. Separar conteúdo de estilo é uma das ideias mais importantes da web."},
     {"kind":"cultura","title":"O box model","big":"BOX",
      "body":"Todo elemento é uma caixa com: conteúdo, padding (espaço interno), border (borda) e margin (espaço externo). Entender a 'caixa' é o segredo para controlar qualquer layout."},
   ],
   "steps":[
     {"title":"Adicione o <style>","body":"No <head>, crie uma tag <style></style>. É onde o CSS vai morar (jeito mais simples para começar)."},
     {"title":"Estilize o body","body":"Escolha fonte, cor de fundo e cor do texto para a página inteira (1º slide de código)."},
     {"title":"Deixe o botão bonito","body":"Dê cor, padding e cantos arredondados (border-radius) ao <button>. Ele vira um botão de verdade."},
     {"title":"Centralize com flexbox","body":"Crie uma .classe com display:flex para alinhar e centralizar os elementos (2º slide de código)."},
     {"title":"Refine","body":"Ajuste tamanhos, espaços (margin/padding) e cores até a página ficar do seu jeito.",
      "tip":"Mude 1 propriedade por vez e atualize (F5) para ver o efeito."},
   ],
   "code_slides":[
     {"title":"Estilo base (body e button)","lang":"CSS","lines":[
        "body {",
        "  font-family: sans-serif;",
        "  background: #0f172a;",
        "  color: #f8fafc;",
        "  text-align: center;",
        "}",
        "button {",
        "  background: #0ea5a9;",
        "  color: #ffffff;",
        "  padding: 12px 22px;",
        "  border: none;",
        "  border-radius: 10px;",
        "}",
     ],"caption":"Cada regra é seletor { propriedade: valor; }. Aqui o body e o button ganham cor, fonte e cantos."},
     {"title":"Layout com flexbox","lang":"CSS","lines":[
        ".container {",
        "  display: flex;",
        "  gap: 16px;",
        "  justify-content: center;",
        "  align-items: center;",
        "}",
     ],"caption":"Coloque os botões dentro de uma <div class=\"container\"> para alinhá-los lado a lado, centralizados."},
   ],
   "challenge":{"title":"Desafio: Identidade visual","items":[
      "Defina uma paleta de 2 ou 3 cores e use-a de forma consistente.",
      "Deixe o botão com um efeito de hover (button:hover { ... }).",
      "Garanta bom espaçamento (nada 'grudado').",
   ],"closing":"Amanhã: dar VIDA à página com JavaScript e criar o mini-jogo!"},
   "teacher":{
     "objectives":["Compreender a separação HTML (conteúdo) x CSS (estilo).",
       "Usar seletores, propriedades e o box model.",
       "Estilizar texto, cores e um botão.",
       "Centralizar elementos com flexbox."],
     "pitfalls":[
       "CSS 'não pega': confira se o <style> está no <head> e a sintaxe (dois-pontos e ponto-e-vírgula).",
       "Esqueceram as chaves { }: cada regra precisa abrir e fechar.",
       "Cor não muda: nome/HEX inválido; use #rrggbb.",
       "Flexbox sem efeito: os itens precisam estar DENTRO do elemento com display:flex."],
     "checks":["A página tem cores e fonte definidas?","O botão está estilizado?",
       "Usaram flexbox para alinhar algo?"],
     "differ":["Mais rápidos: gradientes, sombras (box-shadow) e transições.",
       "Apoio: fornecer o bloco CSS base para colar e ajustar cores."],
   }},
  # -------- DIA 3  JS
  {"n":3,"title":"JavaScript: a página ganha vida","theme_line":"Interatividade","focus":"Programar em JavaScript: variáveis, funções, eventos de clique e o mini-jogo de Pedra, Papel e Tesoura.",
   "english":[
     ("Variable","VÉ-ri-a-bol","Uma 'caixinha' que guarda um valor (let/const)."),
     ("Function","FÂNK-shon","Um bloco de código que executa uma tarefa."),
     ("Event","i-VÊNT","Algo que acontece (ex.: um clique)."),
     ("Click","CLIK","O evento de clicar (onclick)."),
     ("Console","con-SÓL","Painel do navegador onde vemos erros (F12)."),
     ("Random","RÉN-dom","Aleatório (Math.random gera sorteio)."),
   ],
   "agenda":[
     ("15 min","English Lab + plano","Termos do dia e a lógica do jogo."),
     ("15 min","O que é JavaScript","A linguagem que reage e muda a página."),
     ("25 min","Primeiro clique","<script>, função e onclick; ver no Console."),
     ("55 min","Mini-jogo + tema","Pedra/Papel/Tesoura com Math.random e trocar tema."),
     ("10 min","Testar + salvar","Jogar algumas vezes e conferir o resultado."),
   ],
   "notes":[
     {"kind":"teoria","title":"JavaScript reage a eventos","big":"JS",
      "body":"Se HTML é estrutura e CSS é estilo, JavaScript é o COMPORTAMENTO. Ele escuta eventos (como cliques) e muda a página em tempo real: troca textos, cores, calcula, sorteia. É o que torna a página 'viva'."},
     {"kind":"cultura","title":"O Console é seu amigo","big":"F12",
      "body":"Aperte F12 no navegador para abrir o Console. É lá que aparecem os erros de JavaScript e onde o console.log mostra mensagens. Todo dev vive de olho no Console."},
   ],
   "steps":[
     {"title":"Adicione o <script>","body":"Antes de </body>, crie uma tag <script></script>. É onde o JavaScript vai ficar."},
     {"title":"Primeiro clique","body":"Crie uma função e ligue-a a um botão com onclick. Use console.log para ver a resposta (1º slide)."},
     {"title":"Prepare o jogo","body":"Adicione 3 botões (pedra, papel, tesoura) e um <p id=\"res\"></p> para mostrar o resultado."},
     {"title":"Programe o jogo","body":"Escreva a função jogar() com Math.random e if/else para decidir quem vence (2º slide de código)."},
     {"title":"Botão de trocar tema","body":"Crie um botão que alterna claro/escuro com classList.toggle (3º slide). A página vira duas!",
      "tip":"Erros? Abra o Console (F12) e leia a mensagem — ela indica a linha."},
   ],
   "code_slides":[
     {"title":"Função + clique","lang":"HTML + JavaScript","lines":[
        "<button onclick=\"jogar('pedra')\">Pedra</button>",
        "<p id=\"res\"></p>",
        "",
        "<script>",
        "  function jogar(escolha) {",
        "    console.log(\"Você jogou:\", escolha);",
        "  }",
        "</script>",
     ],"caption":"onclick chama a função ao clicar. console.log mostra a mensagem no Console (F12)."},
     {"title":"O jogo: Pedra, Papel e Tesoura","lang":"JavaScript","lines":[
        "function jogar(escolha) {",
        "  const op = [\"pedra\", \"papel\", \"tesoura\"];",
        "  const pc = op[Math.floor(Math.random() * 3)];",
        "  let r;",
        "  if (escolha === pc) r = \"Empate!\";",
        "  else if (",
        "    (escolha===\"pedra\"   && pc===\"tesoura\") ||",
        "    (escolha===\"papel\"   && pc===\"pedra\")   ||",
        "    (escolha===\"tesoura\" && pc===\"papel\")",
        "  ) r = \"Você venceu!\";",
        "  else r = \"Você perdeu...\";",
        "  document.getElementById(\"res\").textContent = \"PC: \"+pc+\" - \"+r;",
        "}",
     ],"caption":"Math.random sorteia o PC; o if/else aplica as regras; o resultado aparece no <p id='res'>."},
     {"title":"Trocar o tema (claro/escuro)","lang":"HTML + JavaScript","lines":[
        "<button onclick=\"document.body.classList.toggle('claro')\">",
        "  Trocar tema",
        "</button>",
        "",
        "<!-- no CSS: -->",
        ".claro { background: #f8fafc; color: #0f172a; }",
     ],"caption":"classList.toggle liga/desliga a classe 'claro' no body, alternando o tema num clique."},
   ],
   "challenge":{"title":"Desafio: Deixe o jogo seu","items":[
      "Adicione um placar (variável) que conta suas vitórias.",
      "Mude as mensagens de resultado para o seu estilo.",
      "Garanta que o botão de tema funciona nos dois sentidos.",
   ],"closing":"Amanhã: caçar bugs no Console, deixar responsiva e apresentar!"},
   "teacher":{
     "objectives":["Compreender JavaScript como comportamento (reage a eventos).",
       "Usar variáveis (let/const), funções e onclick.",
       "Manipular a página com getElementById/textContent.",
       "Aplicar Math.random e condicionais (if/else)."],
     "pitfalls":[
       "Função não roda: o nome no onclick deve ser IGUAL ao da função (maiúsc./minúsc. contam).",
       "id não encontrado: o getElementById precisa bater com o id no HTML.",
       "Aspas trocadas: mantenha o padrão (retas) e feche pares.",
       "Erro silencioso: abra o Console (F12) e leia a linha indicada."],
     "checks":["O clique executa a função?","O mini-jogo responde e mostra resultado?",
       "O botão de tema alterna claro/escuro?"],
     "differ":["Mais rápidos: placar com vitórias/derrotas e reset.",
       "Apoio: fornecer a função jogar() pronta para colar e explicar linha a linha."],
   }},
  # -------- DIA 4  Deploy
  {"n":4,"title":"Testar, publicar e apresentar","theme_line":"Ao ar!","focus":"Depurar com o Console, deixar a página responsiva, publicar (opcional) e apresentar no navegador.",
   "english":[
     ("Bug","BÂG","Um erro no código."),
     ("Debug","di-BÂG","Encontrar e corrigir o erro."),
     ("Browser","BRÁU-zer","Navegador (Chrome, Edge, Firefox)."),
     ("Responsive","res-PÓN-siv","Que se adapta a telas de tamanhos diferentes."),
     ("Console","con-SÓL","Painel de erros/mensagens (F12)."),
     ("Deploy","di-PLÓI","Publicar o site na internet."),
   ],
   "agenda":[
     ("10 min","English Lab + checklist","Termos do dia e lista de bugs a caçar."),
     ("30 min","Debug no Console","Abrir F12, ler erros e corrigir a página."),
     ("25 min","Responsivo + polir","Meta viewport, tamanhos flexíveis e acabamento."),
     ("35 min","Publicar (opcional) + ensaiar","Netlify Drop/GitHub Pages e preparar a fala."),
     ("20 min","Apresentações","Cada um mostra a página e joga o mini-jogo na TV."),
   ],
   "notes":[
     {"kind":"teoria","title":"Debug: ler o erro é meio caminho","big":"BUG",
      "body":"Bug é qualquer comportamento errado. O Console (F12) mostra a mensagem e a LINHA do problema. Aprender a ler esse recado é uma das habilidades mais valiosas de quem programa."},
     {"kind":"dica","title":"Publicar na internet","body":"Você pode colocar a página no ar: arraste a pasta no Netlify Drop ou use o GitHub Pages. Aí é só compartilhar o link com quem quiser — sua página no mundo real!"},
   ],
   "steps":[
     {"title":"Cace bugs no Console","body":"Abra o navegador, aperte F12 e veja o Console. Corrija cada erro (nome, id, aspas, chaves)."},
     {"title":"Deixe responsiva","body":"No <head>, adicione a meta viewport e use tamanhos flexíveis (%, flex) para funcionar no celular (slide)."},
     {"title":"Polir","body":"Revise cores, espaçamentos e textos. Confira se o jogo e o tema funcionam sempre."},
     {"title":"Publicar (opcional)","body":"Arraste a pasta em app.netlify.com/drop OU use GitHub Pages. Você recebe um link público para compartilhar."},
     {"title":"Apresente","body":"Abra a página na TV, jogue o mini-jogo e mostre 1 trecho de HTML, 1 de CSS e 1 de JS que você criou."},
   ],
   "code_slides":[
     {"title":"Tornar responsivo","lang":"HTML + CSS","lines":[
        "<!-- dentro do <head> -->",
        "<meta name=\"viewport\"",
        "      content=\"width=device-width, initial-scale=1\">",
        "",
        "/* no CSS: largura flexível */",
        "img { max-width: 100%; height: auto; }",
     ],"caption":"A meta viewport faz o navegador respeitar o tamanho da tela; max-width:100% evita imagens estourando."},
   ],
   "challenge":{"title":"Missão final: No ar!","items":[
      "Zero erros no Console (F12).",
      "Página legível no computador E no celular.",
      "Mini-jogo e tema funcionando; apresentada (e, se quiser, publicada).",
   ],"closing":"Parabéns! Você é oficialmente um(a) criador(a) da web."},
   "teacher":{
     "objectives":["Depurar usando o Console do navegador.",
       "Tornar a página responsiva (viewport + tamanhos flexíveis).",
       "Publicar o site (Netlify Drop / GitHub Pages) — opcional.",
       "Apresentar explicando um trecho de cada linguagem."],
     "pitfalls":[
       "Erros ignorados: garanta que TODOS abram o Console e leiam as mensagens.",
       "Não fica responsiva: faltou a meta viewport no <head>.",
       "Publicação confusa: Netlify Drop (arrastar a pasta) é o caminho mais simples em sala.",
       "Tempo curto: priorize página funcional + apresentação; deploy é bônus."],
     "checks":["A página está sem erros no Console?","Funciona bem em tela pequena?",
       "Cada aluno apresentou e mostrou os 3 tipos de código?"],
     "differ":["Mais rápidos: publicar e customizar o link; adicionar mais um recurso JS.",
       "Apoio: focar em página local funcional e uma apresentação simples."],
   }},
 ],
}

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv)>1 else "."
    a,b = engine.build_all(course, outdir)
    print("OK", a, b)
