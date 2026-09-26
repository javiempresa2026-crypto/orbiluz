import cv2, numpy as np
names=['lamp_saturn','lamp_moon','lamp_galaxy','lamp_solar']
k=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
ims=[cv2.imread(f'src/{n}.jpg') for n in names]
grs=[cv2.cvtColor(i,cv2.COLOR_BGR2GRAY).astype(np.float32) for i in ims]
ths=[cv2.morphologyEx(g,cv2.MORPH_TOPHAT,k) for g in grs]
common=np.min(ths,axis=0)
H,W=common.shape; yy,xx=np.mgrid[:H,:W]; s=xx+yy
band=np.zeros_like(common,bool)
for c in (385,805,1207): band|=np.abs(s-c)<24
base=(common>4)&band
for n,im,g,th in zip(names,ims,grs,ths):
    ok=base&(th<common*2.2+5)&(g<170)
    m=cv2.dilate(ok.astype(np.uint8)*255,np.ones((3,3),np.uint8),iterations=2)
    # remove dilated pixels that land on bright engraving
    m[(g>170)]=0
    out=cv2.inpaint(im,m,3,cv2.INPAINT_TELEA)
    cv2.imwrite(f'src/{n}_clean.png',out)
    th2=cv2.morphologyEx(cv2.cvtColor(out,cv2.COLOR_BGR2GRAY).astype(np.float32),cv2.MORPH_TOPHAT,k)
    cv2.imwrite(f'res_clean_{n}.jpg',np.clip(th2*6,0,255).astype(np.uint8))
