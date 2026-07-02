# -*- coding: utf-8 -*-
"""
Motor de design para os Cursos de Ferias.
Gera:
  - Versao ALUNO  : slides 16:9 (para exibir na TV, texto grande, 1 ideia por tela)
  - Versao PROFESSOR : guia A4 retrato (roteiro imprimivel, denso e estruturado)
Desenvolvido por Matheus Marques.
"""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Paragraph, Table, TableStyle, SimpleDocTemplate,
                                Spacer, Frame, KeepTogether, ListFlowable, ListItem, Preformatted, Flowable)
import math
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.units import mm

# ---------------------------------------------------------------- fonts
# Cross-platform: prefer DejaVu fonts BUNDLED next to this file (portable, works in
# Claude Code on macOS/Windows/Linux); fall back to common system locations.
_HERE = os.path.dirname(os.path.abspath(__file__))
def _font_dir():
    for d in [os.path.join(_HERE, "fonts"),
              "/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/dejavu",
              "/usr/share/fonts/TTF", "/usr/local/share/fonts",
              "/Library/Fonts", os.path.expanduser("~/Library/Fonts"),
              r"C:\Windows\Fonts"]:
        if os.path.isfile(os.path.join(d, "DejaVuSans.ttf")):
            return d
    return os.path.join(_HERE, "fonts")   # portable fallback (bundle the .ttf here)
FONTDIR = _font_dir()
def _rf(name, fn): pdfmetrics.registerFont(TTFont(name, os.path.join(FONTDIR, fn)))
_rf("Body",    "DejaVuSans.ttf")
_rf("Body-B",  "DejaVuSans-Bold.ttf")
_rf("Body-I",  "DejaVuSans-Oblique.ttf")
_rf("Body-BI", "DejaVuSans-BoldOblique.ttf")
_rf("Mono",    "DejaVuSansMono.ttf")
_rf("Mono-B",  "DejaVuSansMono-Bold.ttf")
_rf("Cond-B",  "DejaVuSansCondensed-Bold.ttf")
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Body", normal="Body", bold="Body-B", italic="Body-I", boldItalic="Body-BI")

CREDIT = "Desenvolvido por Matheus Marques"
W, H = 960, 540          # slide 16:9

def mix(c1, c2, t):
    return Color(c1.red+(c2.red-c1.red)*t, c1.green+(c2.green-c1.green)*t, c1.blue+(c2.blue-c1.blue)*t)

def hx(c):
    return "#%02X%02X%02X" % (int(round(c.red*255)), int(round(c.green*255)), int(round(c.blue*255)))

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def escape_content(o):
    """Escape &,<,> in all content strings so tags in prose render literally.
    Code lines (key 'lines') stay raw — they are drawn on canvas, not parsed."""
    if isinstance(o, str):
        return esc(o)
    if isinstance(o, list):
        return [escape_content(x) for x in o]
    if isinstance(o, tuple):
        return tuple(escape_content(x) for x in o)
    if isinstance(o, dict):
        return {k: (v if k == "lines" else escape_content(v)) for k, v in o.items()}
    return o

# ---------------------------------------------------------------- low level draw
def rrect(c, x, y, w, h, r, fill=None, stroke=None, sw=1):
    if fill is not None:
        c.setFillColor(fill)
    if stroke is not None:
        c.setStrokeColor(stroke); c.setLineWidth(sw)
    c.roundRect(x, y, w, h, r, stroke=1 if stroke is not None else 0,
                fill=1 if fill is not None else 0)

def para(text, font="Body", size=18, color=black, leading=None, align=TA_LEFT,
         space_after=0, space_before=0):
    st = ParagraphStyle("s", fontName=font, fontSize=size,
                        leading=leading or size*1.28, textColor=color, alignment=align,
                        spaceAfter=space_after, spaceBefore=space_before)
    return Paragraph(text, st)

def draw_para(c, p, x, y_top, w, max_h=10000):
    """draw paragraph with its TOP-LEFT at (x, y_top). returns height used."""
    pw, ph = p.wrap(w, max_h)
    p.drawOn(c, x, y_top - ph)
    return ph

def confetti(c, colors, seed=0, zone="top"):
    """light decorative shapes."""
    import random
    rnd = random.Random(seed)
    shapes = 14
    for i in range(shapes):
        col = rnd.choice(colors)
        c.setFillColor(Color(col.red, col.green, col.blue, alpha=0.16))
        x = rnd.uniform(0, W)
        if zone == "top":
            y = rnd.uniform(H-120, H-8)
        else:
            y = rnd.uniform(8, 120)
        s = rnd.uniform(8, 22)
        k = rnd.random()
        if k < 0.34:
            c.rect(x, y, s, s, fill=1, stroke=0)
        elif k < 0.67:
            c.circle(x, y, s*0.55, fill=1, stroke=0)
        else:
            c.saveState(); c.translate(x, y); c.rotate(rnd.uniform(0,60))
            path = c.beginPath(); path.moveTo(0, s*0.6); path.lineTo(s*0.5, -s*0.4)
            path.lineTo(-s*0.5, -s*0.4); path.close(); c.drawPath(path, fill=1, stroke=0)
            c.restoreState()

def footer(c, th, page_label=None):
    # Credit line intentionally NOT drawn here (only on page 1 of each course).
    if page_label:
        c.setFillColor(HexColor("#b8bdc4"))
        c.setFont("Body-B", 9)
        c.drawRightString(W-30, 16, page_label)

def chip(c, x, y, text, bg, fg=white, font="Cond-B", size=12, padx=10, pady=6):
    tw = pdfmetrics.stringWidth(text, font, size)
    w = tw + padx*2; h = size + pady*2
    rrect(c, x, y, w, h, h/2, fill=bg)
    c.setFillColor(fg); c.setFont(font, size)
    c.drawString(x+padx, y+pady+1, text)
    return w, h

# ---- friendly flat-art mascot (original character) ---------------------------
def mascot(c, cx, cy, s=1.0, pose="wave", c1=None, c2=None, accent=None):
    c1 = c1 or HexColor("#5B7CFA"); c2 = c2 or HexColor("#EAF0FF"); accent = accent or HexColor("#FFC531")
    ol = mix(c1, black, 0.40)
    c.saveState(); c.translate(cx, cy); c.scale(s, s)
    def capsule(x,y,w,h,r,fill):
        c.setFillColor(fill); c.roundRect(x,y,w,h,r,fill=1,stroke=0)
    # feet
    c.setFillColor(ol); c.ellipse(-19,-52,-3,-41,fill=1,stroke=0); c.ellipse(3,-52,19,-41,fill=1,stroke=0)
    # arms (behind body)
    if pose=="cheer":
        c.saveState(); c.translate(-27,8); c.rotate(38); capsule(-6,-2,12,30,6,c1); c.restoreState()
        c.saveState(); c.translate(27,8); c.rotate(-38); capsule(-6,-2,12,30,6,c1); c.restoreState()
    else:
        capsule(-35,-16,12,30,6,c1)
        c.saveState(); c.translate(27,10); c.rotate(-42); capsule(-6,-2,12,30,6,c1); c.restoreState()
    # body
    c.setFillColor(c1); c.setStrokeColor(ol); c.setLineWidth(3); c.roundRect(-30,-42,60,74,24,fill=1,stroke=1)
    # belly
    c.setFillColor(c2); c.roundRect(-18,-34,36,44,15,fill=1,stroke=0)
    # antenna
    c.setStrokeColor(ol); c.setLineWidth(3); c.line(0,32,0,43)
    c.setFillColor(accent); c.circle(0,47,5,fill=1,stroke=0)
    # eyes
    for ex in (-11,11):
        c.setFillColor(white); c.circle(ex,7,8,fill=1,stroke=0)
        c.setStrokeColor(ol); c.setLineWidth(1.4); c.circle(ex,7,8,fill=0,stroke=1)
        c.setFillColor(HexColor("#232733")); c.circle(ex+1.4,6,3.6,fill=1,stroke=0)
        c.setFillColor(white); c.circle(ex+2.8,7.6,1.5,fill=1,stroke=0)
    # cheeks
    c.setFillColor(Color(1,0.42,0.5,alpha=0.55)); c.circle(-18,-3,4,fill=1,stroke=0); c.circle(18,-3,4,fill=1,stroke=0)
    # smile
    c.setStrokeColor(ol); c.setLineWidth(2.4)
    p=c.beginPath(); p.moveTo(-7,-9); p.curveTo(-3,-15,3,-15,7,-9); c.drawPath(p,fill=0,stroke=1)
    c.restoreState()

def seal(c, cx, cy, col, top, mid, bottom, scale=1.0):
    """A rubber-stamp style authorship seal (rotated rounded frame + 3 short lines)."""
    c.saveState(); c.translate(cx, cy); c.scale(scale, scale); c.rotate(-5)
    c.setStrokeColor(col); c.setLineWidth(2.6); c.roundRect(-146,-36,292,72,13,stroke=1,fill=0)
    c.setLineWidth(1); c.roundRect(-139,-29,278,58,9,stroke=1,fill=0)
    c.setFillColor(col)
    c.setFont("Cond-B", 10.5); c.drawCentredString(0, 15, top)
    c.setFont("Body-B", 16); c.drawCentredString(0, -6, mid)
    c.setFont("Cond-B", 9); c.drawCentredString(0, -26, bottom)
    c.restoreState()

class SealFlowable(Flowable):
    def __init__(self, col, top, mid, bottom, w, h=92):
        Flowable.__init__(self); self.col=col; self.top=top; self.mid=mid; self.bottom=bottom
        self.width=w; self.height=h
    def draw(self):
        seal(self.canv, self.width/2, self.height/2, self.col, self.top, self.mid, self.bottom, scale=0.9)

# ================================================================ STUDENT SLIDES
def s_cover(c, th, course):
    c.setFillColor(th["primary"]); c.rect(0,0,W,H, fill=1, stroke=0)
    # big soft blobs
    c.setFillColor(mix(th["primary"], white, 0.12)); c.circle(W*0.86, H*0.82, 220, fill=1, stroke=0)
    c.setFillColor(mix(th["primary"], black, 0.10)); c.circle(W*0.12, H*0.10, 190, fill=1, stroke=0)
    confetti(c, th["confetti"], seed=1, zone="top")
    confetti(c, th["confetti"], seed=2, zone="bottom")
    # course tag (top) — age intentionally not shown on the cover
    chip(c, 60, H-96, "CURSO DE FÉRIAS", mix(th["primary"], black,0.18), white, size=14)
    # title + subtitle (left column kept clear of the platform card on the right)
    left_w = (W-330) - 60 - 40
    th_h = draw_para(c, para(course["title"], "Body-B", 58, white, leading=62), 60, H-146, left_w)
    sub_top = H-146 - th_h - 20
    draw_para(c, para(course["subtitle"], "Body", 22, mix(th["primary"], white,0.90), leading=29),
              60, sub_top, left_w)
    # platform badge card
    bx, by, bw, bh = W-330, 172, 270, 116
    rrect(c, bx, by, bw, bh, 22, fill=white)
    c.setFillColor(th["secondary"]); c.setFont("Cond-B", 13); c.drawString(bx+24, by+bh-36, "PLATAFORMA")
    pfont = 30
    while pdfmetrics.stringWidth(course["platform"], "Body-B", pfont) > bw-46 and pfont > 15:
        pfont -= 1
    c.setFillColor(th["ink"]); c.setFont("Body-B", pfont); c.drawString(bx+24, by+30, course["platform"])
    # bottom strip
    chip(c, 60, 70, "4 DIAS", th["accent"], th["ink"], size=15)
    chip(c, 190, 70, "1 GRANDE PROJETO", th["accent"], th["ink"], size=15)
    # credit — bold, only on page 1 of the course (footer)
    c.setFillColor(Color(1,1,1,alpha=0.92)); c.setFont("Body-B", 12)
    c.drawString(60, 30, CREDIT)
    c.showPage()

def s_section(c, th, n, title, theme_line, focus, masc=False):
    c.setFillColor(th["paper"]); c.rect(0,0,W,H, fill=1, stroke=0)
    c.setFillColor(th["primary"]); c.rect(0,0,26,H, fill=1, stroke=0)
    confetti(c, th["confetti"], seed=10+n, zone="top")
    cx, cy = 250, H/2+18
    c.setFillColor(th["primary"]); c.circle(cx, cy, 120, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("Cond-B", 24); c.drawCentredString(cx, cy+38, "DIA")
    c.setFillColor(white); c.setFont("Body-B", 112); c.drawCentredString(cx, cy-56, str(n))
    x = 430
    chip(c, x, cy+96, theme_line.upper(), th["secondary"], white, size=13)
    th_h = draw_para(c, para(title, "Body-B", 44, th["ink"], leading=48), x, cy+74, W-x-54)
    draw_para(c, para(focus, "Body", 21, HexColor("#4a4f55"), leading=28), x, cy+74 - th_h - 20, W-x-54)
    if masc: mascot(c, cx, 94, 0.8, "wave", th["primary"], mix(th["primary"],white,0.85), th["accent"])
    footer(c, th, "DIA %d" % n)
    c.showPage()

def _panel_header(c, th, x, y, w, tag, title, tag_bg, tag_fg=white):
    tw,_ = chip(c, x, y-2, tag, tag_bg, tag_fg, size=12)
    c.setFillColor(th["ink"]); c.setFont("Body-B", 30)
    c.drawString(x+tw+16, y+2, title)

def s_english(c, th, n, terms, part=1, parts=1, masc=False):
    """draws up to 6 term-cards (2 x 3)."""
    c.setFillColor(HexColor("#0f1b2d")); c.rect(0,0,W,H, fill=1, stroke=0)
    for i in range(9):
        c.setFillColor(Color(1,1,1,alpha=0.04)); c.rect(0, H-60*i-30, W, 2, fill=1, stroke=0)
    lbl = "ENGLISH LAB  •  DIA %d"%n + (("  •  %d/%d"%(part,parts)) if parts>1 else "")
    chip(c, 60, H-92, lbl, HexColor("#ffd23f"), HexColor("#0f1b2d"), size=14)
    c.setFillColor(white); c.setFont("Body-B", 38); c.drawString(60, H-150, "Termos de hoje")
    c.setFillColor(HexColor("#9fb3c8")); c.setFont("Body-I", 16)
    c.drawString(60, H-176, "As plataformas estão em inglês. Aprenda as palavras antes de começar!")
    cols = 2
    cardw = (W-120-30)/cols
    cardh = 94
    x0, y0 = 60, H-200
    gx, gy = 30, 8
    acc = th["accent"]
    for i, (term, pron, mean) in enumerate(terms[:6]):
        r = i // cols; col = i % cols
        x = x0 + col*(cardw+gx); y = y0 - r*(cardh+gy) - cardh
        rrect(c, x, y, cardw, cardh, 16, fill=HexColor("#17233b"), stroke=HexColor("#2d3f5e"), sw=1.2)
        c.setFillColor(white); c.setFont("Body-B", 21); c.drawString(x+22, y+cardh-33, term)
        pf = 12; pw = pdfmetrics.stringWidth(pron, "Mono", pf) + 20
        c.setFillColor(Color(acc.red, acc.green, acc.blue, alpha=0.16))
        c.roundRect(x+cardw-pw-16, y+cardh-39, pw, 22, 11, fill=1, stroke=0)
        c.setFillColor(acc); c.setFont("Mono", pf); c.drawCentredString(x+cardw-pw/2-16, y+cardh-32, pron)
        draw_para(c, para(mean, "Body", 14.5, HexColor("#c7d3e0"), leading=18), x+22, y+cardh-52, cardw-44)
    if masc: mascot(c, W-86, H-82, 0.48, "wave", th["primary"], mix(th["primary"], white,0.85), th["accent"])
    footer(c, th, "DIA %d — ENGLISH"%n)
    c.showPage()

def s_agenda(c, th, n, total_label, blocks, masc=False):
    c.setFillColor(th["paper"]); c.rect(0,0,W,H, fill=1, stroke=0)
    _panel_header(c, th, 60, H-96, W-120, "AGENDA", "Como vai ser a aula de hoje", th["secondary"])
    x = 92; top = H-152; row_h = (top-64)/len(blocks)
    c.setStrokeColor(mix(th["primary"], white,0.4)); c.setLineWidth(3)
    c.line(x, 64, x, top)
    for i,(mins, label, desc) in enumerate(blocks):
        cy = top - i*row_h - row_h/2
        c.setFillColor(th["primary"]); c.circle(x, cy, 9, fill=1, stroke=0)
        c.setFillColor(white); c.circle(x, cy, 4, fill=1, stroke=0)
        c.setFillColor(th["ink"]); c.setFont("Body-B", 22); c.drawString(x+30, cy+4, label)
        draw_para(c, para(desc, "Body", 15.5, HexColor("#5a6068"), leading=19), x+30, cy-9, W-x-120)
    if masc: mascot(c, W-92, H-92, 0.5, "wave", th["primary"], mix(th["primary"], white,0.85), th["accent"])
    footer(c, th, "DIA %d — AGENDA"%n)
    c.showPage()

NOTE_STYLES = {
    "teoria":  ("TEORIA",        "#2563eb"),
    "cultura": ("CULTURA DIGITAL","#0f9d8b"),
    "dica":    ("DICA",          "#f59e0b"),
    "curiosidade": ("VOCÊ SABIA?","#a855f7"),
    "seguranca": ("SEGURANÇA",   "#ef4444"),
}
def s_note(c, th, n, kind, title, body, big_word=None, masc=False):
    base = HexColor(NOTE_STYLES[kind][1])
    c.setFillColor(mix(base, white, 0.90)); c.rect(0,0,W,H, fill=1, stroke=0)
    c.setFillColor(base); c.rect(0,0,W,120, fill=1, stroke=0)
    if not masc:
        c.setFillColor(mix(base, white,0.15)); c.circle(W-45, H-38, 104, fill=1, stroke=0)
    chip(c, 60, H-96, NOTE_STYLES[kind][0], base, white, size=14)
    th_h = draw_para(c, para(title, "Body-B", 34, mix(base,black,0.35), leading=39), 60, H-150, W-170)
    # two-column content region below the title; body (left) and concept card (right)
    # share the SAME vertical centre so everything is aligned and symmetric.
    region_top = (H-150 - th_h) - 26
    region_cy = (region_top + 82) / 2.0
    if big_word:
        cw, ch = 300, 178
        cx0 = W - 60 - cw
        rrect(c, cx0, region_cy - ch/2, cw, ch, 24, fill=white, stroke=base, sw=2)
        c.setFillColor(base); c.setFont("Body-B", 52); c.drawCentredString(cx0+cw/2, region_cy + 2, big_word)
        c.setFillColor(HexColor("#8a9099")); c.setFont("Body-I", 15)
        c.drawCentredString(cx0+cw/2, region_cy - 44, "conceito-chave")
        body_w = cx0 - 60 - 40
    else:
        body_w = W - 120
    p = para(body, "Body", 21, HexColor("#333a42"), leading=30)
    _, bh = p.wrap(body_w, 2000)
    p.drawOn(c, 60, region_cy - bh/2)   # body vertically centred on the same axis as the card
    if masc: mascot(c, W-92, H-90, 0.54, "wave", base, mix(base,white,0.86), th["accent"])
    footer(c, th, "DIA %d"%n)
    c.showPage()

def s_step(c, th, n, idx, total, title, body, tip=None, masc=False):
    c.setFillColor(white); c.rect(0,0,W,H, fill=1, stroke=0)
    c.setFillColor(th["primary"]); c.rect(0,0,W,80, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("Cond-B", 15); c.drawString(60, 31, ("MÃO NA MASSA  •  PASSO %d DE %d"%(idx,total)).upper())
    c.setFillColor(Color(1,1,1,alpha=0.9)); c.setFont("Body-B", 12); c.drawRightString(W-40, 31, "DIA %d"%n)
    # step number badge
    c.setFillColor(th["accent"]); c.circle(118, H-142, 58, fill=1, stroke=0)
    c.setFillColor(th["ink"]); c.setFont("Body-B", 58); c.drawCentredString(118, H-162, str(idx))
    tx = 206
    th_h = draw_para(c, para(title, "Body-B", 34, th["ink"], leading=39), tx, H-100, W-tx-70)
    body_top = H-100 - th_h - 16
    draw_para(c, para(body, "Body", 21, HexColor("#33383e"), leading=30), tx, body_top, W-tx-70)
    if tip:
        ty = 146
        rrect(c, tx, ty, W-tx-70, 92, 16, fill=HexColor("#fff7e6"), stroke=HexColor("#f2b13a"), sw=1.4)
        c.setFillColor(HexColor("#b45309")); c.setFont("Body-B", 14); c.drawString(tx+22, ty+60, "DICA")
        draw_para(c, para(tip, "Body", 16, HexColor("#7c4a03"), leading=20), tx+22, ty+42, W-tx-116)
    if masc: mascot(c, W-84, H-56, 0.44, "wave", th["primary"], mix(th["primary"], white,0.85), th["accent"])
    c.showPage()

def _is_comment(s):
    t = s.strip()
    return t.startswith("//") or t.startswith("#") or t.startswith("<!--") or t.startswith("--")

def s_code(c, th, n, title, lines, caption=None, lang="CÓDIGO", masc=False):
    c.setFillColor(HexColor("#0e1524")); c.rect(0,0,W,H, fill=1, stroke=0)
    chip(c, 60, H-90, lang.upper(), th["accent"], th["ink"], size=13)
    c.setFillColor(white); c.setFont("Body-B", 30); c.drawString(60, H-140, title)
    if masc: mascot(c, W-82, H-70, 0.44, "wave", th["primary"], mix(th["primary"], white,0.85), th["accent"])
    m = len(lines)
    line_h = 24 if m <= 8 else (20 if m <= 11 else 17)
    fs = 14 if m <= 8 else (12.5 if m <= 11 else 11)
    nf = 12 if m <= 8 else 10
    px, pw = 60, W-120
    ph = line_h*m + 42
    ytop = H-168
    min_py = 92 if caption else 58
    py = ytop - ph
    if py < min_py:
        line_h = max(13, int((ytop - min_py - 42) / max(m, 1)))
        fs = min(fs, line_h - 4); ph = line_h*m + 42; py = ytop - ph
    rrect(c, px, py, pw, ph, 16, fill=HexColor("#0a0f1c"), stroke=HexColor("#1e2a44"), sw=1.5)
    for i, dot in enumerate([HexColor("#ff5f56"),HexColor("#ffbd2e"),HexColor("#27c93f")]):
        c.setFillColor(dot); c.circle(px+24+i*20, py+ph-20, 5.5, fill=1, stroke=0)
    ty = py+ph-46
    for i, ln in enumerate(lines):
        c.setFillColor(HexColor("#3a4a66")); c.setFont("Mono", nf); c.drawRightString(px+46, ty, str(i+1))
        col = HexColor("#6b829e") if _is_comment(ln) else HexColor("#d6e6f5")
        c.setFillColor(col); c.setFont("Mono", fs); c.drawString(px+58, ty, ln)
        ty -= line_h
    if caption and py-14 > 40:
        draw_para(c, para("→ " + caption, "Body-I", 16, HexColor("#9fb3c8"), leading=21), 60, py-14, W-120)
    footer(c, th, "DIA %d — CÓDIGO"%n)
    c.showPage()

def s_challenge(c, th, n, title, items, closing=None, masc=False):
    c.setFillColor(th["ink"]); c.rect(0,0,W,H, fill=1, stroke=0)
    confetti(c, th["confetti"], seed=77+n, zone="top")
    confetti(c, th["confetti"], seed=88+n, zone="bottom")
    chip(c, 60, H-100, "DESAFIO", th["accent"], th["ink"], size=15)
    draw_para(c, para(title, "Body-B", 40, white, leading=44), 60, H-150, W-120)
    y = H-206
    iw = (W-300) if masc else (W-180)
    for it in items:
        c.setFillColor(th["accent"]); c.circle(78, y-4, 7, fill=1, stroke=0)
        h = draw_para(c, para(it, "Body", 21, HexColor("#e8eef5"), leading=27), 100, y+8, iw)
        y -= h + 16
    if closing:
        c.setFillColor(th["accent"]); c.setFont("Body-BI", 20); c.drawString(60, 66, closing)
    if masc: mascot(c, W-108, 130, 0.72, "cheer", th["primary"], mix(th["primary"], white,0.85), th["accent"])
    footer(c, th, "DIA %d — DESAFIO"%n)
    c.showPage()

def s_closing(c, th, course):
    c.setFillColor(th["primary"]); c.rect(0,0,W,H, fill=1, stroke=0)
    c.setFillColor(mix(th["primary"], black,0.10)); c.circle(W*0.15, H*0.9, 200, fill=1, stroke=0)
    confetti(c, th["confetti"], seed=5, zone="bottom")
    c.setFillColor(white); c.setFont("Body-B", 54); c.drawCentredString(W/2, H-150, "Parabéns!")
    bh = draw_para(c, para(course["closing"], "Body", 21, mix(th["primary"], white,0.94), leading=29, align=TA_CENTER),
                   140, H-192, W-280)
    txt = "VOCÊ VIROU UM CRIADOR DIGITAL"
    cw = pdfmetrics.stringWidth(txt, "Cond-B", 14) + 24
    chip(c, (W-cw)/2, (H-192) - bh - 32, txt, mix(th["primary"], black,0.20), white, size=14)
    # authorship seal (last page)
    seal(c, W/2, 122, mix(th["primary"], white, 0.92), course["seal"][0], course["seal"][1], course["seal"][2], scale=0.82)
    # source note (non-obstructive, bottom)
    if course.get("source_note"):
        c.setFillColor(mix(th["primary"], white, 0.72)); c.setFont("Body", 9.5)
        c.drawCentredString(W/2, 34, course["source_note"])
    c.showPage()

# ================================================================ INTERFACE DIAGRAMS
HLC = HexColor("#FF375F")   # highlight / attention color
def _t(c,x,y,s,f,sz,col): c.setFillColor(col); c.setFont(f,sz); c.drawString(x,y,s)
def _tc(c,x,y,s,f,sz,col): c.setFillColor(col); c.setFont(f,sz); c.drawCentredString(x,y,s)
def _hl(c,x,y,w,h,col=HLC,r=6):
    c.setStrokeColor(col); c.setLineWidth(3); c.roundRect(x-3,y-3,w+6,h+6,r,stroke=1,fill=0)
def _nb(c,x,y,num,col=HLC):
    c.setFillColor(col); c.circle(x,y,12,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("Body-B",13); c.drawCentredString(x,y-4.5,str(num))
def _arrow(c,x1,y1,x2,y2,col=HLC,sw=2.6):
    c.setStrokeColor(col); c.setLineWidth(sw); c.line(x1,y1,x2,y2)
    a=math.atan2(y2-y1,x2-x1); L=9; c.setFillColor(col)
    p=c.beginPath(); p.moveTo(x2,y2)
    p.lineTo(x2-L*math.cos(a-0.42), y2-L*math.sin(a-0.42))
    p.lineTo(x2-L*math.cos(a+0.42), y2-L*math.sin(a+0.42)); p.close()
    c.drawPath(p,fill=1,stroke=0)

def _figure(c,x,y):  # tiny voxel character (pixel cubes)
    grid=[(1,4,"#f4c542"),(2,4,"#f4c542"),(0,3,"#3aa0e0"),(1,3,"#3aa0e0"),(2,3,"#3aa0e0"),(3,3,"#3aa0e0"),
          (1,2,"#3aa0e0"),(2,2,"#3aa0e0"),(1,1,"#e0673a"),(2,1,"#e0673a"),(1,0,"#2ecc71"),(2,0,"#2ecc71")]
    s=13
    for gx,gy,col in grid:
        c.setFillColor(HexColor(col)); c.rect(x+gx*s, y+gy*s, s-2, s-2, fill=1, stroke=0)

# ---- MagicaVoxel
def draw_mv(c,x,y,w,h,day):
    rrect(c,x,y,w,h,10,fill=HexColor("#262626"))
    c.setFillColor(HexColor("#171717")); c.rect(x,y+h-28,w,28,fill=1,stroke=0)
    _t(c,x+14,y+h-19,"MagicaVoxel","Body-B",10,HexColor("#e6e6e6"))
    tx=x+w-210
    for name in ["Model","Render","World"]:
        onR=(name=="Render" and day==4)
        col=HLC if onR else (HexColor("#c9c9c9") if (name=="Model" and day!=4) else HexColor("#8a8a8a"))
        _t(c,tx,y+h-19,name,"Body-B",10.5,col)
        if onR: _hl(c,tx-6,y+h-24,60,21)
        tx+=68
    iy=y+10; ih=h-40
    # tools
    lx=x+10; lw=w*0.20
    rrect(c,lx,iy,lw,ih,7,fill=HexColor("#333333"))
    _t(c,lx+9,iy+ih-15,"FERRAMENTAS","Cond-B",7.5,HexColor("#9a9a9a"))
    tools=["Attach","Erase","Paint","Box","Mirror"]
    for i,tl in enumerate(tools):
        yy=iy+ih-34-i*((ih-40)/5.5)
        act=(tl=="Attach" and day==1) or (tl=="Box" and day in(2,3)) or (tl=="Mirror" and day==2)
        rrect(c,lx+8,yy-3,lw-16,20,4,fill=(HexColor("#3b7ddd") if act else HexColor("#424242")))
        _t(c,lx+15,yy+2,tl,"Body",9,white if act else HexColor("#d4d4d4"))
        if (tl=="Attach" and day==1) or (tl=="Mirror" and day==2): _hl(c,lx+8,yy-3,lw-16,20)
    # palette
    pw=w*0.20; px=x+w-pw-10
    rrect(c,px,iy,pw,ih,7,fill=HexColor("#333333"))
    _t(c,px+9,iy+ih-15,"PALETTE","Cond-B",7.5,HexColor("#9a9a9a"))
    pc=["#e74c3c","#e67e22","#f1c40f","#2ecc71","#1abc9c","#3498db","#9b59b6","#e84393","#ecf0f1","#95a5a6"]
    import random; rnd=random.Random(7); cs=(pw-22)/5
    for r in range(5):
        for cc in range(5):
            c.setFillColor(HexColor(rnd.choice(pc))); c.rect(px+10+cc*cs, iy+ih-38-r*cs, cs-3, cs-3, fill=1,stroke=0)
    if day==1: _hl(c,px+6,iy,pw-2,ih)
    # viewport
    vx=lx+lw+12; vw=px-vx-12
    rrect(c,vx,iy,vw,ih,7,fill=HexColor("#1f2a35"))
    _figure(c, vx+vw/2-13, iy+ih/2-30)
    if day==3:
        c.setFillColor(HexColor("#2e7d4f")); c.rect(vx+16, iy+14, vw-32, 14, fill=1, stroke=0)  # ground
        _t(c,vx+20,iy+30,"cenário (chão + objetos)","Body-I",8.5,HexColor("#9fb3c8"))
    if day==1: _nb(c, px-2, iy+ih+2, 1)
    elif day==2: _nb(c, lx+lw+2, iy+ih-40, 1)
    elif day==4: _nb(c, x+w-210+42, y+h-13, 1)

# ---- Roblox Studio
def draw_roblox(c,x,y,w,h,day):
    rrect(c,x,y,w,h,10,fill=HexColor("#2b2f36"))
    c.setFillColor(HexColor("#e9edf2")); c.rect(x,y+h-30,w,30,fill=1,stroke=0)
    for i,tb in enumerate(["Home","Model","Test"]):
        _t(c,x+16+i*46,y+h-20,tb,"Body-B",9.5,HexColor("#3b4048") if i==0 else HexColor("#8a9099"))
    # ribbon tools
    tools=["Move","Scale","Rotate","Part","Play"]
    tx=x+170
    for tl in tools:
        act=(tl=="Part" and day==1) or (tl=="Play" and day==4)
        rrect(c,tx,y+h-26,44,20,4,fill=(HLC if act else HexColor("#ffffff")),stroke=HexColor("#cfd6dd"),sw=0.7)
        _tc(c,tx+22,y+h-20,tl,"Body",8.5,white if act else HexColor("#4a4f57"))
        if act: _hl(c,tx,y+h-26,44,20)
        tx+=50
    iy=y+10; ih=h-42
    # viewport
    vx=x+10; vw=w*0.56
    rrect(c,vx,iy,vw,ih,7,fill=HexColor("#8fbfe0"))
    c.setFillColor(HexColor("#7a8a99")); c.rect(vx,iy,vw,ih*0.34,fill=1,stroke=0)  # baseplate
    for i,(bx,bw,col) in enumerate([(0.12,0.14,"#e74c3c"),(0.34,0.14,"#f1c40f"),(0.56,0.16,"#2ecc71")]):
        c.setFillColor(HexColor(col)); c.rect(vx+vw*bx, iy+ih*0.34, vw*bw, ih*0.16, fill=1,stroke=0)
    if day==2:
        c.setFillColor(HexColor("#c0392b")); c.rect(vx+vw*0.40, iy+ih*0.34, vw*0.16, ih*0.07, fill=1,stroke=0)
        _t(c,vx+vw*0.30, iy+ih*0.34+ih*0.09,"lava","Body-B",8,white)
    if day==3:
        c.setFillColor(HexColor("#f5c542")); c.rect(vx+vw-38, iy+ih*0.34, 22, ih*0.22, fill=1,stroke=0)
        _t(c,vx+vw-58, iy+ih*0.60,"Win","Body-B",8,HexColor("#7a5b00"))
    # explorer
    exx=vx+vw+10; exw=w-(exx-x)-10
    rrect(c,exx,iy+ih*0.42,exw,ih*0.58,6,fill=white,stroke=HexColor("#d7dde3"),sw=0.8)
    _t(c,exx+8,iy+ih-14,"Explorer","Body-B",8.5,HexColor("#3b4048"))
    tree=["Workspace","  SpawnLocation","  Part","    Script"]
    for i,node in enumerate(tree):
        hln=(day==3 and "Spawn" in node) or (day==2 and "Script" in node)
        _t(c,exx+10,iy+ih-30-i*13,node,"Body",8, HLC if hln else HexColor("#5a616a"))
    # properties (Anchored)
    rrect(c,exx,iy,exw,ih*0.38,6,fill=white,stroke=HexColor("#d7dde3"),sw=0.8)
    _t(c,exx+8,iy+ih*0.38-14,"Properties","Body-B",8.5,HexColor("#3b4048"))
    _t(c,exx+10,iy+ih*0.38-30,"Anchored","Body",8,HexColor("#5a616a"))
    bxx=exx+exw-20
    c.setFillColor(HLC if day==1 else HexColor("#2ecc71")); c.rect(bxx,iy+ih*0.38-33,10,10,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("Body-B",8); c.drawCentredString(bxx+5,iy+ih*0.38-31,"v")
    if day==1: _hl(c,exx+6,iy+ih*0.38-34,exw-12,16)
    # badges
    if day==1: _nb(c,exx+exw-6,iy+ih*0.38-25,1)
    elif day==2: _nb(c,exx-2,iy+ih-30,1)
    elif day==3: _nb(c,exx-2,iy+ih-43,1)
    elif day==4: _nb(c,tx-58,y+h-16,1)

# ---- Construct 3
def draw_construct(c,x,y,w,h,day):
    rrect(c,x,y,w,h,10,fill=HexColor("#3a3f4b"))
    c.setFillColor(HexColor("#2b2f38")); c.rect(x,y+h-26,w,26,fill=1,stroke=0)
    for i,tab in enumerate(["Layout 1","Event sheet 1"]):
        act=(i==0 and day in(1,4)) or (i==1 and day in(2,3))
        rrect(c,x+10+i*104,y+h-24,100,20,4,fill=(HexColor("#4a90d9") if act else HexColor("#20242c")))
        _tc(c,x+10+i*104+50,y+h-18,tab,"Body-B",8.5,white if act else HexColor("#9aa0a8"))
    rrect(c,x+w-70,y+h-24,60,20,4,fill=(HLC if day==4 else HexColor("#2ecc71")))
    _tc(c,x+w-40,y+h-18,"▶ Play","Body-B",8.5,white)
    if day==4: _hl(c,x+w-70,y+h-24,60,20)
    iy=y+10; ih=h-40
    # center
    cx=x+10; cw=w*0.62
    if day in(2,3):
        rrect(c,cx,iy,cw,ih,7,fill=HexColor("#1f2530"))
        _t(c,cx+10,iy+ih-15,"Event sheet","Cond-B",8,HexColor("#8a93a0"))
        rows=[("Player → On collision with Coin","Coin: Destroy • Add 1 to Score",2),
              ("Player → On collision with Spike","System: Restart layout",3),
              ("Player → On collision with Goal","System: Go to layout \"Vitoria\"",3)]
        yy=iy+ih-34
        for cond,act,dd in rows:
            show = (day==2 and "Coin" in cond) or (day==3)
            colc=HexColor("#e6edf5") if show else HexColor("#4a525e")
            c.setFillColor(HexColor("#2a3140")); c.rect(cx+8,yy-6,cw-16,26,fill=1,stroke=0)
            _t(c,cx+14,yy+8,cond,"Mono",8,colc)
            _t(c,cx+26,yy-4,act,"Mono",8,HexColor("#7fd1a0") if show else HexColor("#454d59"))
            if (day==2 and "Coin" in cond) or (day==3 and "Spike" in cond): _hl(c,cx+8,yy-6,cw-16,26)
            yy-=32
    else:
        rrect(c,cx,iy,cw,ih*0.68,7,fill=HexColor("#bfe3f5"))   # sky
        c.setFillColor(HexColor("#6a9a4a")); c.rect(cx,iy,cw,ih*0.16,fill=1,stroke=0)  # ground
        c.setFillColor(HexColor("#8a5a3a")); c.rect(cx+cw*0.30,iy+ih*0.16,cw*0.18,ih*0.10,fill=1,stroke=0)
        c.setFillColor(HexColor("#e0673a")); c.rect(cx+cw*0.10,iy+ih*0.16,16,20,fill=1,stroke=0)  # player
        c.setFillColor(HexColor("#f1c40f")); c.circle(cx+cw*0.55,iy+ih*0.42,7,fill=1,stroke=0)   # coin
        c.setFillColor(HexColor("#c0392b"))
        p=c.beginPath(); p.moveTo(cx+cw*0.72,iy+ih*0.16); p.lineTo(cx+cw*0.75,iy+ih*0.30); p.lineTo(cx+cw*0.78,iy+ih*0.16); p.close()
        c.drawPath(p,fill=1,stroke=0)  # spike
        c.setFillColor(HexColor("#2ecc71")); c.rect(cx+cw*0.90,iy+ih*0.16,4,ih*0.24,fill=1,stroke=0)  # flag
        _t(c,cx+10,iy+ih*0.68+6,"Layout (a fase)","Body-I",8.5,HexColor("#2b2f38"))
    # right panels: Layers + Properties
    rxx=cx+cw+10; rxw=w-(rxx-x)-10
    rrect(c,rxx,iy+ih*0.5,rxw,ih*0.5,6,fill=HexColor("#20242c"))
    _t(c,rxx+8,iy+ih-14,"Layers","Body-B",8.5,HexColor("#cdd3db"))
    for i,ly in enumerate(["Game","Background"]):
        _t(c,rxx+12,iy+ih-30-i*14,"▤ "+ly,"Body",8.5,HexColor("#e6edf5"))
    if day==1: _hl(c,rxx+6,iy+ih*0.5,rxw-2,ih*0.5); _nb(c,rxx-2,iy+ih-24,1)
    rrect(c,rxx,iy,rxw,ih*0.44,6,fill=HexColor("#20242c"))
    _t(c,rxx+8,iy+ih*0.44-14,"Behaviors","Body-B",8.5,HexColor("#cdd3db"))
    for i,bh in enumerate(["Platform","Solid"]):
        _t(c,rxx+12,iy+ih*0.44-30-i*14,"+ "+bh,"Body",8.5,HexColor("#7fd1a0"))
    if day in(2,3): _nb(c,cx+cw*0.55,iy+ih*0.42+14,1)

# ---- Web (editor + browser)
def draw_web(c,x,y,w,h,day):
    rrect(c,x,y,w,h,10,fill=HexColor("#0f1420"))
    half=w/2
    # editor
    ex=x+8; ew=half-12
    rrect(c,ex,y+8,ew,h-16,8,fill=HexColor("#1e1e2e"))
    c.setFillColor(HexColor("#12121c")); c.rect(ex,y+h-30,ew,22,fill=1,stroke=0)
    _t(c,ex+12,y+h-24,"index.html","Body",9,HexColor("#c9d1d9"))
    code={
      1:[("<!DOCTYPE html>","#6b829e"),("<html>","#e06c75"),("  <body>","#e06c75"),
         ("    <h1>Meu Perfil</h1>","#98c379"),("    <button>Jogar</button>","#98c379"),("  </body>","#e06c75")],
      2:[("<style>","#c678dd"),("  body {","#e6edf5"),("    background:#0f172a;","#98c379"),
         ("    color:#f8fafc;","#98c379"),("  }","#e6edf5"),("</style>","#c678dd")],
      3:[("<script>","#c678dd"),("function jogar(e){","#61afef"),("  const pc = op[...]","#e6edf5"),
         ("  // sorteia e compara","#6b829e"),("}","#61afef"),("</script>","#c678dd")],
      4:[("// abra o Console (F12)","#6b829e"),("<meta name=viewport ...>","#98c379"),
         ("img{max-width:100%}","#e6edf5"),("// corrija os bugs","#6b829e")],
    }[day]
    yy=y+h-48
    for i,(ln,col) in enumerate(code):
        _t(c,ex+10,yy,str(i+1),"Mono",8,HexColor("#3a4a66")); _t(c,ex+26,yy,ln,"Mono",8.5,HexColor(col)); yy-=15
    if day in(1,3): _hl(c,ex,y+8,ew,h-16)
    # browser
    bx=x+half+4; bw=half-12
    rrect(c,bx,y+8,bw,h-16,8,fill=white)
    c.setFillColor(HexColor("#e9edf2")); c.rect(bx,y+h-30,bw,22,fill=1,stroke=0)
    for i,dc in enumerate(["#ff5f56","#ffbd2e","#27c93f"]):
        c.setFillColor(HexColor(dc)); c.circle(bx+12+i*11,y+h-19,3.5,fill=1,stroke=0)
    rrect(c,bx+48,y+h-27,bw-58,15,7,fill=white,stroke=HexColor("#cfd6dd"),sw=0.7)
    _t(c,bx+56,y+h-23,"index.html","Body",7.5,HexColor("#6b7681"))
    # page
    styled = day>=2
    _tc(c,bx+bw/2,y+h-56,"Meu Perfil","Body-B",13,HexColor("#0f172a") if not styled else HexColor("#0ea5a9"))
    _tc(c,bx+bw/2,y+h-74,"games e tecnologia","Body",8.5,HexColor("#5a616a"))
    if day>=3:
        for i,lab in enumerate(["Pedra","Papel","Tesoura"]):
            rrect(c,bx+18+i*(bw-36)/3,y+h-108,(bw-46)/3,18,5,fill=HexColor("#0ea5a9"))
            _tc(c,bx+18+i*(bw-36)/3+(bw-46)/6,y+h-102,lab,"Body-B",8,white)
        _tc(c,bx+bw/2,y+h-124,"PC: papel — Você venceu!","Body",8,HexColor("#0f172a"))
    else:
        rrect(c,bx+bw/2-30,y+h-104,60,18,5,fill=(HexColor("#0ea5a9") if styled else HexColor("#dfe3e8")))
        _tc(c,bx+bw/2,y+h-98,"Jogar","Body-B",8,white if styled else HexColor("#6b7681"))
    if day in(2,4): _hl(c,bx,y+8,bw,h-16)
    # console
    if day in(3,4):
        rrect(c,bx+6,y+12,bw-12,h*0.22,5,fill=HexColor("#11151d"))
        _t(c,bx+12,y+12+h*0.22-13,"Console  (F12)","Cond-B",7.5,HexColor("#8a93a0"))
        _t(c,bx+12,y+16,"> Uncaught ReferenceError...","Mono",7.5,HexColor("#ff6b6b"))
        if day==4: _hl(c,bx+6,y+12,bw-12,h*0.22)
    # badges
    if day==1: _nb(c,ex+ew-6,y+h-16,1)
    elif day==2: _nb(c,bx+6,y+h-16,1)
    elif day==3: _nb(c,ex+ew-6,y+h-16,1)
    elif day==4: _nb(c,bx+bw-8,y+22,1)

SCREEN_DRAWER = {"01_KIDS_MagicaVoxel":draw_mv, "02_TEENS_RobloxStudio":draw_roblox,
                 "03_YOUNG_Construct3":draw_construct, "04_YOUNG_HTML_CSS_JS":draw_web}
SCREEN_INFO = {
 "01_KIDS_MagicaVoxel":{
   1:("A tela do MagicaVoxel","1) Escolha a cor na PALETTE (direita) e clique no modelo para colar cubos (Attach). Gire arrastando no espaço vazio."),
   2:("Onde fica o espelho","1) Ligue MIRROR na coluna de FERRAMENTAS: tudo que fizer de um lado aparece igual do outro."),
   3:("Montando o cenário","Use BOX para criar o chão e os objetos ao redor do personagem, no centro (viewport)."),
   4:("Hora de renderizar","1) Troque para a aba RENDER (topo direito) para ganhar luz e sombra; depois exporte a imagem."),
 },
 "02_TEENS_RobloxStudio":{
   1:("A tela do Roblox Studio","1) Marque ANCHORED em Properties para a peça não cair. Insira peças com PART (barra Home)."),
   2:("Onde vai o script","1) No EXPLORER, adicione um Script dentro da peça de lava (Workspace > Part > Script)."),
   3:("Checkpoints e vitória","1) Insira SpawnLocation no EXPLORER e marque Neutral para virar checkpoint. Peça 'Win' dourada no fim."),
   4:("Testar e publicar","1) Clique em PLAY (barra Home) para testar o obby antes de publicar."),
 },
 "03_YOUNG_Construct3":{
   1:("A tela do Construct 3","1) No painel LAYERS (direita) use só 2 camadas: Background e Game. Adicione behaviors (Platform/Solid)."),
   2:("A folha de eventos","1) No EVENT SHEET, crie: Player colide com Coin -> Destroy + Add 1 to Score."),
   3:("Perder e vencer","1) Adicione: colidir com Spike -> Restart layout; colidir com Goal -> Go to layout 'Vitoria'."),
   4:("Testar no Preview","1) Clique em PLAY (topo) para rodar o jogo e caçar bugs dentro dos limites do plano Free."),
 },
 "04_YOUNG_HTML_CSS_JS":{
   1:("Editor + navegador","1) Escreva o HTML no editor (esquerda), salve (Ctrl+S) e atualize o navegador (F5) para ver."),
   2:("Estilizando com CSS","1) O CSS muda a aparência: veja o navegador (direita) ganhar cores e um botão de verdade."),
   3:("JavaScript no ar","1) O <script> cria o jogo. Abra o Console (F12) para acompanhar e achar erros."),
   4:("Debug + responsivo","1) Leia os erros no CONSOLE (F12) e ajuste a página para funcionar no celular."),
 },
}

def s_screen(c, th, n, title, caption, drawer, day, masc=False):
    c.setFillColor(HexColor("#eef1f4")); c.rect(0,0,W,H,fill=1,stroke=0)
    chip(c,60,H-92,"ONDE CLICAR  •  DIA %d"%n, th["primary"], white, size=13)
    c.setFillColor(th["ink"]); c.setFont("Body-B",30); c.drawString(60,H-140,title)
    if masc: mascot(c, W-82, H-72, 0.46, "wave", th["primary"], mix(th["primary"], white,0.85), th["accent"])
    mx,my,mw,mh = 60,152,W-120,H-262
    c.setFillColor(white); rrect(c,mx-6,my-6,mw+12,mh+12,14,fill=HexColor("#ffffff"),stroke=HexColor("#dfe3e8"),sw=1)
    drawer(c, mx, my, mw, mh, day)
    draw_para(c, para(esc(caption),"Body",16,HexColor("#3a4149"),leading=21), 60, 126, W-120)
    footer(c, th, "DIA %d — INTERFACE"%n)
    c.showPage()

class ScreenFlowable(Flowable):
    def __init__(self, drawer, day, w, h):
        Flowable.__init__(self); self.drawer=drawer; self.day=day; self.width=w; self.height=h
    def draw(self):
        c=self.canv
        rrect(c,0,0,self.width,self.height,10,fill=HexColor("#ffffff"),stroke=HexColor("#dfe3e8"),sw=0.8)
        self.drawer(c, 5, 5, self.width-10, self.height-10, self.day)

# ================================================================ build STUDENT
def build_student(course, path):
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle(course["title"] + " — Aluno")
    c.setAuthor("Matheus Marques")
    th = course["theme"]
    s_cover(c, th, course)
    for d in course["days"]:
        # collect this day's slides as thunks; mascot only on first / middle / last
        slides = []
        slides.append(lambda m: s_section(c, th, d["n"], d["title"], d["theme_line"], d["focus"], masc=m))
        terms = d["english"]; chunks = [terms[i:i+6] for i in range(0, len(terms), 6)]
        for pi, ch in enumerate(chunks, 1):
            slides.append(lambda m, ch=ch, pi=pi: s_english(c, th, d["n"], ch, pi, len(chunks), masc=m))
        slides.append(lambda m: s_agenda(c, th, d["n"], "", d["agenda"], masc=m))
        if course["slug"] in SCREEN_DRAWER:
            ti, cap = SCREEN_INFO[course["slug"]][d["n"]]
            slides.append(lambda m, ti=ti, cap=cap:
                          s_screen(c, th, d["n"], ti, cap, SCREEN_DRAWER[course["slug"]], d["n"], masc=m))
        for nt in d.get("notes", []):
            slides.append(lambda m, nt=nt: s_note(c, th, d["n"], nt["kind"], nt["title"], nt["body"], nt.get("big"), masc=m))
        steps = d.get("steps", [])
        for i, stp in enumerate(steps, 1):
            slides.append(lambda m, i=i, stp=stp:
                          s_step(c, th, d["n"], i, len(steps), stp["title"], stp["body"], stp.get("tip"), masc=m))
        for cs in d.get("code_slides", []):
            slides.append(lambda m, cs=cs:
                          s_code(c, th, d["n"], cs["title"], cs["lines"], cs.get("caption"), cs.get("lang","CÓDIGO"), masc=m))
        if d.get("challenge"):
            slides.append(lambda m: s_challenge(c, th, d["n"], d["challenge"]["title"], d["challenge"]["items"],
                                                d["challenge"].get("closing"), masc=m))
        N = len(slides); marks = {0, N // 2, N - 1}
        for i, fn in enumerate(slides):
            fn(i in marks)
    s_closing(c, th, course)
    c.save()
    return path

# ================================================================ build TEACHER (A4 portrait)
PA_W, PA_H = 595.27, 841.89
def _tstyles(th):
    return {
        "h1": ParagraphStyle("h1", fontName="Body-B", fontSize=22, leading=26, textColor=th["ink"], spaceAfter=4),
        "sub": ParagraphStyle("sub", fontName="Body", fontSize=11, leading=15, textColor=HexColor("#5a6068")),
        "h2": ParagraphStyle("h2", fontName="Body-B", fontSize=14, leading=18, textColor=white),
        "h3": ParagraphStyle("h3", fontName="Body-B", fontSize=12.5, leading=16, textColor=th["primary"], spaceBefore=6, spaceAfter=3),
        "body": ParagraphStyle("body", fontName="Body", fontSize=10.5, leading=15, textColor=HexColor("#2b2f36"), alignment=TA_JUSTIFY),
        "li": ParagraphStyle("li", fontName="Body", fontSize=10.5, leading=15, textColor=HexColor("#2b2f36")),
        "small": ParagraphStyle("small", fontName="Body", fontSize=9.5, leading=13, textColor=HexColor("#4a4f55")),
        "mono": ParagraphStyle("mono", fontName="Mono", fontSize=9, leading=12.5, textColor=HexColor("#0f2540")),
        "tag": ParagraphStyle("tag", fontName="Cond-B", fontSize=9, leading=11, textColor=white),
    }

def _bullets(items, style):
    return ListFlowable([ListItem(Paragraph(t, style), leftIndent=6, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=12, bulletFontName="Body-B",
                        bulletColor=HexColor("#888"))

def band(text, accent, S):
    """Editorial section header: small accent tick + dark title + thin accent rule."""
    p = Paragraph('<font color="%s">▪</font>&nbsp;&nbsp;%s' % (hx(accent), text),
                  ParagraphStyle("band", fontName="Body-B", fontSize=15, leading=19,
                                 textColor=HexColor("#171b22")))
    t = Table([[p]], colWidths=[PA_W-80])
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("LINEBELOW",(0,0),(-1,-1),1.5,accent)]))
    return t

def infocard(title, rows, accent, S):
    """Premium hairline card: white surface, keyline border, title divider, em-dash rows."""
    hair = HexColor("#DDE1E6"); body = HexColor("#3b424b")
    tcol = mix(accent, black, 0.34); dash = "#C4CACF"
    tsty = ParagraphStyle("ic_t", fontName="Body-B", fontSize=11.5, leading=15, textColor=tcol)
    rsty = ParagraphStyle("ic_r", fontName="Body", fontSize=10.5, leading=15,
                          leftIndent=16, firstLineIndent=-16, textColor=body)
    data = [[Paragraph('<font color="%s">▪</font>&nbsp;&nbsp;%s' % (hx(accent), title), tsty)]]
    for r in rows:
        data.append([Paragraph('<font color="%s">—</font>&nbsp;&nbsp;%s' % (dash, r), rsty)])
    t = Table(data, colWidths=[PA_W-80])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),white),
        ("BOX",(0,0),(-1,-1),0.8,hair),
        ("ROUNDEDCORNERS",[12,12,12,12]),
        ("LINEBELOW",(0,0),(0,0),0.8,hair),
        ("LEFTPADDING",(0,0),(-1,-1),16),("RIGHTPADDING",(0,0),(-1,-1),16),
        ("TOPPADDING",(0,0),(0,0),11),("BOTTOMPADDING",(0,0),(0,0),9),
        ("TOPPADDING",(0,1),(-1,-1),4),("BOTTOMPADDING",(0,1),(-1,-1),4),
        ("TOPPADDING",(0,1),(0,1),9),
        ("BOTTOMPADDING",(0,-1),(-1,-1),11)]))
    return t

def eng_table(terms, th, S):
    data = [[Paragraph("<b>Term (EN)</b>",S["small"]),Paragraph("<b>Pronuncia</b>",S["small"]),
             Paragraph("<b>Significado (PT)</b>",S["small"])]]
    for term,pron,mean in terms:
        data.append([Paragraph("<b>%s</b>"%term, S["li"]), Paragraph(pron, S["mono"]), Paragraph(mean, S["li"])])
    t = Table(data, colWidths=[110, 120, PA_W-80-230])
    ts=[("BACKGROUND",(0,0),(-1,0),th["primary"]),("TEXTCOLOR",(0,0),(-1,0),white),
        ("FONTNAME",(0,0),(-1,0),"Body-B"),("GRID",(0,0),(-1,-1),0.5,HexColor("#dfe3e8")),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),("ROUNDEDCORNERS",[5,5,5,5])]
    for i in range(1,len(data)):
        if i%2==0: ts.append(("BACKGROUND",(0,i),(-1,i),HexColor("#f4f6f9")))
    t.setStyle(TableStyle(ts))
    return t

def agenda_table(blocks, S, th):
    data=[]
    for mins,label,desc in blocks:
        data.append([Paragraph('<font color="%s">▪</font>&nbsp;&nbsp;<b>%s</b> — %s'
                               % (hx(th["primary"]), label, desc), S["li"])])
    t=Table(data, colWidths=[PA_W-80])
    ts=[("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("LINEBELOW",(0,0),(-1,-2),0.5,HexColor("#e8ebef"))]
    t.setStyle(TableStyle(ts))
    return t

def code_box(cs, S):
    els = [Paragraph("&lt;/&gt;&nbsp; %s"%cs["title"], S["h3"])]
    pre = Preformatted("\n".join(esc(x) for x in cs["lines"]),
                       ParagraphStyle("code", fontName="Mono", fontSize=8.5, leading=12.5, textColor=HexColor("#e6edf5")))
    t = Table([[pre]], colWidths=[PA_W-80])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),HexColor("#0d1526")),("LEFTPADDING",(0,0),(-1,-1),12),
        ("RIGHTPADDING",(0,0),(-1,-1),12),("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
        ("ROUNDEDCORNERS",[7,7,7,7])]))
    els.append(t)
    if cs.get("caption"):
        els.append(Paragraph("<i>%s</i>"%cs["caption"], S["small"]))
    return KeepTogether(els)

def build_teacher(course, path):
    th = course["theme"]; S=_tstyles(th)
    story=[]
    def header_footer(cv, doc):
        cv.saveState()
        cv.setFillColor(th["primary"]); cv.rect(0, PA_H-14, PA_W, 14, fill=1, stroke=0)
        if doc.page == 1:
            cv.setFillColor(HexColor("#2f343b")); cv.setFont("Body-B",9)
            cv.drawString(40,21, CREDIT)
        cv.setFillColor(th["primary"]); cv.setFont("Body-B",8)
        cv.drawRightString(PA_W-40,22, "%s — GUIA DO PROFESSOR"%course["audience"])
        cv.setFont("Body",8); cv.setFillColor(HexColor("#9aa0a6"))
        cv.drawCentredString(PA_W/2,22,"pag. %d"%doc.page)
        cv.restoreState()
    # ---- capa
    story.append(Spacer(1,10))
    cap = Table([[Paragraph("GUIA DO PROFESSOR", S["tag"])]], colWidths=[150])
    cap.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),th["secondary"]),("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("ROUNDEDCORNERS",[6,6,6,6])]))
    story.append(cap); story.append(Spacer(1,10))
    story.append(Paragraph(course["title"], ParagraphStyle("c",fontName="Body-B",fontSize=26,leading=30,textColor=th["ink"])))
    story.append(Paragraph(course["subtitle"], S["sub"])); story.append(Spacer(1,6))
    story.append(Paragraph("Plataforma: <b>%s</b>  &nbsp;|&nbsp;  4 dias · 1 projeto"
                           % course["platform"], S["small"]))
    story.append(Spacer(1,12))
    story.append(band("VISÃO GERAL DO CURSO", th["primary"], S)); story.append(Spacer(1,8))
    story.append(Paragraph(course["overview"], S["body"])); story.append(Spacer(1,10))
    tv = course["teacher_intro"]
    for title, rows, accent in [
        ("Objetivo do projeto final", [tv["project_goal"]], th["primary"]),
        ("Preparação / setup da sala", tv["setup"], HexColor("#0f9d8b")),
        ("Materiais e acesso", tv["materials"], HexColor("#c2760c")),
        ("Dicas de condução", tv["management"], HexColor("#8b3ec2")),
    ]:
        story.append(KeepTogether(infocard(title, rows, accent, S))); story.append(Spacer(1,9))
    from reportlab.platypus import PageBreak
    story.append(Spacer(1,4))
    # ---- dias
    for d in course["days"]:
        story.append(KeepTogether([band("DIA %d — %s"%(d["n"], d["title"]), th["primary"], S), Spacer(1,4),
                                   Paragraph("<b>Foco:</b> %s"%d["focus"], S["small"]), Spacer(1,8),
                                   Paragraph("Objetivos de aprendizagem", S["h3"]),
                                   _bullets(d["teacher"]["objectives"], S["li"])]))
        story.append(Spacer(1,8))
        story.append(Paragraph("English Lab — vocabulário técnico do dia", S["h3"]))
        story.append(eng_table(d["english"], th, S)); story.append(Spacer(1,8))
        story.append(Paragraph("Roteiro da aula", S["h3"]))
        story.append(agenda_table(d["agenda"], S, th)); story.append(Spacer(1,8))
        if course["slug"] in SCREEN_DRAWER:
            ti, cap = SCREEN_INFO[course["slug"]][d["n"]]
            story.append(Paragraph("Interface — onde clicar", S["h3"]))
            story.append(KeepTogether([ScreenFlowable(SCREEN_DRAWER[course["slug"]], d["n"], PA_W-80, 170),
                                       Spacer(1,4), Paragraph("<i>%s</i>"%esc(cap), S["small"])]))
            story.append(Spacer(1,9))
        if d.get("steps"):
            story.append(Paragraph("Passo a passo do projeto (o que os alunos fazem)", S["h3"]))
            steps=[ "<b>%d. %s</b> — %s"%(i,s["title"],s["body"]) for i,s in enumerate(d["steps"],1)]
            story.append(_bullets(steps, S["li"])); story.append(Spacer(1,8))
        for cs in d.get("code_slides", []):
            story.append(code_box(cs, S)); story.append(Spacer(1,8))
        story.append(KeepTogether(infocard("Erros comuns & como resolver", d["teacher"]["pitfalls"], HexColor("#d1373b"), S))); story.append(Spacer(1,9))
        story.append(KeepTogether(infocard("Checagem rápida (todos conseguiram?)", d["teacher"]["checks"], HexColor("#0f9d8b"), S))); story.append(Spacer(1,9))
        story.append(KeepTogether(infocard("Diferenciação (mais rápidos / mais devagar)", d["teacher"]["differ"], th["primary"], S)))
        story.append(PageBreak())
    # ---- encerramento
    story.append(band("AVALIAÇÃO & APRESENTAÇÃO (DIA 4)", th["secondary"], S)); story.append(Spacer(1,8))
    story.append(Paragraph(course["assessment_intro"], S["body"])); story.append(Spacer(1,8))
    story.append(KeepTogether(infocard("Rubrica simples de avaliação", course["rubric"], th["primary"], S))); story.append(Spacer(1,9))
    story.append(KeepTogether(infocard("Roteiro da apresentação final", course["presentation"], HexColor("#0f9d8b"), S)))
    fontes = [band("FONTES CONSULTADAS", HexColor("#7c8794"), S), Spacer(1,6),
              Paragraph("Informações sobre acesso e recursos das plataformas, verificadas em fontes oficiais na internet:", S["small"]),
              Spacer(1,5)]
    for src in course.get("sources", []):
        fontes.append(Paragraph('<font color="#9aa0a6">▪</font>&nbsp;&nbsp;%s'%src, S["small"]))
    fontes += [Spacer(1,18), SealFlowable(th["primary"], course["seal"][0], course["seal"][1], course["seal"][2], PA_W-80)]
    story.append(Spacer(1,14)); story.append(KeepTogether(fontes))
    doc = SimpleDocTemplate(path, pagesize=(PA_W,PA_H), leftMargin=40,rightMargin=40,topMargin=34,bottomMargin=34,
                            title=course["title"]+" — Professor", author="Matheus Marques")
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return path

def build_all(course, outdir):
    course = escape_content(course)
    os.makedirs(outdir, exist_ok=True)
    a = build_student(course, os.path.join(outdir, course["slug"]+"_ALUNO.pdf"))
    b = build_teacher(course, os.path.join(outdir, course["slug"]+"_PROFESSOR.pdf"))
    return a, b
