from lib import *
import sys
R='rooms/'; C='cut/'
def room(n): return Image.open(R+n+'.png').convert('RGBA')
def soft_shadow(bg,cx,by,w,a=150,flat=0.035,up=0.0):
    by=by-w*up
    sh=Image.new('RGBA',bg.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
    d.ellipse((cx-w*0.52,by-w*flat*1.3,cx+w*0.52,by+w*flat*0.5),fill=(0,0,0,a))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(w*0.025)))
def put(bg,obj,cx,by,height,glow=None,ga=110,gr=1.0,shadow=150,foot=0.0,up=0.0,flat=0.035):
    a=obj.getchannel('A').point(lambda v:255 if v>60 else 0); obj=obj.crop(a.getbbox()); r=height/obj.height; obj=obj.resize((int(obj.width*r),int(obj.height*r)),Image.LANCZOS)
    x=int(cx-obj.width/2); y=int(by+foot*obj.height-obj.height)
    if glow:
        bg.alpha_composite(radial(bg.size,(cx,y+obj.height*0.5),obj.width*1.6*gr,glow,ga))
        # light pool on the surface
        pool=Image.new('RGBA',bg.size,(0,0,0,0)); d=ImageDraw.Draw(pool)
        d.ellipse((cx-obj.width*1.1,by-obj.width*0.12,cx+obj.width*1.1,by+obj.width*0.18),fill=glow+(int(ga*0.8),))
        bg.alpha_composite(pool.filter(ImageFilter.GaussianBlur(obj.width*0.18)))
    if shadow: soft_shadow(bg,cx,by,obj.width,shadow,flat,up)
    bg.alpha_composite(obj,(x,y)); return (x,y,obj.width,obj.height)
def dim(bg,f):
    a=np.array(bg).astype(float); a[:,:,:3]*=f; return Image.fromarray(a.clip(0,255).astype('uint8'))
def crop_sq(bg,cx,cy,size,out=2000):
    x0=int(max(0,min(bg.width-size,cx-size/2))); y0=int(max(0,min(bg.height-size,cy-size/2)))
    return bg.crop((x0,y0,x0+size,y0+size)).resize((out,out),Image.LANCZOS)
WARM=(255,190,110); TEAL=(90,220,235); GOLD=(255,196,90); WHITE=(235,240,255)
res={}
# 1 lámpara Saturno en mesilla
bg=dim(room('mesilla2'),0.62)
put(bg,Image.open(C+'lamp_saturn_clean.png').convert('RGBA'),1000,1215,380,glow=WARM,ga=170,gr=1.3,foot=0.095,shadow=200)
res['lampara-saturno-mesilla']=crop_sq(bg,1050,1030,1100)
# 2 proyector en mesilla
bg=dim(room('mesilla1'),0.6)
put(bg,Image.open(C+'w_teal_gold.png').convert('RGBA'),960,1420,400,glow=TEAL,ga=150,gr=1.3,shadow=230,up=0.06,flat=0.08)
res['proyector-ondas-mesilla']=crop_sq(bg,960,1180,1300)
# 3 globo en escritorio
bg=dim(room('escritorio1'),0.85)
put(bg,Image.open(C+'globo_g01_full.png').convert('RGBA'),1080,1640,860,glow=GOLD,ga=100,shadow=170)
res['globo-levita-escritorio']=crop_sq(bg,1080,1250,1450)
# 4 reloj en estante
bg=dim(room('salon2'),0.68)
put(bg,Image.open(C+'clock_04__bir.png').convert('RGBA'),1020,1040,190,glow=WHITE,ga=55,shadow=140)
res['reloj-3d-estante']=crop_sq(bg,1020,960,950)
for k,v in res.items():
    v.convert('RGB').save('rooms/out_'+k+'.jpg',quality=88); print(k)
