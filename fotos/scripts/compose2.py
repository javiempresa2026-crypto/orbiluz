from lib import *
C='cut/'
TEAL=(60,220,230)
def decable(im):
    a=np.array(im); al=a[:,:,3]; bb=im.getbbox()
    rows=al[:int(bb[3]*0.8)]>40; cols=np.where(rows.any(0))[0]; a[:, cols.max()+6:,3]=0
    return Image.fromarray(a)
def fit_cover(img,size):
    w,h=size; r=max(w/img.width,h/img.height); img=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(img.width-w)//2; y=(img.height-h)//2; return img.crop((x,y,x+w,y+h))
def rounded(img,rad):
    m=Image.new('L',img.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,img.width,img.height),rad,fill=255); img=img.convert('RGBA'); img.putalpha(m); return img
def title(d,text,y=170,size=84,color=NOCHE): d.text((S/2,y),text,font=font('Unbounded-Bold.ttf',size),fill=color,anchor='mm')
def bullets(d,items,x,y,step=110,color=NOCHE,sub=(90,90,130)):
    for t,s in items:
        d.ellipse((x-14,y-14,x+14,y+14),fill=AMBAR); d.text((x+40,y),t,font=font('DMSans-Bold.ttf',50),fill=color,anchor='lm')
        if s: d.text((x+40,y+56),s,font=font('DMSans-Regular.ttf',40),fill=sub,anchor='lm'); y+=60
        y+=step
# ---------- PROYECTOR ----------
wt=Image.open(C+'w_teal_dark.png').convert('RGBA'); wg=Image.open(C+'w_teal_gold.png').convert('RGBA'); wa=Image.open(C+'w_amber.png').convert('RGBA')
a=np.array(wg); a[:130,:90,3]=0; wg=Image.fromarray(a)
bg,fy=night_bg(seed=31,floor=0.74)
place(bg,wt,S/2,fy+80,height=1180,glow=TEAL,glow_a=120,glow_r=0.75,reflect=0.3,shadow_dark=True)
save(bg,'proyector-ondas-noche')
bg,fy=studio_bg()
place(bg,wa,S/2,fy+60,height=1150)
save(bg,'proyector-ondas-ambar')
# real effect photos in brand frame
eff=Image.open('src/wave_Sebd9297a37504bc391fad56bc3397127C.jpg').convert('RGB').crop((0,0,680,430))
bg=Image.new('RGBA',(S,S),NOCHE+(255,)); bg.alpha_composite(radial((S,S),(S/2,S*0.4),S*0.7,NEB,90))
ph=rounded(fit_cover(eff,(1760,1300)),48); bg.alpha_composite(ph,(120,120))
d=ImageDraw.Draw(bg)
d.text((S/2,1600),'Olas de luz en techo y paredes',font=font('Unbounded-Bold.ttf',80),fill=LUNA,anchor='mm')
d.text((S/2,1720),'Efecto real del proyector en una habitación a oscuras',font=font('DMSans-Regular.ttf',48),fill=NIEBLA,anchor='mm')
save(bg,'proyector-ondas-efecto')
eff2=Image.open('src/wave_S6d6bcc882e2d422b844230074482802df.png').convert('RGB').crop((0,0,1667,760))
bg=Image.new('RGBA',(S,S),NOCHE+(255,)); bg.alpha_composite(radial((S,S),(S/2,S*0.3),S*0.7,TEAL,60))
ph=rounded(fit_cover(eff2,(1760,800)),48); bg.alpha_composite(ph,(120,120))
place(bg,wg,S/2,1880,height=900,shadow_dark=True,glow=TEAL,glow_a=60)
save(bg,'proyector-ondas-techo')
# 16 colours
strip=Image.open('src/wave_S115e686037ea4a6084442aab980e2ffeX.jpg').convert('RGB').crop((546,2650,2570,3200))
bg,fy=studio_bg(floor=0.9)
d=ImageDraw.Draw(bg); title(d,'16 colores con el mando',y=200)
d.text((S/2,310),'Y brillo regulable a tu gusto',font=font('DMSans-Medium.ttf',54),fill=(90,90,130),anchor='mm')
st=strip.resize((1800,int(strip.height*1800/strip.width)),Image.LANCZOS); bg.alpha_composite(rounded(st,36),(100,470))
bullets(d,[('Mando a distancia incluido',''),('Botón táctil en la base',''),('Efecto de agua en movimiento','(gira por dentro)')],300,470+st.height+170)
save(bg,'proyector-ondas-colores')
# specs
bg,fy=studio_bg(floor=0.62)
d=ImageDraw.Draw(bg); title(d,'Pequeño, pero llena la habitación',y=160,size=72)
x,y,w,h=place(bg,wg,S/2-120,int(S*0.62),height=880)
bx=x+w+60
d.line((bx,y+40,bx,y+h),fill=NOCHE,width=5); d.line((bx-20,y+40,bx+20,y+40),fill=NOCHE,width=5); d.line((bx-20,y+h,bx+20,y+h),fill=NOCHE,width=5)
d.text((bx+40,y+h/2),'Aprox. 11 cm',font=font('DMSans-Bold.ttf',58),fill=NOCHE,anchor='lm')
bullets(d,[('Funciona por USB (cable de 1,3 m)','Enchúfalo a un cargador USB o al ordenador'),('Mando con 16 colores y brillo',''),('Base clara u oscura según el lote','')],300,int(S*0.62)+150)
save(bg,'proyector-ondas-medidas')

# ---------- RELOJ 3D ----------
clk=Image.open(C+'clock_04__bir.png').convert('RGBA')
bg,fy=night_bg(seed=11,floor=0.66)
place(bg,clk,S/2,fy+80,width=1650,glow=(235,240,255),glow_a=90,glow_r=0.45,reflect=0.3,shadow_dark=True)
save(bg,'reloj-3d-noche')
bg,fy=studio_bg(floor=0.66)
place(bg,clk,S/2,fy+60,width=1650)
save(bg,'reloj-3d-estudio')
clk5=Image.open(C+'clock_5__bir.png').convert('RGBA'); a=np.array(clk5); a[:, :60,3]=0; clk5=Image.fromarray(a)
bg=Image.new('RGBA',(S,S),NOCHE+(255,)); bg.alpha_composite(radial((S,S),(S/2,S*0.55),S*0.7,NEB,150))
place(bg,clk5,S/2,int(S*0.72),width=1700,shadow_dark=True)
save(bg,'reloj-3d-perfil')
bg,fy=studio_bg(floor=0.52)
d=ImageDraw.Draw(bg); title(d,'Mucho más que la hora')
x,y,w,h=place(bg,clk,S/2,int(S*0.52),width=1500)
d.line((x,y+h+60,x+w,y+h+60),fill=NOCHE,width=5)
for xx in (x,x+w): d.line((xx,y+h+40,xx,y+h+80),fill=NOCHE,width=5)
d.text((S/2,y+h+120),'16,3 × 6 × 1,65 cm',font=font('DMSans-Bold.ttf',56),fill=NOCHE,anchor='mm')
bullets(d,[('Hora, fecha y temperatura',''),('3 alarmas y modo noche',''),('3 niveles de brillo · de mesa o de pared',''),('USB 5 V (cable incluido)','')],330,y+h+260,step=105)
save(bg,'reloj-3d-funciones')

# ---------- LAMPARA ----------
L={k:decable(Image.open(C+f'lamp_{k}_clean.png').convert('RGBA')) for k in ['saturn','moon','galaxy','solar']}
for k,nm in [('saturn','saturno'),('moon','luna'),('galaxy','galaxia'),('solar','sistema-solar')]:
    bg,fy=night_bg(seed=hash(k)%100)
    place(bg,L[k],S/2,fy+60,height=1250,glow=AMBAR,glow_a=110,reflect=0.28,shadow_dark=True)
    save(bg,f'lampara-{nm}-noche')
bg,fy=studio_bg(); place(bg,L['saturn'],S/2,fy+40,height=1250); save(bg,'lampara-saturno-estudio')
bg,fy=night_bg(seed=7)
for k,cx,h,by in [('galaxy',380,700,fy-10),('solar',1620,700,fy-10),('moon',800,860,fy+70),('saturn',1220,860,fy+70)]:
    place(bg,L[k],cx,by,height=h,glow=AMBAR,glow_a=55,shadow_dark=True)
save(bg,'lampara-4-modelos')
bg,fy=studio_bg(floor=0.8); d=ImageDraw.Draw(bg); title(d,'Pequeña, pero se hace notar',y=170,size=82)
x,y,w,h=place(bg,L['saturn'],S/2-150,int(S*0.8)+10,height=1060)
f=font('DMSans-Bold.ttf',58); bx=x+w+70; bt=y+int(h*0.02); bb=y+int(h*0.72); base=y+h
for (a1,a2) in ((bt,bb),(bb+25,base)):
    d.line((bx,a1,bx,a2),fill=NOCHE,width=5); d.line((bx-20,a1,bx+20,a1),fill=NOCHE,width=5); d.line((bx-20,a2,bx+20,a2),fill=NOCHE,width=5)
d.text((bx+40,(bt+bb)/2),'Bola de 5 cm',font=f,fill=NOCHE,anchor='lm'); d.text((bx+40,(bb+base)/2+10),'Base 5 × 2 cm',font=f,fill=NOCHE,anchor='lm')
d.text((S/2,S-150),'Cristal grabado por láser · base de madera · USB, cable de 1 m',font=font('DMSans-Regular.ttf',46),fill=(70,70,110),anchor='mm')
save(bg,'lampara-medidas')

# ---------- BANNERS ----------
def hero(size,name,floor,items):
    bg,fy=night_bg(size=size,seed=99,floor=floor)
    for key,cx,by,hh in items:
        if key=='clk': place(bg,clk,cx,by,width=hh,glow=(235,240,255),glow_a=60,glow_r=0.4,reflect=0.2,shadow_dark=True)
        elif key=='wave': place(bg,wt,cx,by,height=hh,glow=TEAL,glow_a=110,glow_r=0.7,reflect=0.22,shadow_dark=True)
        else: place(bg,L['saturn'],cx,by,height=hh,glow=AMBAR,glow_a=90,reflect=0.22,shadow_dark=True)
    save(bg,name)
W,H=2400,1200; f=int(H*0.76)
hero((W,H),'banner-portada-escritorio',0.76,[('clk',1760,f-420,900),('wave',1500,f+40,560),('sat',2050,f+40,520)])
W,H=1200,1500; f=int(H*0.8)
hero((W,H),'banner-portada-movil',0.8,[('clk',600,f-520,960),('wave',380,f+40,520),('sat',860,f+40,470)])
