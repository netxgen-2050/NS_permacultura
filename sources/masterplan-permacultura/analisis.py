import json, sys, numpy as np, rasterio
from rasterio.windows import from_bounds
from shapely.geometry import shape, Point
S=sys.argv[1]; G=sys.argv[2]
d=json.load(open(G))
macro=[f for f in d['features'] if f['properties']['tipo']=='macrolote'][0]
poly=shape(macro['geometry']); print('bounds',poly.bounds)
minx,miny,maxx,maxy=poly.bounds
m=0.03
with rasterio.open(S+'/dem/Copernicus_DSM_COG_10_S40_00_W068_00_DEM.tif') as src:
    w=from_bounds(minx-m,miny-0.05,maxx+m,maxy+0.01,src.transform)
    z=src.read(1,window=w).astype(float); T=src.window_transform(w)
print('shape',z.shape,'z',z.min(),z.max())
np.save(S+'/z.npy',z); json.dump(list(T)[:6],open(S+'/T.json','w'))
# mask inside polygon
H,W=z.shape
ins=np.zeros_like(z,bool)
for r in range(H):
  for c in range(W):
    x,y=T*(c+0.5,r+0.5)
    ins[r,c]=poly.contains(Point(x,y))
np.save(S+'/ins.npy',ins)
zi=z[ins]; print('inside cells',ins.sum(),'z inside min/max/pcts',zi.min(),zi.max(),np.percentile(zi,[5,25,50,75,95]))
