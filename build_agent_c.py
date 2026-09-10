"""Agent C — Build Teachers, Biagio, deepen Blog. All rewrites in place."""
import os, re, pathlib
ROOT = pathlib.Path("/home/user/workspace/club-italia")

# --------- read partials ---------
NAV  = (ROOT/"_partials/nav.html").read_text()
FOOT = (ROOT/"_partials/footer.html").read_text()

def adapt(html, depth):
    """Adjust relative paths in nav/footer for the file's depth (0 = root, 2 = pages/x/)."""
    prefix = "../" * depth
    # Replace href / src attributes that start with plain relative paths.
    def r(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(("http", "#", "mailto:", "tel:", "/")):
            return m.group(0)
        return f'{attr}="{prefix}{url}"'
    return re.sub(r'(href|src)="([^"#/][^"]*)"', r, html)

def page(title, desc, body, depth=0, extra_head=""):
    css = ("../" * depth) + "css/ci.css"
    js  = ("../" * depth) + "js/ci.js"
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{css}">
{extra_head}
</head><body>
{adapt(NAV, depth)}

{body}

{adapt(FOOT, depth)}
<script src="{js}"></script>
</body></html>"""

# ============================================================
# TEACHER DATA
# ============================================================
TEACHERS = [
  {
    "slug":"chiara", "first":"Chiara", "last":"Bellini",
    "city":"Firenze", "region":"Toscana",
    "eyebrow":"Firenze · Toscana",
    "signature":"L'italiano si apre come un affresco. Un dettaglio alla volta.",
    "signature_en":"Italian opens like a fresco. One detail at a time.",
    "bio_short":"Renaissance-city Italian, taught with the eye of an art historian and the ear of a Florentine.",
    "tagline":"Nine years in Florence's classrooms. Fluent in art, food, and the perfect subjunctive.",
    "certs":["Università per Stranieri di Siena — CEDILS (Certificazione in Didattica dell'Italiano a Stranieri)",
             "MA · Italian Literature, Università degli Studi di Firenze",
             "Ten years teaching adult foreign learners, seven of them at the British Institute of Florence",
             "Native Florentine, born and raised in the Oltrarno"],
    "region_essay":[
      "Toscana is the region that gave the Italian language its shape. When Dante Alighieri, born in Firenze in 1265, chose to write the Divina Commedia in the volgare fiorentino instead of in Latin, he did not just write a poem, he handed a national tongue to a peninsula that did not yet know it was a nation. Five and a half centuries later, when Alessandro Manzoni set out to rewrite I promessi sposi, he moved to Florence, quite literally, to \"rinse his laundry in the Arno\" and re-write the novel in the Tuscan the city spoke.",
      "To learn Italian with a Florentine is to inherit that lineage. Not the accent of a television anchor, which is Tuscan-derived and slightly softened, but the real cadence of the streets of Santo Spirito, of the market of San Lorenzo, of the bar on the corner of Via Maggio at eight in the morning where the barista greets you and remembers whether you take sugar. There is a distinctive Florentine sound that turns hard c into a breathy h, la Coca-Cola becomes la hoha-hola, and while I do not push my students to imitate this, I do teach them to hear it and to smile at it.",
      "Toscana is also the region of the Renaissance, of the Uffizi and the Accademia and the Bargello, of the first modern banks and the first modern art criticism. My lessons on Botticelli, on Piero della Francesca, on the sculpture of Donatello, are not decoration. They are the way I teach the words for light, for weight, for the human body, for time. A student who has spent an hour with me in front of the Primavera has learned twenty-five nouns and six adjectives without ever seeing a vocabulary list."
    ],
    "manifesto":[
      "I do not believe in language drills the way most people mean the word. I believe in attention. When I ask a beginner to describe the espresso we are drinking, in the first lesson, in a mix of hand gestures and single Italian words, we are already doing everything language classes are supposed to do, we are noticing, comparing, choosing, correcting. That is Italian. The grammar comes to serve the noticing, not the other way round.",
      "My students are almost always adults, most of them Americans, many of them retired professionals with sharper minds than they give themselves credit for. What they lack is not intelligence, it is patience with themselves. So the first job I do, in the first three or four lessons, is to slow us both down to a pace where making a mistake in Italian is interesting instead of embarrassing. I speak slowly, I repeat, I let silence sit. And then the sentences start coming.",
      "I teach with real things. A postcard from Fiesole. A photograph of my grandmother's kitchen in Certaldo. A page from a 1950s cookbook. A recording of my aunt describing the day of the alluvione, the flood of 1966. Language that is attached to a real Italian object is language that stays. Language that is attached to a page in a textbook is language that leaves the moment the class ends.",
      "By the end of six months with me, my students can order in a Florentine trattoria without switching to English, hold a fifteen minute conversation with a stranger on the train, read the main text of a newspaper article on a subject they care about, and, most importantly, they no longer apologise for their Italian. That last one, I care about the most."
    ],
    "testimonials":[
      {"q":"Chiara took me from tourist-Italian to actually holding a conversation with my mother-in-law in Prato. She teaches with real Florence, not with a textbook.", "n":"Kate M., Boston · CI Intermedio, 2025"},
      {"q":"I have taken Italian classes for thirty years, on and off, in three different countries. Chiara is the only teacher who has ever made the congiuntivo feel like a friend instead of a threat.", "n":"Robert J., San Francisco · CI Avanzato, 2026"},
      {"q":"Every lesson feels like a walk through Florence. I miss my class the way I miss a good coffee shop.", "n":"Maria L., Chicago · CI Elementare, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Rituale d'apertura. Chiara opens with two minutes of small talk in Italian about the weather, the day, a piece of news from Florence. Every student contributes one sentence. She writes any new word on the shared whiteboard."),
      ("Minutes 10 to 30","Il testo del giorno. A short authentic text, a menu, a headline, a recipe, sometimes a Renaissance quotation, is read aloud. Students take turns. Chiara does not correct pronunciation on the fly, she notes and returns."),
      ("Minutes 30 to 55","Il punto di grammatica. One narrow grammar point is drawn out of the text and drilled with speech, not with worksheets. Students speak, Chiara corrects with a single Italian question that redirects them."),
      ("Minutes 55 to 75","Conversazione libera. Twenty minutes of free conversation, in pairs and then to the whole class, on a prompt Chiara has chosen from the day's material."),
      ("Minutes 75 to 85","Chiusura e compiti. Recap in Italian, homework assigned as a five-minute audio recording rather than a written exercise, and the goodbye that is always ci vediamo martedì, we see each other Tuesday.")
    ],
    "courses":[("pages/courses/ci2.html","CI Elementare · A1.1 → A1.2"),
               ("pages/courses/ci3.html","CI Intermedio · A1.2 → A2.1"),
               ("pages/culture/cap-art.html","Culture Capsule · L'Arte")],
    "schedule":[("Monday","19:00 ET","CI Intermedio","3 of 12"),
                ("Tuesday","12:00 ET","CI Elementare","5 of 12"),
                ("Wednesday","20:00 ET","Capsule · L'Arte","2 of 10"),
                ("Thursday","19:00 ET","CI Intermedio","waitlist"),
                ("Saturday","10:00 ET","Conversazione libera","6 of 8")],
    "portrait":"assets/img/teacher-chiara.jpg",
    "region_photo":"assets/img/pillar-art.jpg",
  },
  {
    "slug":"marco", "first":"Marco", "last":"Rinaldi",
    "city":"Roma", "region":"Lazio",
    "eyebrow":"Roma · Lazio",
    "signature":"A Roma non si insegna l'italiano. Si mangia, si passeggia, si discute, e alla fine si parla.",
    "signature_en":"In Rome you do not teach Italian. You eat, you walk, you argue, and by the end you speak.",
    "bio_short":"Rome-native, football-obsessed, cinema-literate. Teaches Italian with the pace and the wit of the city itself.",
    "tagline":"Twelve years in Roman classrooms. Fluent in Fellini, in Roma-Lazio derby, and in the fine art of not taking anything too seriously.",
    "certs":["Università degli Studi Roma Tre — Laurea magistrale in Linguistica",
             "DITALS II · Università per Stranieri di Siena",
             "Twelve years teaching at Scuola Leonardo da Vinci, Piazza dell'Orologio",
             "Native Roman, born in Trastevere, Roma tifoso since 1998"],
    "region_essay":[
      "Roma is the capital, and Romans will tell you this before you ask. It is the capital of Italy, of Catholicism, of a certain kind of Mediterranean pace that treats punctuality as a matter of guidance rather than of law. To teach Italian from Roma is to teach the language in the register in which the country actually speaks it, direct, ironic, comfortable with a small profanity, allergic to formality unless formality is truly required.",
      "The romanesco dialect, which you will hear at any market and in most trattorias, is not the Italian I teach. But its rhythms are. Romans truncate their words, romanesco says damme instead of dammi, tengo instead of ho, and you will hear these on the bus and be tempted to imitate. I will teach you to hear them without repeating them until you are ready.",
      "Lazio is the region, and while Roma dominates it in every measurable way, do not overlook the rest. Viterbo has some of the best-preserved medieval streets in central Italy. The Castelli Romani, the hill towns south of the city, are where Romans go on a Sunday afternoon to eat porchetta and drink Frascati. Tivoli and its two great villas, Adriana and d'Este, are one train ride and a lifetime of architecture away. I bring pieces of Lazio into every semester."
    ],
    "manifesto":[
      "My rule is simple, Italian is not a subject you study, it is a conversation you enter. So from the very first lesson, we are having a conversation. It is a small conversation, in the beginning it is mostly single words and hand gestures, but it is a conversation. You will not be asked to conjugate anything in isolation before you have used the conjugation in a real exchange with me.",
      "I am a Roman, and Romans argue. Not in an angry sense, in a discursive sense, we love a good debate about coffee, about politics, about whether tiramisù was invented in Treviso or in Tuscany. I bring this into class. I will disagree with you, gently and in Italian, about the film we just watched, about whether pasta alla carbonara should ever contain cream, no, it should not, about whether Roma will finally win a scudetto this decade. Disagreement is where the best Italian happens.",
      "I use film obsessively. Fellini, De Sica, Sorrentino, Garrone. Not because I want to make you a critic, but because Italian cinema is where the modern spoken language lives. A five-minute scene from La grande bellezza teaches vocabulary, register, gesture, and cultural context in a way no textbook ever will. My students learn to catch a joke in a Sorrentino monologue before they can write a formal email, and I am fine with that ordering.",
      "By the end of a course with me, my students can hold their own in a Roman bar. That is my measure. If you can order, joke, disagree, get the bill and leave a small tip in Italian, without switching to English, I have done my job. Everything else is decoration."
    ],
    "testimonials":[
      {"q":"Marco is the reason I no longer feel like a tourist in Rome. He gave me the language, but he also gave me the confidence to use it badly and still keep talking.", "n":"David T., New York · CI Intermedio, 2025"},
      {"q":"His film class is worth the tuition on its own. I have watched La grande bellezza four times, and each time I understand more of the jokes.", "n":"Susan H., Denver · Culture Capsule, 2026"},
      {"q":"He is patient in a way that Romans supposedly are not. He also makes me laugh in Italian, which is a strange and wonderful feeling.", "n":"Alan P., Miami · Parliamo Confident, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Chiacchierata romana. Marco opens with a two-minute rant about the traffic, the weather, or the most recent Roma-Lazio result. Students respond, in Italian, at their level."),
      ("Minutes 10 to 25","La scena. A short film clip, three to four minutes, is played twice. First without subtitles, then with. Students describe what happened, in Italian, one sentence each."),
      ("Minutes 25 to 45","Il punto di lingua. One structure, drawn from the scene, is taught and drilled through speech. Marco corrects with imitation, not with rules, he says the sentence correctly and asks the student to repeat."),
      ("Minutes 45 to 70","Dibattito. Twenty-five minutes of argued conversation on a prompt drawn from the film. Two teams, no English, Marco moderates and jumps in when a group stalls."),
      ("Minutes 70 to 85","Chiusura. Recap, homework which is always to watch one more Italian film scene of the student's choosing, and the sign-off that is always alla prossima, until next time.")
    ],
    "courses":[("pages/courses/ci3.html","CI Intermedio · A1.2 → A2.1"),
               ("pages/courses/ci4.html","CI Avanzato · A2.1 → A2.2"),
               ("pages/spoken/ps4.html","Parliamo · Chiacchierando (Confident)")],
    "schedule":[("Monday","20:00 ET","CI Avanzato","4 of 12"),
                ("Tuesday","19:00 ET","Parliamo Confident","2 of 10"),
                ("Wednesday","12:00 ET","CI Intermedio","full · waitlist"),
                ("Friday","19:00 ET","Cinema Club","5 of 12"),
                ("Sunday","11:00 ET","Conversazione romana","3 of 8")],
    "portrait":"assets/img/teacher-marco.jpg",
    "region_photo":"assets/img/pillar-cinema.jpg",
  },
  {
    "slug":"giulia", "first":"Giulia", "last":"Moretti",
    "city":"Bologna", "region":"Emilia-Romagna",
    "eyebrow":"Bologna · Emilia-Romagna",
    "signature":"Se sai cucinare, sai già parlare. L'italiano è la lingua che si cucina.",
    "signature_en":"If you can cook, you can already speak. Italian is a language that is cooked.",
    "bio_short":"Bologna-trained linguist, home-cook, holder of a family recipe book six generations deep.",
    "tagline":"Fifteen years teaching adult Italian, most of them at ALMA, the international school of Italian cuisine.",
    "certs":["Università di Bologna — Laurea Magistrale in Italianistica",
             "CEDILS · Università Ca' Foscari di Venezia",
             "Adjunct instructor, ALMA, La scuola internazionale di cucina italiana (2018 to present)",
             "Author of two Italian textbooks for adult learners, published by Alma Edizioni"],
    "region_essay":[
      "Emilia-Romagna is, by unanimous Italian agreement, the region where the country eats best. That statement is not made lightly. Every Italian region will fight for the title, but when you visit an emiliano you are witnessing a food culture that is at once monumental, disciplined, generous, and old, tagliatelle al ragù, tortellini in brodo, mortadella, prosciutto di Parma, Parmigiano Reggiano, aceto balsamico tradizionale di Modena, all come from this one region.",
      "Bologna is my city. It has three nicknames, la dotta because of its university, the oldest in the Western world, founded in 1088, la grassa because of its cooking, and la rossa because of the red brick of its porticoes, thirty-eight kilometres of arcades under which one can walk the entire historic centre without getting wet. All three nicknames are the truth. I teach in the shadow of all three.",
      "The Bolognese accent is soft, almost a lilt. The famous emiliano double consonant is not double the way it is farther south, it is elongated, like a musical note held. When my students first hear a Bolognese speaker they often say the sound is more comforting than that of, say, a Roman. I do not push my students into the local accent. But I make sure they hear it and they learn to love it."
    ],
    "manifesto":[
      "I teach Italian through food, because food is the shortest route into the head of an adult learner. Vocabulary that arrives with a plate of tagliatelle in front of it stays. Vocabulary that arrives on a slide does not. I have taught this way for fifteen years and I have never yet met the exception.",
      "In my classes we cook. Not always literally, though I do run a monthly Saturday cucina live, but always metaphorically, every grammar point is served with a dish, every dish arrives with a story, every story lands the grammar. Il congiuntivo, that great fear of the intermediate learner, is introduced not with a table of endings but with the sentence penso che il ragù sia meglio dopo un giorno, I think the ragù is better after a day, and by the end of the hour everyone has generated ten such sentences and never opened a chart.",
      "I also teach with rigour. My reputation among students is warm but demanding. I will make you repeat a sentence three times if the second time is not right. I will give you homework. I will follow up in the week between classes with a five-minute audio message you must reply to. And I will notice, with fondness, when you get it. Adults do not respond to soft standards, they respond to being taken seriously.",
      "By the end of a year with me, my students cook two Emilian menus from memory in Italian, can read a Gambero Rosso review without a dictionary, and can hold a forty-five minute conversation about food that never once resorts to English. That is the culture I hand them. Everything else, the trains, the pharmacies, the paperwork, they can figure out."
    ],
    "testimonials":[
      {"q":"Giulia turned my Italian around. I signed up because I love food, I stayed because she is one of the finest teachers I have ever had, in any subject.", "n":"Ellen R., Portland · CI Elementare, 2025"},
      {"q":"Her Saturday cucina live is the highlight of my week. We cook, we talk, we never speak English, and I have never learned more vocabulary in less time.", "n":"Michael B., Toronto · Culture Capsule, 2026"},
      {"q":"She is exacting, warm, funny, and generous. I have taken every course she teaches, and I will keep signing up until she throws me out.", "n":"Barbara S., Austin · CI Avanzato, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Buongiorno bolognese. Giulia greets each student by name, asks one specific question, cosa hai mangiato ieri sera, and writes new food words on the shared board."),
      ("Minutes 10 to 30","La ricetta del giorno. A short Italian recipe is projected. Students read aloud, in turn, and Giulia interrupts only for pronunciation of an unfamiliar ingredient or verb."),
      ("Minutes 30 to 55","Il punto di lingua. One grammar item, drawn from the recipe, is taught, drilled and produced in student sentences. Correction happens through Italian reformulation, not English translation."),
      ("Minutes 55 to 75","Conversazione a tavola. A twenty-minute simulated meal, in Italian, using the vocabulary of the recipe. Students order, react, disagree, offer more."),
      ("Minutes 75 to 85","Chiusura. Recap, homework which is to send one photo of a meal and one sentence describing it in Italian by Friday, and the sign-off that is always buon appetito.")
    ],
    "courses":[("pages/courses/ci2.html","CI Elementare · A1.1 → A1.2"),
               ("pages/courses/ci4.html","CI Avanzato · A2.1 → A2.2"),
               ("pages/culture/cap-food.html","Culture Capsule · La Cucina")],
    "schedule":[("Monday","12:00 ET","CI Elementare","full · waitlist"),
                ("Tuesday","19:00 ET","CI Avanzato","3 of 12"),
                ("Wednesday","19:00 ET","Capsule · La Cucina","2 of 10"),
                ("Saturday","09:00 ET","Cucina Live","4 of 8"),
                ("Sunday","12:00 ET","Conversazione a tavola","5 of 8")],
    "portrait":"assets/img/teacher-giulia.jpg",
    "region_photo":"assets/img/pillar-food.jpg",
  },
  {
    "slug":"alessandro", "first":"Alessandro", "last":"Ferri",
    "city":"Milano", "region":"Lombardia",
    "eyebrow":"Milano · Lombardia",
    "signature":"L'italiano dei milanesi è preciso, veloce, gentile. Come un tram che arriva in orario.",
    "signature_en":"The Italian of the Milanese is precise, fast, polite. Like a tram that arrives on time.",
    "bio_short":"Milan-born business Italian specialist. Teaches with the pace of the north and the ear of a translator.",
    "tagline":"Nine years in the classrooms of Bocconi and IES Abroad. Specialist in professional and academic register.",
    "certs":["Università Cattolica del Sacro Cuore di Milano — Laurea Magistrale in Linguistica",
             "DITALS II · Università per Stranieri di Siena",
             "Certified interpreter, Italian to English, AITI",
             "Adjunct Italian instructor, IES Abroad Milano (2019 to present)"],
    "region_essay":[
      "Lombardia is the industrial engine of the country, and Milano is its capital. This is the region of Fiat's old suppliers, of Pirelli, of the Borsa Italiana, of the fashion houses of Via Montenapoleone, of the tech corridors between the city and its hinterland. It is also the region of the Duomo, of Leonardo's Ultima Cena, of the Alps that rise ninety minutes north of the city, of Lago di Como and Lago di Garda.",
      "The Milanese Italian is close to the standard, but faster, with clipped endings and a slightly Germanic precision. You will hear it in the shops of the Quadrilatero, in the boardrooms of Porta Nuova, in the aperitivo bars of Brera at seven in the evening. It is the Italian of a city that runs on time and expects you to as well.",
      "Milano is also the city where la settimana della moda, la Fashion Week, and il Salone del Mobile, the design fair, happen twice a year. It is the Italian city where an American professional is most likely to find themselves for work. That is why my Italian classes lean, deliberately, toward the vocabulary of contracts, meetings, presentations, and the very particular art of the Milanese aperitivo, which is at once a social ritual and, more often than a foreigner realises, a business meeting."
    ],
    "manifesto":[
      "I teach Italian to adults who need to work in Italian, or who want to. That is a distinct pedagogy. It is not the pedagogy of the tourist who needs to order at a trattoria, and it is not the pedagogy of the retiree who wants to read Dante in the original. It is somewhere between the two, technical vocabulary paired with the small-talk grammar that surrounds it, and it needs to arrive quickly.",
      "My method is dense. I ask my students to spend fifteen minutes a day between classes, reading a short authentic Italian text I have curated. Not a page from a textbook, a page from Il Corriere della Sera, from Il Sole 24 Ore, from an Italian LinkedIn post. Then in class we unpack the text together, we harvest the vocabulary and the structures, and we produce our own.",
      "I do not believe in translation drills. When my students ask me how to say something in Italian, I do not translate. I ask them to describe the thing in the Italian they already have, and I fill in the gaps. This is slower for the first ten lessons and dramatically faster for the next hundred.",
      "By the end of a course with me, my students can present a five-minute business idea in Italian, negotiate a contract in Italian at a basic level, participate in an aperitivo without slipping into English, and read an Italian financial news article at seventy per cent comprehension. That last number is not aspirational, it is what I measure."
    ],
    "testimonials":[
      {"q":"Alessandro trained me for a client meeting in Milan and I walked out of that meeting having spoken Italian for ninety minutes. Two years ago I could not order coffee.", "n":"James P., Chicago · CI Avanzato, 2025"},
      {"q":"He teaches Italian the way a good CFO reads a spreadsheet. Precisely, patiently, and with the assumption that you can handle the truth.", "n":"Rachel M., New York · Parliamo Confident, 2026"},
      {"q":"His curated news readings turned my daily commute into a language lesson. I have never had a teacher this deliberate.", "n":"Peter K., Houston · CI Intermedio, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Notizia del giorno. Alessandro opens with one headline from that morning's Italian press. Students respond in Italian, one sentence each."),
      ("Minutes 10 to 30","La lettura. A curated one-page authentic Italian text is read aloud. Vocabulary is unpacked as it appears, not before."),
      ("Minutes 30 to 55","Il punto di lingua. One structure, drawn from the text, is taught and produced in student sentences. Correction is precise and Italian-only."),
      ("Minutes 55 to 75","Applicazione professionale. Twenty minutes of role-play, meeting, presentation, negotiation, mixed pairs, Italian throughout."),
      ("Minutes 75 to 85","Chiusura. Recap, homework which is a two-hundred-word Italian LinkedIn-style post to be shared before the next class.")
    ],
    "courses":[("pages/courses/ci3.html","CI Intermedio · A1.2 → A2.1"),
               ("pages/courses/ci4.html","CI Avanzato · A2.1 → A2.2"),
               ("pages/spoken/ps4.html","Parliamo · Chiacchierando (Confident)")],
    "schedule":[("Monday","07:30 ET","CI Avanzato","4 of 12"),
                ("Tuesday","19:00 ET","Business Italian","3 of 10"),
                ("Wednesday","07:30 ET","CI Intermedio","6 of 12"),
                ("Thursday","19:00 ET","Parliamo Confident","2 of 10"),
                ("Friday","07:30 ET","Aperitivo del venerdì","5 of 8")],
    "portrait":"assets/img/teacher-alessandro.jpg",
    "region_photo":"assets/img/pillar-travel.jpg",
  },
  {
    "slug":"francesca", "first":"Francesca", "last":"Zeno",
    "city":"Venezia", "region":"Veneto",
    "eyebrow":"Venezia · Veneto",
    "signature":"A Venezia si impara ad ascoltare prima di parlare. La città è fatta di silenzi.",
    "signature_en":"In Venice you learn to listen before you speak. The city is made of silences.",
    "bio_short":"Venetian-born literature scholar. Teaches Italian with the patience of a lagoon and the precision of a librarian.",
    "tagline":"Eleven years at Ca' Foscari, seven of them coordinating Italian-for-foreigners. Specialist in literary Italian.",
    "certs":["Università Ca' Foscari di Venezia — Dottorato in Italianistica",
             "CEDILS · Ca' Foscari, senior examiner",
             "Coordinator, Corsi di Italiano per Stranieri, Ca' Foscari (2020 to 2024)",
             "Author of scholarly work on Carlo Goldoni and eighteenth-century Venetian theatre"],
    "region_essay":[
      "Veneto is the region of the lagoon, of the Dolomites, of the plains that Napoleon crossed in 1797 and that gave Italy Palladio, Tiziano, Tintoretto, Veronese, Canaletto, Goldoni, and Casanova. It is also, quietly, one of the most economically productive regions of the country, and one of the most linguistically complex, the venetian dialect, or veneto, is not a corruption of Italian but a sibling of it, with its own literature stretching back to the 1200s.",
      "Venezia is my city and I have to declare, gently, that Venezia is unlike anywhere else, not just in Italy, in the world. It is the only major European city where the streets are water, where the only vehicle is a boat, where the daily rhythm is set by tides and by the vaporetti. Learning Italian from a Venetian is learning to speak more slowly, to leave pauses, to notice light.",
      "The venetian dialect is a joy and a hazard. My students will hear ciao, invented in Venice from the phrase s-ciavo vostro, your servant, and its softened venetian form s'ciào. They will hear campi and campielli instead of piazze. They will notice that Venetians address their friends with tu but their acquaintances with the archaic voi rather than lei, a pattern the rest of Italy discarded in the twentieth century. I teach my students to hear these things, to smile at them, and to speak standard Italian throughout."
    ],
    "manifesto":[
      "I teach Italian slowly. I do not mean I teach it inefficiently, I mean I teach it at the pace at which language is best absorbed by an adult mind, which is roughly the pace at which a Venetian walks along the Zattere on a Sunday morning, unhurried, attentive, willing to stop.",
      "My method is grounded in reading. Not in the childish reading of a graded textbook, in the real reading of adapted but authentic Italian prose, from the first month. A beginner does not begin with a page of Manzoni, but they do begin with the first two paragraphs of an Italian short story I have chosen, and by the end of six months they are reading Buzzati, Ginzburg, Calvino in the original, at their level.",
      "I also teach with theatre. Venice gave the world Carlo Goldoni, the reformer of the commedia dell'arte, and a Goldoni play is, unexpectedly, a magnificent teaching text, spoken language, real registers, comic timing, and dialogue that adults can read aloud without feeling patronised. Once a semester my students perform a five-minute Goldoni scene together, in Italian, on video. They remember the scene for years.",
      "By the end of a year with me, my students read Italian literature at their level with pleasure, hold a sustained conversation on almost any topic, and, most importantly, have developed the habit of noticing Italian. Noticing a word in a Ferrante novel. Noticing a phrase in an interview. Noticing the way a friend from Padua says qua for qui. That habit is the thing that will make them lifelong Italian speakers."
    ],
    "testimonials":[
      {"q":"Francesca gave me a reading life in Italian. I now read Ferrante in the original on the train home. I did not know that was going to be possible.", "n":"Elena D., Boston · CI Avanzato, 2025"},
      {"q":"Her Goldoni performance week is the most fun I have ever had learning any language. I am fifty-eight and I have never done anything like it.", "n":"Anna G., Los Angeles · Culture Capsule, 2026"},
      {"q":"She is patient in a way that made me stop apologising for my Italian. That was the shift I needed.", "n":"Robert H., Philadelphia · CI Intermedio, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Lettura silenziosa. Students receive a short authentic Italian paragraph and read it silently while Francesca reads it aloud, once."),
      ("Minutes 10 to 30","La lettura ad alta voce. Each student reads a portion aloud. Francesca corrects rhythm and pronunciation, not vocabulary."),
      ("Minutes 30 to 55","Il punto di lingua. One structure, drawn from the text, is taught and produced in student sentences, spoken and written."),
      ("Minutes 55 to 75","Interpretazione. Twenty minutes of role-play or short dramatic reading, in pairs, in Italian."),
      ("Minutes 75 to 85","Chiusura. Recap, homework which is to read one more page of the same author, plus a five-minute audio reflection.")
    ],
    "courses":[("pages/courses/ci3.html","CI Intermedio · A1.2 → A2.1"),
               ("pages/courses/ci4.html","CI Avanzato · A2.1 → A2.2"),
               ("pages/culture/cap-opera.html","Culture Capsule · L'Opera")],
    "schedule":[("Monday","13:00 ET","CI Avanzato","5 of 12"),
                ("Tuesday","20:00 ET","Lettura italiana","3 of 10"),
                ("Wednesday","13:00 ET","CI Intermedio","full · waitlist"),
                ("Thursday","20:00 ET","Capsule · L'Opera","4 of 10"),
                ("Saturday","11:00 ET","Goldoni Reading Circle","2 of 8")],
    "portrait":"assets/img/teacher-francesca.jpg",
    "region_photo":"assets/img/pillar-opera.jpg",
  },
  {
    "slug":"luca", "first":"Luca", "last":"De Simone",
    "city":"Napoli", "region":"Campania",
    "eyebrow":"Napoli · Campania",
    "signature":"Napoli non si insegna, si contagia. E anche l'italiano, con lei, si prende come una bella febbre.",
    "signature_en":"Naples is not taught, it is caught. And Italian, along with it, is caught like a beautiful fever.",
    "bio_short":"Neapolitan-born, opera-raised, football-obsessed. Teaches Italian with the theatricality of the south.",
    "tagline":"Ten years at the Università degli Studi di Napoli L'Orientale, four seasons of coaching amateur opera choirs.",
    "certs":["Università di Napoli L'Orientale — Laurea Magistrale in Linguistica",
             "DITALS II · Università per Stranieri di Siena",
             "Choir director, Teatro Sannazaro, Napoli (amateur programme)",
             "Native Neapolitan, born in the Sanità district"],
    "region_essay":[
      "Campania is the region of contradictions. It is the region of Napoli, of Pompei and Ercolano, of the Costiera Amalfitana, of the pizza, of the Camorra, of Elena Ferrante's Naples novels, of Diego Armando Maradona, of the songs of the Piedigrotta festival, of a cuisine that runs from the poorest cucina povera to the finest ristoranti stellati. To love Campania is to love a place that is too much of everything at once.",
      "Napoli is the third largest city in Italy and, by a considerable margin, the most theatrically Italian. Neapolitans speak with their whole body. They embrace, they gesture, they interrupt, they finish each other's sentences in a way that a northern Italian would find impolite and that Neapolitans find affectionate. To learn Italian from a Neapolitan is to accept that language is inseparable from body, from tone, from performance.",
      "The Neapolitan dialect, napoletano, is a rich and old language in its own right, with a literature that runs from Basile in the seventeenth century to the songs of Pino Daniele in the twentieth. I teach standard Italian in class, but I bring in one napoletano word or phrase each session, always with translation, so my students can hear a piece of the city as it actually sounds. Watching a scene of Gomorra without hearing the word guagliò is like watching Rome without hearing dai."
    ],
    "manifesto":[
      "I teach loudly. I do not mean the volume, I mean the presence. When you are in my class, in Italian, you are in the room, you are speaking, you are responding to me and to your classmates as if we were sitting on the terrace of a bar in the Vomero on a warm September evening. There is no place to hide, and this is deliberate.",
      "The Neapolitan tradition is a tradition of performance. I use songs, obsessively. The great Neapolitan song, from O sole mio to Napule è, is one of the most reliable teaching aids on earth. Students who cannot yet form a sentence in the passato prossimo can nonetheless sing a chorus in the imperfetto and, doing so, absorb the tense in a way no drill will ever produce.",
      "I also use theatre. Eduardo De Filippo, the great twentieth-century Neapolitan playwright, wrote in a mix of standard Italian and napoletano that is uniquely suited to teaching, because his rhythms are the rhythms of adult conversation. My students read short scenes aloud, they play the parts, they get corrected on the fly, and they learn to speak in real registers.",
      "By the end of a year with me my students can hold a conversation with a Neapolitan without flinching, can sing at least three canzoni napoletane from memory, and, most importantly, no longer feel that Italian is a language they have to earn. It is, at that point, a language they can inhabit."
    ],
    "testimonials":[
      {"q":"Luca is a force. I have never worked harder in a class, and I have never had more fun. He turned me from an intermediate student into a confident speaker in six months.", "n":"Karen M., Atlanta · CI Intermedio, 2025"},
      {"q":"His Neapolitan song sessions are the most joyful hour of my week. I go to sleep humming O surdato 'nnammurato and I wake up ready to speak Italian.", "n":"Michael J., Seattle · Culture Capsule, 2026"},
      {"q":"He is theatrical, generous, insistent, patient, and hilarious. Everything a great Italian teacher should be.", "n":"Nancy R., Miami · Parliamo Beginner, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Buongiorno Napoli. Luca opens with a two-minute story from his week, or a headline from Napoli's news. Students respond, in Italian."),
      ("Minutes 10 to 30","La canzone o la scena. A short Neapolitan song or a scene from Eduardo De Filippo is played and read aloud together."),
      ("Minutes 30 to 55","Il punto di lingua. One grammar item, drawn from the song or scene, is taught, drilled and produced in student sentences."),
      ("Minutes 55 to 75","Interpretazione. Twenty minutes of dramatised speaking, in pairs, in Italian, drawn from the day's material."),
      ("Minutes 75 to 85","Chiusura. Recap, homework which is to record one voice memo in Italian describing your day, and the sign-off which is always jamm'.")
    ],
    "courses":[("pages/courses/ci1.html","CI Principiante · A0 → A1.1"),
               ("pages/courses/ci2.html","CI Elementare · A1.1 → A1.2"),
               ("pages/spoken/ps2.html","Parliamo · Iniziamo (Beginner)")],
    "schedule":[("Monday","19:00 ET","CI Principiante","5 of 12"),
                ("Tuesday","12:00 ET","CI Elementare","3 of 12"),
                ("Wednesday","19:00 ET","Parliamo Beginner","full · waitlist"),
                ("Thursday","12:00 ET","Canzone Napoletana","6 of 10"),
                ("Saturday","10:00 ET","Teatro con Luca","4 of 8")],
    "portrait":"assets/img/teacher-luca.jpg",
    "region_photo":"assets/img/pillar-tradition.jpg",
  },
  {
    "slug":"sofia", "first":"Sofia", "last":"Mazzara",
    "city":"Palermo", "region":"Sicilia",
    "eyebrow":"Palermo · Sicilia",
    "signature":"L'italiano dei siciliani è generoso. Ci mette dentro la storia di tutto il Mediterraneo.",
    "signature_en":"The Italian of Sicilians is generous. It carries inside it the history of the whole Mediterranean.",
    "bio_short":"Palermo-native, historian by training, patient by nature. Teaches Italian through the layered history of her island.",
    "tagline":"Eight years at the Università di Palermo, three seasons as a licensed cultural guide for the Zisa and the Cappella Palatina.",
    "certs":["Università degli Studi di Palermo — Laurea Magistrale in Storia dell'Arte",
             "CEDILS · Università Ca' Foscari di Venezia",
             "Licensed cultural guide, Regione Siciliana (2019 to present)",
             "Native Palermitana, born and raised in the Kalsa"],
    "region_essay":[
      "Sicilia is the largest island in the Mediterranean and, by any honest measure, a civilization of its own. Greek, Phoenician, Roman, Arab, Norman, Aragonese, Bourbon, Italian, each of these left their language, their food, their architecture, and their words in the Sicilian mouth. To learn Italian from a Sicilian is to receive a language that has, buried in it, every empire that ever crossed the Mediterranean.",
      "Palermo is my city and it is one of the most historically compressed cities I know. In one square kilometre you can walk from a Phoenician wall to a Norman cathedral built by Arab craftsmen for a Christian king, to a Baroque church, to a Liberty-style villa from 1900, to a street market that sounds and smells more like Marrakech than like Rome. The city is a book that Italians themselves come to read.",
      "The Sicilian dialect, siciliano, is a language in its own right, recognised as such by UNESCO. It is not the Italian I teach. But its cadences, its slower vowels, its love of the passato remoto, the remote past tense that the north has largely abandoned but that Sicilians use daily, all of these leave their imprint on the Italian I speak. My students learn to hear that imprint, to smile at it, and to speak standard Italian throughout."
    ],
    "manifesto":[
      "I teach Italian as if it were a museum I know very well and want to show you slowly. The point is not to see everything on the first visit. The point is to see one room with real attention, so that when you come back, on your own, you already know how to look.",
      "My method is grounded in history. Not in a dry way, in the way a good tour guide grounds an afternoon walk, this piazza was built here because of that battle, this word for a fruit comes from Arabic because of these merchants, this building is Norman on the outside and Byzantine on the inside because of that marriage. Language becomes memorable when it is attached to a place, and my job is to attach it.",
      "I am patient. I am the teacher my students describe as calm, which is a word I take seriously. Adults learning a new language often carry with them the frustrated eight-year-old they once were in French class. My job is to make them, over the first five lessons, forget that eight-year-old, and become the curious adult they actually are.",
      "By the end of a year with me my students can hold a forty-five minute conversation about anything in Italian, can navigate any Sicilian town with confidence, and can read a piece of Italian art history at their level with pleasure. But more than that, they have learned to notice. To notice a word in a menu, a gesture in a market, a loanword in a song. That noticing is what makes an Italian speaker for life."
    ],
    "testimonials":[
      {"q":"Sofia is the calmest, most attentive teacher I have ever had. She made me feel I could learn Italian at fifty-nine, and then she made it true.", "n":"Diane M., Baltimore · CI Elementare, 2025"},
      {"q":"Her history-driven lessons are unforgettable. I now think of Italian words the way I think of the buildings in Palermo, layered, story-rich, alive.", "n":"Alan T., Denver · CI Intermedio, 2026"},
      {"q":"I have travelled to Palermo three times because of Sofia. I speak Italian there now. I could not have imagined that four years ago.", "n":"Carla P., Boston · Culture Capsule, 2025"}
    ],
    "typical":[
      ("Minutes 0 to 10","Buongiorno palermitano. Sofia greets each student with one specific historical or cultural question of the day. Students respond in Italian."),
      ("Minutes 10 to 30","La lettura o l'immagine. A short authentic Italian text or one Sicilian image is presented. Students read aloud or describe."),
      ("Minutes 30 to 55","Il punto di lingua. One grammar item is taught, drilled and produced in student sentences, with warm and precise correction."),
      ("Minutes 55 to 75","Passeggiata. Twenty minutes of guided speaking, as if walking through a Sicilian street, in Italian only."),
      ("Minutes 75 to 85","Chiusura. Recap, homework which is a short written or recorded reflection on the day's material, and the sign-off which is always a prestu, until soon.")
    ],
    "courses":[("pages/courses/ci1.html","CI Principiante · A0 → A1.1"),
               ("pages/courses/ci3.html","CI Intermedio · A1.2 → A2.1"),
               ("pages/culture/cap-art.html","Culture Capsule · L'Arte")],
    "schedule":[("Monday","10:00 ET","CI Principiante","6 of 12"),
                ("Tuesday","19:00 ET","CI Intermedio","4 of 12"),
                ("Wednesday","10:00 ET","Capsule · L'Arte","3 of 10"),
                ("Thursday","19:00 ET","Sicilia Storica","5 of 10"),
                ("Sunday","10:00 ET","Passeggiata in Italiano","4 of 8")],
    "portrait":"assets/img/teacher-sofia.jpg",
    "region_photo":"assets/img/culture.jpg",
  },
]

# ============================================================
# INLINE STYLES (page-scoped, keeping global CSS untouched)
# ============================================================
TEACHER_PAGE_CSS = """
<style>
.t-hero{position:relative;min-height:100vh;background:linear-gradient(120deg,var(--navy-deep) 0%,var(--navy) 55%,var(--navy-soft) 100%);color:var(--on-dark);display:flex;align-items:stretch;overflow:hidden}
.t-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 82% 30%,rgba(201,162,75,.14),transparent 55%);pointer-events:none}
.t-hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:0;width:100%;align-items:stretch;position:relative;z-index:2}
@media (max-width:960px){.t-hero-grid{grid-template-columns:1fr}}
.t-hero-copy{padding:9rem clamp(1.6rem,5vw,6rem) 5rem;display:flex;flex-direction:column;justify-content:center}
.t-hero-eyebrow{font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:2rem;display:inline-flex;align-items:center;gap:.9rem}
.t-hero-eyebrow::before{content:"";width:2.4rem;height:1px;background:var(--gold-soft)}
.t-hero-name{font-family:var(--serif);font-style:italic;font-weight:500;font-size:clamp(3.6rem,7vw,7rem);line-height:.98;letter-spacing:-.02em;margin:0 0 .4rem;color:var(--on-dark)}
.t-hero-last{display:block;color:var(--gold-soft);font-style:italic}
.t-hero-role{font-family:var(--serif);font-size:1.35rem;font-style:italic;color:var(--on-dark-soft);margin:2rem 0 2.4rem;max-width:36ch;line-height:1.4}
.t-hero-quote{border-left:2px solid var(--gold);padding:.4rem 0 .4rem 1.4rem;font-family:var(--serif);font-style:italic;font-size:1.25rem;color:var(--on-dark);max-width:44ch;margin-bottom:.6rem}
.t-hero-quote-en{font-size:.86rem;letter-spacing:.02em;color:var(--on-dark-faint);max-width:44ch;margin-bottom:2.4rem}
.t-hero-portrait{position:relative;overflow:hidden;background:var(--navy-mid);min-height:64vh}
.t-hero-portrait img{width:100%;height:100%;object-fit:cover;object-position:center 20%}
.t-hero-portrait::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(34,8,11,.55) 0%,rgba(34,8,11,0) 30%),linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,.35) 100%);pointer-events:none}

.region-band{display:grid;grid-template-columns:.7fr 1.3fr;gap:0}
@media (max-width:960px){.region-band{grid-template-columns:1fr}}
.region-photo{position:relative;min-height:64vh;overflow:hidden}
.region-photo img{width:100%;height:100%;object-fit:cover}
.region-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(34,8,11,0) 60%,rgba(243,237,223,.15) 100%);pointer-events:none}
.region-essay{padding:clamp(4rem,7vw,7rem) clamp(1.6rem,5vw,6rem);background:var(--paper);color:var(--on-light)}
.region-essay h2{font-family:var(--serif);font-weight:500;font-size:clamp(2rem,3.6vw,3rem);line-height:1.1;margin:0 0 2rem;max-width:22ch;color:var(--navy)}
.region-essay .region-eyebrow{font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:1.4rem;display:block}
.region-essay p{font-size:1.08rem;line-height:1.75;margin-bottom:1.2rem;color:var(--on-light-soft)}
.region-essay .drop::first-letter{font-family:var(--serif);float:left;font-size:4.6rem;line-height:.9;padding:.4rem .6rem 0 0;color:var(--gold-deep);font-weight:600}

.manifesto{background:var(--ivory);padding:clamp(4rem,7vw,7rem) 0}
.manifesto-head{max-width:820px;margin:0 auto 3rem;padding:0 clamp(1.4rem,3vw,3rem)}
.manifesto-head .eyebrow{color:var(--gold-deep)}
.manifesto-body{max-width:760px;margin:0 auto;padding:0 clamp(1.4rem,3vw,3rem)}
.manifesto-body p{font-size:1.13rem;line-height:1.78;color:var(--on-light);margin-bottom:1.4rem}
.manifesto-body p:first-child::first-letter{font-family:var(--serif);float:left;font-size:5rem;line-height:.9;padding:.3rem .55rem 0 0;color:var(--terra-deep);font-weight:600}
.manifesto-sign{margin-top:2rem;font-family:var(--serif);font-style:italic;color:var(--terra-deep);font-size:1.1rem}

.cred-band{background:var(--navy);color:var(--on-dark);padding:clamp(4rem,7vw,7rem) 0}
.cred-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:3rem;align-items:start}
@media (max-width:960px){.cred-grid{grid-template-columns:1fr}}
.cred-title{font-family:var(--serif);font-style:italic;font-weight:500;font-size:clamp(2rem,3.6vw,3rem);line-height:1.05;color:var(--gold-soft)}
.cred-list{list-style:none;padding:0;margin:0}
.cred-list li{padding:1.2rem 0;border-top:1px solid var(--gold-line-soft);font-size:1.02rem;line-height:1.55;color:var(--on-dark);display:grid;grid-template-columns:auto 1fr;gap:1.4rem;align-items:baseline}
.cred-list li:last-child{border-bottom:1px solid var(--gold-line-soft)}
.cred-list .cred-num{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.35rem;min-width:2ch}

.t-testimonials{background:var(--paper);padding:clamp(4rem,7vw,7rem) 0}
.t-test-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem}
@media (max-width:960px){.t-test-grid{grid-template-columns:1fr}}
.t-test{background:var(--white);border:1px solid var(--gold-line-soft);padding:2.2rem 2rem;position:relative}
.t-test::before{content:"\\201C";position:absolute;top:-.1rem;left:1.4rem;font-family:var(--serif);color:var(--gold);font-size:5rem;line-height:1;font-weight:600}
.t-test p{font-family:var(--serif);font-style:italic;font-size:1.15rem;line-height:1.5;color:var(--on-light);margin-top:1.8rem;margin-bottom:1.4rem}
.t-test .t-test-src{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep);border-top:1px solid var(--light-line);padding-top:1rem}

.lesson-band{background:var(--cream);padding:clamp(4rem,7vw,7rem) 0}
.lesson-timeline{max-width:900px;margin:0 auto;padding:0 clamp(1.4rem,3vw,3rem);position:relative}
.lesson-timeline::before{content:"";position:absolute;left:calc(clamp(1.4rem,3vw,3rem) + 5rem);top:0;bottom:0;width:1px;background:var(--gold-line)}
@media (max-width:640px){.lesson-timeline::before{display:none}}
.lesson-row{display:grid;grid-template-columns:6rem 1fr;gap:2rem;padding:1.8rem 0;border-bottom:1px solid var(--light-line);position:relative}
.lesson-row:last-child{border-bottom:none}
.lesson-row::before{content:"";position:absolute;left:calc(5rem - 4px);top:2.2rem;width:9px;height:9px;background:var(--gold);border-radius:50%}
@media (max-width:640px){.lesson-row{grid-template-columns:1fr;gap:.4rem}.lesson-row::before{display:none}}
.lesson-time{font-family:var(--serif);font-style:italic;color:var(--terra-deep);font-size:1.05rem;line-height:1.3}
.lesson-desc{font-size:1.02rem;line-height:1.6;color:var(--on-light);padding-left:1.4rem}
@media (max-width:640px){.lesson-desc{padding-left:0}}

.t-courses{background:var(--paper);padding:clamp(4rem,7vw,7rem) 0}
.t-course-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
@media (max-width:900px){.t-course-grid{grid-template-columns:1fr}}
.t-course-card{background:var(--white);border:1px solid var(--gold-line-soft);padding:2rem 1.8rem;display:flex;flex-direction:column;justify-content:space-between;transition:all .3s var(--ease);text-decoration:none;color:inherit}
.t-course-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(58,14,18,.14);border-color:var(--gold-line)}
.t-course-card .tcc-eyebrow{font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:1.4rem}
.t-course-card h3{font-family:var(--serif);font-size:1.55rem;margin-bottom:1rem;color:var(--navy);line-height:1.15}
.t-course-card .tcc-cta{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--terra-deep);margin-top:1.4rem}

.schedule-band{background:var(--navy);color:var(--on-dark);padding:clamp(4rem,7vw,7rem) 0}
.schedule-table{max-width:900px;margin:0 auto;padding:0 clamp(1.4rem,3vw,3rem)}
.sched-row{display:grid;grid-template-columns:1fr 1fr 1.6fr auto;gap:2rem;padding:1.4rem 0;border-bottom:1px solid var(--gold-line-soft);align-items:baseline;font-size:1rem}
.sched-row.head{font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-soft);border-bottom:1px solid var(--gold);padding-bottom:1rem;font-family:var(--sans)}
@media (max-width:720px){.sched-row{grid-template-columns:1fr 1fr;gap:.6rem;padding:1.2rem 0}.sched-row.head{display:none}}
.sched-day{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.2rem}
.sched-time{color:var(--on-dark);font-variant-numeric:tabular-nums}
.sched-course{color:var(--on-dark-soft)}
.sched-seats{font-size:.82rem;letter-spacing:.06em;color:var(--gold-soft);white-space:nowrap;font-variant-numeric:tabular-nums}
.sched-seats.full{color:var(--terra-soft)}

.t-book{background:linear-gradient(140deg,var(--terra-deep) 0%,var(--navy) 60%);color:var(--on-dark);padding:clamp(4rem,7vw,7rem) 0;text-align:center}
.t-book h2{font-family:var(--serif);font-style:italic;font-weight:500;font-size:clamp(2.4rem,5vw,3.8rem);line-height:1.05;margin-bottom:1.6rem}
.t-book p{font-size:1.15rem;color:var(--on-dark-soft);max-width:60ch;margin:0 auto 2.4rem}
</style>
"""

def teacher_page(t):
    portrait = "../../" + t["portrait"]
    region_photo = "../../" + t["region_photo"]

    hero = f"""
<!-- FOLD 1 · HERO -->
<section class="t-hero"><div class="t-hero-grid">
<div class="t-hero-copy reveal">
  <span class="t-hero-eyebrow">{t['eyebrow']}</span>
  <h1 class="t-hero-name">{t['first']} <span class="t-hero-last">{t['last']}</span></h1>
  <p class="t-hero-role">{t['tagline']}</p>
  <blockquote class="t-hero-quote">{t['signature']}</blockquote>
  <p class="t-hero-quote-en">{t['signature_en']}</p>
  <div class="hero-ctas"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Book a Lesson with {t['first']}</button><a class="btn btn-3d btn-3d-ghost" href="#schedule">See {t['first']}'s Schedule</a></div>
</div>
<div class="t-hero-portrait reveal reveal-d1"><img src="{portrait}" alt="Portrait of {t['first']} {t['last']}, Italian teacher from {t['city']}"></div>
</div></section>
"""

    region_paras = "\n".join([f'<p{" class=\"drop\"" if i==0 else ""}>{p}</p>' for i,p in enumerate(t["region_essay"])])
    region = f"""
<!-- FOLD 2 · THE REGION -->
<section class="region-band">
<div class="region-photo reveal"><img src="{region_photo}" alt="{t['region']} landscape"></div>
<div class="region-essay reveal reveal-d1">
  <span class="region-eyebrow">{t['region']} · The Region</span>
  <h2>The Italy I teach from.</h2>
  {region_paras}
</div>
</section>
"""

    mani_paras = "\n".join([f"<p>{p}</p>" for p in t["manifesto"]])
    manifesto = f"""
<!-- FOLD 3 · HOW I TEACH -->
<section class="manifesto">
<div class="manifesto-head reveal">
  <span class="eyebrow eyebrow-line">How I Teach · A Manifesto</span>
  <h2 class="display-md" style="color:var(--navy)">The classroom I run.</h2>
</div>
<div class="manifesto-body reveal">
  {mani_paras}
  <p class="manifesto-sign">— {t['first']} {t['last']}, {t['city']}</p>
</div>
</section>
"""

    cred_items = "\n".join([f'<li><span class="cred-num">{i+1:02d}</span><span>{c}</span></li>' for i,c in enumerate(t["certs"])])
    creds = f"""
<!-- FOLD 4 · CREDENTIALS -->
<section class="cred-band">
<div class="wrap"><div class="cred-grid">
<div class="reveal"><span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Credenziali</span><h2 class="cred-title">Certified, trained, rooted in {t['city']}.</h2></div>
<ul class="cred-list reveal reveal-d1">{cred_items}</ul>
</div></div></section>
"""

    tests = "\n".join([f'<div class="t-test reveal reveal-d{i}"><p>{tt["q"]}</p><div class="t-test-src">{tt["n"]}</div></div>' for i,tt in enumerate(t["testimonials"])])
    testimonials = f"""
<!-- FOLD 5 · TESTIMONIALS -->
<section class="t-testimonials">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">What My Students Say</span><h2 class="display-md" style="color:var(--navy)">In their own words.</h2></div>
<div class="t-test-grid">{tests}</div>
</div></section>
"""

    lesson_rows = "\n".join([f'<div class="lesson-row reveal"><div class="lesson-time">{tm}</div><div class="lesson-desc">{ds}</div></div>' for tm,ds in t["typical"]])
    lesson = f"""
<!-- FOLD 6 · A TYPICAL LESSON -->
<section class="lesson-band">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">A Typical Lesson</span><h2 class="display-md" style="color:var(--navy)">85 minutes with {t['first']}.</h2><p class="lead">Every {t['first']} class runs for eighty-five minutes and follows the same architecture. The topics change every week, the rhythm does not.</p></div></div>
<div class="lesson-timeline">{lesson_rows}</div>
</section>
"""

    cc = "\n".join([f'<a class="t-course-card reveal" href="../../{url}"><div><span class="tcc-eyebrow">Course</span><h3>{name}</h3></div><span class="tcc-cta">See the syllabus →</span></a>' for url,name in t["courses"]])
    courses = f"""
<!-- FOLD 7 · COURSES -->
<section class="t-courses">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line">Where You'll Find Me</span><h2 class="display-md" style="color:var(--navy)">Courses I teach.</h2></div>
<div class="t-course-grid">{cc}</div>
</div></section>
"""

    sched_rows = "\n".join([f'<div class="sched-row"><span class="sched-day">{d}</span><span class="sched-time">{tm}</span><span class="sched-course">{c}</span><span class="sched-seats {"full" if "full" in s or "waitlist" in s else ""}">seats: {s}</span></div>' for d,tm,c,s in t["schedule"]])
    sched = f"""
<!-- FOLD 8 · SCHEDULE -->
<section class="schedule-band" id="schedule">
<div class="wrap"><div class="section-head reveal"><span class="eyebrow eyebrow-line" style="color:var(--gold-soft)">Open Cohorts · September 2026</span><h2 class="display-md">{t['first']}'s live schedule.</h2><p class="lead" style="color:var(--on-dark-soft)">All times shown in US Eastern. Every class is live, small, and taught by {t['first']} in person from {t['city']}.</p></div>
<div class="schedule-table">
<div class="sched-row head"><span>Day</span><span>Time (ET)</span><span>Course</span><span>Seats</span></div>
{sched_rows}
</div></div></section>
"""

    book = f"""
<!-- FOLD 9 · BOOK CTA -->
<section class="t-book"><div class="wrap-narrow reveal">
<h2>Learn Italian with {t['first']}.</h2>
<p>An advisor will help you place, choose the right cohort, and reserve a seat with {t['first']}. There is no obligation. The consultation is free.</p>
<div class="hero-ctas" style="justify-content:center;display:flex"><button class="btn btn-3d btn-3d-primary" data-advisor type="button">Book My Placement Call</button><a class="btn btn-3d btn-3d-ghost" href="../../teachers.html">Meet the Other Teachers</a></div>
</div></section>
"""

    body = hero + region + manifesto + creds + testimonials + lesson + courses + sched + book
    p = page(f"{t['first']} {t['last']} — Italian Teacher from {t['city']} · Club Italia by eTeacher",
             f"{t['first']} {t['last']}, native Italian teacher from {t['city']}, {t['region']}. {t['bio_short']}",
             body, depth=2, extra_head=TEACHER_PAGE_CSS)
    return p

# Write teacher pages
for t in TEACHERS:
    out = ROOT / f"pages/teachers/{t['slug']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(teacher_page(t))
    print(f"wrote {out}")

print("teacher pages done")
