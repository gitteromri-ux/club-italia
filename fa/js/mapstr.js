/* ============================================================
   MAPSTR ENGINE, REAL interactive map of France (MapLibre GL JS)
   Club Italia by eTeacher · dark-navy + gold luxury styling

   Self-contained: renders a genuine MapLibre raster map of France
   (CARTO dark-matter tiles, no API key), luxury numbered gold journey
   markers at REAL geographic coordinates, an animated gold route line,
   three FA journeys as toggle tabs, a glass info panel per stop, and a
   legend. Auto-mounts into the first #mapstr-mount on DOM ready.

   Public API:
     window.Mapstr.mount(target)   // selector or Element; default '#mapstr-mount'
     window.Mapstr.data            // the course/journey dataset
     returns { root, setJourney(id), openStop(id), closePanel() }
   ============================================================ */
(function () {
  'use strict';

  /* ---------- DATA (embedded from data/courses_geo.json) ---------- */
  var DATA = {"tagline": "Italian is learned where it is lived: at the bar, at the market, on the piazza, on the quay.", "courses": [{"id": "ci1", "name": "CI Principiante", "level": "A0 to A1.1", "shortLevel": "A0", "region": "Roma", "href": "pages/courses/ci1.html", "color": "#C8A96B", "routeColor": "#C8A96B", "description": "Your first Italian, taught in Rome, the city where the language began.", "pins": [{"id": "colosseo", "city": "Roma, Colosseo", "lat": 41.8902, "lng": 12.4922, "location": "Colosseo and the Roman Forum", "image": "assets/img/city-roma.jpg", "credit": "", "photoSrc": "", "units": [{"num": 1, "fr": "Ciao, Roma!", "en": "The Italian sound system, greetings, subject pronouns, the verb essere. Set at Fiumicino, first steps in Rome."}, {"num": 2, "fr": "Chi sei?", "en": "Introducing yourself, nationalities, avere, definite articles. A dialogue at a Roman café."}, {"num": 3, "fr": "La mia famiglia", "en": "Family vocabulary, possessive adjectives, plural nouns. Photos from a real Roman family."}, {"num": 4, "fr": "Al bar", "en": "Ordering coffee, present tense of regular verbs (-are), c'è / ci sono. The espresso ritual."}]}, {"id": "trevi", "city": "Roma, Fontana di Trevi", "lat": 41.9009, "lng": 12.4833, "location": "Fontana di Trevi, rione Trevi", "image": "assets/img/ag-roma-statue-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 5, "fr": "In città", "en": "Prepositions of place, andare and venire, asking for directions. The seven hills of Rome."}, {"num": 6, "fr": "A che ora?", "en": "Telling time, days of the week, months, the verb fare. A day in the life of a Roman."}, {"num": 7, "fr": "A tavola", "en": "Food vocabulary, partitives, quanto costa, ordering in a trattoria. Cucina romana."}, {"num": 8, "fr": "Mi piace", "en": "Piacere, opinions, comparatives, likes and dislikes. Italian film and music."}]}, {"id": "navona", "city": "Roma, Piazza Navona", "lat": 41.8992, "lng": 12.4731, "location": "Piazza Navona, rione Parione", "image": "assets/img/roma-piazza-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 9, "fr": "Che tempo fa?", "en": "Weather, seasons, dovere / potere / volere. Weekends in the Roman countryside."}, {"num": 10, "fr": "A casa", "en": "Rooms of the house, furniture, dare and stare. Roman apartment life."}, {"num": 11, "fr": "Vestiti", "en": "Clothes, colours, adjectives that agree, sapere vs conoscere. Via del Corso, the shopping street."}, {"num": 12, "fr": "Al mercato", "en": "Food shopping, markets, imperative for polite requests. Campo de' Fiori."}]}, {"id": "trastevere", "city": "Roma, Trastevere", "lat": 41.8897, "lng": 12.47, "location": "The lanes of Trastevere", "image": "assets/img/life-caffe-roma.jpg", "credit": "", "photoSrc": "", "units": [{"num": 13, "fr": "In ufficio", "en": "Work vocabulary, jobs, telefonare, scrivere. A day in a Roman office."}, {"num": 14, "fr": "In viaggio", "en": "Trains, tickets, hotels, the near future with andare a + infinitive. Termini Station."}, {"num": 15, "fr": "A che punto sei?", "en": "Review, mini test, oral presentation. Half-way milestone."}, {"num": 16, "fr": "Passato prossimo", "en": "Introduction to the past tense with avere. Yesterday in Rome."}]}, {"id": "sanpietro", "city": "Roma, San Pietro", "lat": 41.9022, "lng": 12.4539, "location": "Basilica di San Pietro and Prati", "image": "assets/img/ag-rome-basilica-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 17, "fr": "Passato prossimo con essere", "en": "The past with essere, agreement of the past participle. Stories from a Sunday."}, {"num": 18, "fr": "Il mio quartiere", "en": "Describing places, reflexive verbs, daily routine. Trastevere on a Saturday."}, {"num": 19, "fr": "Il fine settimana", "en": "Weekend plans, imperfetto introduced, contrastive with passato. A country outing."}, {"num": 20, "fr": "Arrivederci, Roma!", "en": "Full oral CEFR A1.1 assessment, farewell dialogue, next steps. Ready for CI Elementare."}]}], "routeOrder": ["colosseo", "trevi", "navona", "trastevere", "sanpietro"]}, {"id": "ci2", "name": "CI Elementare", "level": "A1.1 to A1.2", "shortLevel": "A1.1", "region": "Firenze", "href": "pages/courses/ci2.html", "color": "#E8A87C", "routeColor": "#E8A87C", "description": "Everyday Italian from Florence, the city where the language was standardised.", "pins": [{"id": "duomo-fi", "city": "Firenze, Duomo", "lat": 43.7731, "lng": 11.256, "location": "Cattedrale di Santa Maria del Fiore", "image": "assets/img/city-firenze.jpg", "credit": "", "photoSrc": "", "units": [{"num": 1, "fr": "Firenze, culla della lingua", "en": "Why Italian is Tuscan. Dante, Boccaccio, Petrarch. Review of A1.1."}, {"num": 2, "fr": "Ricordi d'estate", "en": "Passato prossimo consolidation, time markers (ieri, la settimana scorsa)."}, {"num": 3, "fr": "Da piccolo", "en": "Imperfetto for description and habit, comparison with passato prossimo."}, {"num": 4, "fr": "Le persone", "en": "Describing people physically and in character. Adjective agreement in depth."}, {"num": 5, "fr": "A casa mia", "en": "Rooms, prepositions of place, ci per luogo. A Florentine apartment tour."}]}, {"id": "pontevecchio", "city": "Firenze, Ponte Vecchio", "lat": 43.768, "lng": 11.2531, "location": "Ponte Vecchio on the Arno", "image": "assets/img/firenze-arno-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 6, "fr": "Nella cucina toscana", "en": "Regional food vocabulary, ne partitivo, cooking verbs. Ribollita, bistecca, cantucci."}, {"num": 7, "fr": "Al ristorante", "en": "Full dining dialogue, complaining politely, tipping, il conto per favore."}, {"num": 8, "fr": "Fare la spesa", "en": "Weights, containers, packaging. Mercato Centrale."}, {"num": 9, "fr": "Al telefono", "en": "Phone conventions, formal register, leaving a message."}, {"num": 10, "fr": "Prendo appuntamento", "en": "Making appointments, doctor, hairdresser, notary. The Italian bureaucratic register."}]}, {"id": "mercato-fi", "city": "Firenze, Mercato Centrale", "lat": 43.7764, "lng": 11.2532, "location": "Mercato Centrale, San Lorenzo", "image": "assets/img/ag-market-produce-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 11, "fr": "Il corpo umano", "en": "Body vocabulary, at the pharmacy, common ailments, mi fa male + body part."}, {"num": 12, "fr": "Vestirsi", "en": "Reflexive verbs, morning routine, adverbs of frequency."}, {"num": 13, "fr": "Il tempo libero", "en": "Hobbies, sport, Serie A football, Sunday papers."}, {"num": 14, "fr": "Cinema italiano", "en": "Fellini and Sorrentino, film vocabulary, expressing opinion."}, {"num": 15, "fr": "A metà strada", "en": "Midpoint review, oral test, cultural quiz on Florence."}]}, {"id": "sangimignano", "city": "San Gimignano", "lat": 43.4677, "lng": 11.0432, "location": "The towers of San Gimignano", "image": "assets/img/ag-san-gimignano-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 16, "fr": "Il futuro", "en": "Simple future tense, plans, promises, predictions."}, {"num": 17, "fr": "Se… allora", "en": "Introduction to hypothetical: se + present / future, se + imperfetto / condizionale (light touch)."}, {"num": 18, "fr": "Il condizionale", "en": "Condizionale for polite requests and wishes: vorrei, mi piacerebbe, potrei."}, {"num": 19, "fr": "Scrivere una mail", "en": "Email conventions, formal vs informal register, greetings and sign-offs."}, {"num": 20, "fr": "A presto, Firenze!", "en": "CEFR A1.2 full assessment, cultural presentation, path to CI Intermedio."}]}], "routeOrder": ["duomo-fi", "pontevecchio", "mercato-fi", "sangimignano"]}, {"id": "ci3", "name": "CI Intermedio", "level": "A1.2 to A2.1", "shortLevel": "A1.2", "region": "Bologna", "href": "pages/courses/ci3.html", "color": "#D4A574", "routeColor": "#D4A574", "description": "Confident daily Italian from Bologna, la Dotta, la Grassa, la Rossa.", "pins": [{"id": "maggiore", "city": "Bologna, Piazza Maggiore", "lat": 44.4938, "lng": 11.343, "location": "Piazza Maggiore and San Petronio", "image": "assets/img/city-bologna.jpg", "credit": "", "photoSrc": "", "units": [{"num": 1, "fr": "Bologna la dotta", "en": "Italy's oldest university, the arcades, the food. Review of A1.2."}, {"num": 2, "fr": "Passato remoto in the wild", "en": "Recognising passato remoto in fairy tales and news. Passive knowledge only."}, {"num": 3, "fr": "Trapassato prossimo", "en": "Talking about what happened before what happened. Storytelling structure."}, {"num": 4, "fr": "Imperfetto vs passato prossimo", "en": "The Italian storytelling engine. Real narratives from a Bolognese childhood."}, {"num": 5, "fr": "La cucina emiliana", "en": "Ragù, tortellini, mortadella, Parmigiano. Cooking verbs and cultural vocabulary."}, {"num": 6, "fr": "A tavola con gli amici", "en": "Dinner-party Italian. Interrupting politely, agreeing, disagreeing, refilling wine."}]}, {"id": "quadrilatero", "city": "Bologna, Quadrilatero", "lat": 44.493, "lng": 11.3455, "location": "The market lanes of the Quadrilatero", "image": "assets/img/life-market-bologna.jpg", "credit": "", "photoSrc": "", "units": [{"num": 7, "fr": "Ho un'opinione", "en": "Expressing opinion: penso che, credo che, secondo me. Congiuntivo introduced softly."}, {"num": 8, "fr": "Il mio quartiere", "en": "Comparing places: più / meno / così… come. Bologna vs Milano vs Roma."}, {"num": 9, "fr": "Andiamo al cinema", "en": "Reserving tickets, film genres, describing a plot, recommending."}, {"num": 10, "fr": "La musica italiana", "en": "Lucio Dalla, Battisti, De Andrè, contemporary indie. Listening lab."}, {"num": 11, "fr": "A metà del cammino", "en": "Midpoint oral assessment, cultural presentation."}, {"num": 12, "fr": "Se dovessi scegliere", "en": "Hypothetical in the present: se + congiuntivo imperfetto + condizionale."}]}, {"id": "portici", "city": "Bologna, i portici", "lat": 44.4943, "lng": 11.3466, "location": "The porticoes near the Due Torri", "image": "assets/img/bologna-portici-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 13, "fr": "Le città italiane", "en": "Describing Italian cities, geography, north / centre / south differences."}, {"num": 14, "fr": "Il lavoro in Italia", "en": "Vocabulary of work, CV, colloquio di lavoro, contratti."}, {"num": 15, "fr": "La sanità", "en": "Healthcare vocabulary, at the doctor, at the hospital, the Italian public system."}, {"num": 16, "fr": "La banca", "en": "Bank vocabulary, opening an account, paying bills, ordering online."}, {"num": 17, "fr": "La casa in affitto", "en": "Renting an apartment, understanding a contract, negotiating with a landlord."}, {"num": 18, "fr": "Feste italiane", "en": "Italian holidays: Natale, Pasqua, Ferragosto, Palio di Siena, Carnevale di Venezia."}, {"num": 19, "fr": "Il dialetto", "en": "Introduction to Italian dialects, bolognese, romanesco, napoletano, siciliano, as cultural heritage."}, {"num": 20, "fr": "Arrivederci, Bologna!", "en": "Full CEFR A2.1 assessment, oral presentation, path to CI Avanzato."}]}], "routeOrder": ["maggiore", "quadrilatero", "portici"]}, {"id": "ci4", "name": "CI Avanzato", "level": "A2.1 to A2.2", "shortLevel": "A2.1", "region": "Napoli e Palermo", "href": "pages/courses/ci4.html", "color": "#9DB08A", "routeColor": "#9DB08A", "description": "Real Italian for real life, between the warmth of Naples and the sharpness of Milan.", "pins": [{"id": "spaccanapoli", "city": "Napoli, Spaccanapoli", "lat": 40.849, "lng": 14.256, "location": "Spaccanapoli, centro storico", "image": "assets/img/city-napoli.jpg", "credit": "", "photoSrc": "", "units": [{"num": 1, "fr": "Napoli e Milano, due Italie", "en": "The northern-southern axis of Italian identity. Review of A2.1."}, {"num": 2, "fr": "Congiuntivo presente", "en": "Full introduction to the subjunctive: after verbs of opinion, doubt, feeling."}, {"num": 3, "fr": "Congiuntivo imperfetto", "en": "Backshift, hypothetical use, se + imperfetto + condizionale."}, {"num": 4, "fr": "Discorso indiretto", "en": "Reported speech: he said that…, she asked whether…"}, {"num": 5, "fr": "La stampa italiana", "en": "Reading Corriere della Sera and la Repubblica. Newspaper Italian."}]}, {"id": "lungomare", "city": "Napoli, Lungomare", "lat": 40.832, "lng": 14.244, "location": "The seafront at Via Caracciolo", "image": "assets/img/napoli-mare-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 6, "fr": "Il cinema italiano", "en": "Full film analysis: La Grande Bellezza, La Vita è Bella, Il Postino."}, {"num": 7, "fr": "Opera in italiano", "en": "Understanding a Verdi libretto. Aria listening lab."}, {"num": 8, "fr": "Business Italian", "en": "Meeting vocabulary, presenting, negotiating, closing a deal."}, {"num": 9, "fr": "La politica italiana", "en": "Institutions, parties, elections, the vocabulary of civic life."}, {"num": 10, "fr": "Metà strada", "en": "Full midpoint oral, written and listening assessment."}]}, {"id": "amalfi", "city": "Costiera Amalfitana", "lat": 40.634, "lng": 14.6027, "location": "The Amalfi coast", "image": "assets/img/life-amalfi-coast.jpg", "credit": "", "photoSrc": "", "units": [{"num": 11, "fr": "Argomentare", "en": "Debating in Italian. Structured arguments, giving and refuting points."}, {"num": 12, "fr": "Persuadere", "en": "The language of sales, marketing and advertising. Rhetorical devices."}, {"num": 13, "fr": "Napoli, la lingua della strada", "en": "Napoletano expressions that entered standard Italian. Neapolitan cinema."}, {"num": 14, "fr": "Milano, la lingua degli affari", "en": "Milanese business register, aperitivo culture, fashion vocabulary."}, {"num": 15, "fr": "La letteratura contemporanea", "en": "Ferrante, Calvino, Baricco, reading passages and discussion."}]}, {"id": "palermo", "city": "Palermo, centro storico", "lat": 38.1157, "lng": 13.3615, "location": "Quattro Canti and the old markets", "image": "assets/img/city-palermo.jpg", "credit": "", "photoSrc": "", "units": [{"num": 16, "fr": "La cucina regionale", "en": "Twenty regions, twenty cuisines, a culinary tour of Italy."}, {"num": 17, "fr": "Il sistema scolastico", "en": "Italian education from elementari to università, plus the language of academia."}, {"num": 18, "fr": "Vivere in Italia", "en": "Practical language for moving to Italy: codice fiscale, permesso di soggiorno, sanità."}, {"num": 19, "fr": "Cittadinanza italiana", "en": "The language of jure sanguinis, applications, consular Italian."}, {"num": 20, "fr": "Arrivederci, a presto, in Italia!", "en": "Full CEFR A2.2 assessment, cultural graduation, path to B1."}]}], "routeOrder": ["spaccanapoli", "lungomare", "amalfi", "palermo"]}, {"id": "ps3", "name": "In Viaggio", "level": "Spoken A2", "shortLevel": "Spoken", "region": "Venezia", "href": "pages/spoken/ps3.html", "color": "#B5607A", "routeColor": "#B5607A", "description": "Twenty live conversation sessions for people who actually travel Italy, trains, hotels, museums, mountain refuges, sailing the Amalfi coast..", "pins": [{"id": "rialto", "city": "Venezia, Rialto", "lat": 45.438, "lng": 12.3359, "location": "Ponte di Rialto and the market", "image": "assets/img/city-venezia.jpg", "credit": "", "photoSrc": "", "units": [{"num": 1, "fr": "Alla stazione", "en": "Buying a ticket at Termini, Trenitalia vs Italo, first vs second class."}, {"num": 2, "fr": "In treno", "en": "Italian train vocabulary. Coincidence, ritardo, il capotreno."}, {"num": 3, "fr": "All'aeroporto", "en": "Check-in, security, boarding, delays, Italian airport register."}, {"num": 4, "fr": "In taxi", "en": "Taxi Italian, meter, tipping, negotiating an out-of-town ride."}, {"num": 5, "fr": "In albergo", "en": "Hotel check-in and check-out. Requesting a room change, room service, breakfast."}, {"num": 6, "fr": "Al B&B", "en": "Bed & breakfast Italian, meeting the host, house rules, breakfast conversations."}]}, {"id": "sanmarco", "city": "Venezia, San Marco", "lat": 45.4341, "lng": 12.3388, "location": "Piazza San Marco", "image": "assets/img/ag-venice-gondola-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 7, "fr": "In Airbnb", "en": "Renting a private apartment, codes, keys, house manuals, neighbour relations."}, {"num": 8, "fr": "Al museo", "en": "Museum Italian, audio guide, guided tour, understanding a wall label."}, {"num": 9, "fr": "Alla mostra", "en": "Exhibition Italian, talking to a curator, buying the catalogue, opinion."}, {"num": 10, "fr": "Metà strada", "en": "Midpoint full oral assessment set on a virtual Italian trip."}, {"num": 11, "fr": "In farmacia", "en": "Pharmacy Italian, describing symptoms, over-the-counter medicine, prescriptions."}, {"num": 12, "fr": "Dal medico", "en": "At the doctor, the appointment, the visit, the referral."}]}, {"id": "cannaregio", "city": "Venezia, Cannaregio", "lat": 45.4445, "lng": 12.329, "location": "Canals of Cannaregio", "image": "assets/img/life-gondola-venezia.jpg", "credit": "", "photoSrc": "", "units": [{"num": 13, "fr": "Al pronto soccorso", "en": "Emergency room Italian, the codes, the triage, the paperwork."}, {"num": 14, "fr": "In banca", "en": "Bank Italian, changing money, opening an account, ATM problems."}, {"num": 15, "fr": "Alla posta", "en": "Post office Italian, sending a package, paying a bill, buying stamps."}, {"num": 16, "fr": "Al ristorante in autostrada", "en": "Autogrill Italian, the fast lunch on the motorway, ordering at the counter."}, {"num": 17, "fr": "In montagna", "en": "Mountain Italian, rifugio, sentiero, guida alpina, mal di montagna."}, {"num": 18, "fr": "Al mare", "en": "Beach Italian, lettino, ombrellone, bagnino, cabina."}, {"num": 19, "fr": "In città", "en": "Urban Italian, public transport, ZTL, parking, the metro in Rome, Milan, Naples."}, {"num": 20, "fr": "Arrivederci, e buon viaggio", "en": "Final oral, cultural graduation, path to Chiacchierando."}]}], "routeOrder": ["rialto", "sanmarco", "cannaregio"]}, {"id": "ps4", "name": "Chiacchierando", "level": "Spoken A2 to B1", "shortLevel": "Spoken", "region": "Milano", "href": "pages/spoken/ps4.html", "color": "#8B7BB5", "routeColor": "#8B7BB5", "description": "Twenty live conversation sessions on the four things Italians actually do all day: opinion, humour, disagreement and storytelling.", "pins": [{"id": "duomo-mi", "city": "Milano, Duomo", "lat": 45.4642, "lng": 9.19, "location": "Duomo di Milano", "image": "assets/img/city-milano.jpg", "credit": "", "photoSrc": "", "units": [{"num": 1, "fr": "Chiacchierare, l'arte italiana", "en": "What chiacchierare really means. The philosophy of unhurried talk."}, {"num": 2, "fr": "Raccontare una storia", "en": "Storytelling structure, introduction, complication, punchline. Italian narrative style."}, {"num": 3, "fr": "Fare una battuta", "en": "Italian humour, the setup, the beat, the payoff. Regional humour."}, {"num": 4, "fr": "Discutere di calcio", "en": "Football arguments. Fifteen minutes on Juve vs Milan and no one leaves offended."}, {"num": 5, "fr": "Discutere di politica", "en": "Political conversation, how to hold a strong opinion without breaking a friendship."}, {"num": 6, "fr": "Parlare di famiglia", "en": "Family talk, the mother-in-law joke, the cousin gossip, the Sunday lunch."}, {"num": 7, "fr": "Parlare di lavoro", "en": "Work talk, complaining, bragging, gossiping about the boss."}, {"num": 8, "fr": "Parlare di soldi", "en": "Money talk, Italy's ambiguity around money. What is said and what is meant."}, {"num": 9, "fr": "Parlare di amore", "en": "Love talk, flirting, breaking up, staying friends. The vocabulary of the heart."}, {"num": 10, "fr": "Metà strada", "en": "Full midpoint conversation lab, 30-minute unstructured chat with the teacher."}]}, {"id": "scala", "city": "Milano, Teatro alla Scala", "lat": 45.4674, "lng": 9.1895, "location": "Teatro alla Scala", "image": "assets/img/opera-scala-poster.jpg", "credit": "Footage still: Artgrid, licensed", "photoSrc": "", "units": [{"num": 11, "fr": "Il pettegolezzo", "en": "Gossip Italian, the register, the euphemisms, the raised eyebrow."}, {"num": 12, "fr": "La lamentela", "en": "The Italian art of complaining, bureaucratic, personal, existential."}, {"num": 13, "fr": "Il consiglio", "en": "Giving advice in Italian, what to say, what to never say."}, {"num": 14, "fr": "La discussione", "en": "Real disagreement, how to argue and still finish the meal together."}, {"num": 15, "fr": "La riconciliazione", "en": "Making up in Italian, the words, the gestures, the coffee that follows."}, {"num": 16, "fr": "Il monologo comico", "en": "Stand-up Italian, analyzing a comedian's routine and trying one yourself."}, {"num": 17, "fr": "Il talk show", "en": "Watching a real Italian talk show together. Register, interrupting, humour."}, {"num": 18, "fr": "Il podcast", "en": "Listening to a real Italian podcast, then discussing it in Italian for 40 minutes."}, {"num": 19, "fr": "L'intervista", "en": "Being interviewed and interviewing, a full role-play in Italian."}, {"num": 20, "fr": "Arrivederci, al livello B1", "en": "Final CEFR B1 oral assessment, graduation ceremony, path to advanced study."}]}], "routeOrder": ["duomo-mi", "scala"]}]};
  /* ---------- CONFIG ---------- */
  var GOLD = '#C8A96B';
  // CARTO "dark-matter" raster, the brand's dark-navy luxury basemap.
  // (Reverted from voyager per user; keeps the premium night-map look
  //  with gold journey markers reading cleanly on a dark canvas.)
  var DARK_TILES = [
    'https://a.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}{r}.png',
    'https://b.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}{r}.png',
    'https://c.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}{r}.png',
    'https://d.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}{r}.png'
  ];
  var ATTRIB = '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors © <a href="https://openfreemap.org" target="_blank" rel="noopener">OpenFreeMap</a> © <a href="https://www.openmaptiles.org/" target="_blank" rel="noopener">OpenMapTiles</a>';
  var FRANCE_CENTER = [12.6, 42.0];
  var FRANCE_ZOOM = 5.0;
  var MAP_PITCH = 40;   // subtle 3D tilt for depth
  var MAP_BEARING = 0;  // no rotation, keeps the frame clean, tiles fully cover

  /* ---------- HELPERS ---------- */
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function courseById(id) {
    for (var i = 0; i < DATA.courses.length; i++) if (DATA.courses[i].id === id) return DATA.courses[i];
    return DATA.courses[0];
  }
  function pinById(course, id) {
    for (var i = 0; i < course.pins.length; i++) if (course.pins[i].id === id) return course.pins[i];
    return null;
  }
  function orderedPins(course) {
    return course.routeOrder.map(function (id) { return pinById(course, id); }).filter(Boolean);
  }

  /* ---------- ALL-JOURNEYS aggregate (every place across all 6 courses) ----------
     A synthetic "course" used by the master map mode. It collects every unique
     pin across all courses (dedup by rounded lat/lng so the same physical place
     shared between courses appears once) and remembers which course each pin
     belongs to, so a click still opens the correct lesson + course CTA. */
  var ALL_ID = '__all__';
  function buildAllCourse() {
    var seen = {}, pins = [], order = [];
    DATA.courses.forEach(function (c) {
      orderedPins(c).forEach(function (p) {
        var key = p.lat.toFixed(3) + ',' + p.lng.toFixed(3);
        if (seen[key]) return;
        seen[key] = true;
        var clone = {
          id: p.id, city: p.city, lat: p.lat, lng: p.lng, location: p.location,
          image: p.image, credit: p.credit, photoSrc: p.photoSrc, units: p.units,
          _ownerId: c.id, _ownerName: c.name, _ownerLevel: c.level, _ownerHref: c.href,
          _ownerColor: c.color
        };
        pins.push(clone);
        order.push(p.id + '@' + c.id);
      });
    });
    return {
      id: ALL_ID, name: 'All Journeys', level: 'Every city of Italy',
      shortLevel: 'ALL', region: 'Every city & region', href: 'courses.html',
      color: '#E8C77A', routeColor: '#E8C77A',
      description: 'Every place Club Italia teaches, across six courses.',
      pins: pins, routeOrder: order, isAll: true
    };
  }
  var ALL_COURSE = buildAllCourse();
  function courseByIdX(id) { return id === ALL_ID ? ALL_COURSE : courseById(id); }
  function pinByIdX(course, id) {
    // "all" routeOrder ids are "pinId@courseId"; match on the leading pinId
    if (course.isAll) {
      var pid = id.split('@')[0];
      for (var i = 0; i < course.pins.length; i++) if (course.pins[i].id === pid) return course.pins[i];
      return null;
    }
    return pinById(course, id);
  }
  function orderedPinsX(course) {
    if (course.isAll) return course.pins.slice();
    return orderedPins(course);
  }

  /* ============================================================
     MOUNT
     ============================================================ */
  function mount(target) {
    var root = typeof target === 'string' ? document.querySelector(target)
      : (target || document.querySelector('#mapstr-mount'));
    if (!root) return null;
    if (root.getAttribute('data-mapstr-ready') === '1') return null;
    root.setAttribute('data-mapstr-ready', '1');

    var compact = root.hasAttribute('data-compact') || root.closest('#mapstr') != null && document.body.classList.contains('home');
    // Homepage uses #mapstr wrapper section; treat that as compact unless on map.html
    var isMapPage = /map\.html$/.test(location.pathname) || document.querySelector('.map-hero') != null;
    compact = !isMapPage;

    root.classList.add('ms-root');
    if (compact) root.classList.add('ms-compact');

    /* ----- Scaffold ----- */
    root.innerHTML = '';

    var shell = el('div', 'ms-shell');
    root.appendChild(shell);

    // Header (eyebrow + title + tagline)
    var head = el('div', 'ms-head');
    head.innerHTML =
      '<span class="ms-eyebrow">Interactive map of Italy</span>' +
      '<h2 class="ms-title">Follow your <span class="ms-ital">journey</span> across Italy</h2>' +
      '<p class="ms-tagline">' + esc(DATA.tagline) + '</p>';
    shell.appendChild(head);

    // Tabs
    var tabs = el('div', 'ms-tabs');
    tabs.setAttribute('role', 'tablist');
    // "All Journeys" master tab first, the whole map of France across every course.
    (function () {
      var ta = el('button', 'ms-tab ms-tab-all', '');
      ta.type = 'button';
      ta.setAttribute('role', 'tab');
      ta.dataset.course = ALL_ID;
      var allCourse = courseByIdX(ALL_ID);
      var placeCount = (allCourse && allCourse.routeOrder) ? allCourse.routeOrder.length : 72;
      var journeyCount = DATA.courses.length;
      ta.innerHTML = '<span class="ms-tab-all-mark" aria-hidden="true">' +
          '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">' +
          '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.4 2.6 15.6 0 18M12 3c-2.6 2.4-2.6 15.6 0 18"/></svg></span>' +
        '<span class="ms-tab-text">' +
          '<span class="ms-tab-level">The complete atlas</span>' +
          '<span class="ms-tab-name">All Journeys</span>' +
          '<span class="ms-tab-region">Every city &amp; region across all ' + journeyCount + ' courses</span>' +
        '</span>' +
        '<span class="ms-tab-all-cue" aria-hidden="true"><b>' + journeyCount + '</b>&nbsp;journeys&nbsp; · &nbsp;<b>' + placeCount + '</b>&nbsp;places</span>';
      ta.setAttribute('aria-label', 'All Journeys, every city and region across all ' + journeyCount + ' courses, ' + placeCount + ' places');
      ta.addEventListener('click', function () { setJourney(ALL_ID, true); });
      tabs.appendChild(ta);
    })();
    DATA.courses.forEach(function (c, i) {
      var t = el('button', 'ms-tab', '');
      t.type = 'button';
      t.setAttribute('role', 'tab');
      t.dataset.course = c.id;
      t.innerHTML = '<span class="ms-tab-level">' + esc(c.shortLevel) + '</span>' +
        '<span class="ms-tab-name">' + esc(c.name) + '</span>' +
        '<span class="ms-tab-region">' + esc(c.region) + '</span>';
      t.addEventListener('click', function () { setJourney(c.id, true); });
      tabs.appendChild(t);
    });
    shell.appendChild(tabs);

    // Map + panel stage
    var stage = el('div', 'ms-stage');
    var mapEl = el('div', 'ms-map');
    mapEl.id = 'ms-map-' + Math.random().toString(36).slice(2, 8);
    stage.appendChild(mapEl);

    // Legend
    var legend = el('div', 'ms-legend');
    stage.appendChild(legend);

    // Info panel (glass)
    var panel = el('aside', 'ms-panel');
    panel.setAttribute('aria-hidden', 'true');
    stage.appendChild(panel);

    // Floating real-place photo card (top-left, 3D pop on click)
    var photoPop = el('figure', 'ms-photo-pop');
    photoPop.setAttribute('aria-hidden', 'true');
    stage.appendChild(photoPop);

    shell.appendChild(stage);
    root.appendChild(shell);

    /* ----- State ----- */
    var map = null;
    var markers = [];
    var activeCourse = null;
    var ready = false;

    /* ----- MapLibre guard ----- */
    if (typeof maplibregl === 'undefined') {
      stage.classList.add('ms-noscript');
      mapEl.innerHTML = '<div class="ms-fallback"><p>The interactive map is loading…</p>' +
        '<p class="ms-fallback-sub">If it does not appear, please check your connection, the map of Italy loads from a map-tile service.</p></div>';
      // still render tabs/legend with data so structure is correct.
      // Default to the All Journeys master view, not a single course.
      buildLegend(courseByIdX(ALL_ID));
      activeCourse = courseByIdX(ALL_ID);
      tabs.children[0].classList.add('active');
      return { root: root, setJourney: function () {}, openStop: function () {}, closePanel: function () {} };
    }

    /* ----- Build map ----- */
    // Key-free vector dark basemap (OpenFreeMap), replaces CARTO raster tiles,
    // which now watermark "API KEY REQUIRED" on every tile without a paid key.
    var style = 'https://tiles.openfreemap.org/styles/dark';

    map = new maplibregl.Map({
      container: mapEl.id,
      style: style,
      center: FRANCE_CENTER,
      zoom: (window.innerWidth <= 760) ? (FRANCE_ZOOM - 0.4) : (compact ? FRANCE_ZOOM - 0.2 : FRANCE_ZOOM),
      pitch: MAP_PITCH,
      bearing: MAP_BEARING,
      minZoom: 3.8,
      maxZoom: 12,
      maxPitch: 70,
      attributionControl: false,
      cooperativeGestures: compact,
      dragRotate: true,
      pitchWithRotate: true
    });
    map.on('style.load', function () {
      try {
        map.setPaintProperty('background', 'background-color', '#00001F');
        map.setPaintProperty('water', 'fill-color', '#050A2E');
        map.setPaintProperty('landuse_park', 'fill-color', '#0B1230');
        map.setPaintProperty('landcover_wood', 'fill-color', '#0B1230');
      } catch (e) {}
    });
    map.addControl(new maplibregl.AttributionControl({ compact: true }), 'bottom-right');
    // Start with the compact attribution collapsed (MapLibre opens it by default on narrow screens)
    map.once('load', function () { document.querySelectorAll('#mapstr .maplibregl-ctrl-attrib').forEach(function (e) { e.classList.remove('maplibregl-compact-show'); }); });
    map.addControl(new maplibregl.NavigationControl({ showCompass: true, visualizePitch: true }), 'top-right');

    // Metropolitan France boundary (mainland + Corsica), used to make France
    // glow and stand out strongly within the darker Europe map.
    var FRANCE_GEO = {"type": "Feature", "properties": {}, "geometry": {"type": "MultiPolygon", "coordinates": [[[[7.021, 45.926], [7.056, 45.904], [7.129, 45.88], [7.328, 45.912], [7.452, 45.944], [7.539, 45.978], [7.593, 45.972], [7.788, 45.922], [7.852, 45.947], [7.993, 46.016], [8.014, 46.052], [8.125, 46.161], [8.127, 46.188], [8.082, 46.256], [8.096, 46.271], [8.232, 46.341], [8.299, 46.403], [8.371, 46.445], [8.423, 46.446], [8.437, 46.432], [8.443, 46.403], [8.438, 46.283], [8.458, 46.246], [8.565, 46.16], [8.642, 46.111], [8.819, 46.077], [8.827, 46.061], [8.778, 45.996], [8.885, 45.919], [8.904, 45.862], [8.954, 45.83], [9.024, 45.846], [9.047, 45.876], [9.019, 45.928], [8.999, 45.983], [9.003, 46.015], [9.022, 46.051], [9.071, 46.102], [9.203, 46.219], [9.251, 46.287], [9.26, 46.391], [9.26, 46.475], [9.304, 46.496], [9.399, 46.481], [9.428, 46.482], [9.441, 46.431], [9.481, 46.349], [9.529, 46.306], [9.58, 46.296], [9.639, 46.296], [9.788, 46.346], [9.884, 46.368], [9.939, 46.362], [9.972, 46.328], [10.041, 46.238], [10.081, 46.228], [10.128, 46.238], [10.145, 46.254], [10.13, 46.288], [10.11, 46.363], [10.082, 46.421], [10.046, 46.448], [10.038, 46.483], [10.061, 46.547], [10.087, 46.6], [10.137, 46.614], [10.196, 46.621], [10.272, 46.565], [10.363, 46.547], [10.431, 46.55], [10.442, 46.583], [10.438, 46.619], [10.398, 46.665], [10.406, 46.735], [10.453, 46.865], [10.479, 46.855], [10.58, 46.854], [10.689, 46.846], [10.76, 46.793], [10.829, 46.775], [10.927, 46.769], [10.993, 46.777], [11.025, 46.797], [11.063, 46.859], [11.134, 46.936], [11.244, 46.976], [11.433, 46.983], [11.528, 46.997], [11.625, 46.997], [11.699, 46.985], [11.776, 46.986], [11.97, 47.04], [12.169, 47.082], [12.197, 47.075], [12.201, 47.061], [12.166, 47.028], [12.131, 46.985], [12.154, 46.935], [12.268, 46.836], [12.33, 46.76], [12.388, 46.703], [12.479, 46.673], [12.599, 46.654], [12.7, 46.647], [12.806, 46.626], [13.169, 46.573], [13.352, 46.558], [13.49, 46.556], [13.7, 46.52], [13.68, 46.463], [13.637, 46.449], [13.563, 46.415], [13.479, 46.369], [13.4, 46.318], [13.378, 46.262], [13.4, 46.225], [13.421, 46.212], [13.45, 46.224], [13.492, 46.217], [13.545, 46.197], [13.633, 46.177], [13.635, 46.158], [13.617, 46.133], [13.548, 46.089], [13.486, 46.04], [13.48, 46.009], [13.488, 45.987], [13.509, 45.974], [13.601, 45.98], [13.614, 45.962], [13.57, 45.834], [13.583, 45.812], [13.663, 45.792], [13.722, 45.761], [13.831, 45.68], [13.875, 45.615], [13.845, 45.593], [13.776, 45.582], [13.72, 45.588], [13.783, 45.627], [13.628, 45.771], [13.558, 45.771], [13.465, 45.71], [13.206, 45.771], [13.157, 45.747], [13.12, 45.698], [13.03, 45.638], [12.903, 45.611], [12.761, 45.544], [12.612, 45.497], [12.498, 45.462], [12.432, 45.468], [12.536, 45.545], [12.492, 45.546], [12.354, 45.492], [12.274, 45.446], [12.249, 45.369], [12.226, 45.242], [12.286, 45.208], [12.392, 45.04], [12.523, 44.968], [12.498, 44.899], [12.464, 44.845], [12.384, 44.798], [12.319, 44.833], [12.279, 44.832], [12.248, 44.723], [12.305, 44.429], [12.396, 44.224], [12.487, 44.134], [12.691, 43.995], [12.907, 43.921], [13.295, 43.686], [13.508, 43.612], [13.564, 43.571], [13.693, 43.39], [13.805, 43.18], [13.925, 42.852], [14.01, 42.69], [14.183, 42.506], [14.541, 42.244], [14.866, 42.053], [15.169, 41.934], [15.405, 41.913], [15.964, 41.939], [16.062, 41.928], [16.165, 41.896], [16.189, 41.814], [16.151, 41.758], [16.034, 41.701], [15.914, 41.621], [15.9, 41.512], [16.013, 41.435], [16.552, 41.232], [17.103, 41.062], [17.275, 40.975], [17.474, 40.841], [17.955, 40.655], [18.036, 40.565], [18.328, 40.371], [18.461, 40.221], [18.486, 40.105], [18.423, 39.987], [18.393, 39.904], [18.344, 39.821], [18.219, 39.853], [18.078, 39.937], [17.865, 40.28], [17.476, 40.315], [17.396, 40.34], [17.258, 40.399], [17.249, 40.438], [17.215, 40.486], [17.18, 40.503], [17.031, 40.513], [16.928, 40.458], [16.807, 40.326], [16.67, 40.137], [16.53, 39.86], [16.522, 39.748], [16.598, 39.639], [16.824, 39.578], [16.999, 39.482], [17.115, 39.381], [17.123, 39.137], [17.175, 38.998], [17.099, 38.919], [16.951, 38.94], [16.755, 38.89], [16.617, 38.8], [16.559, 38.715], [16.574, 38.494], [16.546, 38.409], [16.282, 38.25], [16.144, 38.086], [16.11, 38.019], [16.057, 37.942], [15.725, 37.939], [15.646, 38.034], [15.643, 38.175], [15.7, 38.262], [15.822, 38.303], [15.905, 38.483], [15.879, 38.614], [15.927, 38.672], [15.972, 38.713], [16.066, 38.736], [16.197, 38.759], [16.21, 38.941], [16.107, 39.024], [16.071, 39.139], [16.024, 39.354], [15.854, 39.627], [15.764, 39.87], [15.693, 39.99], [15.585, 40.053], [15.391, 40.052], [15.295, 40.07], [14.951, 40.239], [14.927, 40.265], [14.929, 40.31], [14.986, 40.377], [14.948, 40.469], [14.907, 40.556], [14.84, 40.63], [14.766, 40.668], [14.611, 40.645], [14.557, 40.626], [14.459, 40.633], [14.383, 40.6], [14.34, 40.599], [14.461, 40.729], [14.428, 40.759], [14.309, 40.813], [14.147, 40.821], [14.102, 40.827], [14.076, 40.794], [14.044, 40.812], [14.048, 40.87], [13.86, 41.13], [13.733, 41.236], [13.67, 41.254], [13.555, 41.232], [13.362, 41.279], [13.247, 41.289], [13.183, 41.278], [13.089, 41.244], [13.041, 41.266], [13.024, 41.301], [12.849, 41.409], [12.631, 41.47], [12.206, 41.813], [12.075, 41.941], [11.807, 42.082], [11.637, 42.288], [11.498, 42.363], [11.296, 42.423], [11.25, 42.416], [11.189, 42.393], [11.141, 42.39], [11.103, 42.417], [11.142, 42.444], [11.185, 42.457], [11.168, 42.535], [10.938, 42.739], [10.803, 42.804], [10.765, 42.845], [10.737, 42.9], [10.708, 42.936], [10.645, 42.957], [10.59, 42.954], [10.515, 42.968], [10.517, 43.065], [10.532, 43.14], [10.521, 43.204], [10.448, 43.371], [10.321, 43.513], [10.246, 43.852], [10.188, 43.948], [10.048, 44.02], [9.731, 44.101], [9.289, 44.319], [9.196, 44.323], [8.93, 44.408], [8.766, 44.422], [8.552, 44.346], [8.292, 44.137], [8.082, 43.919], [8.005, 43.877], [7.733, 43.803], [7.493, 43.767], [7.491, 43.823], [7.482, 43.865], [7.523, 43.911], [7.59, 43.965], [7.651, 44.034], [7.677, 44.083], [7.665, 44.116], [7.637, 44.165], [7.599, 44.168], [7.371, 44.127], [7.319, 44.138], [7.149, 44.202], [6.967, 44.28], [6.9, 44.336], [6.875, 44.392], [6.894, 44.428], [6.879, 44.463], [6.843, 44.511], [6.875, 44.565], [6.932, 44.632], [6.96, 44.677], [7.008, 44.689], [7.031, 44.717], [6.993, 44.827], [6.973, 44.845], [6.94, 44.859], [6.889, 44.86], [6.801, 44.883], [6.738, 44.921], [6.725, 44.973], [6.691, 45.023], [6.635, 45.068], [6.628, 45.118], [6.692, 45.144], [6.78, 45.145], [6.842, 45.136], [6.981, 45.216], [7.032, 45.223], [7.078, 45.24], [7.117, 45.349], [7.146, 45.382], [7.153, 45.401], [7.126, 45.424], [7.014, 45.5], [6.962, 45.581], [6.881, 45.67], [6.806, 45.71], [6.791, 45.741], [6.789, 45.78], [6.804, 45.815], [6.941, 45.868], [7.021, 45.926]], [[12.439, 41.898], [12.438, 41.906], [12.431, 41.905], [12.428, 41.901], [12.431, 41.898], [12.439, 41.898]], [[12.485, 43.901], [12.515, 43.953], [12.504, 43.99], [12.441, 43.982], [12.397, 43.935], [12.426, 43.894], [12.485, 43.901]]], [[[10.395, 42.858], [10.428, 42.819], [10.432, 42.797], [10.41, 42.771], [10.419, 42.713], [10.336, 42.761], [10.209, 42.737], [10.131, 42.742], [10.11, 42.785], [10.128, 42.81], [10.248, 42.816], [10.286, 42.828], [10.359, 42.822], [10.395, 42.858]]], [[[13.938, 40.706], [13.894, 40.697], [13.868, 40.709], [13.854, 40.724], [13.871, 40.762], [13.962, 40.739], [13.961, 40.718], [13.938, 40.706]]], [[[12.051, 36.757], [12.003, 36.746], [11.941, 36.78], [11.936, 36.829], [11.948, 36.843], [12.024, 36.821], [12.048, 36.776], [12.051, 36.757]]], [[[15.577, 38.22], [15.509, 38.107], [15.476, 38.063], [15.234, 37.785], [15.207, 37.721], [15.19, 37.651], [15.165, 37.59], [15.131, 37.532], [15.1, 37.459], [15.106, 37.375], [15.117, 37.335], [15.146, 37.308], [15.194, 37.283], [15.23, 37.244], [15.174, 37.209], [15.236, 37.139], [15.289, 37.097], [15.296, 37.055], [15.295, 37.013], [15.185, 36.935], [15.142, 36.892], [15.116, 36.839], [15.104, 36.785], [15.116, 36.736], [15.113, 36.688], [15.002, 36.694], [14.89, 36.724], [14.776, 36.71], [14.614, 36.767], [14.555, 36.777], [14.502, 36.799], [14.367, 36.973], [14.259, 37.046], [14.143, 37.104], [14.024, 37.107], [13.905, 37.101], [13.801, 37.136], [13.587, 37.254], [13.361, 37.349], [13.265, 37.41], [13.221, 37.452], [13.17, 37.479], [13.04, 37.507], [12.924, 37.571], [12.871, 37.575], [12.757, 37.567], [12.699, 37.572], [12.64, 37.594], [12.527, 37.67], [12.454, 37.774], [12.436, 37.82], [12.487, 37.939], [12.548, 38.053], [12.602, 38.085], [12.664, 38.108], [12.702, 38.142], [12.734, 38.183], [12.851, 38.064], [12.903, 38.035], [12.955, 38.041], [13.049, 38.084], [13.057, 38.131], [13.16, 38.19], [13.291, 38.191], [13.352, 38.181], [13.383, 38.127], [13.433, 38.11], [13.491, 38.103], [13.682, 38.001], [13.735, 37.984], [13.789, 37.981], [13.937, 38.024], [14.05, 38.041], [14.288, 38.017], [14.416, 38.043], [14.506, 38.046], [14.637, 38.085], [14.737, 38.151], [14.79, 38.167], [14.846, 38.172], [14.982, 38.168], [15.119, 38.153], [15.176, 38.168], [15.224, 38.211], [15.28, 38.23], [15.341, 38.217], [15.499, 38.291], [15.568, 38.296], [15.635, 38.268], [15.577, 38.22]]], [[[9.632, 40.882], [9.682, 40.818], [9.794, 40.556], [9.805, 40.5], [9.783, 40.442], [9.754, 40.4], [9.643, 40.268], [9.659, 40.159], [9.701, 40.092], [9.707, 40.017], [9.686, 39.924], [9.617, 39.354], [9.584, 39.254], [9.562, 39.166], [9.486, 39.14], [9.388, 39.168], [9.264, 39.217], [9.207, 39.214], [9.149, 39.197], [9.102, 39.211], [9.056, 39.239], [9.023, 39.043], [8.967, 38.964], [8.881, 38.913], [8.801, 38.91], [8.719, 38.927], [8.649, 38.927], [8.595, 38.964], [8.553, 39.03], [8.486, 39.11], [8.418, 39.206], [8.411, 39.292], [8.399, 39.482], [8.419, 39.523], [8.447, 39.563], [8.461, 39.648], [8.451, 39.722], [8.471, 39.748], [8.511, 39.722], [8.541, 39.732], [8.539, 39.77], [8.548, 39.839], [8.496, 39.897], [8.408, 39.917], [8.399, 39.978], [8.409, 40.038], [8.455, 40.078], [8.471, 40.131], [8.471, 40.293], [8.409, 40.352], [8.385, 40.443], [8.353, 40.501], [8.296, 40.559], [8.23, 40.606], [8.19, 40.652], [8.181, 40.771], [8.204, 40.871], [8.224, 40.913], [8.245, 40.907], [8.31, 40.858], [8.363, 40.846], [8.468, 40.834], [8.572, 40.85], [8.699, 40.895], [8.821, 40.95], [8.998, 41.11], [9.107, 41.143], [9.163, 41.185], [9.182, 41.242], [9.228, 41.257], [9.283, 41.202], [9.351, 41.196], [9.455, 41.15], [9.5, 41.106], [9.539, 41.054], [9.576, 41.031], [9.615, 41.017], [9.621, 41.005], [9.59, 40.992], [9.554, 40.932], [9.574, 40.915], [9.632, 40.882]]], [[[8.479, 39.068], [8.421, 38.969], [8.361, 39.039], [8.359, 39.099], [8.367, 39.116], [8.441, 39.091], [8.479, 39.068]]], [[[8.286, 41.04], [8.253, 40.994], [8.206, 40.997], [8.224, 41.031], [8.267, 41.099], [8.32, 41.122], [8.344, 41.102], [8.319, 41.063], [8.286, 41.04]]]]}};

    map.on('load', function () {
      ready = true;
      // ----- France highlight: make the whole France landmass stand out -----
      // A dimming veil over everything, then a luminous blue France fill +
      // a bright neon outline, so France clearly pops within darker Europe.
      try {
        map.addSource('france', { type: 'geojson', data: FRANCE_GEO });
        // 1) Dim the rest of Europe so France reads brighter by contrast.
        map.addLayer({
          id: 'world-dim', type: 'background',
          paint: { 'background-color': '#00001F', 'background-opacity': 0.42 }
        });
        // 2) Soft luminous blue fill inside France.
        map.addLayer({
          id: 'france-fill', type: 'fill', source: 'france',
          paint: { 'fill-color': '#C8A96B', 'fill-opacity': 0.16 }
        });
        // 3) Wide soft glow outline.
        map.addLayer({
          id: 'france-glow', type: 'line', source: 'france',
          layout: { 'line-join': 'round', 'line-cap': 'round' },
          paint: { 'line-color': '#E8C77A', 'line-width': 9, 'line-blur': 8, 'line-opacity': 0.55 }
        });
        // 4) Crisp bright neon border.
        map.addLayer({
          id: 'france-line', type: 'line', source: 'france',
          layout: { 'line-join': 'round', 'line-cap': 'round' },
          paint: { 'line-color': '#BFE4FF', 'line-width': 2, 'line-opacity': 0.95 }
        });
      } catch (e) { /* highlight is non-fatal */ }
      // NO route lines anywhere, only the blue dot markers. Per design,
      // the map shows clean luminous blue dots and never a connecting trail.
      // Auto-land on the All Journeys master view (every region of France),
      // not on any single individual course.
      setJourney(ALL_ID, false);
    });

    map.on('error', function (e) { /* tile load errors are non-fatal */ });

    /* ----- GeoJSON helpers ----- */
    function emptyFC() { return { type: 'FeatureCollection', features: [] }; }
    function lineFeature(coords) {
      return { type: 'FeatureCollection', features: [{ type: 'Feature', geometry: { type: 'LineString', coordinates: coords } }] };
    }
    /* Catmull-Rom spline -> smooth flowing curve through every stop.
       Turns the jagged straight-line zigzag into one elegant journey trail. */
    function smoothPath(pts, segments) {
      if (!pts || pts.length < 3) return pts ? pts.slice() : [];
      segments = segments || 22;
      var out = [];
      var p = pts.slice();
      // pad ends so the curve reaches the first/last point cleanly
      p.unshift(pts[0]);
      p.push(pts[pts.length - 1]);
      for (var i = 1; i < p.length - 2; i++) {
        var p0 = p[i - 1], p1 = p[i], p2 = p[i + 1], p3 = p[i + 2];
        for (var t = 0; t < segments; t++) {
          var s = t / segments, s2 = s * s, s3 = s2 * s;
          var x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * s +
            (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * s2 +
            (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * s3);
          var y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * s +
            (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * s2 +
            (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * s3);
          out.push([x, y]);
        }
      }
      out.push(pts[pts.length - 1]);
      return out;
    }

    /* ----- Route animation ----- */
    var animTimer = null;
    function animateRoute(coords) {
      if (animTimer) { clearInterval(animTimer); animTimer = null; }
      if (!coords || coords.length < 2) return;
      // densify into a polyline of points for a smooth trace
      var dense = densify(coords, 60);
      var win = Math.max(8, Math.round(dense.length * 0.08)); // short travelling window (a comet of light)
      var i = 0;
      var src = map.getSource('ms-route-anim');
      if (!src) return;
      animTimer = setInterval(function () {
        i += 1;
        if (i > dense.length + win) { i = 0; } // loop the glide
        var start = Math.max(0, i - win);
        var end = Math.min(dense.length, i);
        if (end - start < 2) { src.setData(emptyFC()); return; }
        src.setData(lineFeature(dense.slice(start, end)));
      }, 30);
    }
    function densify(coords, perSeg) {
      var out = [];
      for (var s = 0; s < coords.length - 1; s++) {
        var a = coords[s], b = coords[s + 1];
        for (var t = 0; t < perSeg; t++) {
          var f = t / perSeg;
          out.push([a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f]);
        }
      }
      out.push(coords[coords.length - 1]);
      return out;
    }

    /* ----- Markers ----- */
    function clearMarkers() {
      markers.forEach(function (m) { m.remove(); });
      markers = [];
    }
    function buildMarkers(course) {
      clearMarkers();
      var isAll = !!course.isAll;
      var pins = orderedPinsX(course);
      pins.forEach(function (p, idx) {
        var node = el('div', 'ms-marker' + (isAll ? ' ms-marker-dot' : ''));
        node.setAttribute('role', 'button');
        node.setAttribute('tabindex', '0');
        node.setAttribute('aria-label', isAll ? p.city : (p.city + ', stop ' + (idx + 1)));
        // Apple-sleek: small calm blue dot by default; lights to strong neon
        // on hover/active (CSS). In ALL mode there is no sequence, dot only,
        // no number, so the whole-France view reads clean and premium.
        // NO numbers on ANY blue element, dots only, always. The map reads as
        // clean luminous points of light; the active stop is shown by glow + the
        // info panel/label, never a number badge.
        node.innerHTML =
          '<span class="ms-marker-pin"></span>' +
          '<span class="ms-marker-label">' + esc(p.city) + '</span>';
        node.addEventListener('click', function (ev) { ev.stopPropagation(); openStop(course, p, idx); });
        node.addEventListener('keydown', function (ev) {
          if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); openStop(course, p, idx); }
        });
        // Anchor at CENTER so the dot sits exactly on its coordinate.
        var mk = new maplibregl.Marker({ element: node, anchor: 'center' })
          .setLngLat([p.lng, p.lat]).addTo(map);
        node._pinId = p.id;
        markers.push(mk);
      });
    }
    function highlightMarker(pinId) {
      markers.forEach(function (m) {
        var e = m.getElement();
        e.classList.toggle('active', e._pinId === pinId);
      });
    }

    /* ----- Legend ----- */
    function buildLegend(course) {
      if (course.isAll) {
        legend.innerHTML =
          '<div class="ms-legend-row"><span class="ms-legend-dot"></span>' +
            '<span class="ms-legend-txt">All journeys  ·  every city &amp; region</span></div>' +
          '<div class="ms-legend-row ms-legend-route"><span class="ms-legend-txt ms-legend-sub">' +
            course.pins.length + ' places across all 6 courses</span></div>' +
          '<div class="ms-legend-hint">Tap any blue dot to open its lesson</div>';
        return;
      }
      legend.innerHTML =
        '<div class="ms-legend-row"><span class="ms-legend-dot"></span>' +
          '<span class="ms-legend-txt">' + esc(course.name) + '  ·  ' + esc(course.level) + '</span></div>' +
        '<div class="ms-legend-row ms-legend-route"><span class="ms-legend-txt ms-legend-sub">' +
          course.routeOrder.length + ' places in this journey</span></div>' +
        '<div class="ms-legend-hint">Tap any blue dot to open its lesson</div>';
    }

    /* ----- Info panel ----- */
    function openStop(course, p, idx) {
      // In ALL mode the synthetic course has no single owner, each pin
      // remembers its real course (name/level/href) so the tag + CTA stay correct.
      var isAll = !!course.isAll;
      var ownName = isAll ? (p._ownerName || course.name) : course.name;
      var ownLevel = isAll ? (p._ownerLevel || course.level) : course.level;
      var ownHref = isAll ? (p._ownerHref || course.href) : course.href;
      var totalStops = course.routeOrder.length;
      var unitsHTML = p.units.map(function (u) {
        return '<li class="ms-unit">' +
          '<span class="ms-unit-num">Unit ' + u.num + '</span>' +
          '<h4 class="ms-unit-fr">' + esc(u.fr) + '</h4>' +
          '<p class="ms-unit-en">' + esc(u.en) + '</p>' +
        '</li>';
      }).join('');
      // Populate the separate top-left photo pop-up (real place image, 3D)
      if (p.image) {
        photoPop.innerHTML =
          '<span class="ms-photo-pop-glow" aria-hidden="true"></span>' +
          '<img class="ms-photo-pop-img" src="' + esc(p.image) + '" alt="' + esc(p.city) + '" loading="eager" decoding="async">' +
          '<figcaption class="ms-photo-pop-cap">' +
            '<span class="ms-photo-pop-step">' + (isAll ? esc(p.location) : ('Stop ' + (idx + 1))) + '</span>' +
            '<span class="ms-photo-pop-city">' + esc(p.city) + '</span>' +
            (p.credit ? '<span class="ms-photo-pop-credit">' + esc(p.credit) + '</span>' : '') +
          '</figcaption>';
        photoPop.classList.remove('open');
        // force reflow so the pop animation re-triggers each click
        void photoPop.offsetWidth;
        photoPop.classList.add('open');
        photoPop.setAttribute('aria-hidden', 'false');
      } else {
        photoPop.classList.remove('open');
        photoPop.setAttribute('aria-hidden', 'true');
        photoPop.innerHTML = '';
      }
      panel.innerHTML =
        '<button class="ms-panel-close" type="button" aria-label="Close">&times;</button>' +
        '<div class="ms-panel-head">' +
          '<span class="ms-panel-step">' + (isAll ? esc(p.location) : ('Stop ' + (idx + 1) + ' of ' + totalStops)) + '</span>' +
          '<h3 class="ms-panel-city">' + esc(p.city) + '</h3>' +
          '<p class="ms-panel-loc">' + (isAll ? 'Featured in the journey below' : esc(p.location)) + '</p>' +
        '</div>' +
        '<div class="ms-panel-course">' +
          '<span class="ms-panel-coursetag">' + esc(ownName) + '  ·  ' + esc(ownLevel) + '</span>' +
        '</div>' +
        '<ul class="ms-panel-units">' + unitsHTML + '</ul>' +
        '<a class="ms-panel-cta" href="' + esc(ownHref) + '">View the ' + esc(ownName) + ' course' +
          '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>';
      panel.querySelector('.ms-panel-close').addEventListener('click', closePanel);
      panel.classList.add('open');
      panel.setAttribute('aria-hidden', 'false');
      highlightMarker(p.id);
      // Ease toward the stop without losing journey context. On phones keep
      // the flat top-down view and never collapse below a city zoom, so the
      // surrounding stops stay in frame when the bottom sheet opens.
      if (ready) {
        var narrow = (window.matchMedia && window.matchMedia('(max-width:760px)').matches) || window.innerWidth <= 760;
        var opt = { center: [p.lng, p.lat], pitch: narrow ? 0 : MAP_PITCH, duration: 2400,
          offset: narrow ? [0, -150] : (compact ? [0, -30] : [-110, -10]) };
        if (narrow && map.getZoom() < 9) { opt.zoom = 10.6; }
        map.easeTo(opt);
      }
    }
    function closePanel() {
      panel.classList.remove('open');
      panel.setAttribute('aria-hidden', 'true');
      photoPop.classList.remove('open');
      photoPop.setAttribute('aria-hidden', 'true');
      highlightMarker(null);
    }
    stage.addEventListener('click', function (e) {
      if (e.target === stage) closePanel();
    });

    /* ----- Journey switch ----- */
    function setJourney(courseId, userInitiated) {
      var course = courseByIdX(courseId);
      activeCourse = course;
      var isAll = !!course.isAll;
      root.classList.toggle('ms-all-mode', isAll);

      // tabs
      Array.prototype.forEach.call(tabs.children, function (t) {
        t.classList.toggle('active', t.dataset.course === courseId);
      });

      buildLegend(course);
      closePanel();

      if (!ready) return; // markers/route get built on load via initial setJourney

      buildMarkers(course);

      var pins = orderedPinsX(course);
      var coords = pins.map(function (p) { return [p.lng, p.lat]; });

      // ---- ALL-JOURNEYS master mode ----------------------------------
      // The whole map of France, every place across every course. No single
      // route trail (that would be a meaningless tangle), just calm blue
      // dots over all of France, Apple-clean. Frame the entire country.
      if (isAll) {
        var ba = new maplibregl.LngLatBounds();
        coords.forEach(function (c) { ba.extend(c); });
        var isNarrowA = (window.matchMedia && window.matchMedia('(max-width:760px)').matches) || window.innerWidth <= 760;
        map.fitBounds(ba, {
          padding: isNarrowA ? { top: 60, bottom: 90, left: 34, right: 34 }
                             : { top: 90, bottom: 90, left: 70, right: 70 },
          pitch: 0,
          bearing: 0,
          duration: userInitiated ? 2600 : 0,
          maxZoom: isNarrowA ? 5.6 : 6.0
        });
        return; // no route, no auto-open in all mode
      }

      // No route line, dots only. Just frame the journey's places.
      // fit bounds to the journey
      var b = new maplibregl.LngLatBounds();
      coords.forEach(function (c) { b.extend(c); });
      // Responsive framing. The padding MUST be keyed to the real map size,
      // not the `compact` flag, map.html runs with compact=false even on a
      // phone, and the wide desktop padding (left 90 + right 416 = 506px)
      // exceeds a ~360px mobile map, so fitBounds silently fails ("Map cannot
      // fit within canvas") and the camera stays zoomed out over all France.
      var isNarrow = (window.matchMedia && window.matchMedia('(max-width:760px)').matches) ||
        window.innerWidth <= 760;
      var mapW = mapEl.offsetWidth || window.innerWidth;
      var mapH = mapEl.offsetHeight || window.innerHeight;
      var pad = (compact || isNarrow)
        ? { top: 70, bottom: 150, left: 38, right: 38 }
        : { top: 96, bottom: 110, left: 90, right: 416 };
      // Safety: never let padding swallow the canvas (keeps fitBounds valid).
      var maxH = Math.max(20, mapW * 0.34);
      var maxV = Math.max(20, mapH * 0.30);
      if (pad.left + pad.right > mapW * 0.72) { pad.left = Math.min(pad.left, maxH); pad.right = Math.min(pad.right, maxH); }
      if (pad.top + pad.bottom > mapH * 0.66) { pad.top = Math.min(pad.top, maxV); pad.bottom = Math.min(pad.bottom, maxV * 1.4); }
      // Compact Paris courses cluster tightly -> allow a closer zoom so the
      // curve reads as a real journey across the city, not a tiny tangle.
      // Cap a touch lower on phones so all stops fit without colliding pins.
      var tightCity = (course.id === 'fa-foundation' ||
        course.id === 'lsf-foundation' || course.id === 'lsf-beginner' ||
        course.id === 'lsf-elementary');
      var tightMax = isNarrow ? 11.2 : 12;
      // On phones, render the journey FLAT (pitch 0). The 40° tilt makes
      // fitBounds unpredictable in portrait and pushes the far end off-screen;
      // a top-down view frames a tall north-south route cleanly every time.
      var fitPitch = isNarrow ? 0 : MAP_PITCH;
      map.fitBounds(b, {
        padding: pad,
        pitch: fitPitch,
        bearing: MAP_BEARING,
        duration: userInitiated ? 2600 : 0,
        maxZoom: tightCity ? tightMax : (isNarrow ? 6.4 : 7.2)
      });
      // Open the first stop automatically so the map arrives alive, not empty
      //, with its photo card + lesson panel showing. DESKTOP ONLY: on mobile
      // the bottom sheet would cover the journey, so we leave the map clear
      // and let the user tap a stop.
      var firstPin = pins[0];
      if (firstPin && !compact && !isNarrow) {
        if (autoOpenTimer) { clearTimeout(autoOpenTimer); }
        autoOpenTimer = setTimeout(function () {
          openStop(course, firstPin, 0);
        }, userInitiated ? 900 : 650);
      }
    }
    var autoOpenTimer = null;

    return {
      root: root,
      map: map,
      setJourney: setJourney,
      openStop: function (id) {
        var c = activeCourse || courseById(DATA.courses[0].id);
        var p = pinByIdX(c, id);
        var idx = c.routeOrder.indexOf(id);
        if (p) openStop(c, p, idx);
      },
      closePanel: closePanel
    };
  }

  /* ---------- AUTO-MOUNT ---------- */
  function boot() {
    var first = document.querySelector('#mapstr-mount');
    if (first) { window.__mapstrInstance = mount(first); }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  window.Mapstr = { mount: mount, data: DATA };
})();
