import json, sys, heapq, numpy as np
S=sys.argv[1]
z=np.load(S+'/z.npy'); ins=np.load(S+'/ins.npy'); T=json.load(open(S+'/T.json'))
H,W=z.shape
dx=abs(T[0])*111320*np.cos(np.radians(39.13)); dy=abs(T[4])*110950
print('cell m',dx,dy)
# priority flood fill
f=z.copy(); seen=np.zeros_like(z,bool); pq=[]
for r in range(H):
  for c in range(W):
    if r in (0,H-1) or c in (0,W-1):
      heapq.heappush(pq,(f[r,c],r,c)); seen[r,c]=True
N=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
while pq:
  e,r,c=heapq.heappop(pq)
  for a,b in N:
    rr,cc=r+a,c+b
    if 0<=rr<H and 0<=cc<W and not seen[rr,cc]:
      seen[rr,cc]=True
      if f[rr,cc]<=e: f[rr,cc]=e+1e-3
      heapq.heappush(pq,(f[rr,cc],rr,cc))
# D8
dist=[np.hypot(a*dy,b*dx) for a,b in N]
fd=-np.ones((H,W),int)
for r in range(1,H-1):
  for c in range(1,W-1):
    best=0;bi=-1
    for i,(a,b) in enumerate(N):
      s=(f[r,c]-f[r+a,c+b])/dist[i]
      if s>best: best=s;bi=i
    fd[r,c]=bi
order=np.argsort(-f,axis=None)
acc=np.ones((H,W))
for k in order:
  r,c=divmod(k,W); i=fd[r,c]
  if i>=0: acc[r+N[i][0],c+N[i][1]]+=acc[r,c]
area=acc*dx*dy/1e4  # ha
gy,gx=np.gradient(z,dy,dx); slope=np.hypot(gx,gy)*100
np.save(S+'/f.npy',f);np.save(S+'/fd.npy',fd);np.save(S+'/acc_ha.npy',area);np.save(S+'/slope.npy',slope)
print('slope inside pcts',np.percentile(slope[ins],[10,25,50,75,90,97]))
# outlets inside polygon: max area cells inside
idx=np.argsort(-area*ins,axis=None)[:5]
for k in idx:
  r,c=divmod(k,W); x,y=T[2]+T[0]*(c+.5),T[5]+T[4]*(r+.5); print('max acc',round(area[r,c]),'ha at',round(x,5),round(y,5),'z',round(z[r,c],1))
