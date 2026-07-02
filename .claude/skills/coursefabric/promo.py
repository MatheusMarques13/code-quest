# -*- coding: utf-8 -*-
"""Square (1:1) promo posts — CNA brand style (ref-based). ONE template, per-level text only."""
import engine, math, sys, os
from engine import rrect, mix, para, draw_para
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_LEFT

S = 1080
NAVY  = HexColor("#17255E")
NAVY2 = HexColor("#0F1B49")
RED   = HexColor("#E2231A")
INK   = HexColor("#26324D")
GREY  = HexColor("#5A6577")
BLUE  = HexColor("#2F6BEB")
CYAN  = HexColor("#38E0F0")
YELL  = HexColor("#FFC531")
GREEN = HexColor("#2ECC71")

def t(c,x,y,s,f,sz,col): c.setFillColor(col); c.setFont(f,sz); c.drawString(x,y,s)
def tc(c,x,y,s,f,sz,col): c.setFillColor(col); c.setFont(f,sz); c.drawCentredString(x,y,s)

def pin(c,x,y,r,col):
    c.setFillColor(col); c.circle(x,y+r*0.4,r,fill=1,stroke=0)
    p=c.beginPath(); p.moveTo(x-r*0.7,y+r*0.4); p.lineTo(x,y-r*1.1); p.lineTo(x+r*0.7,y+r*0.4); p.close()
    c.drawPath(p,fill=1,stroke=0)
    c.setFillColor(white); c.circle(x,y+r*0.4,r*0.4,fill=1,stroke=0)

def dots(c,x,y,cols,rows,gap,r,col,alpha):
    c.setFillColor(Color(col.red,col.green,col.blue,alpha=alpha))
    for i in range(cols):
        for j in range(rows):
            c.circle(x+i*gap, y+j*gap, r, fill=1, stroke=0)

# ---------------------------------------------------------------- robot
def robot(c, cx, cy, s=1.0):
    c.saveState(); c.translate(cx, cy); c.scale(s, s)
    bod=BLUE; dk=mix(BLUE,black,0.30); lite=mix(BLUE,white,0.55)
    def cap(x,y,w,h,r,f): c.setFillColor(f); c.roundRect(x,y,w,h,r,fill=1,stroke=0)
    # feet
    c.setFillColor(dk); c.roundRect(-58,-176,44,26,10,fill=1,stroke=0); c.roundRect(14,-176,44,26,10,fill=1,stroke=0)
    # arms (behind)
    c.saveState(); c.translate(-92,-40); c.rotate(18); cap(-16,-70,30,96,15,bod); c.setFillColor(lite); c.circle(0,-74,20,fill=1,stroke=0); c.restoreState()
    c.saveState(); c.translate(92,10); c.rotate(-32); cap(-14,-16,30,110,15,bod); c.setFillColor(YELL); c.circle(0,96,22,fill=1,stroke=0); c.restoreState()
    # body
    c.setFillColor(bod); c.roundRect(-96,-150,192,168,34,fill=1,stroke=0)
    c.setFillColor(lite); c.roundRect(-96,-150,192,168,34,fill=0,stroke=0)
    # chest panel
    c.setFillColor(NAVY2); c.roundRect(-66,-118,132,96,20,fill=1,stroke=0)
    for i,(col) in enumerate([RED,YELL,GREEN]):
        c.setFillColor(col); c.circle(-38+i*38,-48,11,fill=1,stroke=0)
    c.setFillColor(CYAN)
    for k in range(4): c.roundRect(-50+k*26,-96,16,10,4,fill=1,stroke=0)
    # neck
    c.setFillColor(dk); c.roundRect(-20,10,40,22,6,fill=1,stroke=0)
    # head
    c.setFillColor(mix(BLUE,white,0.30)); c.roundRect(-104,28,208,150,40,fill=1,stroke=0)
    # ears/bolts
    c.setFillColor(dk); c.circle(-116,104,20,fill=1,stroke=0); c.circle(116,104,20,fill=1,stroke=0)
    c.setFillColor(CYAN); c.circle(-116,104,8,fill=1,stroke=0); c.circle(116,104,8,fill=1,stroke=0)
    # screen face
    c.setFillColor(NAVY2); c.roundRect(-84,52,168,104,26,fill=1,stroke=0)
    c.setFillColor(CYAN)
    c.ellipse(-52,86,-8,132,fill=1,stroke=0); c.ellipse(8,86,52,132,fill=1,stroke=0)  # eyes
    c.setFillColor(white); c.ellipse(-40,110,-24,128,fill=1,stroke=0); c.ellipse(20,110,36,128,fill=1,stroke=0)
    c.setStrokeColor(CYAN); c.setLineWidth(6)   # smile
    p=c.beginPath(); p.moveTo(-30,72); p.curveTo(-12,60,12,60,30,72); c.drawPath(p,fill=0,stroke=1)
    # antenna
    c.setStrokeColor(dk); c.setLineWidth(7); c.line(0,178,0,214)
    c.setFillColor(Color(RED.red,RED.green,RED.blue,alpha=0.35)); c.circle(0,222,22,fill=1,stroke=0)
    c.setFillColor(RED); c.circle(0,222,13,fill=1,stroke=0)
    c.restoreState()

def cta(c, x, y, label):
    w=pdfmetrics.stringWidth(label,"Body-B",25)+120; h=74
    rrect(c, x, y, w, h, h/2, fill=RED)
    c.setFillColor(white); c.setFont("Body-B", 25); c.drawString(x+34, y+26, label)
    # check circle
    ccx=x+w-46
    c.setFillColor(white); c.circle(ccx, y+h/2, 22, fill=1, stroke=0)
    c.setStrokeColor(RED); c.setLineWidth(5); c.setLineCap(1)
    p=c.beginPath(); p.moveTo(ccx-9,y+h/2-1); p.lineTo(ccx-2,y+h/2-9); p.lineTo(ccx+10,y+h/2+9); c.drawPath(p,fill=0,stroke=1)

def logo_footer(c, x, y):
    # reversed CNA wordmark on the navy footer (transparent style)
    c.setFillColor(white); c.setFont("Body-B", 40); c.drawString(x, y, "CNA")
    wcna=pdfmetrics.stringWidth("CNA","Body-B",40)
    c.setFillColor(RED); c.setFont("Body-B", 15); c.drawString(x+wcna+5, y+24, "®")
    c.setFillColor(HexColor("#AEB9D6")); c.setFont("Cond-B", 15); c.drawString(x+2, y-20, "I D I O M A S")

def build(spec, path):
    c=canvas.Canvas(path, pagesize=(S,S))
    c.setFillColor(HexColor("#F5F7FB")); c.rect(0,0,S,S,fill=1,stroke=0)   # very light bg
    # brand accents
    c.setFillColor(Color(RED.red,RED.green,RED.blue,alpha=0.12)); c.circle(S+40, S-30, 250, fill=1, stroke=0)
    dots(c, 60, S-150, 6, 4, 26, 4.5, NAVY, 0.14)
    c.setFillColor(Color(BLUE.red,BLUE.green,BLUE.blue,alpha=0.07)); c.circle(180, 470, 240, fill=1, stroke=0)
    FH=160  # footer height
    # ---- content column (left) ----
    x=84
    t(c, x, S-96, "CURSO DE FÉRIAS  •  ROBÓTICA & PROGRAMAÇÃO", "Cond-B", 20, RED)
    # TURMA chip
    lab="TURMA "+spec["level"]; lw=pdfmetrics.stringWidth(lab,"Cond-B",19)+30
    rrect(c, x, S-150, lw, 40, 20, fill=NAVY); c.setFillColor(white); c.setFont("Cond-B",19); c.drawString(x+15, S-138, lab)
    # big headline (navy + red word), left aligned
    hp=para(spec["headline"], "Body-B", 68, NAVY, leading=70, align=TA_LEFT)
    hh=draw_para(c, hp, x, S-176, 610)
    # body
    bp=para(spec["desc"], "Body", 24, INK, leading=32, align=TA_LEFT)
    draw_para(c, bp, x, S-176-hh-34, 560)
    # CTA
    cta(c, x, 250, "GARANTA A SUA VAGA")
    # badges under CTA
    bx=x
    for lbl in ["4 dias","1 grande projeto","vagas limitadas"]:
        bw=pdfmetrics.stringWidth(lbl,"Body-B",15)+28
        rrect(c, bx, 205, bw, 30, 15, fill=white, stroke=HexColor("#D5DCEA"), sw=1)
        c.setFillColor(GREY); c.setFont("Body-B",15); c.drawString(bx+14, 213, lbl); bx+=bw+12
    # ---- robot (right) ----
    robot(c, 838, 606, 1.02)
    # ---- footer bar ----
    c.setFillColor(NAVY); c.rect(0,0,S,FH,fill=1,stroke=0)
    c.setFillColor(NAVY2)
    pth=c.beginPath(); pth.moveTo(S,0); pth.lineTo(S,FH); pth.lineTo(S-210,0); pth.close(); c.drawPath(pth,fill=1,stroke=0)
    c.setFillColor(Color(RED.red,RED.green,RED.blue,alpha=0.9)); c.circle(S-40, FH+6, 60, fill=1, stroke=0)
    dots(c, S-250, 34, 5, 3, 22, 3.5, white, 0.18)
    logo_footer(c, 84, 78)
    pin(c, 560, 74, 13, RED)
    t(c, 585, 66, "CNA Idiomas  •  Unidade Via Sul", "Body-B", 21, white)
    c.showPage(); c.save(); return path

SPECS={
 "kids":{"level":"KIDS","headline":"Criação de <font color='#E2231A'>Mundos 3D</font>",
   "desc":"Seu filho cria personagens e mundos em 3D no computador — programando e se divertindo nas férias."},
 "teens":{"level":"TEENS","headline":"Crie o seu Jogo no <font color='#E2231A'>Roblox</font>",
   "desc":"Construa e publique um jogo (obby) de verdade no Roblox Studio, do zero ao fim."},
 "young":{"level":"YOUNG","headline":"Programe Jogos e <font color='#E2231A'>Sites</font>",
   "desc":"Crie um jogo 2D completo e uma página web com HTML, CSS e JavaScript, como um dev de verdade."},
}
if __name__=="__main__":
    # usage: python3 promo.py [key|all] [outdir]
    which  = sys.argv[1] if len(sys.argv) > 1 else "all"
    outdir = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(outdir, exist_ok=True)
    keys = list(SPECS) if which == "all" else [which]
    for k in keys:
        build(SPECS[k], os.path.join(outdir, "PROMO_%s.pdf" % k.upper()))
        print("OK", k)
