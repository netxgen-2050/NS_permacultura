import json,sys,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape, Point, Polygon, LineString, MultiPolygon, mapping, box
from shapely.ops import unary_union, transform
from pyproj import Transformer
S=sys.argv[1]; G=sys.argv[2]; OUT=sys.argv[3]
z=np.load(S+'/z.npy'); ins=np.load(S+'/ins.npy'); T=json.load(open(S+'/T.json')); A=np.load(S+'/acc_ha.npy'); sl=np.load(S+'/slope.npy')
H,W=z.shape
fw=Transformer.from_crs(4326,32719,always_xy=True).transform; bw=Transformer.from_crs(32719,4326,always_xy=True).transform
d=json.load(open(G)); macro=transform(fw,shape([f for f in d['features'] if f['properties']['tipo']=='macrolote'][0]['geometry']))
def xy(r,c): return T[2]+T[0]*(c+.5),T[5]+T[4]*(r+.5)
def cells(mask,grow=0):
  # union of cell rectangles in UTM
  polys=[]
  for r,c in np.argwhere(mask):
    x0,y0=T[2]+T[0]*c,T[5]+T[4]*r; x1,y1=x0+T[0],y0+T[4]
    polys.append(transform(fw,box(min(x0,x1),min(y0,y1),max(x0,x1),max(y0,y1))))
  u=unary_union(polys)
  return u.buffer(grow) if grow else u
def lp(m): return transform(fw,Point(*m))
def clean(g,simp=12):
  g=g.intersection(macro).buffer(0).simplify(simp)
  if g.geom_type=='GeometryCollection': g=unary_union([p for p in g.geoms if p.area>0])
  return g
def ha(g): return round(g.area/1e4,1)
# --- agua
main=A>=300; ramas=(A>=80)&~main
corr=unary_union([cells(main).buffer(100), cells(ramas).buffer(40)])
corr=clean(corr.buffer(20).buffer(-20),15)
plan=clean(cells(z<=216).buffer(10),10)
river=np.load(S+'/river.npy'); riv=cells(river)
edge=macro.exterior.intersection(transform(fw,box(-67.33,-39.1125,-67.30,-39.10)))
ripa=clean(macro.intersection(edge.buffer(90)).intersection(plan.buffer(40)),8)
chacra=clean(plan.difference(ripa).difference(corr),8)
# outlet / desembocadura
k=np.argmax(A*ins); r0,c0=divmod(k,W); out=lp(xy(r0,c0))
desem=clean(out.buffer(85),5)
# --- primera hectarea y crecimiento
h1c=lp((-67.3132,-39.1131))
h1=h1c.buffer(56.4)  # 1 ha
def anillo(ha_obj):
  r=math.sqrt(ha_obj*1e4/math.pi)
  for k in range(60):
    g=h1c.buffer(r).intersection(macro).difference(ripa).difference(corr).union(h1)
    if g.area>=ha_obj*1e4: break
    r*=1.05
  return clean(g,6)
f4=anillo(7); f7=anillo(33)
# --- clusters en terrazas a ~241 m
cand=np.load(S+'/cand.npy')
lab,n=ndimage.label(cand)
ter=[]
for i in range(1,n+1):
  m=lab==i
  if m.sum()*0.0739>2: ter.append(clean(cells(m).buffer(-10).buffer(10),8))
ter.sort(key=lambda g:g.centroid.x)
clusters=[]
for t in ter:
  c=t.centroid
  # two clusters per terrace, along terrace main axis
  mrr=t.minimum_rotated_rectangle; pts=list(mrr.exterior.coords)
  e=[(pts[i],pts[i+1]) for i in range(4)]; e.sort(key=lambda s:-math.dist(*s))
  (ax,ay),(bx,by)=e[0]; L=math.dist((ax,ay),(bx,by)); ux,uy=(bx-ax)/L,(by-ay)/L
  for s in (-1,1):
    p=Point(c.x+s*ux*L*0.22,c.y+s*uy*L*0.22)
    clusters.append(clean(p.buffer(100).intersection(t.buffer(40)),4))
z2=clean(unary_union([cl.buffer(60) for cl in clusters]).difference(unary_union(clusters)).difference(corr),8)
# nucleo comun: al oeste de h1, sobre la planicie alta, fuera del corredor
nuc=clean(lp((-67.3118,-39.1148)).buffer(110).difference(corr).difference(ripa).difference(h1).difference(unary_union(clusters).buffer(60)),5)
# --- bandas de zonas 3/4/5 por altura
north=lambda g: g
z3m=ins&(z>216)&(z<=262)
z4m=ins&(z>262)&(z<=292)
z5m=ins&(z>292)
ocup=unary_union([corr,plan,desem,f7,nuc,z2]+clusters)
z3=clean(cells(z3m).difference(ocup),15)
z4=clean(cells(z4m).difference(ocup),20)
z5=clean(cells(z5m).difference(ocup),20)
# --- lineas
def line(pts): return LineString([lp(p) for p in pts])
camino=line([(-67.2972,-39.1595),(-67.2983,-39.1400),(-67.2993,-39.1260),(-67.3000,-39.1210),(-67.3045,-39.1185),(-67.3098,-39.1172),(-67.3135,-39.1168),(-67.3160,-39.1175),(-67.3180,-39.1190)])
bajada=line([(-67.3135,-39.1168),(-67.3138,-39.1150),(-67.3140,-39.1137)])
# sample acc along road
for nm,g in (('camino',camino),('bajada',bajada)):
  bad=0
  for i in range(0,int(g.length),30):
    p=transform(bw,g.interpolate(i)); c=int((p.x-T[2])/T[0]); r=int((p.y-T[5])/T[4])
    if 0<=r<H and 0<=c<W and A[r,c]>=40: bad+=1
  print(nm,'m',round(g.length),'cruces de cauce (celdas)',bad)
rompe=[]
wind=(-math.sin(math.radians(225)),-math.cos(math.radians(225)))  # vector toward SW
perp=(math.cos(math.radians(135)),math.sin(math.radians(135)))  # NW-SE direction
for g in clusters+[h1]:
  c=g.centroid; off=130 if g is not h1 else 90
  cx,cy=c.x-0.7071*off,c.y-0.7071*off
  dx,dy=0.7071*170,-0.7071*170  # NW-SE line
  rompe.append(LineString([(cx-dx,cy-dy),(cx+dx,cy+dy)]))
# obras de agua sobre el cauce principal cada ~500 m
trace=cells(main)
obras=[]
mc=np.argwhere(main&ins); mc=sorted(mc,key=lambda rc:z[rc[0],rc[1]])
last=None
for r,c in mc:
  p=lp(xy(r,c))
  if all(p.distance(o)>550 for o in obras) and macro.contains(p): obras.append(p)
tanque=lp((-67.3112,-39.1160))
from shapely.geometry import MultiLineString, MultiPoint
def r6(o):
  if isinstance(o,float): return round(o,6)
  if isinstance(o,(list,tuple)): return [r6(x) for x in o]
  return o
F=[]
def add(g,id,capa,es,en,marca='[criterio]'):
  g=transform(bw,g)
  props=dict(id=id,capa=capa,nombre=es[0],zona=es[1],descripcion=es[2],nombre_en=en[0],zona_en=en[1],descripcion_en=en[2],marca=marca)
  if g.geom_type in('Polygon','MultiPolygon'): props['area_ha']=round(transform(fw,g).area/1e4,1)
  geo=mapping(g); geo={'type':geo['type'],'coordinates':r6(geo['coordinates'])}
  F.append(dict(type='Feature',properties=props,geometry=geo))
add(ripa,'pc-ribera','agua',
 ('Franja ribereña · bosque de ribera','Zona 5 · bien común','Retiro ancho sobre el río: restauración del bosque ribereño con nativas, sin construcción ni animales. Los sauces exóticos se reemplazan de a poco, porque hoy sostienen la orilla; el sauce criollo se conserva.'),
 ('Riverside strip · riparian forest','Zone 5 · commons','A wide setback along the river: restoring the riparian forest with native species, with no buildings and no livestock. Exotic willows are replaced gradually because they hold the bank today; the native willow stays.'))
add(chacra,'pc-planicie','produccion',
 ('Planicie inundable · chacra comunitaria','Zona 2–3 · sin vivienda','La mejor tierra y la napa más cerca: huerta y frutales comunitarios, vivero y semillero, invernaderos anclados. Nada residencial: debajo de la cota de inundación solo hay producción.'),
 ('Floodplain · community farm','Zone 2–3 · no housing','The best soil and the shallowest water table: community gardens and orchards, nursery and seed bank, anchored greenhouses. No housing: below the flood line there is only food production.'))
add(corr,'pc-corredor','agua',
 ('Columna verde del cañadón','Zona 4–5 · bien común','Unos 100 m a cada lado del cauce principal y 40 m en los ramales. Las crecidas se esparcen e infiltran con diques bajos de piedra, sin represar. Es el corredor de fauna y la sombra del valle: ningún lote lo corta. Su cuenca tiene unas 2.000 ha, el doble del macrolote.'),
 ('Green spine of the ravine','Zone 4–5 · commons','About 100 m on each side of the main wash and 40 m along its branches. Floods are spread and soaked in with low stone weirs, never dammed. It is the wildlife corridor and the shade of the valley: no plot cuts across it. Its catchment covers about 2,000 ha, twice the size of the macro-lot.'))
add(desem,'pc-desembocadura','agua',
 ('Desembocadura · humedal de infiltración','Zona 4 · bien común','Donde el cañadón se abre sobre la planicie: cuencos de infiltración y un humedal estacional que recargan la napa antes de que el agua llegue al río.'),
 ('Ravine mouth · infiltration wetland','Zone 4 · commons','Where the ravine opens onto the floodplain: infiltration basins and a seasonal wetland that recharge the water table before the water reaches the river.'))
add(h1,'pc-hectarea-1','implementacion',
 ('Primera hectárea · área foco','Año 1','La hectárea piloto, al pie de una subcuenca de unas 47 ha de la barda: un desvío en ladera concentra el escurrimiento sobre ella. Vivero, compost con la poda del valle, plantación en curvas de nivel, parcela testigo y línea de base de carbono. Es lo primero que ve quien visita.'),
 ('First hectare · focus area','Year 1','The pilot hectare, at the foot of a sub-catchment of about 47 ha on the escarpment: a hillside diversion concentrates runoff onto it. Nursery, compost from the valley’s orchard prunings, contour planting, a control plot and a carbon baseline. It is the first thing a visitor sees.'))
add(f4,'pc-crecimiento-4','implementacion',
 ('Crecimiento al año 4 · ~7 ha','Años 2–4','Fibonacci: 1 → 2 → 4 → 7 ha. Cada año se suma superficie con lo que funcionó el anterior: especies, mulch, obras de agua.'),
 ('Growth by year 4 · ~7 ha','Years 2–4','Fibonacci: 1 → 2 → 4 → 7 ha. Each year adds area using what worked the year before: species, mulch, water works.'))
add(f7,'pc-crecimiento-7','implementacion',
 ('Crecimiento al año 7 · ~33 ha','Años 5–7','12 → 20 → 33 ha: un oasis que se puede recorrer, con parcelas de 1 a 7 años de edad. Las ~600 t por año de materia orgánica del valle alcanzan hasta acá.'),
 ('Growth by year 7 · ~33 ha','Years 5–7','12 → 20 → 33 ha: an oasis you can walk through, with plots from 1 to 7 years old. The valley’s ~600 t of organic matter per year is enough up to this point.'))
add(nuc,'pc-nucleo','asentamiento',
 ('Núcleo común y puerta','Zona 1 · común','Centro de visitantes, banco de semillas, escuela de regeneración y residencias de voluntariado (en la reserva fiscal), mercado y acceso público a la costa. Está junto a la primera hectárea: el proyecto se muestra haciendo.'),
 ('Common core and gateway','Zone 1 · commons','Visitor centre, seed bank, regeneration school and volunteer housing (on the public reserve land), market and public access to the riverside. It sits next to the first hectare: the project shows itself by doing.'))
for i,g in enumerate(clusters,1):
  add(g,f'pc-cluster-{i}','asentamiento',
   (f'Cluster {i} · ~16 familias','Zona 0–1','Terraza a unos 241 m, casi plana, lejos de los cauces y siempre por encima de cualquier crecida. Casas agrupadas alrededor de un común (huerta, cisterna, taller), al reparo de su cortina rompevientos del SO. El cluster financia su propia regeneración y aporta al fondo común. No es un lote en venta.'),
   (f'Cluster {i} · ~16 families','Zone 0–1','A nearly flat terrace at about 241 m, away from the washes and always above any flood. Homes grouped around a commons (garden, cistern, workshop), sheltered by their windbreak against the south-west wind. The cluster funds its own regeneration and pays into the common fund. It is not a plot for sale.'))
add(z2,'pc-zona-2','produccion',
 ('Huertas y frutales de los clusters','Zona 2','Anillo productivo de uso diario alrededor de cada cluster: huertas, frutales, gallineros bajo los frutales, aguas grises tratadas en humedales y techos que llenan cisternas.'),
 ('Cluster gardens and orchards','Zone 2','A daily-use productive ring around each cluster: vegetable gardens, fruit trees, hens under the orchard, greywater treated in wetlands and roofs that fill cisterns.'))
add(z3,'pc-zona-3','produccion',
 ('Agroforestería en curvas de nivel','Zona 3','Sistemas agroforestales y olivar o viña en curvas de nivel, solo con agua asegurada: concesión del DPA y balance por parcela. Sin agua, esta franja queda como zona 4.'),
 ('Contour agroforestry','Zone 3','Agroforestry and olive groves or vineyards on contour, only with secured water: a provincial water concession and a water balance per plot. Without water, this band stays as zone 4.'))
add(z4,'pc-zona-4','silvestre',
 ('Monte manejado · cosecha de agua en ladera','Zona 4','Medias lunas, zanjas en curva de nivel y diques de una piedra en las cárcavas. A largo plazo, leña y madera nativa de algarrobo y chañar. Pastoreo solo como experimento con parcela testigo.'),
 ('Managed scrubland · hillside water harvesting','Zone 4','Half-moons, contour trenches and one-rock dams in the gullies. In the long run, firewood and native timber from carob and chañar trees. Grazing only as an experiment with a control plot.'))
add(z5,'pc-zona-5','silvestre',
 ('Meseta y cornisa · Monte silvestre','Zona 5','Rewilding: conservación del Monte, sin animales al principio y con obras mínimas para frenar cárcavas. Es la reserva que lleva la proporción ecológica al 50%.'),
 ('Plateau and rim · wild Monte','Zone 5','Rewilding: conserving the Monte scrubland, with no livestock at first and only minimal works to stop gullies. It is the reserve that brings the ecological share up to 50%.'))
add(camino,'pc-camino','camino',
 ('Acceso por la divisoria este','Caminos','Entra por la huella existente del borde este y baja por la loma, no por el cañadón: un solo cruce del cauce, con badén. Cada badén descarga en una cuenca de árboles: el camino es la primera obra de agua.'),
 ('Access along the eastern ridge','Roads','It comes in on the existing track along the eastern edge and runs down the ridge, not the ravine: a single crossing of the wash, with a ford. Every ford drains into a tree basin: the road is the first water work.'))
add(bajada,'pc-bajada','camino',
 ('Bajada al núcleo','Caminos','Une los clusters con el núcleo y la planicie por la ladera, con badenes que descargan en la primera hectárea.'),
 ('Path down to the core','Roads','Links the clusters with the core and the floodplain across the slope, with fords that drain into the first hectare.'))
add(MultiLineString(rompe),'pc-rompevientos','sector',
 ('Cortinas rompevientos','Sector viento SO','Líneas NO–SE, perpendiculares al viento dominante del SO, del lado de barlovento de cada cluster y de la primera hectárea. Arbustos nativos al frente y árboles atrás.'),
 ('Windbreaks','South-west wind sector','North-west to south-east lines, across the prevailing south-west wind, on the windward side of each cluster and of the first hectare. Native shrubs in front, trees behind.'))
add(MultiPoint(obras),'pc-esparcidores','obra',
 (f'Esparcidores de crecidas ({len(obras)})','Obras de agua','Diques bajos de piedra o gaviones cada ~550 m a lo largo del cañadón, que frenan y esparcen la crecida para que infiltre. Sin represar: en el desierto las represas se llenan de sedimento.'),
 (f'Flood spreaders ({len(obras)})','Water works','Low stone weirs or gabions every ~550 m along the ravine that slow and spread floods so they soak in. No dams: in the desert, dams fill up with sediment.'))
add(tanque,'pc-tanque','obra',
 ('Tanque alto en la barda','Obra de agua','Tanque arriba de la barda, llenado con agua con concesión: presión por gravedad para el núcleo y la primera hectárea, y reserva contra incendios.'),
 ('High tank on the escarpment','Water work','A tank up on the escarpment, filled with licensed water: gravity pressure for the core and the first hectare, and a fire reserve.'))
tot=macro.area/1e4
cons=unary_union([ripa,corr,desem,z5]).area/1e4
basin=np.load(S+'/basin.npy')
fc=dict(type='FeatureCollection',metadata=dict(
  version='0.1',fecha='2026-10-26',autor='Agente de Regeneración (NS_permacultura)',
  metodo='MDE Copernicus GLO-30 (30 m), acumulación de flujo D8, pendientes y cotas; polígono del Macrolote 7 (Biopueblo V11.kmz)',
  nota='Propuesta preliminar e ilustrativa de masterplan de permacultura. No reemplaza el relevamiento, la observación del sitio ni el diseño humano.',
  total_ha=round(tot,1),conservacion_ha=round(cons,1),cuenca_canadon_ha=round(float(basin.sum())*abs(T[0])*111320*math.cos(math.radians(39.13))*abs(T[4])*110950/1e4)),features=F)
json.dump(fc,open(OUT,'w'),ensure_ascii=False,separators=(',',':'))
print('total',round(tot,1),'conservacion',round(cons,1),round(cons/tot*100,1),'%','features',len(F))
