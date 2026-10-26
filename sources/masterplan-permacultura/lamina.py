import json,sys,math,matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from PIL import Image
S,V=sys.argv[1],sys.argv[2]
fc=json.load(open(V+'/alternativa-permacultura.json')); md=fc['metadata']
im=Image.open(S+'/sat16.jpg'); E=[-67.3297119140625,-67.291259765625,-39.16414104768742,-39.10448880944048]
EST={'agua':dict(fc='#6baed6',ec='#08519c',a=.45,ls='-'),'produccion':dict(fc='#fec44f',ec='#b8860b',a=.4,ls='--'),
'asentamiento':dict(fc='#bcbddc',ec='#54278f',a=.85,ls='-'),'implementacion':dict(fc='#fa9fb5',ec='#c51b8a',a=.55,ls='-'),
'silvestre':dict(fc='#41ab5d',ec='#005a32',a=.35,ls=':')}
fig=plt.figure(figsize=(16,14),facecolor='#f6f3ea')
def dibujar(ax,lim,etiquetas):
  ax.imshow(im,extent=E,aspect=1/math.cos(math.radians(39.13)))
  orden=sorted(fc['features'],key=lambda f:-(f['properties'].get('area_ha') or 0))
  for f in orden:
    p=f['properties'];g=f['geometry'];c=p['capa']
    polys=[g['coordinates']] if g['type']=='Polygon' else g['coordinates'] if g['type']=='MultiPolygon' else []
    for pl in polys:
      xs,ys=zip(*pl[0]); e=EST[c]
      crec=p['id'].startswith('pc-crecimiento')
      ax.fill(xs,ys,color=e['fc'],alpha=0.05 if crec else (.18 if p['id']=='pc-zona-4' else e['a']),lw=0)
      ax.plot(xs,ys,color=e['ec'],lw=2.2 if crec else 1.2,ls='--' if crec else e['ls'])
    if g['type'] in('LineString','MultiLineString'):
      ls=[g['coordinates']] if g['type']=='LineString' else g['coordinates']
      for l in ls:
        xs,ys=zip(*l)
        if c=='camino': ax.plot(xs,ys,color='#333',lw=5.5); ax.plot(xs,ys,color='white',lw=3.5)
        else: ax.plot(xs,ys,color='#238b45',lw=3.5,ls=(0,(1,1.5)))
    if g['type'] in('Point','MultiPoint'):
      pts=[g['coordinates']] if g['type']=='Point' else g['coordinates']
      for x,y in pts: ax.plot(x,y,'o' if c=='obra' and g['type']=='MultiPoint' else 's',color='#08519c',mec='white',ms=7 if g['type']=='MultiPoint' else 10)
  m=json.load(open('/Users/gus/Documents/dev/NetXState/lighthouse-platform/lib/territorios/biopueblo-territorios.json'))
  mac=[f for f in m['features'] if f['properties']['tipo']=='macrolote'][0]; xs,ys=zip(*mac['geometry']['coordinates'][0]); ax.plot(xs,ys,color='#d7301f',lw=2.5)
  for f in fc['features']:
    p=f['properties']
    if p['id'] in etiquetas:
      g=f['geometry']; pts=g['coordinates'][0] if g['type']=='Polygon' else g['coordinates'][0][0] if g['type']=='MultiPolygon' else g['coordinates'] if g['type']=='LineString' else g['coordinates'][0] if g['type']=='MultiLineString' else [g['coordinates']]
      x=sum(q[0] for q in pts)/len(pts); y=sum(q[1] for q in pts)/len(pts); dx,dy=etiquetas[p['id']]
      ax.annotate(p['nombre'],(x,y),(x+dx,y+dy),fontsize=9.5,fontweight='bold',color='#14241a',
        bbox=dict(boxstyle='round,pad=0.25',fc='white',ec='#999',alpha=.9),arrowprops=dict(arrowstyle='-',color='white',lw=1.2))
  ax.set_xlim(lim[0],lim[1]); ax.set_ylim(lim[2],lim[3]); ax.set_xticks([]); ax.set_yticks([])
ax1=fig.add_axes([0.01,0.02,0.40,0.85])
dibujar(ax1,(-67.3285,-67.2925,-39.1615,-39.1050),{'pc-zona-5':(-0.004,-0.008),'pc-zona-4':(-0.006,-0.004),'pc-zona-3':(-0.002,-0.006),'pc-corredor':(-0.003,-0.015),'pc-camino':(0.002,0.004)})
ax1.set_title('Macrolote 7 completo · 998 ha',fontsize=13,loc='left')
# escala
x0,y0=-67.3275,-39.1595; km=1/(111.32*math.cos(math.radians(39.13)))
ax1.plot([x0,x0+km],[y0,y0],color='white',lw=4); ax1.text(x0+km/2,y0+0.0006,'1 km',color='white',ha='center',fontsize=10,fontweight='bold')
ax1.annotate('N',(-67.2945,-39.1085),(-67.2945,-39.1115),color='white',ha='center',fontsize=14,fontweight='bold',arrowprops=dict(arrowstyle='->',color='white',lw=2))
ax2=fig.add_axes([0.43,0.35,0.56,0.52])
dibujar(ax2,(-67.3215,-67.3035,-39.1250,-39.1062),{'pc-hectarea-1':(-0.0042,0.0012),'pc-nucleo':(0.0025,0.0009),'pc-cluster-1':(-0.0035,-0.0012),'pc-cluster-2':(-0.0008,0.0032),'pc-cluster-3':(0.0015,-0.0025),'pc-cluster-4':(0.003,0.0005),'pc-ribera':(-0.0015,0.0022),'pc-desembocadura':(-0.0045,-0.0005),'pc-tanque':(0.004,-0.0012),'pc-crecimiento-7':(0.0035,0.0035),'pc-rompevientos':(0.0035,-0.0035)})
ax2.set_title('Detalle: el cono junto al río',fontsize=13,loc='left')
fig.text(0.01,0.955,'Lighthouse · Masterplan de permacultura v0.1 (alternativa)',fontsize=21,fontweight='bold',color='#154626')
fig.text(0.01,0.925,'Borrador del Agente de Regeneración · preliminar e ilustrativo · leído desde el agua y el relieve (MDE Copernicus 30 m) · 26-oct-2026',fontsize=11.5,color='#566258')
leg=[Patch(fc=EST['agua']['fc'],ec=EST['agua']['ec'],label='Agua y bienes comunes: columna verde del cañadón, ribera, desembocadura'),
Patch(fc=EST['implementacion']['fc'],ec=EST['implementacion']['ec'],label='Primera hectárea y crecimiento Fibonacci (año 4: ~7 ha · año 7: ~34 ha)'),
Patch(fc=EST['asentamiento']['fc'],ec=EST['asentamiento']['ec'],label='Asentamiento: núcleo común + 4 clusters de ~16 familias (zona 0–1)'),
Patch(fc=EST['produccion']['fc'],ec=EST['produccion']['ec'],ls='--',label='Producción: huertas (zona 2), planicie sin vivienda, agroforestería con agua (zona 3)'),
Patch(fc=EST['silvestre']['fc'],ec=EST['silvestre']['ec'],ls=':',label='Monte: manejado con cosecha de agua (zona 4) y silvestre (zona 5)'),
Line2D([0],[0],color='#555',lw=3.5,label='Acceso por la divisoria este (un solo cruce del cauce)'),
Line2D([0],[0],color='#238b45',lw=3.5,ls=(0,(1,1.5)),label='Cortinas rompevientos NO–SE (viento dominante del SO)'),
Line2D([0],[0],marker='o',color='w',mfc='#08519c',ms=9,label='Esparcidores de crecidas · ■ tanque alto'),
Line2D([0],[0],color='#d7301f',lw=2.5,label='Límite del Macrolote 7')]
lg=fig.legend(handles=leg,loc='lower left',bbox_to_anchor=(0.43,0.115),fontsize=10,frameon=True,facecolor='white',edgecolor='#ccc',ncol=1)
for t in [('Cuenca del cañadón','~2.000 ha (el doble del lote)'),('Proporción ecológica','~52%'),('Columna verde','~239 ha')]:
  pass
fig.text(0.43,0.06,'Cuenca del cañadón: ~2.000 ha, el doble del lote  ·  Proporción ecológica: ~52%\nColumna verde: ~239 ha  ·  4 clusters: ~12 ha  ·  Primera hectárea al pie de una subcuenca de ~47 ha',fontsize=11,fontweight='bold',color='#14241a')
fig.text(0.43,0.015,'No es un plano: falta relevamiento (cota DPA, LiDAR, suelos, derecho de agua),\nobservación del sitio y diseño humano. Ver doc 21 del vault NS_permacultura.',fontsize=10,color='#5d4300')
fig.savefig(V+'/Masterplan permacultura v0.1 - lamina.png',dpi=110,facecolor=fig.get_facecolor())
