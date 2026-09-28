import os
ROOT=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))+'/'
from lib import *
exec(open('compose_rooms.py').read().split('WARM=')[0].split('from lib import *')[1])
WARM=(255,190,110); TEAL=(90,220,235); GOLD=(255,196,90); WHITE=(235,240,255)
BW,BH=2400,1000
def cut(f): return Image.open(C+f).convert('RGBA')
def night_wide(seed):
    bg,fy=night_bg((BW,BH),floor=0.8,seed=seed); return bg,fy
out={}
# Lámparas: globo + 3 bolas
bg,fy=night_wide(11)
put(bg,cut('globo_g01_full.png'),1700,fy+10,620,glow=GOLD,ga=110,shadow=170)
put(bg,cut('lamp_moon_clean.png'),1250,fy+25,330,glow=WARM,ga=110,foot=0.0)
put(bg,cut('lamp_saturn_clean.png'),2140,fy+25,330,glow=WARM,ga=110,foot=0.095)
out['banner-lamparas']=bg
# Relojes
bg,fy=night_wide(12)
put(bg,cut('clock_04__bir.png'),1650,fy+5,300,glow=WHITE,ga=90,gr=0.9,shadow=170)
out['banner-relojes']=bg
# Todo
bg,fy=night_wide(13)
put(bg,cut('w_teal_gold.png'),1060,fy+15,380,glow=TEAL,ga=110,shadow=180,up=0.06,flat=0.08)
put(bg,cut('clock_04__bir.png'),1470,fy+5,150,glow=WHITE,ga=60,shadow=150)
put(bg,cut('globo_g01_full.png'),1870,fy+10,560,glow=GOLD,ga=100,shadow=170)
put(bg,cut('lamp_saturn_clean.png'),2250,fy+25,300,glow=WARM,ga=110,foot=0.095)
out['banner-todo']=bg
def wide(img,cy,h=853):
    y0=int(max(0,min(img.height-h,cy-h/2))); return img.crop((0,y0,2048,y0+h)).resize((BW,BH),Image.LANCZOS)
# Contacto: escritorio2 + lámpara Saturno
bg=dim(room('escritorio2'),0.8)
put(bg,cut('lamp_saturn_clean.png'),1700,1540,300,glow=WARM,ga=150,gr=1.2,foot=0.095,shadow=200)
out['banner-contacto']=wide(bg,1180)
# Ayuda: dormitorio con proyector
bg=dim(room('mesilla1').transpose(Image.FLIP_LEFT_RIGHT),0.6)
put(bg,cut('w_teal_gold.png'),2048-960,1420,400,glow=TEAL,ga=150,gr=1.3,shadow=230,up=0.06,flat=0.08)
out['banner-ayuda']=wide(bg,1150)
# Legal: cielo con órbita
bg,fy=night_bg((BW,BH),floor=1.2,seed=21)
bg.alpha_composite(radial((BW,BH),(1780,500),700,(124,108,246),120))
pl=Image.new('RGBA',(BW,BH),(0,0,0,0)); d=ImageDraw.Draw(pl)
d.ellipse((1600,320,1960,680),fill=(255,181,71,255))
d.ellipse((1660,360,1760,460),fill=(255,214,140,255))
pl=pl.filter(ImageFilter.GaussianBlur(1)); bg.alpha_composite(radial((BW,BH),(1780,500),420,(255,181,71),120)); bg.alpha_composite(pl)
ring=Image.new('RGBA',(BW,BH),(0,0,0,0)); d=ImageDraw.Draw(ring)
d.ellipse((1380,430,2180,570),outline=(167,160,255,230),width=14)
ring=ring.rotate(-14,center=(1780,500),resample=Image.BICUBIC)
# hide ring part behind planet (upper half inside planet)
m=Image.new('L',(BW,BH),0); dm=ImageDraw.Draw(m); dm.ellipse((1600,320,1960,680),fill=255); dm.rectangle((0,500,BW,BH),fill=0)
rr=ring.copy(); a=np.array(rr); a[:,:,3]=np.where(np.array(m)>0,0,a[:,:,3]); bg.alpha_composite(Image.fromarray(a))
out['banner-legal']=bg
for k,v in out.items():
    v.convert('RGB').save(ROOT+'fotos/'+k+'.jpg',quality=86,optimize=True,progressive=True); print(k)
