import json,re
D=json.load(open('research/course-data.json'))
src=open('/workspace/faport/js/mapstr.js').read()
def cl(s): s=re.sub(r'\s*[—–]\s*',', ',str(s)).replace('→','to');return s
CR="Footage still: Artgrid, licensed"
P={
'ci1':('CI Principiante','Roma','pages/courses/ci1.html','#C8A96B',[('colosseo','Roma, Colosseo',41.8902,12.4922,'Colosseo and the Roman Forum','city-roma.jpg'),('trevi','Roma, Fontana di Trevi',41.9009,12.4833,'Fontana di Trevi, rione Trevi','ag-roma-statue-poster.jpg'),('navona','Roma, Piazza Navona',41.8992,12.4731,'Piazza Navona, rione Parione','roma-piazza-poster.jpg'),('trastevere','Roma, Trastevere',41.8897,12.4700,'The lanes of Trastevere','life-caffe-roma.jpg'),('sanpietro','Roma, San Pietro',41.9022,12.4539,"Basilica di San Pietro and Prati",'ag-rome-basilica-poster.jpg')]),
'ci2':('CI Elementare','Firenze','pages/courses/ci2.html','#E8A87C',[('duomo-fi','Firenze, Duomo',43.7731,11.2560,'Cattedrale di Santa Maria del Fiore','city-firenze.jpg'),('pontevecchio','Firenze, Ponte Vecchio',43.7680,11.2531,'Ponte Vecchio on the Arno','firenze-arno-poster.jpg'),('mercato-fi','Firenze, Mercato Centrale',43.7764,11.2532,'Mercato Centrale, San Lorenzo','ag-market-produce-poster.jpg'),('sangimignano','San Gimignano',43.4677,11.0432,'The towers of San Gimignano','ag-san-gimignano-poster.jpg')]),
'ci3':('CI Intermedio','Bologna','pages/courses/ci3.html','#D4A574',[('maggiore','Bologna, Piazza Maggiore',44.4938,11.3430,'Piazza Maggiore and San Petronio','city-bologna.jpg'),('quadrilatero','Bologna, Quadrilatero',44.4930,11.3455,'The market lanes of the Quadrilatero','life-market-bologna.jpg'),('portici','Bologna, i portici',44.4943,11.3466,'The porticoes near the Due Torri','bologna-portici-poster.jpg')]),
'ci4':('CI Avanzato','Napoli e Palermo','pages/courses/ci4.html','#9DB08A',[('spaccanapoli','Napoli, Spaccanapoli',40.8490,14.2560,'Spaccanapoli, centro storico','city-napoli.jpg'),('lungomare','Napoli, Lungomare',40.8320,14.2440,'The seafront at Via Caracciolo','napoli-mare-poster.jpg'),('amalfi','Costiera Amalfitana',40.6340,14.6027,'The Amalfi coast','life-amalfi-coast.jpg'),('palermo','Palermo, centro storico',38.1157,13.3615,'Quattro Canti and the old markets','city-palermo.jpg')]),
'ps3':('In Viaggio','Venezia','pages/spoken/ps3.html','#B5607A',[('rialto','Venezia, Rialto',45.4380,12.3359,'Ponte di Rialto and the market','city-venezia.jpg'),('sanmarco','Venezia, San Marco',45.4341,12.3388,'Piazza San Marco','ag-venice-gondola-poster.jpg'),('cannaregio','Venezia, Cannaregio',45.4445,12.3290,'Canals of Cannaregio','life-gondola-venezia.jpg')]),
'ps4':('Chiacchierando','Milano','pages/spoken/ps4.html','#8B7BB5',[('duomo-mi','Milano, Duomo',45.4642,9.1900,'Duomo di Milano','city-milano.jpg'),('scala','Milano, Teatro alla Scala',45.4674,9.1895,'Teatro alla Scala','opera-scala-poster.jpg')]),
}
courses=[]
for k,(n,reg,href,col,pins) in P.items():
    syl=D[k]['syllabus'];per=max(1,len(syl)//len(pins));ps=[]
    for i,(pid,city,la,ln,loc,img) in enumerate(pins):
        chunk=syl[i*per:(i+1)*per] if i<len(pins)-1 else syl[i*per:]
        ps.append({'id':pid,'city':city,'lat':la,'lng':ln,'location':loc,'image':'assets/img/'+img,'credit':CR if 'poster' in img else '','photoSrc':'',
          'units':[{'num':syl.index(u)+1,'fr':cl(u[0]),'en':cl(u[1])} for u in chunk]})
    courses.append({'id':k,'name':n,'level':cl(D[k]['cefr']),'shortLevel':cl(D[k]['cefr']).split(' ')[0],'region':reg,'href':href,'color':col,'routeColor':col,
      'description':cl(D[k]['promise']).split('. ')[0]+'.','pins':ps,'routeOrder':[p['id'] for p in ps]})
data={'tagline':'Italian is learned where it is lived: at the bar, at the market, on the piazza, on the quay.','courses':courses}
a=src.index('var DATA = {');b=src.index('/* ---------- CONFIG')
s=src[:a]+'var DATA = '+json.dumps(data,ensure_ascii=False)+';\n  '+src[b:]
g=json.load(open('assets/geo/italy.geojson'));geo=g['features'][0] if g['type']=='FeatureCollection' else g
a=s.index('var FRANCE_GEO = ');b=s.index('\n',a)
s=s[:a]+'var FRANCE_GEO = '+json.dumps(geo)+';'+s[b:]
for x,y in [('[2.6, 46.6]','[12.6, 42.0]'),('FRANCE_ZOOM = 5.1','FRANCE_ZOOM = 5.0'),('duration: 750','duration: 2400'),('userInitiated ? 1200 : 0','userInitiated ? 2600 : 0'),
 ("'Every region of France'","'Every city of Italy'"),('Every place The French Atelier teaches across all seven courses.','Every place Club Italia teaches, across six courses.'),
 ('Interactive Map of France','Interactive map of Italy'),('across France</h2>','across Italy</h2>'),('the map of France loads','the map of Italy loads'),('#6FC4FF','#E8C77A'),('#2FA4FF','#C8A96B'),('47,164,255','200,169,107'),('47, 164, 255','200, 169, 107')]:
    s=s.replace(x,y)
s=re.sub(r'(?<=[\'"])([^\'"\n]*?)France([^\'"\n]*?)(?=[\'"])',lambda m:m.group(0).replace('France','Italy'),s)
s=s.replace('French','Italian').replace('&middot;',' · ')
s=s.replace('all 7 courses','all 6 courses').replace('7 courses','6 courses').replace(' — ',', ').replace('—',',').replace('Acadomia','eTeacher').replace('The Italian Atelier','Club Italia')
s=s.replace("'background-color': '#00001F', 'background-opacity': 0.42","'background-color': '#06112A', 'background-opacity': 0.25").replace("'fill-color': '#C8A96B', 'fill-opacity': 0.16","'fill-color': '#409CFF', 'fill-opacity': 0.22").replace("'line-width': 9, 'line-blur': 8, 'line-opacity': 0.55","'line-width': 8, 'line-blur': 7, 'line-opacity': 0.55").replace("'line-color': '#BFE4FF', 'line-width': 2,","'line-color': '#FFF1C9', 'line-width': 2.2,")
open('fa/js/mapstr.js','w').write(s)
print(len(courses),sum(len(c['pins']) for c in courses))
