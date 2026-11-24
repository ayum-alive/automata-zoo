import numpy as np
n=140
rng=np.random.default_rng(21)
# Rule: Larger than Life-ish "bugs"? use Conway variant HighLife (B36/S23)
g=(rng.random((n,n))<.35).astype(int)
tr=np.zeros((n,n))
for t in range(250):
    s=sum(np.roll(np.roll(g,i,0),j,1) for i in(-1,0,1) for j in(-1,0,1) if i or j)
    g=(((g==1)&((s==2)|(s==3)))|((g==0)&((s==3)|(s==6)))).astype(int)
    tr=np.maximum(tr*.96,g)
a=tr
img=np.stack([a*90+20,a**.8*220+15,a**.6*200+40],-1).astype(np.uint8).repeat(5,0).repeat(5,1)
open('hl.ppm','wb').write(b'P6 %d %d 255\n'%(img.shape[1],img.shape[0])+img.tobytes())
