from lib import *
C='cut/'
GOLD=(255,196,90)
def fit_cover(img,size):
    w,h=size; r=max(w/img.width,h/img.height); img=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(img.width-w)//2; y=(img.height-h)//2; return img.crop((x,y,x+w,y+h))
def rounded(img,rad):
    m=Image.new('L',img.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,img.width,img.height),rad,fill=255); img=img.convert('RGBA'); img.putalpha(m); return img
g1=Image.open(C+'globo_g01_full.png').convert('RGBA')
g5=Image.open(C+'globo_g05_full.png').convert('RGBA')
g6=Image.open(C+'globo_g06_full.png').convert('RGBA')
a=np.array(g6); bb=g6.getbbox(); cut=int(bb[1]+(bb[3]-bb[1])*0.8); a[cut:,:,3]=0; g6=Image.fromarray(a)
bg,fy=night_bg(seed=41,floor=0.78)
place(bg,g1,S/2,fy+70,height=1350,glow=GOLD,glow_a=120,glow_r=0.7,reflect=0.25,shadow_dark=True)
save(bg,'globo-levita-noche')
bg,fy=studio_bg(floor=0.8)
place(bg,g5,S/2,fy+40,height=1400)
save(bg,'globo-levita-estudio')
bg,fy=night_bg(seed=42,floor=0.8)
place(bg,g6,S/2,fy+60,height=1380,glow=GOLD,glow_a=80,glow_r=0.7,shadow_dark=True)
save(bg,'globo-levita-base')
# ambiente real
amb=Image.open('globo/g02.jpg').convert('RGB')
bg=Image.new('RGBA',(S,S),NOCHE+(255,)); bg.alpha_composite(radial((S,S),(S/2,S*0.4),S*0.7,GOLD,50))
ph=rounded(fit_cover(amb,(1760,1440)),48); bg.alpha_composite(ph,(120,120))
d=ImageDraw.Draw(bg)
d.text((S/2,1740),'Flota en el aire. De verdad.',font=font('Unbounded-Bold.ttf',78),fill=LUNA,anchor='mm')
d.text((S/2,1850),'Levitación magnética: el globo se mantiene suspendido sobre la base',font=font('DMSans-Regular.ttf',44),fill=NIEBLA,anchor='mm')
save(bg,'globo-levita-ambiente')
# medidas
bg,fy=studio_bg(floor=0.66)
d=ImageDraw.Draw(bg); d.text((S/2,160),'Una pieza para mirar dos veces',font=font('Unbounded-Bold.ttf',72),fill=NOCHE,anchor='mm')
x,y,w,h=place(bg,g5,S/2-120,int(S*0.66),height=1050)
arr=np.array(g5.crop(g5.getbbox()))[:,:,3]; rows=np.where(arr.max(1)>40)[0]
# find gap (levitation) rows
alpha_rows=arr.max(1)>40
gaps=[i for i in range(int(len(alpha_rows)*0.5),int(len(alpha_rows)*0.95)) if not alpha_rows[i]]
r=h/arr.shape[0]
gstart=int(min(gaps)*r) if gaps else int(h*0.72); gend=int(max(gaps)*r) if gaps else int(h*0.78)
bx=x+w+60; f=font('DMSans-Bold.ttf',56)
for (a1,a2,t) in ((y,y+gstart,'Globo de 14 cm'),(y+gend,y+h,'Base de 17 × 3 cm')):
    d.line((bx,a1,bx,a2),fill=NOCHE,width=5); d.line((bx-20,a1,bx+20,a1),fill=NOCHE,width=5); d.line((bx-20,a2,bx+20,a2),fill=NOCHE,width=5)
    d.text((bx+36,(a1+a2)/2),t,font=f,fill=NOCHE,anchor='lm')
yy=int(S*0.66)+160
for t,sub in [('Levita y gira sobre la base',''),('Luz blanca que ilumina el globo',''),('Botón táctil · base de cristal templado',''),('Adaptador de corriente 12 V / 1 A','')]:
    d.ellipse((300-14,yy-14,300+14,yy+14),fill=AMBAR); d.text((340,yy),t,font=font('DMSans-Bold.ttf',50),fill=NOCHE,anchor='lm'); yy+=100
save(bg,'globo-levita-medidas')
