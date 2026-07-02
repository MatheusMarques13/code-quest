---
name: coursefabric
description: >-
  Generate course/curriculum PDFs plus matching promo posters from a simple Python spec.
  Produces a 16:9 STUDENT slide deck (for a TV/projector) and an A4 TEACHER guide: cover,
  per-day sections, English/vocabulary lab, agenda, optional "where to click" interface
  diagrams, theory/culture notes, step cards, code slides, challenges and closing; the
  teacher guide adds objectives, a vocab table, schedule, pitfalls, checks, differentiation,
  a rubric, sources and an authorship seal — with flat-art mascots and one themable design
  system. Also includes promo.py for square (1:1) brand posters / social art (headline,
  robot, CTA, footer logo). Use for: create a course, lesson plan, curriculum, material de
  curso, curso de férias, workshop or bootcamp handbook, teacher guide + student slides,
  course flyer or poster, arte de divulgação, cartaz do curso.
---

# coursefabric — course & curriculum PDF generator (+ promo posters)

coursefabric turns a structured Python `course` dict into **two matching PDFs**:

- **`<slug>_ALUNO.pdf`** — a 16:9 landscape slide deck for students to follow on a TV/projector
  (big type, one idea per slide).
- **`<slug>_PROFESSOR.pdf`** — an A4 portrait facilitator guide (dense, structured, printable).

Both share one theme (colors + fonts) so the set looks cohesive and professional.

## What each PDF contains

**Student deck (per day):** section divider → English/vocab lab → agenda timeline →
(optional) interface "where to click" diagram → theory/culture note slides → step-by-step
"hands-on" cards → (optional) code slides → challenge. Plus a global cover and closing.
Friendly mascots appear only on the **first, middle and last** slide of each day.

**Teacher guide:** cover + course overview + intro cards (project goal, room setup,
materials, facilitation tips); then per day: learning objectives, a vocab table, the lesson
schedule, the student step list, (optional) code blocks, common pitfalls, quick checks and
differentiation; finally an assessment section (rubric + presentation script), a
**"Fontes consultadas"** sources block, and an authorship **seal**.

## Requirements  (works on macOS / Windows / Linux)

- Python 3 with **reportlab**: `pip install reportlab` (add `--break-system-packages` only if
  pip complains about an externally-managed environment).
- **Fonts are bundled** — the DejaVu `.ttf` files ship inside this skill's `fonts/` folder and
  `engine.py` loads them **relative to itself**, so there is no system font install and no
  hardcoded OS path. (If `fonts/` is removed, it falls back to system DejaVu in common
  locations; on Linux `apt install fonts-dejavu`.)
- Optional, only for visual QA: **poppler** `pdftoppm` to render pages to PNG and eyeball them
  (`brew install poppler` on macOS, `apt install poppler-utils` on Linux).

`engine.py` is the whole design system. You normally do **not** edit it — you only write a
`course` dict and call `engine.build_all(course, outdir)`. Keep `engine.py`, `promo.py` and the
`fonts/` folder together (the example course sits next to them).

## Quick start

1. Copy `engine.py` and `example_course.py` into your working folder.
2. Edit a copy of `example_course.py` (it is a complete, working course) — change the text,
   keep the structure.
3. Build:

```bash
python3 example_course.py .        # writes <slug>_ALUNO.pdf and <slug>_PROFESSOR.pdf
```

or from your own code:

```python
import engine
from mycourse import course
engine.build_all(course, "/path/to/output")   # -> (aluno_pdf, professor_pdf)
```

4. **QA before delivering** (recommended): render a few pages and look at them.

```bash
pdftoppm -png -r 96 -f 1 -l 1 MYCOURSE_ALUNO.pdf preview   # page 1 -> preview-01.png
```

## Content schema (the `course` dict)

```python
theme = {
  "primary":   HexColor("#FF6B4A"),   # main brand color (cover, bands, badges)
  "secondary": HexColor("#12B5A5"),   # accents (agenda header, chips)
  "accent":    HexColor("#FFC531"),   # highlights (badges, step numbers)
  "ink":       HexColor("#2C2340"),   # dark text
  "paper":     HexColor("#FFF6F0"),   # light section background
  "confetti":  [HexColor("#..."), ...]# decorative shapes on cover/section/closing
}

course = {
  "slug": "01_KIDS_Platform",          # file name prefix; also selects built-in interface diagrams
  "audience": "KIDS",                   # short label (footer / teacher header)
  "age": "6 a 9 anos",                  # audience descriptor (used in teacher intro card title)
  "platform": "MagicaVoxel",            # tool/name shown on the cover badge
  "title": "Course Title",
  "subtitle": "One playful sentence.",
  "theme": theme,
  "seal": ("LINE 1", "Line 2", "★ line 3 ★"),   # 3-line stamp on the LAST page (student+teacher)
  "source_note": "Fontes: site.com",            # small line on the student closing slide
  "sources": ["Full citation 1 ...", "..."],    # bullets in the teacher "Fontes consultadas" block
  "overview": "Paragraph describing the whole course (teacher guide).",
  "teacher_intro": {
     "project_goal": "What each student delivers at the end.",
     "setup":     ["Prep step ...", "..."],
     "materials": ["Item ...", "..."],
     "management":["Facilitation tip ...", "..."],
  },
  "closing": "Congratulations paragraph (student closing slide).",
  "assessment_intro": "How day 4 / final assessment works (teacher).",
  "rubric":       ["Criterion? — Yes / Partial / Review", "..."],
  "presentation": ["Presentation-day step ...", "..."],
  "days": [
    {
      "n": 1,
      "title": "Day title",
      "theme_line": "short kicker",             # small chip on the section divider
      "focus": "One sentence: what today covers.",
      "english": [("Term","pro-NUN","meaning in the student's language."), ...],  # 6 recommended
      "agenda": [("15 min","Block label","Short description."), ...],  # minutes are NOT printed,
                                                                       # but are used to validate 120 min/day
      "notes": [                                # theory / culture / tip slides (0+)
        {"kind":"teoria",     "title":"...", "body":"...", "big":"KEY"},   # optional 'big' = concept word
        {"kind":"cultura",    "title":"...", "body":"..."},
        # kinds: teoria, cultura, dica, curiosidade, seguranca
      ],
      "steps": [                                # hands-on cards (0+)
        {"title":"Step title", "body":"What to do.", "tip":"optional tip"},
      ],
      "code_slides": [                          # optional dark "code editor" slides
        {"title":"Snippet name", "lang":"Language", "lines":["line1","line2"], "caption":"one line"},
      ],
      "challenge": {"title":"Challenge", "items":["...","..."], "closing":"optional line"},
      "teacher": {                              # teacher-only, per day
        "objectives": ["...","..."],
        "pitfalls":   ["Problem: fix.", "..."],
        "checks":     ["Did everyone ...?", "..."],
        "differ":     ["Faster: ...", "Support: ..."],
      },
    },
    # ... more days
  ],
}
```

### Notes on fields
- **Text is auto-escaped**, so you can write literal `<tags>`, `&`, `<` in any prose field
  (great for HTML/code courses). Only `code_slides["lines"]` are drawn verbatim.
- **English lab**: keep to ~6 terms/day (they lay out as a 2×3 grid; extras paginate).
- **Agenda minutes**: not printed on the slides, but keep each day summing to your class length
  (the example validates 120 min). Put the real schedule in the labels/descriptions.
- **Interface diagrams**: built in for slugs `01_KIDS_MagicaVoxel`, `02_TEENS_RobloxStudio`,
  `03_YOUNG_Construct3`, `04_YOUNG_HTML_CSS_JS` (see `SCREEN_DRAWER` / `SCREEN_INFO` in
  `engine.py`). For any other slug they are simply skipped — the deck still builds fine. To add
  a new platform diagram, write a `draw_<tool>(c,x,y,w,h,day)` function and register it.
- **Layout is dynamic**: titles/bodies reflow so text never collides. Keep body copy concise.

## Design cheatsheet (already handled by the engine)
- Student deck = 960×540 pt (16:9). Teacher = A4 portrait.
- Editorial teacher cards (white, hairline, accent tick, em-dash rows) — no cheesy colored side-bars.
- Credit/authorship shown only where you set it (`seal`, `source_note`, `sources`).
- Everything themable via the `theme` dict.

## Promo posters (`promo.py`)

Companion tool for **square (1:1) announcement art** for the course — Instagram/WhatsApp/
Facebook or print. One brand template, reused for every level/variant; only the text changes.
Each poster has: a small eyebrow, a `TURMA <LEVEL>` chip, a big navy headline with **one red
keyword**, body copy, a red **"Garanta a sua vaga ✓"** CTA pill, info badges, a friendly
flat-art **robot** (drawn in code), light brand shapes, and a **navy footer bar** with the
logo wordmark + a location line.

Edit the `SPECS` dict and run:

```bash
python3 promo.py all .        # builds PROMO_KIDS.pdf, PROMO_TEENS.pdf, PROMO_YOUNG.pdf
python3 promo.py kids out/    # one variant into ./out
```

```python
SPECS = {
  "kids": {
     "level": "KIDS",
     # headline: reportlab markup; wrap ONE word in red for the brand accent
     "headline": "Criação de <font color='#E2231A'>Mundos 3D</font>",
     "desc": "One or two sentences of body copy.",
  },
  # ... more variants
}
```

Then render a PNG to post/print and **look at it before sending**:

```bash
pdftoppm -png -singlefile -r 150 PROMO_KIDS.pdf PROMO_KIDS   # -> PROMO_KIDS.png (square)
```

Notes:
- Brand colors, the footer bar, the robot and the CTA are constants near the top of
  `promo.py` — tweak `NAVY`, `RED`, `BLUE`, the footer text, etc. there.
- The logo is a **typographic wordmark** (`logo_footer`), not official artwork. If you have
  the real transparent PNG, place it in the footer instead.
- Keep headlines to ~3–4 words (they set at ~68pt); keep `desc` to ~2 short lines.

## Good practice
1. Research/collect the real content first; cite internet-sourced facts in `sources`.
2. Fill the `course` dict; keep prose tight.
3. Build, then **render a few pages with `pdftoppm` and actually look at them** before sending.
4. Ship the two PDFs.
