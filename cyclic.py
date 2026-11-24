import numpy as np
n=120
rng=np.random.default_rng(11)
# Gray-Scott style would be heavy; do cyclic CA (Hodge-like) spirals
S=14
g=rng.integers(0,S,(n,n))
for t in range(120):
    nxt=(g+1)%S
    c=sum((np.roll(np.roll(g,i,0),j,1)==nxt) for i in(-1,0,1) for j in(-1,0,1) if i or j)
    g=np.where(c>=1,nxt,g)
import colorsys
pal=np.array([[int(x*255) for x in colorsys.hsv_to_rgb(k/S,.7,.95)] for k in range(S)],np.uint8)
img=pal[g].repeat(6,0).repeat(6,1)
open('cy.ppm','wb').write(b'P6 %d %d 255\n'%(img.shape[1],img.shape[0])+img.tobytes())
