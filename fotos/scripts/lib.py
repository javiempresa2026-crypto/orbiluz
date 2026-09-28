import os
ROOT=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))+'/'
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import numpy as np, random
F=ROOT+'marca/fuentes/'
OUT=ROOT+'fotos/'
NOCHE=(18,18,58); AMBAR=(255,181,71); NEB=(124,108,246); LUNA=(255,246,233); CORAL=(255,122,89); NIEBLA=(167,169,201)
S=2000
def font(n,s): return ImageFont.truetype(F+n,s)

def trim(im):
    return im.crop(im.getbbox())

def radial(size,center,radius,color,alpha=255):
    w,h=size; y,x=np.ogrid[:h,:w]
    d=np.sqrt((x-center[0])**2+(y-center[1])**2)/radius
    a=np.clip(1-d,0,1)**2*alpha
    im=Image.new('RGBA',size,color+(0,)); im.putalpha(Image.fromarray(a.astype('uint8'))); return im

def night_bg(size=(S,S),stars=True,floor=0.72,seed=1):
    w,h=size
    y=np.linspace(0,1,h)[:,None]
    top=np.array((10,10,34)); mid=np.array(NOCHE); 
    g=(top*(1-y)+mid*y)
    arr=np.repeat(g[:,None,:],w,axis=1).reshape(h,w,3)
    bg=Image.fromarray(arr.astype('uint8')).convert('RGBA')
    bg.alpha_composite(radial(size,(w*0.78,h*0.18),w*0.55,NEB,70))
    bg.alpha_composite(radial(size,(w*0.15,h*0.9),w*0.5,NEB,40))
    if stars:
        rnd=random.Random(seed); d=ImageDraw.Draw(bg)
        for _ in range(int(w*h/9000)):
            x=rnd.random()*w; yy=rnd.random()*h*floor; r=rnd.choice([1,1,1,1.5,2,2.5])*w/2000
            c=rnd.choice([LUNA,LUNA,NIEBLA,AMBAR]); a=rnd.randint(70,200)
            d.ellipse((x-r,yy-r,x+r,yy+r),fill=c+(a,))
    # desk surface
    fl=Image.new('RGBA',size,(0,0,0,0)); fd=ImageDraw.Draw(fl)
    fy=int(h*floor)
    for i in range(h-fy):
        t=i/(h-fy); c=tuple(int(v) for v in (np.array((24,22,64))*(1-t)+np.array((9,9,28))*t))
        fd.line((0,fy+i,w,fy+i),fill=c+(255,))
    bg.alpha_composite(fl)
    fd2=ImageDraw.Draw(bg); fd2.line((0,fy,w,fy),fill=NIEBLA+(40,),width=max(1,w//1000))
    return bg,fy

def studio_bg(size=(S,S),color=LUNA,floor=0.74):
    w,h=size
    bg=Image.new('RGBA',size,color+(255,))
    y=np.linspace(0,1,h)[:,None]
    shade=np.clip((y-floor)*1.2,0,1)*18
    arr=np.array(bg).astype(float); arr[:,:,:3]-=shade[:,:,None]
    bg=Image.fromarray(arr.clip(0,255).astype('uint8'))
    bg.alpha_composite(radial(size,(w*0.5,h*0.45),w*0.6,(255,255,255),120))
    return bg,int(h*floor)

def place(bg,obj,cx,base_y,width=None,height=None,shadow=True,reflect=0.0,glow=None,glow_r=0.6,glow_a=150,shadow_dark=False):
    obj=trim(obj)
    if width: r=width/obj.width
    else: r=height/obj.height
    obj=obj.resize((int(obj.width*r),int(obj.height*r)),Image.LANCZOS)
    x=int(cx-obj.width/2); y=int(base_y-obj.height)
    if glow:
        bg.alpha_composite(radial(bg.size,(cx,y+obj.height*0.45),obj.width*glow_r*1.6,glow,glow_a))
    if shadow:
        sh=Image.new('RGBA',bg.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
        a=170 if shadow_dark else 90
        d.ellipse((cx-obj.width*0.42,base_y-obj.width*0.035,cx+obj.width*0.42,base_y+obj.width*0.035),fill=(0,0,0,a))
        sh=sh.filter(ImageFilter.GaussianBlur(obj.width*0.03)); bg.alpha_composite(sh)
    if reflect>0:
        rf=obj.transpose(Image.FLIP_TOP_BOTTOM)
        h=rf.height; grad=np.linspace(reflect*255,0,h)[:,None]*np.ones((1,rf.width))
        grad=np.minimum(grad,np.array(rf.getchannel('A')).astype(float)*reflect)
        g2=np.zeros((h,rf.width)); g2[:]=grad; g2[int(h*0.35):]=0
        rf.putalpha(Image.fromarray(g2.astype('uint8'))); rf=rf.filter(ImageFilter.GaussianBlur(2))
        bg.alpha_composite(rf,(x,base_y))
    bg.alpha_composite(obj,(x,y))
    return (x,y,obj.width,obj.height)

def save(bg,name,q=88):
    bg.convert('RGB').save(OUT+name+'.jpg',quality=q,optimize=True,progressive=True); print(name)

def logo_small(bg,x,y,w):
    try:
        lg=Image.open(ROOT+'marca/logo/orbiluz-logo-luna.png').convert('RGBA')
        r=w/lg.width; lg=lg.resize((int(lg.width*r),int(lg.height*r)),Image.LANCZOS); bg.alpha_composite(lg,(x,y))
    except Exception as e: print(e)

