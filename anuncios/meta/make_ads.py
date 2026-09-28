import os
ROOT=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))+'/'
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np
F=ROOT+'marca/fuentes/'
LOGO=Image.open(ROOT+'marca/logo/orbiluz-logo-noche-transparente.png').convert('RGBA')
AMB=(255,181,71); LUNA=(255,246,233); NOCHE=(18,18,58)
def font(n,s): return ImageFont.truetype(F+n,s)
def fit(img,W,H):
    r=max(W/img.width,H/img.height); img=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(img.width-W)//2; y=(img.height-H)//2; return img.crop((x,y,x+W,y+H))
def topshade(im,h,a=235):
    W,H=im.size; g=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(g)
    for i in range(h): d.line((0,i,W,i),fill=(10,10,30,int(a*(1-i/h)**1.4)))
    im.alpha_composite(g)
def botshade(im,h,a=220):
    W,H=im.size; g=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(g)
    for i in range(h): d.line((0,H-h+i,W,H-h+i),fill=(10,10,30,int(a*(i/h)**1.4)))
    im.alpha_composite(g)
def headline(im,parts,y,size,maxw=None):
    """parts: list of lines; each line list of (text, highlight)"""
    d=ImageDraw.Draw(im); W=im.size[0]; f=font('Unbounded-Bold.ttf',size)
    for line in parts:
        line=[(t.strip(),h) for t,h in line]
        gap=d.textlength(' ',font=f)+22
        widths=[d.textlength(t,font=f) for t,_ in line]; tw=sum(widths)+gap*(len(line)-1)
        x=(W-tw)/2
        for (t,h),w in zip(line,widths):
            if h:
                bb=d.textbbox((x,y),t,font=f); d.rounded_rectangle((bb[0]-14,bb[1]-10,bb[2]+14,bb[3]+14),18,fill=AMB)
                d.text((x,y),t,font=f,fill=NOCHE)
            else:
                d.text((x+3,y+4),t,font=f,fill=(0,0,0,120)); d.text((x,y),t,font=f,fill=LUNA)
            x+=w+gap
        y+=int(size*1.28)
    return y
def sub(im,t,y,size=40,col=(233,230,255)):
    d=ImageDraw.Draw(im); W=im.size[0]; f=font('DMSans-Bold.ttf',size)
    d.text((W/2+2,y+2),t,font=f,fill=(0,0,0,140),anchor='mm'); d.text((W/2,y),t,font=f,fill=col,anchor='mm')
def logo(im,y,w=250):
    l=LOGO.copy(); l.thumbnail((w,w)); W=im.size[0]; im.alpha_composite(l,((W-l.width)//2,y))
def pill(im,t,y):
    d=ImageDraw.Draw(im); W=im.size[0]; f=font('DMSans-Bold.ttf',34); tw=d.textlength(t,font=f)
    d.rounded_rectangle((W/2-tw/2-30,y-30,W/2+tw/2+30,y+30),30,fill=(255,246,233,235)); d.text((W/2,y),t,font=f,fill=NOCHE,anchor='mm')
def story_from(feed):
    """9:16 a partir del 4:5: fondo desenfocado + imagen centrada"""
    W,H=1080,1920; bg=fit(feed.convert('RGB'),W,H).filter(ImageFilter.GaussianBlur(40)); bg=ImageEnhance.Brightness(bg).enhance(0.45).convert('RGBA')
    bg.alpha_composite(feed,(0,(H-feed.height)//2)); return bg
