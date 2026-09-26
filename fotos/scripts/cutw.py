from rembg import remove, new_session
from PIL import Image
s=new_session('birefnet-general-lite')
def cut(src,box,out):
    im=Image.open('src/'+src).convert('RGB'); W,H=im.size
    if box: im=im.crop(tuple(int(v*W if i%2==0 else v*H) for i,v in enumerate(box)))
    o=remove(im,session=s); o.save('cut/'+out); print(out,o.size,o.getbbox())
cut('wave_S115e686037ea4a6084442aab980e2ffeX.jpg',(0.33,0.22,0.87,0.78),'w_teal_dark.png')  # adjust after look
cut('wave_S6d6bcc882e2d422b844230074482802df.png',(0.40,0.44,0.95,1.0),'w_teal_gold.png')
cut('wave_Sa51a9160c2cd4227897c9f4387026f168.jpg',(0.36,0.31,0.80,0.79),'w_amber.png')
