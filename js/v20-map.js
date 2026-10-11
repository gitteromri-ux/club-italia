(()=>{const el=document.getElementById('map');if(!el||!window.maplibregl)return;const C=JSON.parse(document.getElementById('citydata').textContent);const P=el.dataset.base||'';
const style={version:8,glyphs:'https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf',
sources:{omt:{type:'vector',url:'https://tiles.openfreemap.org/planet'},dem2:{type:'raster-dem',tiles:['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'],encoding:'terrarium',tileSize:256,maxzoom:12},dem:{type:'raster-dem',tiles:['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'],encoding:'terrarium',tileSize:256,maxzoom:12,attribution:'Terrain: Mapzen / AWS Open Data'},it:{type:'geojson',data:P+'assets/geo/italy.geojson'}},
layers:[{id:'bg',type:'background',paint:{'background-color':'#e7d6b0'}},
{id:'lc',type:'fill',source:'omt','source-layer':'landcover',paint:{'fill-color':['match',['get','class'],'wood','#9fb57f','grass','#c8cf94','farmland','#dccf9c','ice','#ffffff','#cdbf8e'],'fill-opacity':.7}},
{id:'hs',type:'hillshade',source:'dem2',paint:{'hillshade-exaggeration':.6,'hillshade-highlight-color':'#fff8e6','hillshade-shadow-color':'#5a4630','hillshade-accent-color':'#8a6a3a','hillshade-illumination-direction':315}},
{id:'water',type:'fill',source:'omt','source-layer':'water',paint:{'fill-color':['interpolate',['linear'],['zoom'],4,'#1f8fa0',10,'#2aa3b0']}},
{id:'wl',type:'line',source:'omt','source-layer':'waterway',paint:{'line-color':'#2aa3b0','line-width':1}},
{id:'itf',type:'fill',source:'it',paint:{'fill-color':'#d8b878','fill-opacity':.14}},
{id:'itg',type:'line',source:'it',paint:{'line-color':'#7a1f30','line-width':10,'line-blur':10,'line-opacity':.45}},
{id:'itl',type:'line',source:'it',paint:{'line-color':'#5a1626','line-width':1.8}},
{id:'bd',type:'line',source:'omt','source-layer':'boundary',filter:['==',['get','admin_level'],2],paint:{'line-color':'rgba(90,60,40,.35)','line-width':.8}},
{id:'rd',type:'line',source:'omt','source-layer':'transportation',minzoom:8,filter:['in',['get','class'],['literal',['motorway','trunk','primary']]],paint:{'line-color':'rgba(255,255,255,.75)','line-width':1}},
{id:'pl',type:'symbol',source:'omt','source-layer':'place',filter:['in',['get','class'],['literal',['city','town']]],minzoom:6.5,layout:{'text-field':['get','name'],'text-font':['Noto Sans Regular'],'text-size':12},paint:{'text-color':'#3d2e22','text-halo-color':'#fff6e0','text-halo-width':1.2}}]};
const map=new maplibregl.Map({container:el,style,center:[12.6,41.9],zoom:5.1,pitch:48,bearing:-12,maxPitch:75,attributionControl:{compact:true},cooperativeGestures:true,dragRotate:false,pitchWithRotate:false,canvasContextAttributes:{preserveDrawingBuffer:false}});
map.addControl(new maplibregl.NavigationControl({visualizePitch:true}),'bottom-right');
map.on('load',()=>{try{map.setTerrain({source:'dem',exaggeration:1.7})}catch(e){}try{map.setSky({'sky-color':'#8cc8d8','horizon-color':'#fbe3b8','fog-color':'#fbe3b8','sky-horizon-blend':.6,'horizon-fog-blend':.7,'fog-ground-blend':.4})}catch(e){}});
const mks={};C.forEach(c=>{const d=document.createElement('div');d.innerHTML='<div class="mk"></div><div class="mkl">'+c.n+'</div>';d.style.cursor='pointer';d.setAttribute('role','button');d.setAttribute('tabindex','0');d.setAttribute('aria-label',c.n);d.onclick=()=>go(c.k,true);d.onkeydown=e=>{if(e.key=='Enter')go(c.k,true)};mks[c.k]=new maplibregl.Marker({element:d,anchor:'top'}).setLngLat(c.ll).addTo(map)});
const card=document.getElementById('mcard'),btns=[...document.querySelectorAll('.jlist button')];let timer,idx=-1;
function go(k,user){btns.forEach(b=>b.setAttribute('aria-pressed',b.dataset.k==k));Object.entries(mks).forEach(([kk,m])=>m.getElement().querySelector('.mk').classList.toggle('on',kk==k));
if(k=='all'){card.classList.remove('on');map.flyTo({center:[12.6,41.9],zoom:5.1,pitch:48,bearing:-12,duration:5500,essential:true});idx=-1;return}
const c=C.find(x=>x.k==k);idx=C.indexOf(c);map.flyTo({center:c.ll,zoom:c.z||10.2,pitch:66,bearing:c.b||-20,duration:6500,curve:1.25,easing:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2,essential:true});
card.classList.remove('on');setTimeout(()=>{const v=card.querySelector('video');v.poster=c.p;v.src=c.v;v.play().catch(()=>{});card.querySelector('h3').textContent=c.n;card.querySelector('.t img').src=c.ti;card.querySelector('.t img').alt=c.t;card.querySelector('#mt').textContent=c.t;card.querySelector('#mc').textContent=c.c;
card.querySelector('ol').innerHTML=c.u.map(u=>`<li><b>${String(u[0]).padStart(2,'0')}</b><span>${u[1]}</span></li>`).join('');card.querySelector('a').href=c.h;card.classList.add('on')},900);if(user)clearInterval(timer)}
btns.forEach(b=>b.onclick=()=>go(b.dataset.k,true));

window.__map=map;})();
