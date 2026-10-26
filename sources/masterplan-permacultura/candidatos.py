import json,sys,numpy as np
from scipy import ndimage
S=sys.argv[1]
z=np.load(S+'/z.npy'); ins=np.load(S+'/ins.npy'); T=json.load(open(S+'/T.json')); A=np.load(S+'/acc_ha.npy'); sl=np.load(S+'/slope.npy')
H,W=z.shape
def xy(r,c): return T[2]+T[0]*(c+.5),T[5]+T[4]*(r+.5)
river=(z<209.5)
lab,n=ndimage.label(river); big=[i for i in range(1,n+1) if (lab==i).sum()>200]; river=np.isin(lab,big)
print('river cells',river.sum())
dr=ndimage.distance_transform_edt(~river,sampling=(30.8,24))
for cota in (214,215,216,217,218):
  fp=(z<=cota)&ins; print('cota',cota,'ha',round(fp.sum()*0.0739,1))
ch=A>=30; dch=ndimage.distance_transform_edt(~ch,sampling=(30.8,24))
main=A>=200; dmain=ndimage.distance_transform_edt(~main,sampling=(30.8,24))
# elevation histogram in north part
north=np.zeros_like(ins); 
for r in range(H):
  x,y=xy(r,0)
  if y>-39.125: north[r]=True
cand=ins&(z>216)&(z<245)&(sl<6)&(dch>80)&(dmain>120)&north
print('cand ha',cand.sum()*0.0739)
lab,n=ndimage.label(cand)
for i in range(1,n+1):
  m=lab==i; s=m.sum()*0.0739
  if s>2:
    rr,cc=np.argwhere(m).mean(0); x,y=xy(rr,cc); print(f'grupo {i}: {s:.1f} ha centro {x:.5f},{y:.5f} z {z[m].mean():.0f} pend {sl[m].mean():.1f}%')
np.save(S+'/cand.npy',cand); np.save(S+'/river.npy',river)
