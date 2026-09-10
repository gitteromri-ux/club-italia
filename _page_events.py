"""Bulk event page generator: 3 cultural event pages, one template, one CSS."""
import os
from _build_new_pages import shell

EVENT_STYLE = '''<style>
/* -------- EVENT PAGE — page-scoped -------- */
.ev-hero{position:relative;min-height:100vh;display:flex;align-items:flex-end;color:var(--on-dark);overflow:hidden;background:var(--navy-deep)}
.ev-hero-bg{position:absolute;inset:0;z-index:0}
.ev-hero-bg img{width:100%;height:100%;object-fit:cover}
.ev-hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(34,8,11,.25) 0%,rgba(34,8,11,.72) 55%,rgba(34,8,11,.94) 100%)}
.ev-hero .wrap{position:relative;z-index:2;padding:10rem 0 5rem}
.ev-hero .kicker{font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:1.8rem}
.ev-hero .kicker span{color:var(--on-dark-soft);margin-left:.6rem}
.ev-hero h1{font-family:var(--serif);font-weight:500;font-size:clamp(3rem,7vw,6.4rem);line-height:.98;letter-spacing:-.02em;max-width:16ch;margin:0 0 1.6rem;color:var(--on-dark)}
.ev-hero .lede{max-width:56ch;color:var(--on-dark-soft);font-weight:300;font-size:clamp(1.15rem,1.5vw,1.4rem);line-height:1.62}
.ev-hero .meta{display:flex;gap:2.4rem;flex-wrap:wrap;margin-top:2.8rem;padding-top:2rem;border-top:1px solid var(--gold-line-soft)}
.ev-hero .meta > div small{display:block;font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--on-dark-soft);margin-bottom:.4rem}
.ev-hero .meta > div strong{font-family:var(--serif);font-size:1.4rem;font-weight:500;color:var(--gold-soft)}

.ev-tri{height:6px;background:linear-gradient(90deg,#009246 0 33.33%,#F6F1E6 33.33% 66.66%,#CE2B37 66.66%)}

.ev-band{padding:6rem 0;position:relative}
.ev-band.dark{background:var(--navy);color:var(--on-dark)}
.ev-band.dark h2,.ev-band.dark h3{color:var(--on-dark)}
.ev-band.dark p{color:var(--on-dark-soft)}
.ev-band.cream{background:var(--ivory)}
.ev-band.paper{background:var(--paper)}
.ev-band h2{font-family:var(--serif);font-size:clamp(2.2rem,4.2vw,3.6rem);line-height:1.04;margin-bottom:1.2rem;max-width:22ch}
.ev-band .lede-p{font-size:1.15rem;line-height:1.7;max-width:60ch;color:var(--on-light-soft)}
.ev-band.dark .lede-p{color:var(--on-dark-soft)}

.ev-mag{display:grid;grid-template-columns:1fr 1.15fr;gap:3.6rem;align-items:start}
@media (max-width:900px){.ev-mag{grid-template-columns:1fr;gap:2rem}}
.ev-mag .body p{font-size:1.02rem;line-height:1.72;margin-bottom:1.2rem;color:var(--on-light-soft)}
.ev-band.dark .ev-mag .body p{color:var(--on-dark-soft)}
.ev-mag .body p em{color:var(--gold-deep);font-style:italic}
.ev-band.dark .ev-mag .body p em{color:var(--gold-soft)}
.ev-mag .drop{font-family:var(--serif);font-style:italic;font-size:9rem;color:var(--gold-soft);opacity:.35;line-height:.9;margin-bottom:-3rem;display:block}

.ev-pull{background:var(--paper);padding:6rem 0;text-align:center;position:relative}
.ev-pull.dark{background:var(--navy-deep);color:var(--on-dark)}
.ev-pull .quote{font-family:var(--serif);font-style:italic;font-size:clamp(1.8rem,3.4vw,2.8rem);line-height:1.24;max-width:32ch;margin:0 auto;color:var(--navy)}
.ev-pull.dark .quote{color:var(--on-dark)}
.ev-pull .sig{margin-top:1.6rem;font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-deep)}
.ev-pull.dark .sig{color:var(--gold-soft)}

.ev-tradition-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem;margin-top:3rem}
@media (max-width:820px){.ev-tradition-grid{grid-template-columns:1fr}}
.ev-tradition-card{background:var(--paper);border:1px solid var(--gold-line-soft);padding:2.2rem 1.8rem}
.ev-band.dark .ev-tradition-card{background:var(--navy-mid);border-color:var(--dark-line-soft)}
.ev-tradition-card .rn{font-family:var(--serif);font-style:italic;font-size:2rem;color:var(--gold-deep);margin-bottom:.6rem}
.ev-band.dark .ev-tradition-card .rn{color:var(--gold-soft)}
.ev-tradition-card h4{font-family:var(--serif);font-size:1.5rem;margin-bottom:.6rem;line-height:1.15}
.ev-tradition-card p{font-size:.95rem;color:var(--on-light-soft);line-height:1.6}
.ev-band.dark .ev-tradition-card p{color:var(--on-dark-soft)}

.ev-timeline{margin-top:2rem}
.ev-tl-row{display:grid;grid-template-columns:110px 1fr;gap:2rem;padding:1.6rem 0;border-bottom:1px solid var(--gold-line-soft)}
.ev-tl-row .yr{font-family:var(--serif);font-style:italic;font-size:1.8rem;color:var(--gold-deep)}
.ev-band.dark .ev-tl-row .yr{color:var(--gold-soft)}
.ev-tl-row h4{font-family:var(--serif);font-size:1.35rem;margin-bottom:.4rem;line-height:1.18}
.ev-tl-row p{font-size:.98rem;color:var(--on-light-soft);line-height:1.62}
.ev-band.dark .ev-tl-row p{color:var(--on-dark-soft)}

.ev-live{background:var(--navy-deep);color:var(--on-dark);padding:6rem 0;position:relative;overflow:hidden}
.ev-live::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 30%,rgba(201,162,75,.16),transparent 55%);pointer-events:none}
.ev-live .grid{display:grid;grid-template-columns:1.15fr 1fr;gap:3rem;align-items:center;position:relative;z-index:1}
@media (max-width:900px){.ev-live .grid{grid-template-columns:1fr}}
.ev-live .video-frame{aspect-ratio:16/9;background:var(--navy);border:1px solid var(--gold-line);position:relative;overflow:hidden}
.ev-live .video-frame img{width:100%;height:100%;object-fit:cover;opacity:.65}
.ev-live .video-frame .play{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:88px;height:88px;border-radius:50%;background:var(--gold-deep);color:var(--navy);display:flex;align-items:center;justify-content:center;font-size:1.6rem;padding-left:6px}
.ev-live .video-frame .live-badge{position:absolute;top:1rem;left:1rem;padding:.4rem .8rem;background:rgba(224,65,63,.9);color:#fff;font-size:.65rem;letter-spacing:.22em;text-transform:uppercase;display:flex;align-items:center;gap:.5rem}
.ev-live .video-frame .live-badge::before{content:"";width:8px;height:8px;background:#fff;border-radius:50%;animation:pulse 2s infinite}
.ev-live h2{color:var(--on-dark)}
.ev-live p{color:var(--on-dark-soft);line-height:1.65;font-size:1.05rem;margin-top:1rem}

.ev-recipe{background:var(--ivory);padding:6rem 0}
.ev-recipe .grid{display:grid;grid-template-columns:1.2fr 1fr;gap:3rem}
@media (max-width:820px){.ev-recipe .grid{grid-template-columns:1fr}}
.ev-recipe h3{font-family:var(--serif);font-size:1.8rem;margin-bottom:1rem}
.ev-recipe ul{list-style:none;padding:0;margin:1rem 0}
.ev-recipe li{padding:.6rem 0;border-bottom:1px dotted var(--gold-line-soft);color:var(--on-light-soft);font-size:.98rem;display:flex;justify-content:space-between}
.ev-recipe li span{font-family:var(--serif);color:var(--navy);font-style:italic}
.ev-recipe .steps p{margin-bottom:1rem;color:var(--on-light-soft);line-height:1.7}
.ev-recipe .steps p::first-letter{font-family:var(--serif);font-size:1.6rem;color:var(--gold-deep);font-style:italic;margin-right:.2rem}

.ev-vocab{padding:6rem 0;background:var(--paper)}
.ev-vocab .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem}
@media (max-width:820px){.ev-vocab .grid{grid-template-columns:1fr}}
.ev-vocab .row{display:grid;grid-template-columns:220px 1fr;gap:1.4rem;padding:1rem 1.2rem;background:var(--white);border:1px solid var(--gold-line-soft)}
.ev-vocab .row .it{font-family:var(--serif);font-style:italic;font-size:1.25rem;color:var(--navy)}
.ev-vocab .row .en{font-size:.95rem;color:var(--on-light-soft);align-self:center}

.ev-cta{background:linear-gradient(140deg,var(--navy) 0%,var(--navy-soft) 60%,var(--terra-deep) 130%);color:var(--on-dark);padding:6rem 0;text-align:center}
.ev-cta h2{color:var(--on-dark);font-family:var(--serif);font-size:clamp(2.2rem,4vw,3.6rem)}
.ev-cta p{color:var(--on-dark-soft);max-width:56ch;margin:1rem auto 2rem;font-size:1.1rem;line-height:1.6}
</style>'''


EVENTS = [
{
  "slug":"festa-repubblica",
  "title":"Festa della Repubblica — Italy's National Day · Club Italia",
  "meta":"June 2, Italy's national holiday. The story of the 1946 referendum, the Frecce Tricolori over the Altare della Patria, and how to celebrate the birth of the Italian Republic — a cultural essay from Club Italia.",
  "img":"assets/img/pillar-tradition.jpg",
  "eyebrow":"Cultural event · Ricorrenza nazionale",
  "date":"2 giugno · every year",
  "since":"Since 1946",
  "place":"Roma, Via dei Fori Imperiali",
  "watch":"Live from Rome",
  "h1":"Festa della",
  "h1gold":"Repubblica.",
  "lede":"On the second of June nineteen forty-six, the Italian people voted, by referendum, to abolish the monarchy and become a republic. Every year since, Rome has closed the Via dei Fori Imperiali, the Frecce Tricolori have painted green, white and red across the sky above the Altare della Patria, and the whole peninsula has stopped for a single day of civic memory. This is what Italian democracy looks like when it dresses up.",
  "vocab":[
    ("la Repubblica","the Republic"),
    ("il referendum","the referendum"),
    ("la Costituzione","the Constitution"),
    ("la sfilata militare","the military parade"),
    ("il tricolore","the tricolour flag"),
    ("le Frecce Tricolori","the aerobatic team"),
    ("l'inno nazionale","the national anthem"),
    ("Fratelli d'Italia","Brothers of Italy (anthem)"),
    ("il Presidente della Repubblica","the President"),
    ("l'Altare della Patria","the Altar of the Fatherland"),
    ("il Quirinale","the presidential palace"),
    ("la deposizione della corona","the wreath-laying")
  ],
  "history":[
    ("1946","<h4>The referendum that made Italy a republic.</h4><p>After twenty years of fascism and a devastating world war, the Italian people were asked a single institutional question: monarchy or republic. Twelve and a half million citizens voted <em>Repubblica</em>; ten and a half million voted <em>Monarchia</em>. Women voted in a national ballot for the first time in Italian history. On 12 June the results were certified. The House of Savoy went into exile. Italy, at last, belonged to Italians.</p>"),
    ("1948","<h4>The Constitution enters into force.</h4><p>The Constituent Assembly, chaired by Meuccio Ruini and drafted by figures from every democratic party, produced a text that came into force on 1 January 1948. Article 1: <em>l'Italia è una Repubblica democratica, fondata sul lavoro</em>. Every Club Italia intermediate learner studies this sentence in the original.</p>"),
    ("1949","<h4>The first modern parade on Via dei Fori Imperiali.</h4><p>The Ministry of Defence proposed a civic-military review along the Roman forums to mark the anniversary. It has run, with only a handful of interruptions, ever since.</p>"),
    ("1961","<h4>The Frecce Tricolori are formed.</h4><p>Italy's national aerobatic team, based at Rivolto, becomes a permanent feature of the Rome parade — the smoke trails timed to the anthem.</p>"),
    ("1977","<h4>The date is briefly moved and returned.</h4><p>For fifteen years the celebration was quietly folded into a Sunday to save the working day. It was restored to a fixed 2 June in 2001, at the request of President Ciampi.</p>"),
    ("Today","<h4>A day of hospitality at the Quirinale.</h4><p>The President opens the gardens of the Quirinale palace to the public. Bands play. Children run under the pines. The gardens close at sunset with a lowering of the flag.</p>")
  ],
  "traditions":[
    ("I","<h4>The parade at the Fori.</h4><p>Twenty regiments, the Alpini in their green feathered hats, the Carabinieri on horseback, the Navy in blues, all march past the presidential stand from the Colosseum to Piazza Venezia. It takes about ninety minutes and it is broadcast on RAI 1 without commercial break.</p>"),
    ("II","<h4>The tricolour over Rome.</h4><p>At the exact moment the anthem finishes, the Frecce Tricolori pass overhead trailing green, white and red smoke that hangs in the Roman air for a full three minutes. Every phone in Piazza Venezia is pointed at the sky.</p>"),
    ("III","<h4>The presidential wreath.</h4><p>The President of the Republic and the presidents of the two chambers place a laurel wreath at the tomb of the Unknown Soldier — the <em>Milite Ignoto</em> — inside the Altare della Patria. A single trumpet plays the <em>Silenzio</em>.</p>"),
    ("IV","<h4>Open day at the Quirinale.</h4><p>The palace, normally strictly closed, opens its Salone dei Corazzieri and the Giardino to any citizen who queues. Free timed tickets are released a week ahead. Waiting time: hours. Nobody complains.</p>"),
    ("V","<h4>Concerts across the country.</h4><p>Regional bands, philharmonic orchestras and city choirs perform the anthem and republican-era repertoire in every capoluogo — from Torino to Bari — often in the main cathedral square.</p>"),
    ("VI","<h4>The family lunch.</h4><p>A public holiday. Offices, ministries and banks close. Families gather. The menu is not fixed but tends toward the Roman: <em>bucatini all'amatriciana</em>, <em>abbacchio al forno</em>, <em>fragole con panna</em>, a bottle of Frascati or a Cesanese from the Alban Hills. Italy is at its most Italian.</p>")
  ],
  "recipe":{
    "name":"Bucatini all'amatriciana",
    "why":"The Roman dish traditionally served on 2 June — from Amatrice in the Sabina, technically a Lazio town, historically a mountain shepherd's plate that entered the Roman canon in the nineteenth century.",
    "ingredients":[("Bucatini pasta","500 g"),("Guanciale (cured pork jowl)","150 g"),("Pecorino romano","80 g grated"),("Peeled San Marzano tomatoes","400 g"),("Dry white wine","1/2 glass"),("Chili (peperoncino)","1 whole"),("Salt","to taste"),("Black pepper","to taste")],
    "steps":"Cut the guanciale into strips the width of a matchstick. Render it slowly, without oil, in a heavy pan until golden and translucent. Deglaze with the white wine and let it evaporate. Add the peperoncino and the crushed tomatoes; simmer twelve minutes until the sauce breaks into oil at the edge. Cook the bucatini in salted water for one minute short of the packet instruction. Transfer directly into the sauce with a ladle of pasta water. Toss over medium heat, off flame add the pecorino in two additions, tossing until glossy. Serve immediately with a further scattering of pecorino and a heavy grind of black pepper. Never — as any Roman will insist — with garlic, and never with onion."
  },
  "quotes":[
    ("Che cosa è la patria? È quella terra dove nostro figlio parlerà la nostra lingua.","Sandro Pertini, President of the Republic (1978–1985)"),
    ("L'Italia è una Repubblica democratica, fondata sul lavoro.","Article 1, Constitution of the Italian Republic")
  ]
},
{
  "slug":"carnevale",
  "title":"Il Carnevale di Venezia — Carnival of Venice · Club Italia",
  "meta":"Ten days of masked baroque theatre across the Venetian lagoon. The history, the great masks, the Flight of the Angel, and a full cultural essay on Venice's carnival — from Club Italia.",
  "img":"assets/img/pillar-tradition.jpg",
  "eyebrow":"Cultural event · Il Carnevale",
  "date":"February · ten days before Lent",
  "since":"Since 1094",
  "place":"Venezia, Piazza San Marco",
  "watch":"Live from the lagoon",
  "h1":"Il Carnevale di",
  "h1gold":"Venezia.",
  "lede":"For ten days every winter, Venice returns to the eighteenth century. The masks come out, the palazzi open their piani nobili, the gondolas fill the small canals, and the whole city agrees, for a brief theatrical moment, that identity itself can be lifted off and set aside. Nowhere on earth performs history quite like this.",
  "vocab":[
    ("il Carnevale","Carnival"),
    ("la maschera","the mask"),
    ("la bautà","classic white male mask"),
    ("la moretta","black velvet ladies' mask"),
    ("il tabarro","the cape"),
    ("il tricorno","the three-cornered hat"),
    ("la Serenissima","the Venetian Republic"),
    ("il gondoliere","the gondolier"),
    ("la calle","narrow Venetian street"),
    ("il campo","square"),
    ("il ridotto","gambling salon"),
    ("le frittelle","carnival doughnuts"),
    ("i galani","sweet fried ribbons"),
    ("il Volo dell'Angelo","Flight of the Angel")
  ],
  "history":[
    ("1094","<h4>The first documented Carnevale.</h4><p>A charter of the doge Vitale Falier mentions a period of public revels in the days before Lent. The lagoon city, already the wealthiest maritime republic in Europe, is beginning to institutionalise its most famous festival.</p>"),
    ("1268","<h4>The first laws about masks.</h4><p>The Great Council issues a decree forbidding masked citizens from throwing perfumed eggs at ladies. The record is our first legal proof that Venice was already, by the thirteenth century, a city that lived behind a face.</p>"),
    ("1436","<h4>The mask-makers guild.</h4><p>Venice grants a formal statute to the <em>maschereri</em>, the mask-makers, who by then have their own workshops around San Cassiano. Papier-mâché, gesso, gold leaf. The craft has changed remarkably little.</p>"),
    ("1797","<h4>Napoleon closes the Republic.</h4><p>Bonaparte's troops enter Venice, the Serenissima falls, and the Austrian and later Italian authorities suppress Carnevale as decadent and politically dangerous. For nearly two centuries the festival vanishes.</p>"),
    ("1979","<h4>The modern revival.</h4><p>A group of Venetian citizens, cultural societies and the municipality restage a full Carnevale in the lagoon. It draws thirty thousand visitors in year one, three million within a decade, and has run every year since.</p>"),
    ("Today","<h4>An officially UNESCO-protected patrimony.</h4><p>The Carnevale is inscribed in the Italian intangible heritage register and studied at university level in the Ca' Foscari department of art history. Club Italia's Venetian units use its costumes as a live grammar of eighteenth-century Italian.</p>")
  ],
  "traditions":[
    ("I","<h4>Il Volo dell'Angelo.</h4><p>Opening Sunday: a young woman, chosen the previous year as Maria del Carnevale, is lowered on a wire from the top of the Campanile of San Marco down to the doge's balcony. The whole piazza looks up. The tradition dates from a Turkish acrobat's stunt of 1548.</p>"),
    ("II","<h4>The masks.</h4><p>Six historical masks recur: the <em>bautà</em> (white male, worn with tricorno and cape), the <em>moretta</em> (silent black velvet held by a mouth-button, for women), the <em>medico della peste</em> (long-beaked plague doctor), the <em>gnaga</em> (cat), the <em>volto</em> and the <em>Colombina</em>. Each has its own social history and its own rules.</p>"),
    ("III","<h4>The private balls.</h4><p>The great palazzi along the Grand Canal — Ca' Vendramin, Palazzo Pisani-Moretta, Ca' Zenobio — host baroque balls where the entire audience is required to arrive in period costume. Tickets run into the thousands of euros. The candlelight is real.</p>"),
    ("IV","<h4>La Festa delle Marie.</h4><p>A costumed procession of twelve young Venetian women, elected by neighbourhood, in medieval dress, from San Pietro di Castello to San Marco. Commemorates a tenth-century rescue of twelve brides kidnapped by Istrian pirates.</p>"),
    ("V","<h4>Frittelle and galani.</h4><p>Every pastry window in the city fills with <em>frittelle</em> — small round doughnuts stuffed with cream, zabaglione or raisins — and <em>galani</em>, thin fried ribbons dusted with icing sugar. The city eats them for breakfast for ten straight days.</p>"),
    ("VI","<h4>The closing at Piazza San Marco.</h4><p>On Shrove Tuesday, a fireworks display over the Bacino, the lowering of the giant Carnevale banner, and the ritual burning of a small paper effigy. Lent begins the next morning. The masks are put away for another year.</p>")
  ],
  "recipe":{
    "name":"Frittelle veneziane",
    "why":"The classic Carnevale doughnut, made in Venetian homes and pastry shops for at least three hundred years. Recipe adapted from the eighteenth-century cookbook of Domenico Felici, Venetian pastry chef.",
    "ingredients":[("00 flour","500 g"),("Fresh yeast","20 g"),("Whole milk","250 ml"),("Eggs","2"),("Sugar","80 g plus for dusting"),("Butter","50 g melted"),("Golden raisins","100 g soaked in grappa"),("Zest of one lemon","—"),("Pinch of salt","—"),("Sunflower oil","for frying")],
    "steps":"Warm the milk to blood heat and dissolve the yeast with a spoon of the sugar. Combine flour, remaining sugar, eggs, melted butter, lemon zest and salt in a bowl. Pour in the milk. Beat to a soft, sticky dough. Fold in the drained raisins. Cover and prove for two hours until doubled. Heat the oil to one hundred and seventy degrees. Drop spoonfuls of dough into the hot oil in batches of six. Cook two minutes each side until deep gold. Drain on paper. Roll in sugar while still warm. Eat within the hour, standing up, ideally on a bridge over a Venetian canal."
  },
  "quotes":[
    ("A Venezia si vive dietro una maschera. È l'unico modo di essere davvero se stessi.","Attributed to Casanova, Histoire de ma vie"),
    ("Venezia, la più bella maschera del Mediterraneo.","Ernest Hemingway, Across the River and into the Trees")
  ]
},
{
  "slug":"palio-siena",
  "title":"Il Palio di Siena — the Bareback Race of the Piazza · Club Italia",
  "meta":"Ninety seconds of bareback horse racing around the Piazza del Campo, contested by seventeen medieval city districts twice a year. The history, the contrade, the strategy, the songs — a Club Italia cultural essay.",
  "img":"assets/img/pillar-tradition.jpg",
  "eyebrow":"Cultural event · Il Palio",
  "date":"2 July · 16 August · every year",
  "since":"Since 1633",
  "place":"Siena, Piazza del Campo",
  "watch":"Live from Tuscany",
  "h1":"Il Palio di",
  "h1gold":"Siena.",
  "lede":"Twice a year, seventeen medieval city districts saddle up ten horses and gallop bareback around a shell-shaped square in the middle of Tuscany. The race lasts ninety seconds. The preparation lasts a lifetime. Anyone who has been in Siena on the second of July or the sixteenth of August knows there is nothing else in Europe quite like it.",
  "vocab":[
    ("il Palio","the banner (and the race)"),
    ("la contrada","medieval city district"),
    ("il fantino","the jockey"),
    ("il cavallo","the horse"),
    ("la Piazza del Campo","the shell-shaped square"),
    ("il tufo","the yellow earth track"),
    ("la mossa","the start"),
    ("il canape","the starting rope"),
    ("il Mangia","the great tower"),
    ("il drappellone","the painted silk banner"),
    ("la benedizione","the horse's blessing in church"),
    ("la cena della prova","the pre-race dinner"),
    ("i colori","the district colours"),
    ("la vittoria","the victory")
  ],
  "history":[
    ("1200s","<h4>Medieval city games.</h4><p>Siena, one of the great banking republics of the Middle Ages, holds bull-hunts, buffalo-races and pugilistic contests in the Campo. The rivalry between the neighbourhoods — the <em>contrade</em> — is already fierce and organised.</p>"),
    ("1633","<h4>The first Palio alla tonda.</h4><p>The city stages the first true bareback horse race around the shell of the Campo. The prize is a painted silk banner — the <em>Palio</em> — which gives the race its name. It has been run twice a year, on 2 July and 16 August, almost every year since.</p>"),
    ("1721","<h4>The seventeen contrade are fixed.</h4><p>A ducal edict reduces the historical thirty-five districts to seventeen and fixes their boundaries. Every Sienese is born into one — the district of the address of the maternity. The affiliation is for life.</p>"),
    ("1729","<h4>Governor Violante formalises the ceremony.</h4><p>The Marchesa Violante Beatrice of Bavaria, governor of Siena, standardises the pre-race parade, the costumes, the flag-throwing and the marching order. The choreography has not meaningfully changed in three hundred years.</p>"),
    ("1899","<h4>The first extraordinary Palio.</h4><p>An additional race is run outside the twice-yearly calendar to mark a national event. This precedent is invoked rarely — for the end of a world war, a papal visit, or a great civic anniversary.</p>"),
    ("Today","<h4>A modern spectacle with medieval bones.</h4><p>Sixty thousand people fill the Campo. The race is broadcast live on RAI. Every hotel in Tuscany is full. The horses arrive by van; the ceremony arrives by history.</p>")
  ],
  "traditions":[
    ("I","<h4>The seventeen contrade.</h4><p>Aquila, Bruco, Chiocciola, Civetta, Drago, Giraffa, Istrice, Leocorno, Lupa, Nicchio, Oca, Onda, Pantera, Selva, Tartuca, Torre and Valdimontone. Each has its own colours, its own hymn, its own church, its own oratory and its own museum. Only ten race per Palio: seven by right, three by lottery.</p>"),
    ("II","<h4>The horse's blessing.</h4><p>An hour before the race, each contrada takes its horse into its own parish church. The priest blesses the animal at the altar. If the horse defecates during the blessing — as they routinely do — it is considered excellent luck.</p>"),
    ("III","<h4>The corteo storico.</h4><p>A two-and-a-half hour procession in medieval costume, with drums, flag-throwers and horses, wends through the streets before assembling on the Campo. Six hundred participants. Every costume is stitched by the contrada seamstresses.</p>"),
    ("IV","<h4>The mossa.</h4><p>The start is chaos by design. Nine horses enter the twin ropes; the tenth — the <em>rincorsa</em> — enters last and triggers the start when it chooses. False starts routinely delay proceedings for an hour. Rival contrade negotiate — and pay — for tactical advantage.</p>"),
    ("V","<h4>The race itself.</h4><p>Three laps of the tufo-covered Campo. Ninety seconds if clean. Two of the three corners — San Martino and the Casato — are treacherous, angled far below their outer walls. Falls are frequent. A horse can win without its jockey.</p>"),
    ("VI","<h4>The dinner of the victory.</h4><p>The winning contrada holds an open-air victory dinner in its streets, sometimes for three thousand seated guests, with the horse at the head of the table. The losing contrade go home in silence. The rivalry resumes the next morning.</p>")
  ],
  "recipe":{
    "name":"Pici all'aglione",
    "why":"The traditional hand-rolled Sienese pasta with an aromatic tomato sauce, eaten across the province in the days around the Palio. Recipe from the Tuscan grandmother tradition of the val di Chiana.",
    "ingredients":[("00 flour","400 g"),("Warm water","200 ml"),("Salt","1 tsp"),("Ripe tomatoes","800 g"),("Aglione garlic","6 cloves (or 3 elephant garlic)"),("Extra virgin olive oil","60 ml"),("Peperoncino","1 whole"),("Fresh basil","a handful"),("Pecorino toscano","to serve")],
    "steps":"Combine the flour and salt on a board, add warm water in stages and knead ten minutes until smooth. Rest under a bowl for thirty minutes. Roll into a two-centimetre sheet. Cut into strips and, on a wooden board, roll each strip under the palm into a long, thick, uneven noodle — that is the <em>pico</em>. Peel and crush the garlic. Warm the oil, add garlic and peperoncino, cook two minutes without browning. Add the peeled crushed tomatoes and simmer twenty-five minutes until the sauce breaks. Season. Cook the pici in salted water for six to seven minutes — they should be al dente and slightly chewy. Toss in the sauce off heat with the torn basil. Serve with a generous grating of pecorino toscano."
  },
  "quotes":[
    ("Il Palio non è una corsa. È la nostra vita in novanta secondi.","Sienese proverb"),
    ("A Siena non si nasce cittadini di Siena. Si nasce cittadini di una contrada.","Local saying, recorded by the anthropologist Alessandro Falassi")
  ]
}
]


def render(ev):
    quotes_html = ""
    for i,(q,who) in enumerate(ev["quotes"]):
        style = "dark" if i%2==0 else ""
        quotes_html += f'''
<section class="ev-pull {style}"><div class="wrap-narrow"><p class="quote">"{q}"</p><p class="sig">{who}</p></div></section>'''

    hist_html = ""
    for yr,html in ev["history"]:
        hist_html += f'<div class="ev-tl-row"><div class="yr">{yr}</div><div>{html}</div></div>'

    trad_html = ""
    for rn,html in ev["traditions"]:
        trad_html += f'<div class="ev-tradition-card"><div class="rn">{rn}</div>{html}</div>'

    vocab_html = ""
    for it,en in ev["vocab"]:
        vocab_html += f'<div class="row"><div class="it">{it}</div><div class="en">{en}</div></div>'

    ing_html = ""
    for i,q in ev["recipe"]["ingredients"]:
        ing_html += f'<li>{i}<span>{q}</span></li>'

    body = f'''
<!--FOLD 1 · HERO-->
<section class="ev-hero">
  <div class="ev-hero-bg"><img src="{ev['img']}" alt=""></div>
  <div class="wrap">
    <p class="kicker">{ev['eyebrow']} <span>· {ev['date']}</span></p>
    <h1>{ev['h1']}<br><span class="gold-ital">{ev['h1gold']}</span></h1>
    <p class="lede">{ev['lede']}</p>
    <div class="meta">
      <div><small>Held on</small><strong>{ev['date']}</strong></div>
      <div><small>Where</small><strong>{ev['place']}</strong></div>
      <div><small>First recorded</small><strong>{ev['since']}</strong></div>
      <div><small>Broadcast</small><strong>{ev['watch']}</strong></div>
    </div>
  </div>
</section>

<div class="ev-tri" aria-hidden="true"></div>

<!--FOLD 2 · CULTURAL ESSAY / 2-col magazine-->
<section class="ev-band paper">
  <div class="wrap">
    <div class="ev-mag">
      <div>
        <span class="drop">01</span>
        <span class="eyebrow eyebrow-line">The cultural essay</span>
        <h2>Why every Italian, on this day, <span class="gold-ital">stops.</span></h2>
        <p class="lede-p">A national holiday is a country's most concentrated form of self-portrait. To understand <em>{ev['recipe']['name'].split()[0]}</em> at a Sienese table, the smoke trails of the Frecce Tricolori over Rome, or the mask of the <em>bautà</em> in a Venetian palazzo, is to understand the Italian idea of belonging.</p>
      </div>
      <div class="body">
        <p>The Italian calendar is not a schedule; it is a liturgy. Every region has its own saints' days, harvests, harbour festivals, chestnut fairs, olive-oil pressings, sagre and processions. Layered on top, only three or four dates belong to the entire peninsula at once. This is one of them.</p>
        <p>When Club Italia builds a cultural unit around a date, the point is never trivia. Italy is a country where the words <em>tradizione</em> and <em>identità</em> still carry weight, where the shape of an event teaches the shape of a language, and where knowing why an event happens, and how it is celebrated, is inseparable from speaking Italian well.</p>
        <p>Our teachers do not lecture on holidays. They walk into their kitchens the morning after, phones on, and describe them. The learner hears the exact register, the exact vocabulary, the emotional colour of the day — spoken, unscripted, by an Italian who lived it the day before.</p>
        <p>What follows is the full editorial file: the history, the traditions, the recipe, the vocabulary and the live broadcast we will run this year. Save it. Come back to it. Bring it into class.</p>
      </div>
    </div>
  </div>
</section>

{quotes_html.split('</section>')[0]}</section>

<!--FOLD 4 · HISTORY TIMELINE-->
<section class="ev-band dark">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">A short history</span>
    <h2>The story, in six <span class="gold-ital">dates.</span></h2>
    <p class="lede-p">Every Italian tradition has a paper trail. Here is the one for this event, as documented by the Italian state archives and the standard scholarly reference works.</p>
    <div class="ev-timeline">
      {hist_html}
    </div>
  </div>
</section>

<!--FOLD 5 · TRADITIONS 6-CARD GRID-->
<section class="ev-band paper">
  <div class="wrap">
    <span class="eyebrow eyebrow-line">The six great traditions</span>
    <h2>What happens on the <span class="gold-ital">day itself.</span></h2>
    <div class="ev-tradition-grid">
      {trad_html}
    </div>
  </div>
</section>

<!--FOLD 6 · SECOND PULL QUOTE-->
{quotes_html.split('</section>')[1]}</section>

<!--FOLD 7 · LIVE BROADCAST-->
<section class="ev-live">
  <div class="wrap">
    <div class="grid">
      <div class="video-frame">
        <img src="{ev['img']}" alt="">
        <span class="live-badge">Live · this year</span>
        <a href="#" class="play" aria-label="Watch live">▶</a>
      </div>
      <div>
        <span class="eyebrow eyebrow-line">Live stream</span>
        <h2>Watch the event <span class="gold-ital">from Italy.</span></h2>
        <p>Club Italia broadcasts a live cultural window from the piazza on the day itself, hosted by one of our resident teachers, with commentary in slow Italian for learners at A1 and above, and a follow-up debrief lesson the following week.</p>
        <p>Members of the Club Italia community receive the calendar invitation automatically. Non-members can register a single-event pass through our advisors.</p>
        <div class="hero-ctas" style="margin-top:1.6rem">
          <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Broadcast Seat</button>
          <a class="btn btn-3d btn-3d-ghost" href="../../events.html">All Events</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!--FOLD 8 · RECIPE-->
<section class="ev-recipe">
  <div class="wrap">
    <div class="grid">
      <div>
        <span class="eyebrow eyebrow-line">The recipe of the day</span>
        <h3>{ev['recipe']['name']}</h3>
        <p style="color:var(--on-light-soft);line-height:1.7">{ev['recipe']['why']}</p>
        <div class="steps" style="margin-top:2rem">
          {"".join(f"<p>{s.strip()}.</p>" for s in ev['recipe']['steps'].split('.') if s.strip())}
        </div>
      </div>
      <div>
        <span class="eyebrow eyebrow-line">Ingredients</span>
        <ul>{ing_html}</ul>
      </div>
    </div>
  </div>
</section>

<!--FOLD 9 · VOCAB TABLE-->
<section class="ev-vocab">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow eyebrow-line">The vocabulary of the day</span>
      <h2 class="display-md">Words for the <span class="gold-ital">occasion.</span></h2>
      <p class="lead">A ready-to-print glossary of the twelve to fifteen Italian words a learner will hear most on the day.</p>
    </div>
    <div class="grid">
      {vocab_html}
    </div>
  </div>
</section>

<!--FOLD 10 · CTA-->
<section class="ev-cta">
  <div class="wrap-narrow">
    <span class="eyebrow eyebrow-line">Join the cultural calendar</span>
    <h2>Every great Italian day, <span class="gold-ital">taught in Italian.</span></h2>
    <p>Every Club Italia course includes a cultural events calendar, live broadcasts from the piazza on the day itself, follow-up debrief lessons in slow Italian, and a recorded archive open to all learners for life.</p>
    <div class="hero-ctas" style="justify-content:center;display:flex">
      <a class="btn btn-3d btn-3d-primary" href="../../courses.html">Explore the Courses</a>
      <button class="btn btn-3d btn-3d-ghost" data-advisor type="button">Talk to an Advisor</button>
    </div>
  </div>
</section>
'''
    html = shell(ev["title"], ev["meta"], body, root="../../", extra_head=EVENT_STYLE)
    # Adjust image paths for pages/events/ depth
    html = html.replace('src="assets/img/','src="../../assets/img/')
    out = f"/home/user/workspace/club-italia/pages/events/{ev['slug']}.html"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out,"w") as f:
        f.write(html)
    print(ev["slug"], len(html), "bytes")

if __name__ == "__main__":
    for e in EVENTS:
        render(e)
