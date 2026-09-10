#!/usr/bin/env python3
"""Club Italia site generator — writes every remaining internal page from data."""
import os, textwrap, json
from pathlib import Path

ROOT = Path("/home/user/workspace/club-italia")

NAV = open(ROOT/"_partials/nav.html").read()
FOOTER = open(ROOT/"_partials/footer.html").read()

def page(title, desc, body, css_extra="", rel="", script="js/ci.js"):
    """Wrap body in the shared shell. rel is '' for root pages, '../../' for subfolders."""
    nav = NAV
    footer = FOOTER
    if rel:
        # rewrite relative asset paths in nav/footer/body
        for tag in ('href="', 'src="'):
            nav = nav.replace(tag+"index.html", tag+rel+"index.html")
        # add rel prefix to all root-relative hrefs that don't start with http, #, mailto, tel, or /
        import re
        def prefix(m):
            attr, val = m.group(1), m.group(2)
            if val.startswith(('http', '#', 'mailto:', 'tel:', '/', rel)): return m.group(0)
            return f'{attr}="{rel}{val}"'
        nav = re.sub(r'(href|src)="([^"]+)"', prefix, nav)
        footer = re.sub(r'(href|src)="([^"]+)"', prefix, footer)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{rel}css/ci.css">
{css_extra}
</head>
<body>
{nav}
{body}
{footer}
<script src="{rel}{script}"></script>
</body>
</html>
"""

# ---------- COURSES DATA (11 total: 4 CI + 4 Parliamo + 3 Capsule) ----------
COURSES = {
    "ci1": {
        "code":"CI · 01","title":"CI Principiante","tag":"Foundation · Roma","cefr":"A0 → A1.1","hours":"20 lessons × 85 min",
        "hero_image":"assets/img/course-ci1.jpg","city":"Rome",
        "promise":"Your first Italian, taught in Rome — the city where the language began. In twenty live lessons you go from the sound of the language to your first real conversations.",
        "outcomes":[
            "Introduce yourself, family and work in Italian",
            "Order food, coffee and drinks with confidence",
            "Understand slow, clear spoken Italian in daily situations",
            "Handle numbers, dates, times and money",
            "Write short messages and postcards in Italian",
            "Read menus, signs and simple posts",
        ],
        "syllabus":[
            ("Ciao, Roma!","The Italian sound system, greetings, subject pronouns, the verb essere. Set at Fiumicino, first steps in Rome."),
            ("Chi sei?","Introducing yourself, nationalities, avere, definite articles. A dialogue at a Roman café."),
            ("La mia famiglia","Family vocabulary, possessive adjectives, plural nouns. Photos from a real Roman family."),
            ("Al bar","Ordering coffee, present tense of regular verbs (-are), c'è / ci sono. The espresso ritual."),
            ("In città","Prepositions of place, andare and venire, asking for directions. The seven hills of Rome."),
            ("A che ora?","Telling time, days of the week, months, the verb fare. A day in the life of a Roman."),
            ("A tavola","Food vocabulary, partitives, quanto costa, ordering in a trattoria. Cucina romana."),
            ("Mi piace","Piacere, opinions, comparatives, likes and dislikes. Italian film and music."),
            ("Che tempo fa?","Weather, seasons, dovere / potere / volere. Weekends in the Roman countryside."),
            ("A casa","Rooms of the house, furniture, dare and stare. Roman apartment life."),
            ("Vestiti","Clothes, colours, adjectives that agree, sapere vs conoscere. Via del Corso, the shopping street."),
            ("Al mercato","Food shopping, markets, imperative for polite requests. Campo de' Fiori."),
            ("In ufficio","Work vocabulary, jobs, telefonare, scrivere. A day in a Roman office."),
            ("In viaggio","Trains, tickets, hotels, the near future with andare a + infinitive. Termini Station."),
            ("A che punto sei?","Review, mini test, oral presentation. Half-way milestone."),
            ("Passato prossimo","Introduction to the past tense with avere. Yesterday in Rome."),
            ("Passato prossimo con essere","The past with essere, agreement of the past participle. Stories from a Sunday."),
            ("Il mio quartiere","Describing places, reflexive verbs, daily routine. Trastevere on a Saturday."),
            ("Il fine settimana","Weekend plans, imperfetto introduced, contrastive with passato. A country outing."),
            ("Arrivederci, Roma!","Full oral CEFR A1.1 assessment, farewell dialogue, next steps. Ready for CI Elementare."),
        ],
    },
    "ci2": {
        "code":"CI · 02","title":"CI Elementare","tag":"Elementare · Firenze","cefr":"A1.1 → A1.2","hours":"20 lessons × 85 min",
        "hero_image":"assets/img/course-ci2.jpg","city":"Florence",
        "promise":"Everyday Italian from Florence, the city where the language was standardised. Twenty live lessons that take you from short replies to full daily narrative.",
        "outcomes":[
            "Narrate a past event or weekend in detail",
            "Describe people, places and things with precision",
            "Make and change plans on the phone",
            "Handle emails and short letters in Italian",
            "Understand a Tuscan waiter, shopkeeper or landlord",
            "Read simple newspaper headlines and short articles",
        ],
        "syllabus":[
            ("Firenze, culla della lingua","Why Italian is Tuscan. Dante, Boccaccio, Petrarch. Review of A1.1."),
            ("Ricordi d'estate","Passato prossimo consolidation, time markers (ieri, la settimana scorsa)."),
            ("Da piccolo","Imperfetto for description and habit, comparison with passato prossimo."),
            ("Le persone","Describing people physically and in character. Adjective agreement in depth."),
            ("A casa mia","Rooms, prepositions of place, ci per luogo. A Florentine apartment tour."),
            ("Nella cucina toscana","Regional food vocabulary, ne partitivo, cooking verbs. Ribollita, bistecca, cantucci."),
            ("Al ristorante","Full dining dialogue, complaining politely, tipping, il conto per favore."),
            ("Fare la spesa","Weights, containers, packaging. Mercato Centrale."),
            ("Al telefono","Phone conventions, formal register, leaving a message."),
            ("Prendo appuntamento","Making appointments — doctor, hairdresser, notary. The Italian bureaucratic register."),
            ("Il corpo umano","Body vocabulary, at the pharmacy, common ailments, mi fa male + body part."),
            ("Vestirsi","Reflexive verbs, morning routine, adverbs of frequency."),
            ("Il tempo libero","Hobbies, sport, Serie A football, Sunday papers."),
            ("Cinema italiano","Fellini and Sorrentino, film vocabulary, expressing opinion."),
            ("A metà strada","Midpoint review, oral test, cultural quiz on Florence."),
            ("Il futuro","Simple future tense, plans, promises, predictions."),
            ("Se… allora","Introduction to hypothetical: se + present / future, se + imperfetto / condizionale (light touch)."),
            ("Il condizionale","Condizionale for polite requests and wishes: vorrei, mi piacerebbe, potrei."),
            ("Scrivere una mail","Email conventions, formal vs informal register, greetings and sign-offs."),
            ("A presto, Firenze!","CEFR A1.2 full assessment, cultural presentation, path to CI Intermedio."),
        ],
    },
    "ci3": {
        "code":"CI · 03","title":"CI Intermedio","tag":"Intermedio · Bologna","cefr":"A1.2 → A2.1","hours":"20 lessons × 85 min",
        "hero_image":"assets/img/course-ci3.jpg","city":"Bologna",
        "promise":"Confident daily Italian from Bologna — la Dotta, la Grassa, la Rossa. Twenty live lessons on tenses, opinion, argument and the language of the Italian table.",
        "outcomes":[
            "Move between passato prossimo, imperfetto and trapassato with ease",
            "Express opinion, doubt and preference clearly",
            "Talk about food, cooking, cuisine and regional identity",
            "Understand fast native speech in most everyday situations",
            "Read blogs, restaurant reviews and short essays",
            "Take part in a small group conversation for the full 85 minutes",
        ],
        "syllabus":[
            ("Bologna la dotta","Italy's oldest university, the arcades, the food. Review of A1.2."),
            ("Passato remoto in the wild","Recognising passato remoto in fairy tales and news. Passive knowledge only."),
            ("Trapassato prossimo","Talking about what happened before what happened. Storytelling structure."),
            ("Imperfetto vs passato prossimo","The Italian storytelling engine. Real narratives from a Bolognese childhood."),
            ("La cucina emiliana","Ragù, tortellini, mortadella, Parmigiano. Cooking verbs and cultural vocabulary."),
            ("A tavola con gli amici","Dinner-party Italian. Interrupting politely, agreeing, disagreeing, refilling wine."),
            ("Ho un'opinione","Expressing opinion: penso che, credo che, secondo me. Congiuntivo introduced softly."),
            ("Il mio quartiere","Comparing places: più / meno / così… come. Bologna vs Milano vs Roma."),
            ("Andiamo al cinema","Reserving tickets, film genres, describing a plot, recommending."),
            ("La musica italiana","Lucio Dalla, Battisti, De Andrè, contemporary indie. Listening lab."),
            ("A metà del cammino","Midpoint oral assessment, cultural presentation."),
            ("Se dovessi scegliere","Hypothetical in the present: se + congiuntivo imperfetto + condizionale."),
            ("Le città italiane","Describing Italian cities, geography, north / centre / south differences."),
            ("Il lavoro in Italia","Vocabulary of work, CV, colloquio di lavoro, contratti."),
            ("La sanità","Healthcare vocabulary, at the doctor, at the hospital, the Italian public system."),
            ("La banca","Bank vocabulary, opening an account, paying bills, ordering online."),
            ("La casa in affitto","Renting an apartment, understanding a contract, negotiating with a landlord."),
            ("Feste italiane","Italian holidays: Natale, Pasqua, Ferragosto, Palio di Siena, Carnevale di Venezia."),
            ("Il dialetto","Introduction to Italian dialects — bolognese, romanesco, napoletano, siciliano — as cultural heritage."),
            ("Arrivederci, Bologna!","Full CEFR A2.1 assessment, oral presentation, path to CI Avanzato."),
        ],
    },
    "ci4": {
        "code":"CI · 04","title":"CI Avanzato","tag":"Avanzato · Napoli & Milano","cefr":"A2.1 → A2.2","hours":"20 lessons × 85 min",
        "hero_image":"assets/img/course-ci4.jpg","city":"Naples & Milan",
        "promise":"Real Italian for real life, between the warmth of Naples and the sharpness of Milan. Twenty live lessons that consolidate CEFR A2 and open the door to B1.",
        "outcomes":[
            "Use congiuntivo in context, not just in tests",
            "Follow a fast Italian film without subtitles most of the time",
            "Argue, persuade and negotiate in a small-group setting",
            "Write structured emails, reviews and short articles",
            "Understand regional accents from north to south",
            "Sit and pass an internationally recognised A2 exam",
        ],
        "syllabus":[
            ("Napoli e Milano — due Italie","The northern-southern axis of Italian identity. Review of A2.1."),
            ("Congiuntivo presente","Full introduction to the subjunctive: after verbs of opinion, doubt, feeling."),
            ("Congiuntivo imperfetto","Backshift, hypothetical use, se + imperfetto + condizionale."),
            ("Discorso indiretto","Reported speech: he said that…, she asked whether…"),
            ("La stampa italiana","Reading Corriere della Sera and la Repubblica. Newspaper Italian."),
            ("Il cinema italiano","Full film analysis: La Grande Bellezza, La Vita è Bella, Il Postino."),
            ("Opera in italiano","Understanding a Verdi libretto. Aria listening lab."),
            ("Business Italian","Meeting vocabulary, presenting, negotiating, closing a deal."),
            ("La politica italiana","Institutions, parties, elections — the vocabulary of civic life."),
            ("Metà strada","Full midpoint oral, written and listening assessment."),
            ("Argomentare","Debating in Italian. Structured arguments, giving and refuting points."),
            ("Persuadere","The language of sales, marketing and advertising. Rhetorical devices."),
            ("Napoli — la lingua della strada","Napoletano expressions that entered standard Italian. Neapolitan cinema."),
            ("Milano — la lingua degli affari","Milanese business register, aperitivo culture, fashion vocabulary."),
            ("La letteratura contemporanea","Ferrante, Calvino, Baricco — reading passages and discussion."),
            ("La cucina regionale","Twenty regions, twenty cuisines — a culinary tour of Italy."),
            ("Il sistema scolastico","Italian education from elementari to università, plus the language of academia."),
            ("Vivere in Italia","Practical language for moving to Italy: codice fiscale, permesso di soggiorno, sanità."),
            ("Cittadinanza italiana","The language of jure sanguinis, applications, consular Italian."),
            ("Arrivederci — a presto, in Italia!","Full CEFR A2.2 assessment, cultural graduation, path to B1."),
        ],
    },
    "ps1": {
        "code":"PS · 01","title":"Al Caffè","tag":"Parliamo · Foundation","cefr":"Spoken A0 → A1","hours":"20 sessions × 85 min",
        "hero_image":"assets/img/spoken-ps1.jpg","city":"Rome cafés",
        "promise":"Twenty live conversation sessions set at Italian cafés. No grammar drills, no textbooks — only spoken Italian, from the first minute.",
        "outcomes":[
            "Order coffee, food and drinks with cultural confidence",
            "Small-talk with a barista, a neighbour or a taxi driver",
            "Understand the fast, warm rhythm of café Italian",
            "Handle greetings, farewells and social pleasantries",
            "React naturally with typical Italian interjections",
            "Speak Italian without stopping to translate in your head",
        ],
        "syllabus":[
            ("Buongiorno, un caffè","The espresso ritual — every word that happens at a Roman bar."),
            ("Al banco","Standing at the bar vs sitting at the table. Prices, timing, tipping."),
            ("Il barista","Meeting the same barista every morning. The Italian art of daily kindness."),
            ("Il vicino di banco","Small talk with the person next to you at the bar."),
            ("Il tempo","Weather chit-chat, the second-most-Italian conversation."),
            ("La squadra","Football at the bar. Every man and woman in Italy has an opinion."),
            ("La politica","Politics at the bar — how to nod, agree, and not commit."),
            ("Il turista","When you are addressed in English — how to reply, gently, in Italian."),
            ("Il cornetto","Ordering breakfast. Sweet vs savoury, cream vs jam, the difference between un cornetto and un croissant."),
            ("Metà strada","Midpoint conversation lab — a full 15-minute unstructured chat with the teacher."),
            ("Il pranzo veloce","Ordering a quick lunch — panino, tramezzino, insalatona."),
            ("L'aperitivo","The Milanese ritual — spritz, negroni, and the vocabulary of small plates."),
            ("Il conto","Paying the bill. Coperto, servizio, mancia. Splitting the bill Italian-style."),
            ("Il caffè da asporto","Take-away Italian — a very recent phenomenon that has its own new vocabulary."),
            ("La colazione della domenica","Sunday breakfast at a bar — bombolone, sfogliatella, maritozzo."),
            ("Il caffè in ufficio","Office caffè culture — the coffee run, the machine, the coffee gossip."),
            ("Il caffè in famiglia","Grandmother's moka pot. The most sacred coffee of all."),
            ("Il caffè in albergo","Hotel breakfast Italian — buffet vs à la carte, the polite requests."),
            ("Il caffè al mare","Summer at the beach bar. Granita, gelato, spremuta d'arancia."),
            ("Arrivederci, e a presto","Final oral conversation, cultural graduation, path to A Tavola."),
        ],
    },
    "ps2": {
        "code":"PS · 02","title":"A Tavola","tag":"Parliamo · Beginner","cefr":"Spoken A1 → A2","hours":"20 sessions × 85 min",
        "hero_image":"assets/img/spoken-ps2.jpg","city":"Tuscan trattorie",
        "promise":"Twenty live conversation sessions set at the Italian table. Order like a Roman, argue like a Neapolitan about pasta shape, and understand a Tuscan grandmother.",
        "outcomes":[
            "Read any Italian menu without pointing",
            "Ask for a table, a wine, a dish, and a change — politely",
            "Understand a waiter's rapid recitation of the specials",
            "Argue politely about a dish or a bill",
            "Talk about food history, region and cuisine",
            "Cook and talk in Italian at the same time",
        ],
        "syllabus":[
            ("Il menù","Reading a full Italian menu: antipasto, primo, secondo, contorno, dolce."),
            ("La prenotazione","Booking a table by phone. Time, number of people, dietary needs."),
            ("Il vino","Ordering wine. Regional grape varieties, house wine vs bottle, the sommelier."),
            ("Gli antipasti","Bruschetta, salumi, formaggi — Italy's opening course in every region."),
            ("I primi","Pasta shapes and their sauces. The rules that Italians never break."),
            ("I secondi","Meat, fish, vegetarian, contorno pairing. Regional traditions."),
            ("Il dolce e il caffè","Tiramisù, panna cotta, cannolo — and the sacred espresso after."),
            ("L'oste","Talking to the owner. The Italian art of building a relationship with the trattoria."),
            ("Al mercato","Buying at the market — asking the fishmonger, the greengrocer, the butcher."),
            ("Metà strada","Midpoint full conversational assessment set in a virtual trattoria."),
            ("La cucina di casa","Home cooking Italian — la nonna, la mamma, la ricetta di famiglia."),
            ("Cucinare insieme","Cooking together in real time — verbs of preparation, quantities, timings."),
            ("La pizza","Ordering a pizza. Neapolitan vs Roman vs alla pala. The rules of margherita."),
            ("Il gelato","Ordering gelato — sizes, flavours, cono vs coppa, panna sì o no."),
            ("La sagra","Italian food festivals — the sagra del tartufo, della porchetta, dell'oliva."),
            ("Il ristorante di lusso","High-end restaurant Italian. Michelin-star register, degustazione."),
            ("La trattoria di quartiere","Neighbourhood trattoria Italian — the friendly regular."),
            ("Le regole non scritte","Cappuccino after 11 am? Never. Parmigiano on seafood? Never. The rules."),
            ("Il conto","Paying the bill. Splitting Italian-style, tipping, the ricevuta fiscale."),
            ("Arrivederci, a tavola","Final oral, cultural graduation, path to In Viaggio."),
        ],
    },
    "ps3": {
        "code":"PS · 03","title":"In Viaggio","tag":"Parliamo · Elementary","cefr":"Spoken A2","hours":"20 sessions × 85 min",
        "hero_image":"assets/img/spoken-ps3.jpg","city":"All of Italy",
        "promise":"Twenty live conversation sessions for people who actually travel Italy — trains, hotels, museums, mountain refuges, sailing the Amalfi coast.",
        "outcomes":[
            "Handle any Italian train, plane or bus without English",
            "Check in and out of any Italian hotel or B&B",
            "Ask for and understand directions in old-town labyrinths",
            "Talk to museum staff, art historians and gallerists",
            "Navigate an Italian pharmacy and doctor's office",
            "Understand regional accents from Bolzano to Palermo",
        ],
        "syllabus":[
            ("Alla stazione","Buying a ticket at Termini, Trenitalia vs Italo, first vs second class."),
            ("In treno","Italian train vocabulary. Coincidence, ritardo, il capotreno."),
            ("All'aeroporto","Check-in, security, boarding, delays — Italian airport register."),
            ("In taxi","Taxi Italian — meter, tipping, negotiating an out-of-town ride."),
            ("In albergo","Hotel check-in and check-out. Requesting a room change, room service, breakfast."),
            ("Al B&B","Bed & breakfast Italian — meeting the host, house rules, breakfast conversations."),
            ("In Airbnb","Renting a private apartment — codes, keys, house manuals, neighbour relations."),
            ("Al museo","Museum Italian — audio guide, guided tour, understanding a wall label."),
            ("Alla mostra","Exhibition Italian — talking to a curator, buying the catalogue, opinion."),
            ("Metà strada","Midpoint full oral assessment set on a virtual Italian trip."),
            ("In farmacia","Pharmacy Italian — describing symptoms, over-the-counter medicine, prescriptions."),
            ("Dal medico","At the doctor — the appointment, the visit, the referral."),
            ("Al pronto soccorso","Emergency room Italian — the codes, the triage, the paperwork."),
            ("In banca","Bank Italian — changing money, opening an account, ATM problems."),
            ("Alla posta","Post office Italian — sending a package, paying a bill, buying stamps."),
            ("Al ristorante in autostrada","Autogrill Italian — the fast lunch on the motorway, ordering at the counter."),
            ("In montagna","Mountain Italian — rifugio, sentiero, guida alpina, mal di montagna."),
            ("Al mare","Beach Italian — lettino, ombrellone, bagnino, cabina."),
            ("In città","Urban Italian — public transport, ZTL, parking, the metro in Rome, Milan, Naples."),
            ("Arrivederci, e buon viaggio","Final oral, cultural graduation, path to Chiacchierando."),
        ],
    },
    "ps4": {
        "code":"PS · 04","title":"Chiacchierando","tag":"Parliamo · Confident","cefr":"Spoken A2 → B1","hours":"20 sessions × 85 min",
        "hero_image":"assets/img/spoken-ps4.jpg","city":"Everywhere Italians talk",
        "promise":"Twenty live conversation sessions on the four things Italians actually do all day: opinion, humour, disagreement and storytelling. This is where confidence becomes fluency.",
        "outcomes":[
            "Hold a full 30-minute Italian conversation on any everyday topic",
            "Express opinion, doubt, sarcasm and humour",
            "Disagree politely and change someone's mind",
            "Tell a story with structure, pacing and punchline",
            "Understand rapid native banter and jokes",
            "Sit and pass an internationally recognised B1 oral exam",
        ],
        "syllabus":[
            ("Chiacchierare — l'arte italiana","What chiacchierare really means. The philosophy of unhurried talk."),
            ("Raccontare una storia","Storytelling structure — introduction, complication, punchline. Italian narrative style."),
            ("Fare una battuta","Italian humour — the setup, the beat, the payoff. Regional humour."),
            ("Discutere di calcio","Football arguments. Fifteen minutes on Juve vs Milan and no one leaves offended."),
            ("Discutere di politica","Political conversation — how to hold a strong opinion without breaking a friendship."),
            ("Parlare di famiglia","Family talk — the mother-in-law joke, the cousin gossip, the Sunday lunch."),
            ("Parlare di lavoro","Work talk — complaining, bragging, gossiping about the boss."),
            ("Parlare di soldi","Money talk — Italy's ambiguity around money. What is said and what is meant."),
            ("Parlare di amore","Love talk — flirting, breaking up, staying friends. The vocabulary of the heart."),
            ("Metà strada","Full midpoint conversation lab — 30-minute unstructured chat with the teacher."),
            ("Il pettegolezzo","Gossip Italian — the register, the euphemisms, the raised eyebrow."),
            ("La lamentela","The Italian art of complaining — bureaucratic, personal, existential."),
            ("Il consiglio","Giving advice in Italian — what to say, what to never say."),
            ("La discussione","Real disagreement — how to argue and still finish the meal together."),
            ("La riconciliazione","Making up in Italian — the words, the gestures, the coffee that follows."),
            ("Il monologo comico","Stand-up Italian — analyzing a comedian's routine and trying one yourself."),
            ("Il talk show","Watching a real Italian talk show together. Register, interrupting, humour."),
            ("Il podcast","Listening to a real Italian podcast, then discussing it in Italian for 40 minutes."),
            ("L'intervista","Being interviewed and interviewing — a full role-play in Italian."),
            ("Arrivederci — al livello B1","Final CEFR B1 oral assessment, graduation ceremony, path to advanced study."),
        ],
    },
    # ---- 3 Capsule Culturali ----
    "cap-food": {
        "code":"CAP · 01","title":"La Cucina — The Language of the Italian Table","tag":"Capsule Culturale · La Cucina","cefr":"Cultural · Any level","hours":"6 sessions × 60 min",
        "hero_image":"assets/img/cap-food.jpg","city":"All of Italy",
        "promise":"Six live cultural sessions on the vocabulary and history of the Italian table — pasta, pane, vino, caffè, and the sacred rituals of the family meal.",
        "outcomes":[
            "Read any Italian recipe with confidence",
            "Understand a regional Italian menu at a glance",
            "Talk knowledgeably about pasta shape, sauce and region",
            "Discuss the history of Italian coffee, wine and olive oil",
            "Understand the ritual grammar of the Italian Sunday lunch",
            "Order, cook and discuss food in Italian at a cultured level",
        ],
        "syllabus":[
            ("La geografia del cibo","How Italy's twenty regions produced twenty cuisines. The north-south axis of butter vs olive oil, rice vs pasta, wine vs beer."),
            ("La pasta — mille forme, mille storie","Four hundred pasta shapes. Why bucatini all'amatriciana can only be bucatini. The unwritten pasta rules."),
            ("Il pane e il forno","The vocabulary of bread — pane sciapo, pagnotta, michetta, focaccia. The village bakery as institution."),
            ("Il vino italiano","Twenty regions, twenty wine cultures. Reading a label, understanding DOC and DOCG, the ritual of the tasting."),
            ("Il caffè — un rito","The Italian relationship with coffee, from Trieste to Naples. The bar, the moka, the caffettiera."),
            ("Il pranzo della domenica","The most sacred meal in Italian life. Six courses, three hours, one grandmother. Cultural graduation."),
        ],
    },
    "cap-art": {
        "code":"CAP · 02","title":"L'Arte — Renaissance in the Words That Made It","tag":"Capsule Culturale · L'Arte","cefr":"Cultural · Any level","hours":"6 sessions × 60 min",
        "hero_image":"assets/img/cap-art.jpg","city":"Florence & Rome",
        "promise":"Six live cultural sessions on the Italian language of art history — from Giotto to Caravaggio — with the vocabulary that lets you read a museum wall label in the Uffizi.",
        "outcomes":[
            "Read a full Italian museum wall label without translation",
            "Understand a Uffizi or Vatican Museums audio guide",
            "Talk about painting, sculpture and architecture in Italian",
            "Grasp the terminology of the Italian Renaissance",
            "Discuss Caravaggio, Michelangelo, Raphael and Bernini in their own language",
            "Take an Italian guided tour with confidence",
        ],
        "syllabus":[
            ("Il vocabolario del dipinto","The Italian vocabulary of painting — tela, tavola, affresco, tempera, olio, sfumato, chiaroscuro."),
            ("Giotto e il Trecento","Giotto and the birth of Western perspective. The vocabulary of pre-Renaissance devotion."),
            ("Il Quattrocento — Firenze","Brunelleschi, Donatello, Botticelli. Reading Vasari on the Uffizi masters."),
            ("Il Cinquecento — Roma","Michelangelo, Raphael, Bramante. The Sistine Chapel and Saint Peter's in their own vocabulary."),
            ("Caravaggio e il Barocco","The Caravaggio revolution — luce, ombra, realismo. Reading a Bellori page."),
            ("Bernini e la Roma barocca","Bernini's Rome — Piazza Navona, Piazza San Pietro, the language of Baroque sculpture. Cultural graduation."),
        ],
    },
    "cap-opera": {
        "code":"CAP · 03","title":"L'Opera — Opera as a Second Language","tag":"Capsule Culturale · L'Opera","cefr":"Cultural · Any level","hours":"6 sessions × 60 min",
        "hero_image":"assets/img/cap-opera.jpg","city":"La Scala, Milan",
        "promise":"Six live cultural sessions on Verdi, Puccini and Rossini. Read a libretto, follow an aria, and understand why Italians still cry at La Scala.",
        "outcomes":[
            "Read a Verdi or Puccini libretto in Italian",
            "Follow an aria and grasp its meaning in real time",
            "Understand the vocabulary of opera — voci, ruoli, registri, ripiene",
            "Talk about opera history from the Camerata to Verismo",
            "Attend a live opera and understand the plot without subtitles",
            "Discuss a performance in Italian with a fellow enthusiast",
        ],
        "syllabus":[
            ("La nascita dell'opera","Florence, 1600 — the Camerata de' Bardi and the invention of opera. Vocabulary of stagecraft."),
            ("Rossini — il Barbiere di Siviglia","Reading and singing along to Largo al factotum. Comic opera vocabulary."),
            ("Verdi — La Traviata","Reading Libiamo ne' lieti calici. Verdi as national poet."),
            ("Verdi — Aida e Nabucco","The political operas. Va, pensiero as second national anthem."),
            ("Puccini — La Bohème","Reading Che gelida manina. The verismo revolution and the vocabulary of Parisian bohemia."),
            ("Puccini — Turandot","Reading Nessun dorma. The final Puccini opera and its cultural afterlife. Cultural graduation."),
        ],
    },
}

# ---------- COURSE PAGE TEMPLATE ----------
def course_page(course_id, c, subfolder="courses"):
    rel = "../../"
    hero_img = c["hero_image"]
    body = f"""
<section class="hero" style="min-height:78vh">
  <div class="hero-bg"><img src="{rel}{hero_img}" alt="{c['title']} in {c['city']}"></div>
  <div class="hero-content">
    <div style="max-width:64ch">
      <p class="hero-tag">{c['tag']} · {c['cefr']}</p>
      <h1>{c['title']}</h1>
      <p class="hero-sub">{c['promise']}</p>
      <div class="hero-ctas">
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
        <a class="btn btn-3d btn-3d-ghost" href="#syllabus">See the Syllabus</a>
        <a class="btn btn-3d btn-3d-ghost" href="{rel}pdf/{course_id}-syllabus.pdf" download>Download PDF</a>
      </div>
    </div>
  </div>
</section>

<section class="section-cream" style="padding:0">
  <div class="wrap" style="padding-top:2rem;padding-bottom:2rem">
    <div class="proof-row">
      <div class="proof-item"><div class="pi-num">{c['hours'].split()[0]}</div><div class="pi-label">Live Lessons</div></div>
      <div class="proof-item"><div class="pi-num">85</div><div class="pi-label">Minutes Each Class</div></div>
      <div class="proof-item"><div class="pi-num">10–12</div><div class="pi-label">Learners per Group</div></div>
      <div class="proof-item"><div class="pi-num">{c['cefr'].split()[-1]}</div><div class="pi-label">CEFR Level on Completion</div></div>
    </div>
  </div>
</section>

<section class="section-paper">
  <div class="wrap-narrow">
    <div class="section-head reveal">
      <span class="eyebrow eyebrow-line">The Promise</span>
      <h2 class="display-md">By the end of {c['title']}, you can:</h2>
    </div>
    <ul class="cc-includes reveal" style="font-size:1.15rem;color:var(--on-light)">
      {"".join(f"<li>{o}</li>" for o in c['outcomes'])}
    </ul>
  </div>
</section>

<section class="section-dark" id="syllabus">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow eyebrow-line">The Syllabus · Week by Week</span>
      <h2 class="display-md">{len(c['syllabus'])} lessons, {c['hours'].split()[0]} weeks, one continuous arc.</h2>
      <p class="lead" style="color:var(--on-dark-soft)">A CEFR-aligned syllabus designed by Italian language specialists. Each lesson is a live 85-minute event set in a specific Italian cultural context.</p>
    </div>
    <div class="syllabus-list">
      {"".join(f'<div class="syl-row reveal"><div class="syl-num">{i+1:02d}</div><div class="syl-topic"><small>Lesson {i+1:02d}</small>{t}</div><div class="syl-grammar">{g}</div></div>' for i,(t,g) in enumerate(c['syllabus']))}
    </div>
    <div class="text-center mt-4"><a class="btn btn-3d btn-3d-primary" href="{rel}pdf/{course_id}-syllabus.pdf" download>Download the Full Syllabus PDF</a></div>
  </div>
</section>

<section class="section-cream">
  <div class="wrap-narrow text-center">
    <p class="big-quote reveal">Twenty lessons that change the way you speak, listen and think in Italian.</p>
  </div>
</section>

<section class="section-paper">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow eyebrow-line">Ready to begin?</span>
      <h2 class="display-md">Speak with a Club Italia advisor.</h2>
      <p class="lead">A free 15-minute placement call. No obligation. You leave with a clear plan.</p>
    </div>
    <div class="text-center"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button></div>
  </div>
</section>
"""
    out = ROOT / f"pages/{subfolder}/{course_id}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(f"{c['title']} — Club Italia by eTeacher", c['promise'][:155], body, rel=rel))
    print(f"wrote {out}")

# Build course pages
for cid in ["ci1","ci2","ci3","ci4"]: course_page(cid, COURSES[cid], "courses")
for cid in ["ps1","ps2","ps3","ps4"]: course_page(cid, COURSES[cid], "spoken")
for cid in ["cap-food","cap-art","cap-opera"]: course_page(cid, COURSES[cid], "culture")

# Save JSON for other tooling
Path(ROOT/"research/course-data.json").write_text(json.dumps(COURSES, indent=2))
print("Wrote all 11 course pages.")
