import numpy as np
# Wireworld-free: Generations "Star Wars" B2/S345/4 style
n=160
rng=np.random.default_rng(7)
g=np.zeros((n,n),int)
m=rng.random((n,n))<.15
g[m]=1
C=4
for t in range(120):
    alive=(g==1).astype(int)
    s=sum(np.roll(np.roll(alive,i,0),j,1) for i in(-1,0,1) for j in(-1,0,1) if i or j)
    new=np.zeros_like(g)
    new[(g==0)&(s==2)]=1
    new[(g==1)&np.isin(s,[3,4,5])]=1
    d=(g==1)&~np.isin(s,[3,4,5]); new[d]=2
    for k in range(2,C-1): new[g==k]=k+1
    g=new
pal=np.array([[10,10,30],[255,240,180],[240,120,60],[150,40,90]],np.uint8)
img=pal[g].repeat(5,0).repeat(5,1)
open('sw.ppm','wb').write(b'P6 %d %d 255\n'%(img.shape[1],img.shape[0])+img.tobytes())
