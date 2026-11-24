import numpy as np
n=200
g=np.zeros((n,n),int); g[n//2-1:n//2+1,n//2-1:n//2+1]=1
acc=np.zeros((n,n))
for t in range(70):
    s=sum(np.roll(np.roll(g,i,0),j,1) for i in(-1,0,1) for j in(-1,0,1) if i or j)
    g=((g==0)&(s==2)).astype(int)
    acc+=g*(t+1)

a=acc/acc.max()
# magma-ish ramp
r=np.clip(a*3,0,1);gc=np.clip(a*3-1,0,1)*.8;b=np.clip(a*2,0,1)*.6+np.clip(a*3-2,0,1)*.4
img=(np.stack([r,gc,b],-1)*255).astype(np.uint8).repeat(4,0).repeat(4,1)
with open('seeds.ppm','wb') as f:
    f.write(b'P6 %d %d 255\n'%(img.shape[1],img.shape[0]));f.write(img.tobytes())
