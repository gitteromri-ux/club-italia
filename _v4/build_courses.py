"""Bulk-generate the 11 course pages (CI1-4, PS1-4, Cap Food/Art/Opera).
Each page: 15 folds, cinematic photography, no SVG UI mockups.
"""
import sys
sys.path.insert(0, "/home/user/workspace/club-italia/_v4")
from common import head, footer_scripts, nav_html, ROOT
from parts import (hero_cinematic, social_proof_strip, zoom_class_fold,
                   life_grid_fold, trustpilot_wall, cta_final, two_col_photo_text)

# Depth 2 for pages/courses/*.html and pages/spoken/*.html and pages/culture/*.html
D = 2
A_ = "../../assets/"
NAV = nav_html(D)
FOOT = footer_scripts(D)

# ============================================================
# COURSE DEFINITIONS
# ============================================================
COURSES = {
    # ---- Club Italia — Il Corso ----
    "ci1": {
        "slug": "pages/courses/ci1.html", "code": "CI1", "track": "Club Italia · Il Corso",
        "cefr_from": "A0", "cefr_to": "A1.1", "name": "Principiante",
        "subtitle": "Your first Italian",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Principiante.</span><br>Your first forty lessons of Italian.',
        "hero_sub": "For learners who begin at zero and want to end the year saying, ordering, and being understood. Forty live classes with a native teacher in Roma. Ten to twelve classmates. Every session recorded for life.",
        "poster": "hero-italian-life.jpg", "video": "roma-piazza.mp4",
        "right_img": "zoom-classroom-marco.jpg",
        "right_caption": "Marco Rinaldi · live from Trastevere",
        "teacher_slug": "marco", "teacher_name": "Marco Rinaldi", "teacher_city": "Roma",
        "teacher_bio": "Marco has taught Italian for eleven years at Sapienza and at Club Italia. He believes the first year of Italian is best learned inside a real Roman morning: at a bar, at a market, in a taxi.",
        "env_img": "env-marco-desk.jpg",
        "life_hero": "life-caffe-roma.jpg",
        "syllabus": [
            ("01", "Piacere · introductions", "Present essere/avere · numbers", "Introduce yourself in Italian"),
            ("02", "Al bar · at the coffee bar", "Definite articles · nouns", "Order coffee and pastries"),
            ("03", "La famiglia · family", "Possessives · plurals", "Describe your immediate family"),
            ("04", "Che ore sono? · telling time", "Numbers 20–100 · time", "Read a clock and a schedule"),
            ("05", "Il mercato · at the market", "Regular verbs -are", "Buy fruit, cheese and bread"),
            ("06", "La routine · daily life", "Regular verbs -ere / -ire", "Describe your daily routine"),
            ("07", "Il fine settimana · weekends", "Andare · fare · venire", "Talk about weekend plans"),
            ("08", "Il ristorante · dining out", "Direct object pronouns", "Order dinner in a Roman trattoria"),
            ("09", "In città · around town", "Prepositions of place", "Ask for and give directions"),
            ("10", "Al telefono · phone Italian", "Formal vs informal you", "Make a phone reservation"),
            ("11", "La casa · at home", "Ci · descriptive adjectives", "Describe your apartment"),
            ("12", "Al lavoro · at work", "Modal verbs potere/dovere", "Talk about your work"),
            ("13", "Il tempo · the weather", "Impersonal verbs", "Discuss weather and travel"),
            ("14", "In viaggio · travel", "Passato prossimo — auxiliary avere", "Recount a past trip"),
            ("15", "Uscite · going out", "Passato prossimo — auxiliary essere", "Tell what you did last night"),
            ("16", "La spesa · groceries", "Ne · partitives", "Do a full week's shopping"),
            ("17", "Al cinema · at the movies", "Piacere and its forms", "Discuss films and preferences"),
            ("18", "La salute · health", "Reflexive verbs", "Book and describe a doctor's visit"),
            ("19", "Le feste · Italian festivities", "Imperativo informale", "Give simple instructions"),
            ("20", "Piccola rivista · midterm review", "Consolidation", "Hold a 10-minute conversation"),
        ],
        "outcomes": [
            "Introduce yourself and hold a 5-minute conversation with a stranger",
            "Order food and drink in a Roman café or trattoria",
            "Read a menu, a signboard, a short article without a phone",
            "Recount a past weekend using the passato prossimo",
            "Understand the difference between formal and informal address",
        ],
    },
    "ci2": {
        "slug": "pages/courses/ci2.html", "code": "CI2", "track": "Club Italia · Il Corso",
        "cefr_from": "A1.1", "cefr_to": "A1.2", "name": "Elementare",
        "subtitle": "Speaking with intention",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Elementare.</span><br>Where your Italian starts to sound like Italian.',
        "hero_sub": "You have the ground under you. Now build the second story. Forty live sessions on the past, the future, and the small imperfect tense that makes stories out of sentences.",
        "poster": "hero-tuscan-classroom.jpg", "video": "firenze-arno.mp4",
        "right_img": "zoom-classroom-chiara.jpg",
        "right_caption": "Chiara Bianchi · live from Firenze",
        "teacher_slug": "chiara", "teacher_name": "Chiara Bianchi", "teacher_city": "Firenze",
        "teacher_bio": "Chiara reads Ferrante on the train and teaches with the calm of a decade in the classroom. Her students say she makes the imperfetto feel like a favor Italian is doing them.",
        "env_img": "env-chiara-desk.jpg",
        "life_hero": "life-uffizi-hall.jpg",
        "syllabus": [
            ("01", "Il passato prossimo, ripasso", "Review · auxiliary choice", "Retell last week's story"),
            ("02", "L'imperfetto · the imperfect", "Imperfect tense · uses", "Describe a childhood"),
            ("03", "Passato vs imperfetto", "Aspect · contrast", "Narrate a memory"),
            ("04", "Il futuro semplice", "Future simple", "Talk about next summer"),
            ("05", "Il condizionale", "Conditional present", "Order politely, say what you would do"),
            ("06", "I comparativi", "Comparisons · superlatives", "Compare cities and cuisines"),
            ("07", "Gerundio · stare + gerundio", "Progressive aspect", "Describe what you're doing"),
            ("08", "Ci pronominale", "Adverbial ci", "Say where and to what you go"),
            ("09", "Ne pronominale", "Partitive ne", "Talk about quantities in Italian"),
            ("10", "Combinazioni di pronomi", "Combined pronouns", "Handle everyday commerce"),
            ("11", "Al negozio · shopping", "Shopping vocabulary", "Try on and negotiate"),
            ("12", "Descrivere persone", "Adjectives · relative clauses (che)", "Describe someone in detail"),
            ("13", "In hotel · at the hotel", "Requests · complaints", "Check in and resolve issues"),
            ("14", "Al medico · at the doctor", "Body · illness", "Explain a health problem"),
            ("15", "Racconti · storytelling", "Past narrative", "Tell a five-minute story"),
            ("16", "Opinioni · opinions", "Introducing opinions", "Discuss a news article"),
            ("17", "Al telefono formale", "Formal register", "Handle a business call"),
            ("18", "Email in italiano", "Written register", "Write a formal email"),
            ("19", "Cultura · a Firenze", "Cultural competence", "Read a museum caption aloud"),
            ("20", "Ripasso finale", "Consolidation", "20-minute assessed conversation"),
        ],
        "outcomes": [
            "Move fluently between past, imperfect, future and conditional",
            "Tell a 5-minute story about your childhood or last trip",
            "Handle a hotel check-in, a doctor's visit, a shopping negotiation",
            "Write a formal email in idiomatic Italian",
            "Read a museum caption in Florence without help",
        ],
    },
    "ci3": {
        "slug": "pages/courses/ci3.html", "code": "CI3", "track": "Club Italia · Il Corso",
        "cefr_from": "A1.2", "cefr_to": "A2.1", "name": "Intermedio",
        "subtitle": "Real conversations",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Intermedio.</span><br>The year your Italian stops translating.',
        "hero_sub": "Forty live sessions on the subjunctive, the passive, and the conversations that separate a tourist from a resident. With Giulia Ferrari, live from Bologna.",
        "poster": "hero-teacher-live.jpg", "video": "bologna-portici.mp4",
        "right_img": "zoom-classroom-marco.jpg",
        "right_caption": "Giulia Ferrari · live from Bologna",
        "teacher_slug": "giulia", "teacher_name": "Giulia Ferrari", "teacher_city": "Bologna",
        "teacher_bio": "Giulia teaches at Alma Mater and at Club Italia. Her third-level students say she is the reason they finally understood the congiuntivo — because she treats it like a mood, not a form.",
        "env_img": "env-giulia-kitchen.jpg",
        "life_hero": "life-market-bologna.jpg",
        "syllabus": [
            ("01", "Il trapassato prossimo", "Pluperfect · storytelling", "Layer a past narrative"),
            ("02", "Il congiuntivo presente", "Present subjunctive · uses", "Express doubt and desire"),
            ("03", "Il congiuntivo passato", "Past subjunctive", "Speak about past unknowns"),
            ("04", "Il periodo ipotetico I", "Real conditionals", "Discuss real hypotheticals"),
            ("05", "Il periodo ipotetico II", "Unreal conditionals", "Discuss what would have been"),
            ("06", "Il congiuntivo imperfetto", "Imperfect subjunctive", "Speak in high register"),
            ("07", "Il discorso indiretto", "Reported speech", "Retell what someone said"),
            ("08", "La forma passiva", "Passive voice", "Handle news and formal writing"),
            ("09", "Gli avverbi", "Adverbs · nuance", "Speak with precision"),
            ("10", "Verbi pronominali", "Idiomatic pronominal verbs", "Sound Italian, not translated"),
            ("11", "Al lavoro · in ufficio", "Professional register", "Handle a work meeting"),
            ("12", "Le notizie · reading news", "Newspaper Italian", "Discuss a Corriere article"),
            ("13", "L'arte · reading paintings", "Cultural register", "Guide a friend through an Uffizi room"),
            ("14", "Regionalismi", "Regional variation", "Understand a Neapolitan or Milanese"),
            ("15", "Racconti letterari", "Literary register", "Read a short Calvino aloud"),
            ("16", "La cucina · food and philosophy", "Cultural discourse", "Argue about pasta shapes"),
            ("17", "Politica e società", "Civic language", "Discuss an Italian issue"),
            ("18", "Cinema italiano", "Film vocabulary", "Discuss a Sorrentino film"),
            ("19", "Un dialogo lungo", "Extended conversation", "Hold a 30-minute conversation"),
            ("20", "Valutazione", "Assessment", "Assessed CEFR A2.1 conversation"),
        ],
        "outcomes": [
            "Use the subjunctive in the four everyday cases (doubt, desire, opinion, emotion)",
            "Discuss news, art, and cinema in native register",
            "Understand a Neapolitan or Milanese accent within a minute",
            "Hold a 30-minute conversation with an Italian stranger",
            "Read a Calvino short story with only occasional dictionary help",
        ],
    },
    "ci4": {
        "slug": "pages/courses/ci4.html", "code": "CI4", "track": "Club Italia · Il Corso",
        "cefr_from": "A2.1", "cefr_to": "A2.2", "name": "Avanzato",
        "subtitle": "Cultural fluency",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Avanzato.</span><br>Italian as a way of thinking.',
        "hero_sub": "Forty live sessions on high register, idiom, film, and the way Italians argue about food, family, and politics. With Alessandro Conti, live from Milano.",
        "poster": "hero-italian-life.jpg", "video": "opera-scala.mp4",
        "right_img": "zoom-classroom-chiara.jpg",
        "right_caption": "Alessandro Conti · live from Milano",
        "teacher_slug": "alessandro", "teacher_name": "Alessandro Conti", "teacher_city": "Milano",
        "teacher_bio": "Alessandro has taught adult learners for twelve years, from Milano and Torino. His fourth-level class reads Ferrante together, argues about Sorrentino, and finishes the year hosting a two-hour dinner in Italian.",
        "env_img": "env-marco-desk.jpg",
        "life_hero": "life-scala-milano.jpg",
        "syllabus": [
            ("01", "Registro alto", "High register", "Read a Repubblica editorial aloud"),
            ("02", "Modi di dire", "Idiomatic expressions", "Use ten idioms in conversation"),
            ("03", "Il gerundio composto", "Compound gerund", "Speak in refined subordination"),
            ("04", "Frasi implicite", "Implicit clauses", "Speak Italian without the crutch of 'che'"),
            ("05", "Concordanza dei tempi", "Sequence of tenses", "Master narrative time"),
            ("06", "Il congiuntivo trapassato", "Pluperfect subjunctive", "Speak in unrealized past"),
            ("07", "Retorica quotidiana", "Everyday rhetoric", "Argue an Italian point"),
            ("08", "Ferrante · lettura", "Literary reading I", "Discuss a Ferrante chapter"),
            ("09", "Calvino · lettura", "Literary reading II", "Discuss a Calvino story"),
            ("10", "Poesia · lettura", "Poetry aloud", "Read a Montale poem aloud"),
            ("11", "Il cinema autoriale", "Auteur cinema", "Discuss a Fellini scene"),
            ("12", "Il cinema contemporaneo", "Contemporary cinema", "Discuss a Sorrentino scene"),
            ("13", "La musica · Battisti", "Cultural listening", "Discuss classic Italian songwriting"),
            ("14", "La musica contemporanea", "Contemporary listening", "Discuss a Baustelle song"),
            ("15", "Politica italiana", "Political discourse", "Speak civilly about Italian politics"),
            ("16", "Filosofia · cibo e famiglia", "Cultural philosophy", "Argue an Italian food principle"),
            ("17", "L'arte contemporanea", "Contemporary art", "Discuss a Cattelan piece"),
            ("18", "Un articolo lungo", "Extended reading", "Analyze a long-form article"),
            ("19", "Cena in italiano", "Extended conversation", "Host a 2-hour dinner in Italian"),
            ("20", "Valutazione finale", "CEFR A2.2 assessment", "Assessed conversation and short essay"),
        ],
        "outcomes": [
            "Read Ferrante and Calvino in the original with occasional support",
            "Discuss film, politics, and food in native register",
            "Use the full sequence of Italian tenses accurately",
            "Host a two-hour dinner conversation in Italian",
            "Sit and pass a CEFR A2.2 external exam if you choose to",
        ],
    },

    # ---- Parliamo Italiano ----
    "ps1": {
        "slug": "pages/spoken/ps1.html", "code": "PS1", "track": "Parliamo Italiano",
        "cefr_from": "—", "cefr_to": "Foundation", "name": "Foundation",
        "subtitle": "Sounds and greetings",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Parliamo · Foundation.</span><br>Twelve weeks of Italian sound.',
        "hero_sub": "A spoken-only course for absolute beginners. Twelve one-hour sessions on the mouth of Italian: rhythm, greetings, café, market, direction. With Sofia Greco, live from Palermo.",
        "poster": "hero-italian-life.jpg", "video": "napoli-mare.mp4",
        "right_img": "zoom-two-phones.jpg",
        "right_caption": "Sofia Greco · live from Palermo",
        "teacher_slug": "sofia", "teacher_name": "Sofia Greco", "teacher_city": "Palermo",
        "teacher_bio": "Sofia teaches beginners with the patience of an aunt. Her Parliamo groups leave with a Sicilian ear and a Roman confidence: they say the word, they mean it.",
        "env_img": "env-chiara-desk.jpg",
        "life_hero": "life-caffe-roma.jpg",
        "syllabus": [
            ("01", "I suoni · Italian sounds", "Rhythm · vowels", "Say your name and be understood"),
            ("02", "I saluti · greetings", "Ciao, buongiorno, arrivederci", "Enter and leave a room in Italian"),
            ("03", "Al bar", "Ordering drinks", "Order caffè, cappuccino, cornetto"),
            ("04", "I numeri", "1–100", "Handle prices and phone numbers"),
            ("05", "L'ora · time", "Telling time", "Read a schedule aloud"),
            ("06", "Al mercato", "Fruits · vegetables", "Buy from a market stall"),
            ("07", "Al ristorante", "Menus · orders", "Order a two-course dinner"),
            ("08", "Direzioni", "Where is · turn left", "Ask and follow directions"),
            ("09", "La famiglia · family", "Family vocabulary", "Introduce your family"),
            ("10", "Al telefono", "Phone Italian", "Book a restaurant on the phone"),
            ("11", "In taxi · in autobus", "Transport", "Get across a city in Italian"),
            ("12", "Una serata · a night out", "Extended conversation", "Order dinner, wine, and a taxi home"),
        ],
        "outcomes": [
            "Order any drink or dish in Italian without hesitation",
            "Ask for and follow directions on foot or by car",
            "Introduce yourself, your family, and your work",
            "Handle a phone reservation or a taxi in Italian",
            "Be understood by a native speaker on the first try",
        ],
    },
    "ps2": {
        "slug": "pages/spoken/ps2.html", "code": "PS2", "track": "Parliamo Italiano",
        "cefr_from": "Foundation", "cefr_to": "Beginner", "name": "Beginner",
        "subtitle": "Ordering and asking",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Parliamo · Beginner.</span><br>Twelve weeks of everyday Italian.',
        "hero_sub": "For learners who have their greetings and want their errands. Twelve spoken sessions on the market, the taxi, the doctor, and the small argument at the trattoria. With Francesca Ricci, live from Napoli.",
        "poster": "hero-tuscan-classroom.jpg", "video": "napoli-mare.mp4",
        "right_img": "zoom-classroom-marco.jpg",
        "right_caption": "Francesca Ricci · live from Napoli",
        "teacher_slug": "francesca", "teacher_name": "Francesca Ricci", "teacher_city": "Napoli",
        "teacher_bio": "Francesca is a Neapolitan who teaches with the warmth and speed of her city. Her Parliamo groups leave able to argue about pasta with the person next to them.",
        "env_img": "env-marco-desk.jpg",
        "life_hero": "life-trattoria-toscana.jpg",
        "syllabus": [
            ("01", "Ripasso", "Sounds · greetings review", "Warm up"),
            ("02", "In banca", "At the bank", "Change money · open an account"),
            ("03", "Alla posta", "At the post", "Send a parcel"),
            ("04", "In farmacia", "At the pharmacy", "Ask for a common remedy"),
            ("05", "Dal medico", "At the doctor", "Describe an ache"),
            ("06", "Il traffico", "In traffic", "Handle a taxi, a delay, a parking spat"),
            ("07", "In hotel", "At the hotel", "Handle a room complaint politely"),
            ("08", "Al ristorante 2", "At the trattoria", "Discuss the menu with the waiter"),
            ("09", "Il caffè lungo", "At the café", "Small talk with a barista"),
            ("10", "Un piccolo litigio", "A small argument", "Assert yourself politely"),
            ("11", "Al telefono 2", "Formal phone", "Handle a work-adjacent call"),
            ("12", "Una giornata piena", "A full day", "Recount a Roman day in Italian"),
        ],
        "outcomes": [
            "Handle a taxi, a bank, a post office, a pharmacy without English",
            "Describe an ache to a pharmacist or a doctor",
            "Order and discuss with a waiter in native register",
            "Assert yourself politely in a small disagreement",
            "Recount your day in fluent, unhesitating Italian",
        ],
    },
    "ps3": {
        "slug": "pages/spoken/ps3.html", "code": "PS3", "track": "Parliamo Italiano",
        "cefr_from": "Beginner", "cefr_to": "Elementary", "name": "Elementary",
        "subtitle": "Telling your day",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Parliamo · Elementary.</span><br>Twelve weeks of the past tense.',
        "hero_sub": "For learners who can order but cannot yet recount. Twelve spoken sessions on the passato prossimo and the imperfetto — the two tenses Italians use to tell each other stories. With Luca Moretti, live from Venezia.",
        "poster": "hero-italian-life.jpg", "video": "venezia-canal.mp4",
        "right_img": "zoom-classroom-chiara.jpg",
        "right_caption": "Luca Moretti · live from Venezia",
        "teacher_slug": "luca", "teacher_name": "Luca Moretti", "teacher_city": "Venezia",
        "teacher_bio": "Luca teaches from a small room above a canal. His Parliamo groups leave able to tell a five-minute story about their last week with the tense-work of a native.",
        "env_img": "env-giulia-kitchen.jpg",
        "life_hero": "life-gondola-venezia.jpg",
        "syllabus": [
            ("01", "Il passato prossimo", "Past · avere", "Recount yesterday"),
            ("02", "Il passato prossimo · essere", "Past · essere", "Recount a walk"),
            ("03", "L'imperfetto", "Imperfect", "Describe a childhood scene"),
            ("04", "Passato vs imperfetto", "Aspect", "Tell a story properly"),
            ("05", "Un weekend a Roma", "Weekend story", "Recount a Roman weekend"),
            ("06", "Un pranzo di famiglia", "Family lunch", "Recount a Sunday lunch"),
            ("07", "Un viaggio", "A trip", "Retell a holiday in Italian"),
            ("08", "Un incontro", "A meeting", "Recount how you met a person"),
            ("09", "Un piccolo disastro", "A small disaster", "Recount a comedic mishap"),
            ("10", "Una serata memorabile", "A memorable night", "Extended past narrative"),
            ("11", "Una decisione", "A decision", "Discuss why you made a choice"),
            ("12", "Racconto libero", "Open storytelling", "Tell any five-minute story"),
        ],
        "outcomes": [
            "Move fluidly between passato prossimo and imperfetto",
            "Tell a five-minute story with pacing and detail",
            "Describe your childhood scenes with an Italian ear",
            "Recount a comedic mishap that will make an Italian laugh",
            "Sound less like a translator and more like a storyteller",
        ],
    },
    "ps4": {
        "slug": "pages/spoken/ps4.html", "code": "PS4", "track": "Parliamo Italiano",
        "cefr_from": "Elementary", "cefr_to": "Confident", "name": "Confident",
        "subtitle": "Holding your ground",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">Parliamo · Confident.</span><br>Twelve weeks of arguing in Italian.',
        "hero_sub": "For learners who can tell a story and want to hold an opinion. Twelve spoken sessions on register, opinion, and how to disagree with an Italian without losing them.",
        "poster": "hero-teacher-live.jpg", "video": "opera-scala.mp4",
        "right_img": "zoom-classroom-marco.jpg",
        "right_caption": "Marco Rinaldi · live from Trastevere",
        "teacher_slug": "marco", "teacher_name": "Marco Rinaldi", "teacher_city": "Roma",
        "teacher_bio": "Marco teaches the fourth spoken level with the calm of a man who has heard every wrong subjunctive. His Parliamo Confident class finishes the year with a full-length staged debate in Italian.",
        "env_img": "env-marco-desk.jpg",
        "life_hero": "life-scala-milano.jpg",
        "syllabus": [
            ("01", "Opinioni · introducing", "According to me", "State an opinion cleanly"),
            ("02", "Sfumature", "Nuance", "Qualify a strong statement"),
            ("03", "Il congiuntivo — spoken", "Subjunctive in speech", "Sound native under doubt"),
            ("04", "Disaccordo cortese", "Polite disagreement", "Disagree without offending"),
            ("05", "Convincere qualcuno", "Persuasion", "Change someone's mind"),
            ("06", "Il registro alto", "High register", "Sound like a Corriere reader"),
            ("07", "Il registro basso", "Low register", "Sound like a Roman waiter"),
            ("08", "Cambiare argomento", "Changing topic", "Handle a conversational pivot"),
            ("09", "Interrompere", "Interrupting", "Interrupt like an Italian"),
            ("10", "Cibo · discussione", "Food debate", "Argue about carbonara"),
            ("11", "Cinema · discussione", "Film debate", "Argue about a film"),
            ("12", "Il dibattito finale", "Final debate", "20-minute assessed debate"),
        ],
        "outcomes": [
            "State and defend an opinion in native register",
            "Disagree with an Italian without offending them",
            "Interrupt fluidly, change subject cleanly, change your mind visibly",
            "Argue about food and film with the passion of the inhabitants",
            "Finish the term with a 20-minute debate in front of the group",
        ],
    },

    # ---- Capsule Culturali ----
    "cap-food": {
        "slug": "pages/culture/cap-food.html", "code": "CAP-FOOD", "track": "Capsule · Culturali",
        "cefr_from": "A1+", "cefr_to": "Cultural competence", "name": "La Cucina Italiana",
        "subtitle": "Regions on a plate",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">La Cucina Italiana.</span><br>Six weeks of Italian, taught by six dishes.',
        "hero_sub": "A capsule culture course for intermediate learners. Six live sessions on the regions of Italian cooking — Roma, Bologna, Napoli, Palermo, Firenze, Milano — taught inside the kitchen of Giulia Ferrari, live from Bologna.",
        "poster": "hero-cucina-italiana.jpg", "video": "cucina-pasta.mp4",
        "right_img": "env-giulia-kitchen.jpg",
        "right_caption": "Giulia Ferrari · from her kitchen in Bologna",
        "teacher_slug": "giulia", "teacher_name": "Giulia Ferrari", "teacher_city": "Bologna",
        "teacher_bio": "Giulia was raised in Bologna and cooks the way she teaches: with respect. Her capsule brings ingredients, dishes, and philosophy into six unhurried Italian evenings.",
        "env_img": "env-giulia-kitchen.jpg",
        "life_hero": "life-trattoria-toscana.jpg",
        "syllabus": [
            ("01", "Roma · Carbonara e Amatriciana", "Regional Italian · Roma", "Argue about guanciale"),
            ("02", "Bologna · Ragù e Tortellini", "Regional Italian · Emilia", "Read a Bolognese recipe aloud"),
            ("03", "Napoli · Pizza e Ragù", "Regional Italian · Campania", "Discuss the pizza vera"),
            ("04", "Palermo · Sardine e Pasta con le sarde", "Regional Italian · Sicilia", "Read a Sicilian menu"),
            ("05", "Firenze · Bistecca e Ribollita", "Regional Italian · Toscana", "Order a full Tuscan dinner"),
            ("06", "Milano · Risotto e Ossobuco", "Regional Italian · Lombardia", "Discuss the risotto giallo"),
        ],
        "outcomes": [
            "Read any Italian menu with regional confidence",
            "Discuss regional cuisine with a native waiter",
            "Argue civilly about the correct carbonara",
            "Cook and discuss six classic Italian dishes in Italian",
            "Understand the philosophy behind Italian food regionalism",
        ],
    },
    "cap-art": {
        "slug": "pages/culture/cap-art.html", "code": "CAP-ART", "track": "Capsule · Culturali",
        "cefr_from": "A1+", "cefr_to": "Cultural competence", "name": "L'Arte del Rinascimento",
        "subtitle": "Reading a Renaissance canvas",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">L\'Arte del Rinascimento.</span><br>Six weeks of Italian, in front of six paintings.',
        "hero_sub": "A capsule culture course for intermediate learners. Six live sessions in the language of the Uffizi — Botticelli, Leonardo, Michelangelo, Raffaello, Caravaggio, and one late surprise. With Chiara Bianchi, live from Firenze.",
        "poster": "hero-italian-life.jpg", "video": "firenze-arno.mp4",
        "right_img": "life-uffizi-hall.jpg",
        "right_caption": "A hall in the Uffizi",
        "teacher_slug": "chiara", "teacher_name": "Chiara Bianchi", "teacher_city": "Firenze",
        "teacher_bio": "Chiara reads paintings the way Florentines have for six centuries: closely. Her capsule turns six masterpieces into six evenings of Italian and cultural competence.",
        "env_img": "env-chiara-desk.jpg",
        "life_hero": "life-uffizi-hall.jpg",
        "syllabus": [
            ("01", "Botticelli · Primavera", "Reading a canvas · vocabulary", "Describe a painting in Italian"),
            ("02", "Leonardo · Annunciazione", "Composition · perspective", "Discuss Leonardo in Italian"),
            ("03", "Michelangelo · Tondo Doni", "Muscular painting", "Describe the human figure"),
            ("04", "Raffaello · Madonna del Cardellino", "Grace · balance", "Read a Madonna scene"),
            ("05", "Caravaggio · Bacchino malato", "Chiaroscuro · realism", "Discuss shadow and light"),
            ("06", "Il tardo Rinascimento", "Late Renaissance", "Guide a friend through an Uffizi room"),
        ],
        "outcomes": [
            "Describe a painting in Italian with technical vocabulary",
            "Discuss the Florentine Renaissance in native register",
            "Read a museum caption without a phone",
            "Guide a visiting friend through an Uffizi room in Italian",
            "Understand why Italians speak about art the way they do",
        ],
    },
    "cap-opera": {
        "slug": "pages/culture/cap-opera.html", "code": "CAP-OPERA", "track": "Capsule · Culturali",
        "cefr_from": "A1+", "cefr_to": "Cultural competence", "name": "L'Opera in Italiano",
        "subtitle": "From La Scala with a libretto",
        "hero_headline": '<span class="accent-ital" style="font-style:italic;color:#E6C99B">L\'Opera in Italiano.</span><br>Six weeks of Italian, sung.',
        "hero_sub": "A capsule culture course for intermediate learners. Six live sessions on the Italian of Verdi, Puccini, Rossini, and Donizetti — read as libretti, discussed in Italian, understood in context. With Alessandro Conti, live from Milano.",
        "poster": "hero-italian-life.jpg", "video": "opera-scala.mp4",
        "right_img": "life-scala-milano.jpg",
        "right_caption": "La Scala di Milano at dusk",
        "teacher_slug": "alessandro", "teacher_name": "Alessandro Conti", "teacher_city": "Milano",
        "teacher_bio": "Alessandro is a Scala regular and a teacher of high register. His capsule reads six of the great Italian opera libretti as literature, and hands you the language they were built from.",
        "env_img": "env-marco-desk.jpg",
        "life_hero": "life-scala-milano.jpg",
        "syllabus": [
            ("01", "Verdi · La Traviata", "Verdi · aria vocabulary", "Follow a Traviata scene"),
            ("02", "Puccini · La Bohème", "Puccini · lyrical Italian", "Read Rodolfo's aria aloud"),
            ("03", "Rossini · Il Barbiere di Siviglia", "Rossini · comic register", "Follow a Rossini duet"),
            ("04", "Donizetti · L'elisir d'amore", "Donizetti · pastoral", "Discuss the aria 'Una furtiva lagrima'"),
            ("05", "Verdi · Rigoletto", "Tragic Italian", "Follow 'La donna è mobile' in context"),
            ("06", "Puccini · Turandot", "Late Puccini", "Follow 'Nessun dorma' and its meaning"),
        ],
        "outcomes": [
            "Read a libretto page as Italian, not as translation",
            "Discuss Verdi, Puccini and Rossini in high register",
            "Follow a broadcast opera without the surtitles",
            "Understand why 'la donna è mobile' is not the whole story",
            "Attend La Scala with a libretto in your hand and follow it",
        ],
    },
}

# ============================================================
# FOLD BUILDERS FOR COURSE PAGES
# ============================================================
def fold_stats(c):
    lessons = 12 if c["code"].startswith("PS") else (6 if c["code"].startswith("CAP") else 40)
    minutes = 60 if c["code"].startswith("PS") else (75 if c["code"].startswith("CAP") else 85)
    seats = "10–12"
    return f"""<section class="section-cream" style="padding:3rem 0;border-bottom:1px solid rgba(0,0,0,.06)">
  <div class="wrap" style="display:grid;grid-template-columns:repeat(5,1fr);gap:0;text-align:center">
    <div style="padding:1.4rem 1rem;border-right:1px solid rgba(0,0,0,.08)"><div style="font-family:'Playfair Display',serif;font-size:2rem;color:#166A47">{c['cefr_from']} → {c['cefr_to']}</div><div style="font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.35rem">CEFR span</div></div>
    <div style="padding:1.4rem 1rem;border-right:1px solid rgba(0,0,0,.08)"><div style="font-family:'Playfair Display',serif;font-size:2rem;color:#166A47">{lessons}</div><div style="font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.35rem">Live lessons</div></div>
    <div style="padding:1.4rem 1rem;border-right:1px solid rgba(0,0,0,.08)"><div style="font-family:'Playfair Display',serif;font-size:2rem;color:#166A47">{minutes} min</div><div style="font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.35rem">Each session</div></div>
    <div style="padding:1.4rem 1rem;border-right:1px solid rgba(0,0,0,.08)"><div style="font-family:'Playfair Display',serif;font-size:2rem;color:#166A47">{seats}</div><div style="font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.35rem">Classmates</div></div>
    <div style="padding:1.4rem 1rem"><div style="font-family:'Playfair Display',serif;font-size:2rem;color:#166A47">Native</div><div style="font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7168;margin-top:.35rem">In-Italy teacher</div></div>
  </div>
</section>"""

def fold_promise(c):
    return f"""<section class="section-cream" style="padding:clamp(4.5rem,9vw,8rem) 0">
  <div class="wrap-narrow" style="text-align:center">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">The promise of this course</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.6rem,5.4vw,4.4rem);line-height:1.05;color:#0e1a14;margin:0 0 1.6rem">By the end of {c['name']}, <span class="accent-ital" style="font-style:italic;color:#166A47">you will not be a beginner in {c['name'].lower()} Italian anymore.</span></h2>
    <p style="font-size:1.2rem;line-height:1.65;color:#3a3f3a;max-width:64ch;margin:0 auto">{c['hero_sub']}</p>
  </div>
</section>"""

def fold_syllabus(c):
    rows = "".join(f"""<div class="sr-row" style="display:grid;grid-template-columns:80px 1.3fr 1fr 1fr;gap:1.4rem;padding:1.2rem 0;border-bottom:1px solid rgba(0,0,0,.06);align-items:baseline">
      <div style="font-family:'Playfair Display',serif;font-style:italic;color:#E6C99B;font-size:1.2rem">{n}</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.15rem;color:#0e1a14">{t}</div>
      <div style="font-size:.9rem;color:#6b7168">{g}</div>
      <div style="font-size:.9rem;color:#3a3f3a;font-style:italic">{o}</div>
    </div>""" for n, t, g, o in c["syllabus"])
    return f"""<section class="section-white" style="padding:clamp(5rem,9vw,8rem) 0">
  <div class="wrap">
    <div style="max-width:820px;margin-bottom:2.6rem">
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">The syllabus, week by week</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0">Every session, <span class="accent-ital" style="font-style:italic;color:#166A47">on record.</span></h2>
    </div>
    <div style="display:grid;grid-template-columns:80px 1.3fr 1fr 1fr;gap:1.4rem;padding:.8rem 0;border-bottom:1px solid rgba(0,0,0,.15);font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:#6b7168">
      <div>#</div><div>Lesson</div><div>Grammar and vocabulary</div><div>You'll be able to</div>
    </div>
    {rows}
  </div>
</section>"""

def fold_teacher(c):
    return f"""<section class="section-cream" style="padding:clamp(5rem,9vw,8rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(2rem,4vw,4rem);align-items:center">
    <figure style="margin:0;display:grid;grid-template-columns:1fr 1fr;gap:1rem">
      <img src="{A_}img/teacher-{c['teacher_slug']}.jpg" alt="{c['teacher_name']}" style="width:100%;aspect-ratio:3/4;object-fit:cover;box-shadow:0 30px 80px -20px rgba(14,26,20,.35)">
      <img src="{A_}img/{c['env_img']}" alt="{c['teacher_name']}'s teaching studio" style="width:100%;aspect-ratio:3/4;object-fit:cover;box-shadow:0 30px 80px -20px rgba(14,26,20,.35)">
    </figure>
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">Your teacher</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.4vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0 0 1rem">{c['teacher_name']},<br><span class="accent-ital" style="font-style:italic;color:#166A47">live from {c['teacher_city']}.</span></h2>
      <p style="font-size:1.12rem;line-height:1.65;color:#3a3f3a;max-width:44ch">{c['teacher_bio']}</p>
    </div>
  </div>
  <style>@media(max-width:820px){{[style*="1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""

def fold_outcomes(c):
    lis = "".join(f'<li style="padding:1.1rem 0;border-bottom:1px solid rgba(255,255,255,.1);color:rgba(251,250,246,.9);font-size:1.1rem;line-height:1.5;display:flex;gap:1.2rem;align-items:baseline"><span style="color:#E6C99B;font-family:\'Playfair Display\',serif;font-style:italic;font-size:1.4rem;flex-shrink:0">{i+1:02d}</span><span>{o}</span></li>' for i, o in enumerate(c["outcomes"]))
    return f"""<section class="section-green" style="padding:clamp(5rem,9vw,8rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:clamp(2.4rem,5vw,5rem);align-items:start">
    <div>
      <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">By the end of {c['name']}</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.4rem,5vw,4rem);line-height:1.05;color:#FBFAF6;margin:0 0 1.6rem">Five things you will <span class="accent-ital" style="font-style:italic;color:#E6C99B">actually be able to do.</span></h2>
      <p style="font-size:1.1rem;line-height:1.6;color:rgba(251,250,246,.8);max-width:46ch">Not "gain exposure to". Not "become familiar with". Each of the five outcomes below is assessed live, on video, with a native speaker.</p>
    </div>
    <ul style="list-style:none;padding:0;margin:0">{lis}</ul>
  </div>
  <style>@media(max-width:820px){{[style*="1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""

def fold_cultural_context(c):
    return f"""<section class="section-cream" style="padding:clamp(5rem,9vw,8rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(2.4rem,5vw,5rem);align-items:center">
    <figure style="margin:0">
      <div style="aspect-ratio:4/5;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
        <img src="{A_}img/{c['life_hero']}" alt="A moment of {c['teacher_city']} life" style="width:100%;height:100%;object-fit:cover">
      </div>
    </figure>
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">The culture behind the classroom</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0 0 1.4rem">Not a language. <span class="accent-ital" style="font-style:italic;color:#166A47">A way of living.</span></h2>
      <p style="font-size:1.12rem;line-height:1.65;color:#3a3f3a;max-width:48ch;margin:0">Every Club Italia session is set inside a piece of Italian daily life. This course is scored to {c['teacher_city']} — its cafés, its markets, its small rituals of politeness. You learn the words the way an Italian learned them: because someone said them to you first.</p>
    </div>
  </div>
  <style>@media(max-width:820px){{[style*="1.1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""

def fold_biagio_inline():
    return f"""<section class="section-red" style="padding:clamp(4.5rem,9vw,8rem) 0;overflow:hidden">
  <div class="wrap" style="display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(2rem,4vw,4rem);align-items:center">
    <div style="position:relative">
      <div style="position:absolute;inset:-20%;background:radial-gradient(circle at center, rgba(230,201,155,.28), transparent 60%);pointer-events:none"></div>
      <img src="{A_}img/biagio.png" alt="Biagio, the AI Italian tutor" style="width:100%;max-width:340px;position:relative;filter:drop-shadow(0 30px 60px rgba(0,0,0,.5))">
    </div>
    <div>
      <div class="eyebrow" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">Between sessions</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#FBFAF6;margin:0 0 1.4rem">And between classes, <span class="accent-ital" style="font-style:italic;color:#E6C99B">Biagio.</span></h2>
      <p style="font-size:1.1rem;line-height:1.6;color:rgba(251,250,246,.86);max-width:52ch;margin:0 0 1.6rem">Biagio is your after-hours Italian tutor. Trained on the exact syllabus of this course. Available at every hour of every day. Included in your enrollment.</p>
      <a class="btn btn-3d btn-3d-primary" href="{A_}../biagio.html">Meet Biagio</a>
    </div>
  </div>
  <style>@media(max-width:820px){{[style*=".85fr 1.15fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""

def fold_pricing_inline():
    return f"""<section class="section-white" style="padding:clamp(5rem,9vw,8rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:2.6rem">
    <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">Enrolment</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0 auto;max-width:22ch">Three ways to <span class="accent-ital" style="font-style:italic;color:#166A47">say yes.</span></h2>
  </div>
  <div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem">
    <div style="background:#fff;border:1px solid rgba(0,0,0,.1);padding:2rem 1.6rem;display:flex;flex-direction:column;gap:1rem">
      <div style="font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:#166A47;font-weight:600">Monthly</div>
      <div style="font-family:'Playfair Display',serif;font-size:3rem;color:#0e1a14;line-height:1">$84<span style="font-size:1rem;color:#6b7168;font-style:italic;margin-left:.4rem">/wk</span></div>
      <p style="font-size:.95rem;color:#3a3f3a;margin:0">Rolling month, cancel at any time.</p>
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="margin-top:auto">Reserve My Placement Call</button>
    </div>
    <div style="position:relative;background:#fff;border:2px solid #166A47;padding:2rem 1.6rem;display:flex;flex-direction:column;gap:1rem">
      <div style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:#166A47;color:#fff;padding:.4rem 1rem;font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;font-weight:600;white-space:nowrap">Best Value · Save $440</div>
      <div style="font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:#166A47;font-weight:600">Annual · 12 months</div>
      <div style="font-family:'Playfair Display',serif;font-size:3rem;color:#0e1a14;line-height:1">$62<span style="font-size:1rem;color:#6b7168;font-style:italic;margin-left:.4rem">/wk</span></div>
      <p style="font-size:.95rem;color:#3a3f3a;margin:0">Priority scheduling and Capsule Culturali included.</p>
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="margin-top:auto">Reserve My Placement Call</button>
    </div>
    <div style="background:#fff;border:1px solid rgba(0,0,0,.1);padding:2rem 1.6rem;display:flex;flex-direction:column;gap:1rem">
      <div style="font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:#166A47;font-weight:600">Term · 4 months</div>
      <div style="font-family:'Playfair Display',serif;font-size:3rem;color:#0e1a14;line-height:1">$73<span style="font-size:1rem;color:#6b7168;font-style:italic;margin-left:.4rem">/wk</span></div>
      <p style="font-size:.95rem;color:#3a3f3a;margin:0">One CEFR level, cover to cover.</p>
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="margin-top:auto">Reserve My Placement Call</button>
    </div>
  </div>
  <style>@media(max-width:960px){{.section-white [style*="repeat(3,1fr)"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""

def fold_certificate():
    return f"""<section class="section-cream" style="padding:clamp(5rem,9vw,8rem) 0">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(2.4rem,5vw,5rem);align-items:center">
    <div>
      <div class="eyebrow" style="color:#166A47;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.4rem">On graduation</div>
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2.2rem,4.6vw,3.6rem);line-height:1.05;color:#0e1a14;margin:0 0 1.4rem">A CEFR certificate. <span class="accent-ital" style="font-style:italic;color:#166A47">A printed one.</span></h2>
      <p style="font-size:1.12rem;line-height:1.65;color:#3a3f3a;max-width:52ch;margin:0">Every completed track ends with a printed, signed Club Italia certificate stating your CEFR level, your teacher, and your cohort. Not a screenshot. A document.</p>
    </div>
    <figure style="margin:0">
      <div style="aspect-ratio:4/5;overflow:hidden;box-shadow:0 40px 100px -30px rgba(14,26,20,.35)">
        <img src="{A_}img/env-chiara-desk.jpg" alt="A Club Italia certificate on a warm wooden table" style="width:100%;height:100%;object-fit:cover">
      </div>
    </figure>
  </div>
  <style>@media(max-width:820px){{[style*="1.1fr 1fr"]{{grid-template-columns:1fr!important}}}}</style>
</section>"""

def fold_faq_short():
    faqs = [
        ("What if I miss a class?", "Every session is recorded and uploaded to your course page within 24 hours. You retain access to your recordings for the life of your enrollment."),
        ("Can I switch levels?", "Yes, within your first four weeks, at no cost. Beyond that, we reassess at the start of every new term and transfers remain free."),
        ("What technology do I need?", "A laptop or tablet with a camera, a stable internet connection, and a quiet room. If you can join a video call, you can attend Club Italia."),
        ("Do you offer a refund?", "Yes. You have seven days from your first live class to request a full refund."),
        ("What is the placement call?", "A 20-minute video call with an academic advisor to place you in the correct level. No test, no fee, no obligation."),
    ]
    items = "".join(f"""<details style="border-bottom:1px solid rgba(0,0,0,.1);padding:1.4rem 0;cursor:pointer">
      <summary style="display:flex;justify-content:space-between;gap:1.4rem;font-family:'Playfair Display',serif;font-size:1.2rem;color:#0e1a14;list-style:none;cursor:pointer"><span>{q}</span><span style="color:#E6C99B;font-size:1.5rem;line-height:1" class="faq-plus">+</span></summary>
      <div style="padding-top:1rem;font-size:1rem;line-height:1.6;color:#3a3f3a">{a}</div>
    </details>""" for q, a in faqs)
    return f"""<section class="section-tint" style="padding:clamp(4.5rem,9vw,8rem) 0;background:#F4EFE5">
  <div class="wrap-narrow">
    <div style="text-align:center;margin-bottom:2.4rem">
      <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2rem,4.4vw,3.4rem);line-height:1.05;color:#0e1a14;margin:0">Questions worth asking.</h2>
    </div>
    {items}
    <div style="text-align:center;margin-top:2rem"><a href="{A_}../faq.html" style="color:#166A47;font-size:.8rem;letter-spacing:.22em;text-transform:uppercase;font-weight:600">All FAQs →</a></div>
  </div>
</section>"""

def fold_teacher_wall_mini():
    teachers_data = [
        ("chiara", "Chiara", "Firenze"), ("marco", "Marco", "Roma"),
        ("giulia", "Giulia", "Bologna"), ("alessandro", "Alessandro", "Milano"),
        ("francesca", "Francesca", "Napoli"), ("luca", "Luca", "Venezia"),
        ("sofia", "Sofia", "Palermo"),
    ]
    cards = "".join(f'''<a href="{A_}../teachers.html" style="text-decoration:none;color:inherit;position:relative;aspect-ratio:3/4;overflow:hidden;background:#000;display:block">
      <img src="{A_}img/teacher-{s}.jpg" alt="{n}" style="width:100%;height:100%;object-fit:cover;filter:grayscale(.1)">
      <div style="position:absolute;left:0;right:0;bottom:0;padding:.9rem 1rem;background:linear-gradient(transparent,rgba(0,0,0,.85));color:#FBFAF6">
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem">{n}</div>
        <div style="font-family:'Playfair Display',serif;font-style:italic;color:#E6C99B;font-size:.85rem">{c}</div>
      </div>
    </a>''' for s, n, c in teachers_data)
    return f"""<section class="section-black" style="padding:clamp(4.5rem,9vw,8rem) 0">
  <div class="wrap" style="text-align:center;margin-bottom:2.4rem">
    <div class="eyebrow paper" style="color:#E6C99B;letter-spacing:.28em;font-size:.78rem;text-transform:uppercase;margin-bottom:1.2rem">The seven teachers</div>
    <h2 style="font-family:'Playfair Display',serif;font-weight:700;font-size:clamp(2rem,4.4vw,3.4rem);line-height:1.05;color:#FBFAF6;margin:0">Seven cities. <span class="accent-ital" style="font-style:italic;color:#E6C99B">One method.</span></h2>
  </div>
  <div class="wrap-flush" style="padding:0 clamp(1rem,2vw,2rem);display:grid;grid-template-columns:repeat(7,1fr);gap:2px">{cards}</div>
  <style>@media(max-width:1000px){{[style*="repeat(7,1fr)"]{{grid-template-columns:repeat(4,1fr)!important}}}}@media(max-width:600px){{[style*="repeat(7,1fr)"]{{grid-template-columns:repeat(2,1fr)!important}}}}</style>
</section>"""

# ============================================================
# ASSEMBLE
# ============================================================
def build_course(c):
    title = f"{c['name']} · {c['track']} · Club Italia"
    desc = f"{c['name']}: {c['subtitle']}. {c['cefr_from']} to {c['cefr_to']}. Live from Italy with {c['teacher_name']}. Club Italia."

    html = head(title, desc, depth=D) + "\n" + NAV + "\n"
    # F1 — Hero
    html += hero_cinematic(A_, c["video"], c["poster"],
                            f"{c['track']} · {c['cefr_from']} → {c['cefr_to']}",
                            c["hero_headline"], c["hero_sub"],
                            cta_ghost=("View the syllabus", "#syllabus"),
                            right_img=c["right_img"], right_caption=c["right_caption"]) + "\n"
    # F2 — stats strip
    html += fold_stats(c) + "\n"
    # F3 — promise
    html += fold_promise(c) + "\n"
    # F4 — live classroom
    zoom_img = "zoom-classroom-chiara.jpg" if c["teacher_slug"] in ("chiara", "luca", "alessandro") else "zoom-classroom-marco.jpg"
    html += zoom_class_fold(A_, img=zoom_img,
                            caption=f"{c['teacher_name']}, live from {c['teacher_city']} · 11 students, one hand raised.",
                            bg="cream") + "\n"
    # F5 — syllabus
    html = html.replace('<section class="section-white" style="padding:clamp(5rem,9vw,8rem) 0">\n  <div class="wrap">\n    <div style="max-width:820px;margin-bottom:2.6rem">\n      <div class="eyebrow"',
                         '<section id="syllabus" class="section-white" style="padding:clamp(5rem,9vw,8rem) 0">\n  <div class="wrap">\n    <div style="max-width:820px;margin-bottom:2.6rem">\n      <div class="eyebrow"', 1)
    html += fold_syllabus(c) + "\n"
    # F6 — teacher
    html += fold_teacher(c) + "\n"
    # F7 — cultural context
    html += fold_cultural_context(c) + "\n"
    # F8 — outcomes (dark green)
    html += fold_outcomes(c) + "\n"
    # F9 — biagio inline (red)
    html += fold_biagio_inline() + "\n"
    # F10 — life grid (ivory)
    html += life_grid_fold(A_, bg="cream") + "\n"
    # F11 — trustpilot (white)
    html += trustpilot_wall(A_) + "\n"
    # F12 — certificate
    html += fold_certificate() + "\n"
    # F13 — pricing
    html += fold_pricing_inline() + "\n"
    # F14 — teacher wall mini (black) then FAQ
    html += fold_teacher_wall_mini() + "\n"
    html += fold_faq_short() + "\n"
    # F15 — final CTA green
    html += cta_final(bg="green",
                      headline_html=f'Ready to say <span class="accent-ital" style="font-style:italic;color:#E6C99B">{c["name"].lower()}?</span>',
                      sub="Twenty minutes with an academic advisor. No aptitude test, no pressure. Just a plan for the year of Italian ahead of you.") + "\n"
    html += FOOT

    from pathlib import Path
    (ROOT / c["slug"]).write_text(html)
    return len(html)

if __name__ == "__main__":
    for key, c in COURSES.items():
        size = build_course(c)
        print(f"{c['slug']} · {size} bytes · 15 folds")
