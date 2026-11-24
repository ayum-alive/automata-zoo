import numpy as np
n=160
rng=np.random.default_rng(3)
g=(rng.random((n,n))<.5).astype(int)
# Life with fading trails
tr=np.zeros((n,n))
for t in range(300):
    s=sum(np.roll(np.roll(g,i,0),j,1) for i in(-1,0,1) for j in(-1,0,1) if i or j)
    g=(((g==1)&((s==2)|(s==3)))|((g==0)&(s==3))).astype(int)
    tr=np.maximum(tr*.97,g)
a=tr
img=np.stack([a**.7*255,a**1.5*200+20,a*120+40],-1).astype(np.uint8).repeat(5,0).repeat(5,1)
open('life.ppm','wb').write(b'P6 %d %d 255\n'%(img.shape[1],img.shape[0])+img.tobytes())
