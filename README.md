# Code Quest

Academia de criação de jogos para crianças — material exclusivo de aulas
particulares de programação (Prof. Matheus Marques).

Front-end estático, estética Ghibli (inspirado no RetroMynd Study Hub).

## Páginas
- `landing.html` — página de apresentação (entrada do site)
- `login.html` — login do aluno (frontend-only: salva no navegador)
- `index.html` — hub do aluno: Timer de Foco, Missões do Dia, Meus Projetos,
  Lições de código e sistema de moedas

## Rodar localmente
Basta abrir `landing.html` no navegador, ou servir a pasta:
```bash
npx serve .
```

## Deploy (Vercel)
Site 100% estático — é só importar este repositório na Vercel, sem build.

## Status
- [x] Landing, login e hub (frontend)
- [ ] Backend (Supabase): login real, nuvem e moedas sincronizadas
