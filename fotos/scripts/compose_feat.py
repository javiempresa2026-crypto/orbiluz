from lib import *
C='cut/'
def obj(f,thr=60):
    o=Image.open(C+f).convert('RGBA'); a=o.getchannel('A').point(lambda v:255 if v>thr else 0); return o.crop(a.getbbox())
def card(bg,x,y,w,h,num,title,sub):
    lay=Image.new('RGBA',bg.size,(0,0,0,0)); d=ImageDraw.Draw(lay)
    d.rounded_rectangle((x,y,x+w,y+h),36,fill=(28,28,78,235),outline=(124,108,246,110),width=2)
    bg.alpha_composite(lay); d=ImageDraw.Draw(bg)
    cx,cy=x+80,y+h/2
    d.ellipse((cx-46,cy-46,cx+46,cy+46),fill=AMBAR)
    d.text((cx,cy+2),str(num),font=font('Unbounded-Bold.ttf',44),fill=NOCHE,anchor='mm')
    d.text((x+160,cy-26),title,font=font('DMSans-Bold.ttf',52),fill=LUNA,anchor='lm')
    d.text((x+160,cy+34),sub,font=font('DMSans-Regular.ttf',38),fill=NIEBLA,anchor='lm')
def make(name,o,glow,title,items,oh):
    bg,fy=night_bg(seed=hash(name)%100,floor=0.9)
    d=ImageDraw.Draw(bg)
    d.text((S/2,150),title,font=font('Unbounded-Bold.ttf',76),fill=LUNA,anchor='mm')
    d.text((S/2,240),'Orbiluz',font=font('DMSans-Bold.ttf',40),fill=AMBAR,anchor='mm')
    # product left
    r=oh/o.height; ow=int(o.width*r)
    if ow>820: r=820/o.width
    oo=o.resize((int(o.width*r),int(o.height*r)),Image.LANCZOS)
    cx=520; by=1180+oo.height/2
    bg.alpha_composite(radial(bg.size,(cx,by-oo.height/2),max(oo.width,oo.height)*1.1,glow,120))
    bg.alpha_composite(oo,(int(cx-oo.width/2),int(by-oo.height)))
    y=560; h=230
    for i,(t,s) in enumerate(items):
        card(bg,1000,y+i*(h+40),900,h,i+1,t,s)
    save(bg,name)
make('lampara-caracteristicas',obj('lamp_saturn_clean.png'),(255,190,110),'Lo que la hace especial',
 [('Grabado láser 3D','Dentro del cristal'),('Luz cálida y suave','Ideal como luz de noche'),('Base de madera natural','Con cable USB de 1 m'),('Bajo consumo','USB, solo 0,5 W')],1000)
make('proyector-caracteristicas',obj('w_teal_gold.png'),(90,220,235),'Todo lo que puede hacer',
 [('16 colores','Y brillo regulable'),('Mando a distancia','Incluido en la caja'),('Botón táctil','En la base, sin buscar el mando'),('Funciona por USB','5 V, con cualquier cargador de móvil')],900)
make('reloj-3d-caracteristicas',obj('clock_04__bir.png'),(235,240,255),'Mucho más que la hora',
 [('Hora, fecha y temperatura','La pantalla va alternando'),('3 alarmas','Para no quedarte dormido'),('Modo noche','Baja el brillo automáticamente'),('De pared o de mesa','Con soporte incluido')],330)
make('globo-levita-caracteristicas',obj('globo_g01_full.png'),(255,196,90),'Una pieza que flota',
 [('Levitación magnética','Sin hilos ni soportes'),('Gira despacio','Sobre su base'),('Se ilumina por dentro','Luz blanca'),('Botón táctil','En la base de cristal templado')],1000)
