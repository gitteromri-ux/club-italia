import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
/* ===== HERO: WebGL video shader ===== */
(function(){const cv=document.getElementById('glhero'),vid=document.getElementById('herovid');if(!cv||!vid||RM)return;
const gl=cv.getContext('webgl',{premultipliedAlpha:false,antialias:false});if(!gl)return;
const vs=`attribute vec2 p;varying vec2 v;void main(){v=p*.5+.5;gl_Position=vec4(p,0,1);}`;
const fs=`precision highp float;varying vec2 v;uniform sampler2D t;uniform vec2 r,vr,m;uniform float time,str,sc;
float h(vec2 p){return fract(sin(dot(p,vec2(12.9898,78.233)))*43758.5453);}
float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
void main(){vec2 uv=v;float ra=r.x/r.y,va=vr.x/vr.y;vec2 s=ra>va?vec2(1.,va/ra):vec2(ra/va,1.);vec2 c=(uv-.5)*s/(1.+sc*.08)+.5;
vec2 d=uv-m;d.x*=ra;float dist=length(d);float rip=sin(dist*38.-time*3.2)*exp(-dist*5.)*.012*str;
vec2 off=normalize(d+1e-4)*rip+vec2(n(uv*3.+time*.08)-.5,n(uv*3.+7.+time*.08)-.5)*.006;
vec2 q=vec2(c.x,1.-c.y)+off;float ca=.0025*str+.0006;
vec3 col=vec3(texture2D(t,q+vec2(ca,0)).r,texture2D(t,q).g,texture2D(t,q-vec2(ca,0)).b);
col=pow(col,vec3(.95));col*=vec3(1.04,1.01,.96);col=mix(vec3(dot(col,vec3(.299,.587,.114))),col,1.18);
col+=(h(uv*r+time)-.5)*.035;gl_FragColor=vec4(col,1.);}`;
const sh=(t,s)=>{const o=gl.createShader(t);gl.shaderSource(o,s);gl.compileShader(o);return o};const pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,vs));gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,fs));gl.linkProgram(pr);gl.useProgram(pr);
const b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);const loc=gl.getAttribLocation(pr,'p');gl.enableVertexAttribArray(loc);gl.vertexAttribPointer(loc,2,gl.FLOAT,false,0,0);
const tx=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,tx);[gl.TEXTURE_WRAP_S,gl.TEXTURE_WRAP_T].forEach(k=>gl.texParameteri(gl.TEXTURE_2D,k,gl.CLAMP_TO_EDGE));gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);
const U=k=>gl.getUniformLocation(pr,k);let mx=.5,my=.5,tm=.5,tmy=.5,str=0,ts=0;
addEventListener('pointermove',e=>{tm=e.clientX/innerWidth;tmy=1-e.clientY/innerHeight;ts=1});
const rs=()=>{const d=Math.min(devicePixelRatio,1.5);cv.width=cv.clientWidth*d;cv.height=cv.clientHeight*d;gl.viewport(0,0,cv.width,cv.height)};addEventListener('resize',rs);rs();
let ready=false;const t0=performance.now();
(function loop(){requestAnimationFrame(loop);if(vid.readyState>=2){gl.texImage2D(gl.TEXTURE_2D,0,gl.RGB,gl.RGB,gl.UNSIGNED_BYTE,vid);if(!ready){ready=true;cv.style.opacity=1}}if(!ready)return;
mx+=(tm-mx)*.06;my+=(tmy-my)*.06;str+=(ts-str)*.04;ts*=.985;const sc=Math.min(1,scrollY/innerHeight);
gl.uniform2f(U('r'),cv.width,cv.height);gl.uniform2f(U('vr'),vid.videoWidth||1920,vid.videoHeight||1080);gl.uniform2f(U('m'),mx,my);gl.uniform1f(U('time'),(performance.now()-t0)/1000);gl.uniform1f(U('str'),str);gl.uniform1f(U('sc'),sc);gl.drawArrays(gl.TRIANGLE_STRIP,0,4)})();
vid.play().catch(()=>{});})();

/* ===== CEFR: lit marble colonnade ===== */
(function(){const cv=document.getElementById('gl3d');if(!cv)return;const sec=cv.closest('.cefr');
const r=new THREE.WebGLRenderer({canvas:cv,antialias:true,alpha:true});r.setPixelRatio(Math.min(devicePixelRatio,1.6));r.shadowMap.enabled=true;r.shadowMap.type=THREE.PCFSoftShadowMap;r.toneMapping=THREE.ACESFilmicToneMapping;r.toneMappingExposure=1.15;r.outputColorSpace=THREE.SRGBColorSpace;
const sc=new THREE.Scene();sc.background=new THREE.Color(0x14495a);sc.fog=new THREE.Fog(0x14495a,16,46);
const cam=new THREE.PerspectiveCamera(36,1,.1,100);
sc.add(new THREE.HemisphereLight(0xfff1dc,0x0d3b45,.9));
const key=new THREE.DirectionalLight(0xffd59a,3.2);key.position.set(-6,12,8);key.castShadow=true;key.shadow.mapSize.set(2048,2048);Object.assign(key.shadow.camera,{left:-20,right:20,top:14,bottom:-6});sc.add(key);
const rim=new THREE.DirectionalLight(0x6fd3d6,1.6);rim.position.set(8,5,-8);sc.add(rim);
const fl=new THREE.Mesh(new THREE.PlaneGeometry(400,400),new THREE.MeshStandardMaterial({color:0x1d5a63,roughness:.9,metalness:0}));fl.rotation.x=-Math.PI/2;fl.receiveShadow=true;sc.add(fl);
// travertine texture via canvas noise
const tc=document.createElement('canvas');tc.width=tc.height=256;const x=tc.getContext('2d');x.fillStyle='#efe4d1';x.fillRect(0,0,256,256);for(let i=0;i<2600;i++){x.fillStyle=`rgba(${150+Math.random()*60|0},${120+Math.random()*50|0},${90+Math.random()*40|0},${Math.random()*.12})`;x.fillRect(Math.random()*256,Math.random()*256,1+Math.random()*10,1)}
const tex=new THREE.CanvasTexture(tc);tex.wrapS=tex.wrapT=THREE.RepeatWrapping;tex.repeat.set(2,4);tex.colorSpace=THREE.SRGBColorSpace;
const mat=new THREE.MeshStandardMaterial({map:tex,roughness:.5,metalness:0,color:0xffffff});
const gold=new THREE.MeshStandardMaterial({color:0xe3b25a,roughness:.28,metalness:.85});
function column(h){const g=new THREE.Group();const geo=new THREE.CylinderGeometry(.52,.6,h,96,24,false);const p=geo.attributes.position;for(let i=0;i<p.count;i++){const vx=p.getX(i),vz=p.getZ(i),a=Math.atan2(vz,vx),rr=Math.hypot(vx,vz);const f=1-.045*Math.pow(Math.abs(Math.cos(a*12)),.6);p.setX(i,Math.cos(a)*rr*f);p.setZ(i,Math.sin(a)*rr*f)}geo.computeVertexNormals();
const sh=new THREE.Mesh(geo,mat);sh.position.y=h/2+.5;sh.castShadow=sh.receiveShadow=true;g.add(sh);
const base=new THREE.Mesh(new THREE.BoxGeometry(1.7,.5,1.7),mat);base.position.y=.25;base.castShadow=base.receiveShadow=true;g.add(base);
const tor=new THREE.Mesh(new THREE.TorusGeometry(.62,.1,16,64),mat);tor.rotation.x=Math.PI/2;tor.position.y=.6;g.add(tor);
const ech=new THREE.Mesh(new THREE.CylinderGeometry(.85,.55,.35,64),mat);ech.position.y=h+.68;ech.castShadow=true;g.add(ech);
const ab=new THREE.Mesh(new THREE.BoxGeometry(1.9,.32,1.9),mat);ab.position.y=h+1.01;ab.castShadow=true;g.add(ab);
const band=new THREE.Mesh(new THREE.TorusGeometry(.56,.035,12,64),gold);band.rotation.x=Math.PI/2;band.position.y=h+.45;g.add(band);return g}
const cols=[];const H=[2.2,3,3.8,4.6,5.4,6.2];H.forEach((h,i)=>{const c=column(h);c.position.set(i*3.4,0,0);c.scale.y=.001;sc.add(c);cols.push(c)});
const rs=()=>{const w=cv.clientWidth,h=cv.clientHeight;r.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix()};addEventListener('resize',rs);rs();
const D=JSON.parse(document.getElementById('laddata').textContent);let last=-1;const T=k=>document.getElementById(k);
let prog=0,sp=0,vis=false;new IntersectionObserver(e=>vis=e[0].isIntersecting).observe(sec);
addEventListener('scroll',()=>{const b=sec.getBoundingClientRect();prog=Math.min(1,Math.max(0,-b.top/(b.height-innerHeight)))},{passive:true});
let mx=0;addEventListener('pointermove',e=>mx=e.clientX/innerWidth-.5);
(function loop(){requestAnimationFrame(loop);if(!vis)return;sp+=((RM?1:prog)-sp)*.08;const f=sp*6;
cols.forEach((c,i)=>{const t=Math.min(1,Math.max(0,f-i));const e=1-Math.pow(1-t,3);c.scale.y=Math.max(.001,e);c.visible=e>.02});
const i=Math.min(5,Math.floor(f));if(i!==last){last=i;const d=D[i];T('lvk').textContent=d.k;T('lvh').innerHTML=d.h;T('lvu').innerHTML=d.u.map(x=>`<li>${x}</li>`).join('');T('lvr').textContent=d.r}
const tx=Math.min(5,f)*3.4;const narrow=innerWidth<900;cam.position.set(tx-(narrow?0:7.2)+mx*1.5,4.8+sp*1.6,narrow?21:17);cam.lookAt(tx-(narrow?0:6.4),3.3+sp*1.2,0);r.render(sc,cam)})();})();
