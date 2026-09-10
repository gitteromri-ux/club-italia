#!/usr/bin/env python3
"""
Rebuilds every CI course page to full editorial depth.
Reads: /home/user/workspace/club-italia/research/course-data.json
Writes: /home/user/workspace/club-italia/pages/{courses,spoken,culture}/*.html
"""

import json, os, html, textwrap

ROOT = "/home/user/workspace/club-italia"
DATA = json.load(open(f"{ROOT}/research/course-data.json"))

# --- Per-course editorial payload (regional flavour + folds 3-11 content) ---

COURSE_META = {
    "ci1": {
        "slug": "ci1", "path": "pages/courses/ci1.html", "up": "../..",
        "code": "CI · 01", "hero_video_poster": "course-ci1.jpg",
        "region_photo": "course-ci1.jpg",
        "prev": None, "next": ("ci2", "CI Elementare", "A1.1 → A1.2 · Firenze"),
        "teacher": {
            "name": "Chiara Baldini", "img": "teacher-chiara.jpg",
            "region": "Roma · Trastevere",
            "role": "Native teacher · Sapienza-trained linguist",
            "bio": "Chiara grew up between the courtyards of Trastevere and the classrooms of Sapienza. For a decade she has taught adult learners how to walk into a Roman café and be served in Italian on the first try. Her method starts with the sound of the language, then the rhythm, and only then the rules.",
            "quote": "In Roma we say the language begins when you stop apologising for your accent. That is lesson one.",
            "creds": "MA Italian Linguistics · Sapienza · CEDILS certified · 11 years teaching adults"
        },
        "city_name": "Rome", "city_italian": "Roma",
        "city_paragraphs": [
            "Rome is where the Italian language was born, argued about, put on trial, and finally set free. We start here because every other Italian city is, in some way, in conversation with Rome — its Latin roots, its Renaissance humanists, its trattorie shouting orders across a piazza at seven in the evening.",
            "A0 belongs to Rome because Rome forgives. Romans are patient in a way northerners often are not. They will slow down, they will repeat, they will laugh with you, not at you. If you are going to make your first mistakes in Italian, make them under a Roman sky, in a Roman café, with a Roman waiter who has heard every mispronunciation of espresso ever attempted.",
            "Every lesson is threaded through the city: the market at Campo de' Fiori, the trams of Trastevere, the tram terminus at Piazza Venezia, a Sunday lunch in a family kitchen in Testaccio. You are not learning tourist Italian. You are learning to belong."
        ],
        "pillars": [
            ("La città come aula", "The classroom is Rome itself. Every dialogue, every audio clip, every reading is filmed and recorded in a real Roman location — from Fiumicino arrivals to a bakery in Monti."),
            ("Il metodo dell'orecchio", "We start with the ear. Ten minutes of every lesson is pure listening: real Italians, real cadence, then imitation. Grammar arrives once your mouth remembers the shape of the language."),
            ("Un insegnante, una città", "Chiara teaches every one of your twenty lessons. No rotating strangers. She learns your voice, corrects your habits, and by lesson six knows exactly which sound you keep flattening.")
        ],
        "week_rhythm": [
            ("Monday", "Live Lesson", "The 85-minute live class with Chiara. Small group of ten to twelve. Cameras on, coffee in hand."),
            ("Wednesday", "Studio Guidato", "A 20-minute private study session on the week's grammar point, with instant feedback from Biagio, our AI tutor."),
            ("Friday", "Ora di Conversazione", "A 30-minute optional conversation salon with your groupmates. Chiara joins from Trastevere."),
            ("Weekend", "Roma dal Vivo", "A short film — a real Roman location, real dialogue, subtitles you can toggle. Watch it Sunday with a coffee.")
        ],
        "sample": {
            "title": "Lesson 02 · A un caffè romano",
            "setting": "A tavolo at Sant'Eustachio, seven forty-five in the morning. The barista, Marco, has seen you three days in a row.",
            "dialogue": [
                ("Marco", "Buongiorno! Il solito?"),
                ("Tu", "Buongiorno Marco. Sì, un cappuccino e un cornetto, per favore."),
                ("Marco", "Alla crema o al cioccolato?"),
                ("Tu", "Al cioccolato. Grazie."),
                ("Marco", "Ecco a te. Uno e ottanta.")
            ],
            "note": "Notice the shift from 'Lei' at first contact to 'tu' by day three. Rome moves through formality faster than the textbooks admit."
        },
        "testimonials": [
            ("“I arrived in Rome for a wedding three weeks after my last lesson and ordered dinner in Italian, argued gently with a taxi driver about a fare, and got a compliment from a nonna. That is what Chiara built.”", "Sarah W.", "London · CI Principiante · Spring 2026"),
            ("“Twenty lessons. Twenty. And I can now understand my Italian mother-in-law when she is not making an effort to slow down. That is a miracle.”", "David K.", "Boston · CI Principiante · Winter 2026"),
            ("“Chiara does not teach Italian. She teaches you how to be a person in Italian. There is a difference and it is enormous.”", "Ana P.", "São Paulo · CI Principiante · Autumn 2025")
        ],
        "promise_headline": "Twenty lessons. One <span class='gold-ital'>Roman</span> voice.",
        "promise_lede": "A0 to A1.1 is the leap where Italian stops being a series of memorised phrases and starts being a way of speaking. This is the course that gets you there.",
        "different_headline": "What makes <span class='gold-ital'>Principiante</span> different",
        "different_lede": "Three things separate this course from every A0 Italian class you have tried before.",
        "city_eyebrow": "The city is the classroom",
        "city_headline": "Why <span class='gold-ital'>Roma</span> teaches the first word",
        "city_lede": "A0 belongs to Rome for the same reason the Republic did: nowhere else forgives beginnings as generously.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "A morning at <span class='gold-ital'>Sant'Eustachio</span>",
        "final_headline": "Say your first sentence in <span class='gold-ital'>Italiano</span>.",
        "final_sub": "Twenty live lessons with Chiara, from Fiumicino to a Sunday lunch in Testaccio. Small group. Lifetime recordings. Certificate on the wall.",
        "start_date": "6 October 2026",
    },
    "ci2": {
        "slug": "ci2", "path": "pages/courses/ci2.html", "up": "../..",
        "code": "CI · 02", "hero_video_poster": "course-ci2.jpg",
        "region_photo": "course-ci2.jpg",
        "prev": ("ci1", "CI Principiante", "A0 → A1.1 · Roma"),
        "next": ("ci3", "CI Intermedio", "A1.2 → A2.1 · Bologna"),
        "teacher": {
            "name": "Alessandro Fiorini", "img": "teacher-alessandro.jpg",
            "region": "Firenze · Oltrarno",
            "role": "Native teacher · former Accademia della Crusca researcher",
            "bio": "Alessandro spent four years at the Accademia della Crusca, the four-hundred-year-old institution that quietly guards the Italian language. He now teaches what most Italians take for granted: why Florence is the city whose dialect became the country. His lessons feel like walking beside a friend who happens to know every etymology on every street sign.",
            "quote": "Dante wrote here. Machiavelli wrote here. Nobody in Firenze speaks like a book, and yet the language of books was invented here. That is the paradox I love to teach.",
            "creds": "MA Filologia · Università di Firenze · former Crusca junior fellow · 9 years teaching"
        },
        "city_name": "Florence", "city_italian": "Firenze",
        "city_paragraphs": [
            "Florence gave Italy its language. Not the Rome of the Popes, not the Milan of the merchants — Florence, because Dante wrote the Commedia in Tuscan, and every child from Sicily to Trentino has learned it since. When we say 'standard Italian' we are, in a very real sense, saying 'Florentine, softened for national use'.",
            "A1.1 to A1.2 is where you begin to feel the shape of the language: the past tense, the polite forms, the vocabulary of everyday errands. Florence is the perfect terrain for that shape, because Florentines are enormously proud of the precision of their speech and enormously willing to correct — gently — anyone who is trying.",
            "The course threads through the city: a morning at the Sant'Ambrogio market, a photography walk in the Oltrarno, an afternoon at a family-run trattoria where the menu has been the same since 1962. You will finish this term saying, and meaning, buongiorno as a Florentine does."
        ],
        "pillars": [
            ("La lingua di Dante, in strada", "Every lesson pairs a grammar point with a passage from Florentine daily life — a signed poster, a market receipt, a Manifesto pasted to a wall. You learn the language by reading the city."),
            ("Il passato prossimo, senza panico", "The passato prossimo is where most learners quit. We teach it as it is spoken in Florence — as a habit, not a rule — with hundreds of repetitions before you ever conjugate."),
            ("Un maestro fiorentino", "Alessandro teaches all twenty lessons. He was trained inside the Accademia della Crusca, the guardian body of the Italian language. You are, in the most literal sense, being taught by the source.")
        ],
        "week_rhythm": [
            ("Monday", "Lezione dal Vivo", "The 85-minute live class with Alessandro. Small group of ten to twelve, cameras on."),
            ("Wednesday", "Studio Guidato", "A 20-minute private study session with Biagio, our AI tutor, on the week's past-tense forms."),
            ("Friday", "Salotto Fiorentino", "A 30-minute conversation salon. Talk about your week in the passato prossimo. Alessandro joins from the Oltrarno."),
            ("Weekend", "Firenze in un Film", "A short weekend film shot in Florence — the Boboli gardens, a leather workshop, the Ponte Vecchio at dawn.")
        ],
        "sample": {
            "title": "Lesson 07 · Al mercato di Sant'Ambrogio",
            "setting": "A Tuesday morning at the produce stalls. La signora Rossi, who has run stall number 14 since 1988, sees you approach.",
            "dialogue": [
                ("Signora Rossi", "Buongiorno, cara. Cosa Le do oggi?"),
                ("Tu", "Buongiorno. Vorrei mezzo chilo di pomodori San Marzano, per favore."),
                ("Signora Rossi", "Belli maturi, guardi. Per stasera? Sugo?"),
                ("Tu", "Sì, ho invitato degli amici. Facciamo una pasta al pomodoro."),
                ("Signora Rossi", "Allora Le metto anche un mazzetto di basilico. Regalo mio.")
            ],
            "note": "The market is where the polite Lei-form comes alive. Florence uses it more than Rome, and this dialogue rehearses six polite constructions in seventy seconds."
        },
        "testimonials": [
            ("“Alessandro's love of Florence is contagious. I came in wanting to order gelato and left able to argue with a stallholder about the price of artichokes. In Italian. Politely.”", "Isabelle M.", "Montreal · CI Elementare · Winter 2026"),
            ("“The passato prossimo used to terrify me. Now I use it every time I tell my husband what I did during the day. That is quite the domestic transformation.”", "Priya S.", "New Delhi · CI Elementare · Spring 2026"),
            ("“I have taken three online Italian courses before this one. None of them made me feel Italian. This one did, by lesson eight.”", "Grant B.", "Melbourne · CI Elementare · Autumn 2025")
        ],
        "promise_headline": "Speak the Italian <span class='gold-ital'>Firenze</span> invented.",
        "promise_lede": "A1.1 to A1.2 is where phrases turn into sentences and sentences turn into a past you can talk about. Twenty lessons rooted in the city that gave Italy its language.",
        "different_headline": "What makes <span class='gold-ital'>Elementare</span> different",
        "different_lede": "Three reasons to learn A1.2 in Florence, and only in Florence.",
        "city_eyebrow": "The city is the classroom",
        "city_headline": "Why <span class='gold-ital'>Firenze</span> teaches the sentence",
        "city_lede": "The past tense was, in a very real sense, standardised on the banks of the Arno. We teach it where it belongs.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "A morning at <span class='gold-ital'>Sant'Ambrogio</span>",
        "final_headline": "Speak Italian in <span class='gold-ital'>full sentences</span>.",
        "final_sub": "Twenty live lessons with Alessandro, from the Uffizi steps to a family kitchen in the Oltrarno. Small group. Lifetime recordings. Certificate on the wall.",
        "start_date": "13 October 2026",
    },
    "ci3": {
        "slug": "ci3", "path": "pages/courses/ci3.html", "up": "../..",
        "code": "CI · 03", "hero_video_poster": "course-ci3.jpg",
        "region_photo": "course-ci3.jpg",
        "prev": ("ci2", "CI Elementare", "A1.1 → A1.2 · Firenze"),
        "next": ("ci4", "CI Avanzato", "A2.1 → A2.2 · Napoli & Milano"),
        "teacher": {
            "name": "Francesca Morandi", "img": "teacher-francesca.jpg",
            "region": "Bologna · Via Zamboni",
            "role": "Native teacher · Alma Mater doctorate in sociolinguistics",
            "bio": "Francesca finished her doctorate at Bologna's Alma Mater — the oldest university in the western world — and never left the city. She teaches Italian the way Bolognesi eat: slowly, generously, always with a second helping. Her students say she has the rare gift of making a subjunctive feel like a warm bowl of tortellini.",
            "quote": "Bologna is la Dotta, la Grassa, la Rossa — the learned, the fat, the red. Three appetites. Italian at A2 needs all three.",
            "creds": "PhD Sociolinguistics · Alma Mater Studiorum · 12 years teaching · published on regional dialects"
        },
        "city_name": "Bologna", "city_italian": "Bologna",
        "city_paragraphs": [
            "Bologna is Italy's classroom. The Alma Mater Studiorum, founded in 1088, made this city a place where people came to learn — and where, over nine hundred years, an entire vocabulary of study, argument, and generous hospitality was polished under the porticoes.",
            "A1.2 to A2.1 is the middle passage — the level where you stop translating in your head and start thinking in Italian. Bologna is the perfect city for that transition, because Bolognesi are precise without being severe. They will finish your sentence for you if you pause, but they will do it kindly, and they will pour you another glass of Sangiovese while they do.",
            "This course lives in the city's three nicknames: la Dotta, the university and its lecture halls; la Grassa, the food markets, tortellini rolled by hand, tagliatelle at Trattoria Anna Maria; and la Rossa, both the terracotta rooftops and the political conversations you will overhear in every osteria after nine at night."
        ],
        "pillars": [
            ("Sotto i portici", "Bologna has forty kilometres of covered arcades. Our lessons take you under them — to bookstores, cafés, and the tables where local politics is argued nightly. You learn the language of an argued opinion."),
            ("Il congiuntivo, con calma", "A2 introduces the subjunctive — the tense that most learners fear. We introduce it slowly, through examples of Bolognese cuisine, and by lesson fifteen you will use it without noticing."),
            ("Una maestra bolognese", "Francesca teaches every lesson. She is a sociolinguist by training, which means she can explain, in one sentence, why a phrase you learned in Rome sounds strange in Bologna — and how to bridge the two.")
        ],
        "week_rhythm": [
            ("Monday", "Lezione dal Vivo", "The 85-minute live class with Francesca. Small group of ten to twelve, always live from Bologna."),
            ("Wednesday", "Studio Guidato", "A 20-minute private session with Biagio, our AI tutor, on the subjunctive and the imperfect."),
            ("Friday", "Osteria della Conversazione", "A 30-minute conversation salon. Real topics, real opinions, gentle correction from Francesca."),
            ("Weekend", "Bologna a Passo", "A short film shot in Bologna — the fish market, a shop that has sold pasta since 1880, an afternoon at Osteria del Sole.")
        ],
        "sample": {
            "title": "Lesson 12 · Un'osteria in via del Pratello",
            "setting": "Nine at night, a wooden table shared with strangers. The waiter, Ruggero, drops off a carafe of red without being asked.",
            "dialogue": [
                ("Ruggero", "Buonasera. Avete deciso?"),
                ("Tu", "Sì, prendo le tagliatelle al ragù. E vorrei un calice di Sangiovese."),
                ("Ruggero", "Bene. E per secondo?"),
                ("Tu", "Non ancora. Torno tra dieci minuti."),
                ("Ruggero", "Come vuole. La cucina chiude alle undici, si ricordi.")
            ],
            "note": "Two conditionals, a future, and a polite imperative — in five turns. This is the density that A2 unlocks."
        },
        "testimonials": [
            ("“Francesca made the subjunctive feel like a promotion. By the end I was using it to argue about football with my Italian husband. He was not amused.”", "Rachel D.", "Chicago · CI Intermedio · Winter 2026"),
            ("“I have taken Italian in three countries and this is the first course that made me feel I was speaking with a real accent, not a textbook one. Bologna deserves the credit.”", "Karim H.", "Cairo · CI Intermedio · Spring 2026"),
            ("“I finally understand what Italians are saying at the dinner table. It has changed my relationship with my in-laws in ways I did not expect.”", "Emma L.", "Sydney · CI Intermedio · Autumn 2025")
        ],
        "promise_headline": "Think in Italian, <span class='gold-ital'>argue</span> in it too.",
        "promise_lede": "A1.2 to A2.1 is the passage from translating to thinking. Twenty lessons under Bologna's porticoes, teaching you the tenses that make an opinion possible.",
        "different_headline": "What makes <span class='gold-ital'>Intermedio</span> different",
        "different_lede": "Three reasons Italy's oldest university city is the right place to graduate from A1.",
        "city_eyebrow": "The city is the classroom",
        "city_headline": "Why <span class='gold-ital'>Bologna</span> teaches the argument",
        "city_lede": "The middle passage of Italian belongs to the city that has been arguing, teaching, and eating since 1088.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "An evening in <span class='gold-ital'>via del Pratello</span>",
        "final_headline": "Argue in <span class='gold-ital'>Italiano</span>.",
        "final_sub": "Twenty live lessons with Francesca, from the porticoes to a shared table on a Friday night. Small group. Lifetime recordings. Certificate on the wall.",
        "start_date": "20 October 2026",
    },
    "ci4": {
        "slug": "ci4", "path": "pages/courses/ci4.html", "up": "../..",
        "code": "CI · 04", "hero_video_poster": "course-ci4.jpg",
        "region_photo": "course-ci4.jpg",
        "prev": ("ci3", "CI Intermedio", "A1.2 → A2.1 · Bologna"),
        "next": None,
        "teacher": {
            "name": "Luca Esposito", "img": "teacher-luca.jpg",
            "region": "Napoli · Vomero, then Milano · Brera",
            "role": "Native teacher · bilingual North-South, actor-trained",
            "bio": "Luca grew up in Napoli, studied acting in Milano, and split his career between the two cities. He teaches CI Avanzato as it must be taught — bilingually across the north-south divide, because real Italian is not one register but the fluent movement between many. His students say he can switch accent mid-sentence and never miss a beat.",
            "quote": "In Napoli we sing the language. In Milano we edit it. If you can do both, you are Italian.",
            "creds": "Diploma Accademia dei Filodrammatici · 10 years teaching · guest lecturer, Politecnico di Milano"
        },
        "city_name": "Naples & Milan", "city_italian": "Napoli & Milano",
        "city_paragraphs": [
            "The Italian language stretches, at A2, between two poles. Naples in the south — musical, rapid, generous with vowels, unapologetic in emotion. Milan in the north — precise, clipped, professional, the Italian of contracts and consulting and the six-thirty evening aperitivo. Real Italian, at real speed, moves between them.",
            "A2.1 to A2.2 is the level where the language becomes yours. You are no longer a tourist. You can hold a meeting in Milan and a family dinner in Naples in the same weekend, and adapt your register in both. This course teaches you how — by staging every unit as a north-south pair.",
            "You will see Vesuvius from a Napoli rooftop and the Duomo from a Milanese office. You will learn the vocabulary of a Neapolitan grandmother's Sunday sauce and the vocabulary of a Milanese boardroom. Twenty lessons, two cities, one language finally in your hands."
        ],
        "pillars": [
            ("Nord e sud, insieme", "Every lesson pairs a Naples scene with a Milan scene. You learn to hear both accents, use both registers, and switch between them without noticing."),
            ("Il condizionale al lavoro", "The conditional — the tense of business, negotiation, and polite disagreement — is drilled through real meeting transcripts and family arguments."),
            ("Un maestro bilingue", "Luca teaches all twenty lessons. Trained as an actor, he can model both accents with equal precision, and he will teach you the invisible cues that Italians use to place each other socially in the first ten seconds.")
        ],
        "week_rhythm": [
            ("Monday", "Lezione dal Vivo", "The 85-minute live class with Luca. Small group of ten to twelve, filmed alternately from Naples and Milan."),
            ("Wednesday", "Studio Guidato", "A 20-minute private session with Biagio, our AI tutor, on the conditional, the future, and the passive voice."),
            ("Friday", "Salotto Bilingue", "A 30-minute conversation salon. Half the group speaks in a northern register, half in a southern one, then they swap."),
            ("Weekend", "Nord e Sud", "Two short films every week — one shot in Naples, one in Milan. Same theme, two accents, two Italies.")
        ],
        "sample": {
            "title": "Lesson 15 · Una riunione a Milano",
            "setting": "Ten past nine, an office in Porta Nuova. Your colleague, Elisa, opens the meeting.",
            "dialogue": [
                ("Elisa", "Buongiorno a tutti. Se siete d'accordo, comincerei con il punto uno."),
                ("Tu", "Certo. Vorrei però prima chiarire una cosa dell'ordine del giorno."),
                ("Elisa", "Prego, dimmi."),
                ("Tu", "Il punto tre, secondo me, andrebbe discusso prima del due. Sono collegati."),
                ("Elisa", "Hai ragione. Cambiamo l'ordine. Grazie della segnalazione.")
            ],
            "note": "Five conditionals in a two-minute exchange. This is Italian at work — polite, precise, never blunt. The southern version of the same meeting is in the course archive."
        },
        "testimonials": [
            ("“I now conduct sales calls in Italian for our Milan office and eat Sunday lunch with my in-laws in Napoli. Luca is the only teacher I have found who prepares you for both.”", "Michael T.", "Toronto · CI Avanzato · Winter 2026"),
            ("“The bilingual north-south framing was a revelation. I finally understand why my Milanese colleague and my Neapolitan friends sound like they are speaking different languages. Now I can speak with both.”", "Yuki I.", "Tokyo · CI Avanzato · Spring 2026"),
            ("“By the end of this course I dreamt in Italian for the first time. I woke up laughing because the dream was in a Neapolitan accent. Luca would be proud.”", "Sam O.", "Cape Town · CI Avanzato · Autumn 2025")
        ],
        "promise_headline": "The <span class='gold-ital'>real</span> Italian, from north to south.",
        "promise_lede": "A2.1 to A2.2 is the level where Italian is finally yours. Twenty lessons paired across Naples and Milan, so you can speak, negotiate, and belong in both.",
        "different_headline": "What makes <span class='gold-ital'>Avanzato</span> different",
        "different_lede": "Three reasons real Italian must be taught bilingually across the north-south divide.",
        "city_eyebrow": "The cities are the classroom",
        "city_headline": "Why <span class='gold-ital'>Napoli e Milano</span>, together",
        "city_lede": "The last mile of A2 belongs to the two cities that are, in every sense, the two Italies.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "A meeting in <span class='gold-ital'>Porta Nuova</span>",
        "final_headline": "Speak Italian, <span class='gold-ital'>north to south</span>.",
        "final_sub": "Twenty live lessons with Luca, bilingual across Naples and Milan. Small group. Lifetime recordings. Certificate on the wall.",
        "start_date": "27 October 2026",
    },
    "ps1": {
        "slug": "ps1", "path": "pages/spoken/ps1.html", "up": "../..",
        "code": "PS · 01", "hero_video_poster": "spoken-ps1.jpg",
        "region_photo": "spoken-ps1.jpg",
        "prev": None, "next": ("ps2", "A Tavola", "A1 → A2 · Tuscan trattorie"),
        "teacher": {
            "name": "Sofia Marchetti", "img": "teacher-sofia.jpg",
            "region": "Roma · Monti",
            "role": "Spoken-Italian coach · former RAI broadcaster",
            "bio": "Sofia spent seven years as a RAI radio host before turning to teaching. Her voice, students say, is what makes them want to answer. Al Caffè is her course from the ground up — designed for absolute beginners who want to speak Italian in a café before they can write a paragraph in it.",
            "quote": "The barista does not want to see your homework. The barista wants to hear a warm buongiorno. That is where we begin.",
            "creds": "Former RAI broadcaster · MA Italian Language Teaching · 6 years spoken-only method"
        },
        "city_name": "Roman cafés", "city_italian": "Al Caffè",
        "city_paragraphs": [
            "The Italian café is a small, mostly standing, mostly loud, always warm institution. There is a bar, a barista, two or three regulars, a newspaper, and a rhythm of orders that has not changed since the espresso machine was invented. If you can be a fluent participant in that rhythm, you have unlocked the front door of the Italian language.",
            "Spoken A0 to A1 is the exact right level for the café. You do not need grammar; you need warmth, sound, and the ten most useful requests in the world. Al Caffè is built around those ten requests, drilled through twenty live sessions until they land without thinking.",
            "Every session is set at a different Roman café — Sant'Eustachio in the Pantheon quarter, Panella in the Esquilino, a neighbourhood bar in Testaccio you have never heard of. You will finish the course able to enter any of them and be treated as a regular."
        ],
        "pillars": [
            ("Nessun libro", "There is no textbook. There is only spoken practice, filmed in real cafés, imitated in your live sessions, corrected in real time by Sofia."),
            ("Dieci ordinazioni", "Ten café orders form the backbone. Coffee, pastry, glass of water, quick sandwich, receipt, tip, exit. You will do each of them in dozens of small variations, so nothing surprises you."),
            ("Un'ex conduttrice RAI", "Sofia teaches all twenty sessions. She has spent seven years training her voice for Italian ears; now she trains yours.")
        ],
        "week_rhythm": [
            ("Monday", "Sessione dal Vivo", "The 85-minute live spoken session with Sofia. Small group, cameras on, coffee in hand."),
            ("Wednesday", "Ripasso Vocale", "A 20-minute audio-only session with Biagio, our AI tutor. You speak, he corrects. No writing."),
            ("Friday", "Al Bar", "A 30-minute optional conversation salon. Order a coffee, read the news headline aloud, chat about your week."),
            ("Weekend", "Al Caffè in Video", "A three-minute film shot inside a real Roman café, with three toggleable subtitle layers.")
        ],
        "sample": {
            "title": "Session 03 · Ordinare un cappuccino",
            "setting": "Eight in the morning, Bar Necci in Pigneto, a district Rome has quietly gentrified. Roberto, the barista, spots you.",
            "dialogue": [
                ("Roberto", "Ciao, dimmi tutto."),
                ("Tu", "Ciao. Un cappuccino, per favore. E un cornetto vuoto."),
                ("Roberto", "Il cornetto lo vuoi caldo?"),
                ("Tu", "Sì, grazie."),
                ("Roberto", "Arriva subito. Fanno due e cinquanta.")
            ],
            "note": "Five turns, one full transaction, zero grammar diagrams. This is what Al Caffè builds — instinct, not analysis."
        },
        "testimonials": [
            ("“I could barely say ciao when I started. Now I have a favourite barista in Trastevere who knows my order. That is a life change.”", "Hannah G.", "Berlin · Al Caffè · Winter 2026"),
            ("“Sofia's voice is like a warm hand on your back. You want to answer her, and that is half the battle.”", "Wei L.", "Singapore · Al Caffè · Spring 2026"),
            ("“I have taken three Italian classes before this one and none of them made me speak out loud in the first ten minutes. This one did.”", "Bea R.", "Buenos Aires · Al Caffè · Autumn 2025")
        ],
        "promise_headline": "Speak Italian <span class='gold-ital'>al bar</span>. From the very first sound.",
        "promise_lede": "Twenty live spoken sessions built around the small, warm, loud institution of the Italian café.",
        "different_headline": "What makes <span class='gold-ital'>Al Caffè</span> different",
        "different_lede": "Three reasons the café is the fastest classroom for absolute beginners.",
        "city_eyebrow": "The café is the classroom",
        "city_headline": "Why <span class='gold-ital'>il caffè</span> teaches you first",
        "city_lede": "The café is where Italian is warmest, most predictable, and most forgiving. It is the ideal front door.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "A morning at <span class='gold-ital'>Bar Necci</span>",
        "final_headline": "Order in <span class='gold-ital'>Italiano</span>.",
        "final_sub": "Twenty live spoken sessions with Sofia, filmed inside real Roman cafés. Small group. Lifetime recordings. No textbook.",
        "start_date": "6 October 2026",
    },
    "ps2": {
        "slug": "ps2", "path": "pages/spoken/ps2.html", "up": "../..",
        "code": "PS · 02", "hero_video_poster": "spoken-ps2.jpg",
        "region_photo": "spoken-ps2.jpg",
        "prev": ("ps1", "Al Caffè", "A0 → A1 · Roman cafés"),
        "next": ("ps3", "In Viaggio", "A2 · All of Italy"),
        "teacher": {
            "name": "Giulia Bianchi", "img": "teacher-giulia.jpg",
            "region": "Firenze · Chianti",
            "role": "Spoken-Italian coach · culinary school-trained",
            "bio": "Giulia trained as a chef at the Cordon Bleu Firenze before turning to teaching. She teaches A Tavola from the actual tables of Chianti — a running kitchen, a wooden board of pecorino, a bottle of Chianti Classico from three towns over. Her students say her lessons taste like Sunday lunch at her mother's.",
            "quote": "You cannot separate Italian from food. Try to and you get a language that nobody speaks. That is the trick I teach.",
            "creds": "Diploma Cordon Bleu Firenze · MA Italian Language · 7 years teaching adult learners"
        },
        "city_name": "Tuscan trattorie", "city_italian": "A Tavola",
        "city_paragraphs": [
            "The Italian table is the true classroom of the language. More Italian is spoken over lunch than in any office, university, or piazza. If you can hold your own at a two-hour Sunday meal — the argument about the sauce, the discussion of the wine, the polite refusal of a third plate — you have arrived.",
            "Spoken A1 to A2 belongs to the table for the same reason A0 belongs to the café: the vocabulary is dense, the rhythm is predictable, and the emotional temperature is warm. A Tavola is built around twenty scenes at real Italian tables — Tuscan trattorie, a Neapolitan pizzeria, a Sardinian shepherd's kitchen.",
            "You will finish able to order without a menu, to compliment the cook in the right register, to argue gently about the amount of salt, and to know when to accept the last biscotto and when to laugh and refuse it."
        ],
        "pillars": [
            ("Nessun menu", "Every session is a real meal. We do not translate menus; we live at the table. You order aloud, you praise aloud, you argue aloud."),
            ("La discussione del vino", "The wine conversation is its own subject. Regions, grapes, pairings, the polite way to send a bottle back. Six sessions are devoted to it."),
            ("Un'insegnante che cucina", "Giulia trained at Cordon Bleu Firenze. She teaches while stirring a pot, describing what she is doing in real time. You learn the language the way a child learns it — inside a kitchen.")
        ],
        "week_rhythm": [
            ("Monday", "Sessione dal Vivo", "The 85-minute live spoken session with Giulia. Small group, kitchen open, wine within reach."),
            ("Wednesday", "Ripasso Vocale", "A 20-minute audio session with Biagio, drilling the food vocabulary of the previous session."),
            ("Friday", "A Tavola", "A 30-minute optional conversation salon. Bring what you are eating. Describe it in Italian."),
            ("Weekend", "Il Pranzo della Domenica", "A short film of a real Sunday lunch — a family in Chianti, a table for eight, a two-hour meal in nine minutes.")
        ],
        "sample": {
            "title": "Session 08 · Al ristorante, ordinare il vino",
            "setting": "A trattoria in Greve in Chianti. The oste, Giovanni, arrives with a folder of wines.",
            "dialogue": [
                ("Giovanni", "Avete scelto il vino?"),
                ("Tu", "Non ancora. Cosa consiglia con la bistecca?"),
                ("Giovanni", "Con la fiorentina, un Chianti Classico Riserva. O, se vuole spendere un po' di più, un Brunello."),
                ("Tu", "Prendiamo il Chianti Classico Riserva. Del 2019, se lo avete."),
                ("Giovanni", "Ottima scelta. Arriva subito.")
            ],
            "note": "The wine dialogue rehearses two conditionals, one polite request, and one confident recommendation. It is the exact shape of A1.2 conversation."
        },
        "testimonials": [
            ("“I now order wine in Italian with confidence, argue with my mother-in-law about the pasta shape, and correctly refuse a third helping without offending. Giulia is a magician.”", "Fiona McL.", "Edinburgh · A Tavola · Winter 2026"),
            ("“I learned more Italian in Giulia's kitchen than in a year of Duolingo. The difference is she is actually cooking.”", "Tom H.", "Auckland · A Tavola · Spring 2026"),
            ("“By session ten I dreamt about pasta al pomodoro in Italian. My husband thought this was very Italian of me.”", "Alia J.", "Dubai · A Tavola · Autumn 2025")
        ],
        "promise_headline": "Speak the Italian of the <span class='gold-ital'>table</span>.",
        "promise_lede": "Twenty live spoken sessions at Italian tables — trattorie, kitchens, Sunday lunches. The vocabulary of belonging.",
        "different_headline": "What makes <span class='gold-ital'>A Tavola</span> different",
        "different_lede": "Three reasons the Italian table is the fastest room to fluency at A1 to A2.",
        "city_eyebrow": "The table is the classroom",
        "city_headline": "Why <span class='gold-ital'>la tavola</span> teaches the sentence",
        "city_lede": "More Italian is spoken over lunch than in any office. A1 to A2 belongs there.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "An evening in <span class='gold-ital'>Chianti</span>",
        "final_headline": "Sit down. Speak <span class='gold-ital'>Italiano</span>.",
        "final_sub": "Twenty live spoken sessions with Giulia, filmed at Italian tables from Chianti to Napoli. Small group. Lifetime recordings.",
        "start_date": "13 October 2026",
    },
    "ps3": {
        "slug": "ps3", "path": "pages/spoken/ps3.html", "up": "../..",
        "code": "PS · 03", "hero_video_poster": "spoken-ps3.jpg",
        "region_photo": "spoken-ps3.jpg",
        "prev": ("ps2", "A Tavola", "A1 → A2 · Tuscan trattorie"),
        "next": ("ps4", "Chiacchierando", "A2 → B1 · Everywhere Italians talk"),
        "teacher": {
            "name": "Marco Rinaldi", "img": "teacher-marco.jpg",
            "region": "Roma · itinerant across Italy",
            "role": "Spoken-Italian coach · former Trenitalia tour guide",
            "bio": "Marco spent five years as a Trenitalia cultural guide, running language-focused rail journeys from Palermo to Bolzano. He now teaches In Viaggio from a rotating series of stations, hotels, and museums. His voice has the calm authority of a man who has said 'binario undici' ten thousand times without irritation.",
            "quote": "Italian at A2 is the language of travel — of asking, of arriving, of getting lost gracefully. That last skill is the most Italian of all.",
            "creds": "5 years Trenitalia cultural guide · MA Tourism Linguistics · 4 years teaching"
        },
        "city_name": "All of Italy", "city_italian": "In Viaggio",
        "city_paragraphs": [
            "Travel is the second reason people learn Italian. Real travel — not tourist packages, but the small movements of the country: a delayed regionale, a lost reservation, a museum ticket booked in the wrong language, a museum guard who wants to talk. In Viaggio is built for the traveller who wants to move through Italy in Italian.",
            "Spoken A2 is the level where you can travel independently and be treated as an equal, not as a customer. In Viaggio drills the ten or twelve conversation shapes that make this possible — the station, the hotel desk, the taxi, the museum, the pharmacy, the small crisis.",
            "You will not learn phrases from a phrasebook. You will learn to improvise inside the shapes, so that when the trip does not go as planned — and it will not — you can still speak. Marco's five years on Trenitalia platforms taught him exactly which sentences you actually need."
        ],
        "pillars": [
            ("Nella stazione", "Six sessions are set inside Italian train stations. Real announcements, real timetables, real conversations with real ticket agents in real regional accents."),
            ("L'imprevisto", "Every session includes a small unexpected event — a delay, a change of plan, a request for help. You learn to speak inside surprise, not just inside script."),
            ("Un'ex guida ferroviaria", "Marco spent five years teaching Italian on Trenitalia routes. He knows which sentence works in Palermo and which one gets you a raised eyebrow in Bolzano.")
        ],
        "week_rhythm": [
            ("Monday", "Sessione dal Vivo", "The 85-minute live spoken session with Marco. Small group, filmed from a rotating Italian location."),
            ("Wednesday", "Ripasso Vocale", "A 20-minute audio session with Biagio on the future tense, the imperative, and travel vocabulary."),
            ("Friday", "In Movimento", "A 30-minute conversation salon. Describe your last trip in Italian. Someone else describes theirs."),
            ("Weekend", "Un Viaggio in Video", "A short film following one journey — a morning train from Firenze to Venezia, a taxi in Palermo, a hotel check-in in Torino.")
        ],
        "sample": {
            "title": "Session 11 · Alla reception di un hotel a Venezia",
            "setting": "Nine in the evening, the small lobby of Locanda Orseolo. The receptionist, Silvia, looks up.",
            "dialogue": [
                ("Silvia", "Buonasera. Ha una prenotazione?"),
                ("Tu", "Sì, a nome Rossi. Due notti, camera doppia."),
                ("Silvia", "Un attimo, controllo. Ah, ecco. La camera dà sul canale. Le va bene?"),
                ("Tu", "Perfetto. A che ora è la colazione, per favore?"),
                ("Silvia", "Dalle sette e mezza alle dieci. Nella saletta a destra.")
            ],
            "note": "Two polite forms, one confirmation, one clarification, one thank-you exchange. This is the standard hotel arrival, and after In Viaggio you will do it in your sleep."
        },
        "testimonials": [
            ("“I just spent three weeks in Italy and never once switched to English. Not once. Marco's course is the reason.”", "James P.", "Vancouver · In Viaggio · Winter 2026"),
            ("“The 'unexpected event' drills were the most useful thing I have ever done in a language class. I now know what to say when the train stops in a field.”", "Sanne V.", "Amsterdam · In Viaggio · Spring 2026"),
            ("“Marco taught me that being lost in Italy is not a failure — it is a conversation waiting to happen. That reframe is worth the tuition.”", "Rosa D.", "Mexico City · In Viaggio · Autumn 2025")
        ],
        "promise_headline": "Move through Italy in <span class='gold-ital'>Italiano</span>.",
        "promise_lede": "Twenty live spoken sessions built for the real Italy of stations, hotels, museums, and small delays.",
        "different_headline": "What makes <span class='gold-ital'>In Viaggio</span> different",
        "different_lede": "Three reasons the traveller's Italian is the most useful A2 in existence.",
        "city_eyebrow": "The country is the classroom",
        "city_headline": "Why <span class='gold-ital'>l'Italia intera</span> teaches A2",
        "city_lede": "The A2 you actually need is the Italian of the small movements of the country.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "An arrival at <span class='gold-ital'>Locanda Orseolo</span>",
        "final_headline": "Travel Italy in <span class='gold-ital'>Italiano</span>.",
        "final_sub": "Twenty live spoken sessions with Marco, filmed across Italy from stations to hotels. Small group. Lifetime recordings.",
        "start_date": "20 October 2026",
    },
    "ps4": {
        "slug": "ps4", "path": "pages/spoken/ps4.html", "up": "../..",
        "code": "PS · 04", "hero_video_poster": "spoken-ps4.jpg",
        "region_photo": "spoken-ps4.jpg",
        "prev": ("ps3", "In Viaggio", "A2 · All of Italy"),
        "next": None,
        "teacher": {
            "name": "Chiara Baldini", "img": "teacher-chiara.jpg",
            "region": "Roma · Trastevere",
            "role": "Spoken-Italian coach · debate-club trained",
            "bio": "Chiara returns for Chiacchierando — the confident spoken course. Her background in Roman debate societies makes her uniquely suited to teach Italians' favourite pastime: the well-argued, half-joking, half-serious conversation that fills every evening in every piazza in the country.",
            "quote": "Italians do not have small talk. They have big talk, always. Chiacchierando teaches you how to keep up.",
            "creds": "MA Italian Linguistics · Sapienza · former Rome debate coach · 11 years teaching adults"
        },
        "city_name": "Everywhere Italians talk", "city_italian": "Chiacchierando",
        "city_paragraphs": [
            "Italians talk. They talk over dinner, they talk over coffee, they talk on the tram, they talk in the queue at the post office. They talk about football, they talk about politics, they talk about the price of parmigiano. If you cannot participate in that talk, you are a spectator in the country, not a citizen of it.",
            "Spoken A2 to B1 is the confident register. You are past survival, past travel, past the transactions of daily life. You are into opinion, humour, gentle disagreement, and the small, warm insults Italians trade with people they love. This is the register that makes friendships possible.",
            "Chiacchierando is set everywhere Italians talk: a piazza in the evening, a bar for the aperitivo, a family dinner that lasts three hours, a queue at the tabacchi. You will finish able to give an opinion, hear one you disagree with, and respond in a way that keeps the conversation alive."
        ],
        "pillars": [
            ("L'opinione, con calma", "Six sessions are devoted to the shape of the Italian opinion — long, warm, argued, always with room for the other person to answer back."),
            ("L'ironia, senza offesa", "Italians tease. It is affection. We teach you how to hear it and how to give it back, without ever crossing into offence."),
            ("Un maestro che discute", "Chiara returns from Principiante, now as your senior conversation coach. She will push you, she will interrupt you, she will laugh with you. That is exactly the training you need.")
        ],
        "week_rhythm": [
            ("Monday", "Sessione dal Vivo", "The 85-minute live spoken session with Chiara. Small group of ten to twelve, real topics, real disagreement."),
            ("Wednesday", "Ripasso Vocale", "A 20-minute session with Biagio on the subjunctive, the conditional, and idiomatic register."),
            ("Friday", "In Piazza", "A 30-minute conversation salon. A news headline of the week. Everyone gives an opinion. Chiara moderates."),
            ("Weekend", "Chiacchierando", "A short film capturing a real Italian conversation — an aperitivo, a family argument about football, a queue at the pharmacy.")
        ],
        "sample": {
            "title": "Session 09 · Aperitivo, si parla di calcio",
            "setting": "Six-thirty in the evening, a bar in Testaccio. Enzo, a friend of a friend, pours you a spritz and grins.",
            "dialogue": [
                ("Enzo", "Allora, chi vince stasera secondo te?"),
                ("Tu", "Boh, dipende. Se giocano bene in difesa, forse la Roma."),
                ("Enzo", "La Roma? Ma dai, sono in crisi da tre mesi."),
                ("Tu", "Lo so, ma stasera in casa hanno una chance."),
                ("Enzo", "Vabbè, ti offro un altro spritz se hanno ragione loro.")
            ],
            "note": "One subjunctive, two conditionals, three idiomatic markers (boh, ma dai, vabbè). This is Italian at full speed, at the aperitivo, and after Chiacchierando you will be inside the exchange, not outside it."
        },
        "testimonials": [
            ("“I now argue in Italian about the referee, the government, and the correct amount of pepper. My Italian friends have stopped switching to English. That is the highest praise.”", "Rebecca S.", "Manchester · Chiacchierando · Winter 2026"),
            ("“Chiara taught me the three-word phrases that unlock the entire language. Boh. Vabbè. Ma dai. Real Italian happens between those three words.”", "Chen X.", "Shanghai · Chiacchierando · Spring 2026"),
            ("“I finally understand Italian jokes. I laugh in real time, not two beats behind. That has changed my whole social life in Italy.”", "Ines T.", "Lisbon · Chiacchierando · Autumn 2025")
        ],
        "promise_headline": "Talk like an <span class='gold-ital'>Italian</span>. Not just to one.",
        "promise_lede": "Twenty live spoken sessions on the four things Italians actually do all day: opinion, humour, argument, and affection.",
        "different_headline": "What makes <span class='gold-ital'>Chiacchierando</span> different",
        "different_lede": "Three reasons the confident spoken register cannot be taught from a textbook.",
        "city_eyebrow": "The country is the classroom",
        "city_headline": "Why <span class='gold-ital'>ovunque</span> teaches confidence",
        "city_lede": "Confident Italian happens wherever Italians talk. We put you there, twenty times.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "An aperitivo in <span class='gold-ital'>Testaccio</span>",
        "final_headline": "Talk like an <span class='gold-ital'>italiano</span>.",
        "final_sub": "Twenty live spoken sessions with Chiara, filmed everywhere Italians actually talk. Small group. Lifetime recordings.",
        "start_date": "27 October 2026",
    },
    "cap-food": {
        "slug": "cap-food", "path": "pages/culture/cap-food.html", "up": "../..",
        "code": "CAP · 01", "hero_video_poster": "cap-food.jpg",
        "region_photo": "cap-food.jpg",
        "prev": None, "next": ("cap-art", "L'Arte", "Renaissance in words"),
        "teacher": {
            "name": "Giulia Bianchi", "img": "teacher-giulia.jpg",
            "region": "Firenze · Chianti",
            "role": "Culture-Capsule host · Cordon Bleu-trained",
            "bio": "Giulia leads La Cucina — the six-session capsule on the language of the Italian table. Her Cordon Bleu training and her lifelong obsession with regional Italian cuisine make her the natural voice for this course. She hosts each session from a working Italian kitchen.",
            "quote": "Every Italian meal is a lecture on twenty regions of grammar. To speak Italian is, in the end, to know how a Sicilian butter differs from a Piedmontese one.",
            "creds": "Diploma Cordon Bleu Firenze · MA Italian Language · 7 years teaching · culinary journalist"
        },
        "city_name": "All of Italy", "city_italian": "La Cucina",
        "city_paragraphs": [
            "There is no Italian cuisine, only Italian cuisines — twenty regions, hundreds of towns, thousands of unwritten rules about which pasta shape belongs with which sauce and which grandmother's recipe is closest to the original. La Cucina is a language before it is a menu.",
            "This six-session capsule is our shortest course and our densest. It is designed for any learner at any level — beginners will pick up the vocabulary; advanced learners will finally understand why bucatini all'amatriciana can only be bucatini. Giulia hosts every session from a working Italian kitchen.",
            "You will finish able to read any Italian menu, argue about it competently, and know why the same tomato in Naples and in Milan tastes like two different words."
        ],
        "pillars": [
            ("Sei sessioni, sei paesaggi", "Six live sessions, each set in a different Italian foodscape — Roman markets, Neapolitan pizzerias, Emilian pasta workshops, Sicilian pastry shops."),
            ("Il vocabolario del gusto", "You learn the vocabulary of taste — dolce, sapido, amaro, umami — as Italians actually use it, with the shades of preference and disagreement that live inside every word."),
            ("Un'insegnante che cucina", "Giulia teaches from a real kitchen, real ingredients, real dishes. You are not watching a lecture; you are watching a meal being made in real time.")
        ],
        "week_rhythm": [
            ("Weeks 1-2", "Le Regioni", "Two sessions on the north-south axis of Italian cuisine."),
            ("Weeks 3-4", "La Pasta", "Two sessions on the four hundred pasta shapes and the rules that govern them."),
            ("Week 5", "Il Vino", "One session on the vocabulary of Italian wine, from Barolo to Nero d'Avola."),
            ("Week 6", "Il Pranzo della Domenica", "The final session — a full Sunday lunch, in real time, in Italian.")
        ],
        "sample": {
            "title": "Session 02 · La pasta, mille forme",
            "setting": "A workshop in Bologna, seventeen wooden boards, a rolling pin, one grandmother named Rita.",
            "dialogue": [
                ("Rita", "Vedi, la sfoglia si tira così, con calma."),
                ("Tu", "Deve essere di questo spessore?"),
                ("Rita", "Sottile come un velo. Se vedi la mano attraverso, va bene."),
                ("Tu", "E per i tortellini?"),
                ("Rita", "Ancora più sottile. Ma quello, cara, si impara con gli anni.")
            ],
            "note": "This is the dialogue that A2 unlocks — the polite question, the elder's answer, the follow-up. The sfoglia is the vocabulary lesson."
        },
        "testimonials": [
            ("“I finally understand why my Italian grandmother refused to make a carbonara with cream. Six sessions and a lifetime of confusion, resolved.”", "Nina C.", "Warsaw · La Cucina · Winter 2026"),
            ("“The capsule format is perfect. Six sessions, six kitchens, and I now read Italian menus like a local. Best small course I have taken.”", "Julian F.", "Copenhagen · La Cucina · Spring 2026"),
            ("“Giulia is a national treasure. I would take her capsule again just to hear her describe a tomato.”", "Maya K.", "New York · La Cucina · Autumn 2025")
        ],
        "promise_headline": "The Italian of the <span class='gold-ital'>table</span>, in six sessions.",
        "promise_lede": "A short, intense capsule on the language and history of the Italian kitchen — for any learner, any level.",
        "different_headline": "What makes <span class='gold-ital'>La Cucina</span> different",
        "different_lede": "Three reasons the capsule format is the right shape for the language of food.",
        "city_eyebrow": "The kitchen is the classroom",
        "city_headline": "Why <span class='gold-ital'>la cucina</span> teaches the culture",
        "city_lede": "Every Italian meal is a language lesson. Six of them, hosted, is a small education.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "A pasta workshop in <span class='gold-ital'>Bologna</span>",
        "final_headline": "Learn the Italian of the <span class='gold-ital'>table</span>.",
        "final_sub": "Six live sessions with Giulia, hosted from working Italian kitchens. Any level. Lifetime recordings.",
        "start_date": "3 November 2026",
    },
    "cap-art": {
        "slug": "cap-art", "path": "pages/culture/cap-art.html", "up": "../..",
        "code": "CAP · 02", "hero_video_poster": "cap-art.jpg",
        "region_photo": "cap-art.jpg",
        "prev": ("cap-food", "La Cucina", "Language of the Italian table"),
        "next": ("cap-opera", "L'Opera", "Opera as a second language"),
        "teacher": {
            "name": "Alessandro Fiorini", "img": "teacher-alessandro.jpg",
            "region": "Firenze · Uffizi",
            "role": "Culture-Capsule host · Uffizi-affiliated lecturer",
            "bio": "Alessandro returns for L'Arte — the six-session capsule on the Italian language of Renaissance art history. His Crusca training and his frequent lectures inside the Uffizi make him the natural host. Each session is filmed inside a real museum or church.",
            "quote": "To understand a Caravaggio in Italian is to understand something a translated wall label can never quite give you. That gap is what this capsule closes.",
            "creds": "MA Filologia · Università di Firenze · former Crusca junior fellow · Uffizi guest lecturer"
        },
        "city_name": "Florence & Rome", "city_italian": "L'Arte",
        "city_paragraphs": [
            "The Italian Renaissance was, in the end, a linguistic project. The painters spoke Tuscan, the patrons spoke Tuscan, the manuals spoke Tuscan. To read Vasari's Vite in Italian is to feel the paintings breathe in a way no English translation quite captures.",
            "This six-session capsule teaches the specific vocabulary of Italian art history — the light, the composition, the pigment, the patron. It is set inside real Italian museums and churches, from the Uffizi to the Santa Maria del Popolo Caravaggios. Alessandro hosts every session.",
            "You will finish able to read an Italian museum wall label, follow an Italian art documentary, and hold a coffee-shop conversation about a Botticelli without ever switching to English."
        ],
        "pillars": [
            ("In museo, in Italiano", "Six sessions filmed inside real Italian museums and churches. The paintings are on the wall behind Alessandro. The vocabulary is on the wall next to them."),
            ("Il vocabolario del chiaroscuro", "You learn the specific Italian language of art criticism — chiaroscuro, sfumato, prospettiva — with the historical weight each word carries."),
            ("Un maestro dell'Accademia", "Alessandro trained at the Crusca and lectures at the Uffizi. He is, in every sense, the right voice for this vocabulary.")
        ],
        "week_rhythm": [
            ("Weeks 1-2", "Il Trecento e il Quattrocento", "Two sessions on Giotto, Masaccio, and the birth of perspective."),
            ("Weeks 3-4", "Il Cinquecento", "Two sessions on Leonardo, Michelangelo, and Raphael."),
            ("Week 5", "Il Barocco", "One session on Caravaggio and the drama of light."),
            ("Week 6", "Al Museo", "The final session — a real museum visit, in real time, in Italian.")
        ],
        "sample": {
            "title": "Session 05 · Il Caravaggio a Santa Maria del Popolo",
            "setting": "Inside the Cerasi Chapel, forty centimetres from the Conversione di San Paolo. Alessandro speaks quietly, because the church has other visitors.",
            "dialogue": [
                ("Alessandro", "Guarda la luce. Da dove arriva?"),
                ("Tu", "Da sinistra, molto forte."),
                ("Alessandro", "Esatto. E il cavallo, dove guarda?"),
                ("Tu", "Verso il basso, verso San Paolo."),
                ("Alessandro", "Bene. È la composizione che ha cambiato la pittura per due secoli.")
            ],
            "note": "Five turns inside a chapel. This is the exact language you will use the next time you stand in an Italian church and want to think in Italian about the painting in front of you."
        },
        "testimonials": [
            ("“Alessandro made me see the Uffizi differently. In Italian. That is a gift I will take back to every museum I visit.”", "Elizabeth H.", "Dublin · L'Arte · Winter 2026"),
            ("“I read Italian art criticism now. Actual sentences, not translated summaries. The capsule opened a door.”", "Peter M.", "San Francisco · L'Arte · Spring 2026"),
            ("“The final museum session was the most alive I have felt in a classroom in twenty years.”", "Marika L.", "Helsinki · L'Arte · Autumn 2025")
        ],
        "promise_headline": "Read the Italian of a <span class='gold-ital'>Caravaggio</span>.",
        "promise_lede": "A six-session capsule on the specific Italian vocabulary of Renaissance and Baroque art, taught inside real Italian museums.",
        "different_headline": "What makes <span class='gold-ital'>L'Arte</span> different",
        "different_lede": "Three reasons the language of Italian art must be taught inside Italian art.",
        "city_eyebrow": "The museum is the classroom",
        "city_headline": "Why <span class='gold-ital'>l'arte</span> lives in Italian",
        "city_lede": "The Italian language of art was invented inside these galleries. We teach it there.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "Inside the <span class='gold-ital'>Cerasi Chapel</span>",
        "final_headline": "See Italian art in <span class='gold-ital'>Italiano</span>.",
        "final_sub": "Six live sessions with Alessandro, hosted inside real Italian museums and churches. Any level. Lifetime recordings.",
        "start_date": "3 November 2026",
    },
    "cap-opera": {
        "slug": "cap-opera", "path": "pages/culture/cap-opera.html", "up": "../..",
        "code": "CAP · 03", "hero_video_poster": "cap-opera.jpg",
        "region_photo": "cap-opera.jpg",
        "prev": ("cap-art", "L'Arte", "Renaissance in words"),
        "next": None,
        "teacher": {
            "name": "Sofia Marchetti", "img": "teacher-sofia.jpg",
            "region": "Milano · Teatro alla Scala",
            "role": "Culture-Capsule host · former RAI opera correspondent",
            "bio": "Sofia hosts L'Opera. Her seven years at RAI included three seasons as a specialist opera correspondent from La Scala. She teaches this capsule as it should be taught — with a libretto in one hand, a conductor's score in the other, and a warm, precise voice that can make Verdi feel like a friend.",
            "quote": "An aria is a paragraph of pure Italian. To follow it is to hold, for four minutes, the whole language in one breath.",
            "creds": "Former RAI opera correspondent · MA Italian Language Teaching · 6 years teaching"
        },
        "city_name": "La Scala, Milan", "city_italian": "L'Opera",
        "city_paragraphs": [
            "Opera is the Italian language performed at its most extreme — sung, condensed, emotional, memorised by heart across four hundred years. To follow an Italian aria is to feel the language work at a pressure it never reaches in ordinary speech.",
            "This six-session capsule teaches you how to read a libretto, follow an aria in real time, and hear the emotional weight the composer built into every syllable. Sofia hosts every session from Milan, with visits to La Scala and to the Verdi museums of Emilia-Romagna.",
            "You will finish able to attend an Italian opera and follow the words. That is a specific, small, and enormous cultural achievement — and it is what six sessions of L'Opera unlock."
        ],
        "pillars": [
            ("Il libretto, in mano", "Six sessions, six librettos. You will hold Rigoletto, La Traviata, Turandot, and three others in your hand and read along as the aria plays."),
            ("La musica delle parole", "Italian is the language opera was invented in. We teach you why — the length of the vowels, the openness of the sound, the way the words meet the melody without resistance."),
            ("Un'ex critica lirica", "Sofia spent three seasons as a RAI opera correspondent. She knows every La Scala production of the last fifteen years and she will teach you to hear what she hears.")
        ],
        "week_rhythm": [
            ("Weeks 1-2", "Verdi", "Two sessions on Rigoletto and La Traviata — the language of tragedy and the language of a party."),
            ("Weeks 3-4", "Puccini", "Two sessions on La Bohème and Turandot — the language of intimacy and the language of spectacle."),
            ("Week 5", "Rossini", "One session on Il Barbiere di Siviglia and the language of Italian comedy."),
            ("Week 6", "Alla Scala", "The final session — a filmed visit to La Scala, in real time, in Italian.")
        ],
        "sample": {
            "title": "Session 03 · La Traviata, il brindisi",
            "setting": "A dining table in Violetta's palazzo. The stage is full. Alfredo raises his glass.",
            "dialogue": [
                ("Alfredo", "Libiamo, libiamo ne'lieti calici che la bellezza infiora…"),
                ("Sofia (voce)", "'Libiamo' — beviamo, in italiano di allora. 'Ne'lieti calici' — nei calici gioiosi."),
                ("Violetta", "Tra voi saprò dividere il tempo mio giocondo…"),
                ("Sofia (voce)", "'Giocondo' — allegro, felice. Ma con l'ombra della malattia già presente."),
                ("Tu (lettore)", "Sento la parola 'calici'. La riconosco.")
            ],
            "note": "Every aria is a language lesson at concert pitch. We slow it down, we translate the archaic forms, and by session six you follow along in real time."
        },
        "testimonials": [
            ("“I attended La Scala last month and understood the libretto. Not from the subtitles — from the words. Sofia's course made that happen.”", "Alistair R.", "Edinburgh · L'Opera · Winter 2026"),
            ("“Six sessions and my Italian is now inside opera in a way I did not think possible. Best cultural course I have ever taken.”", "Ilya S.", "Berlin · L'Opera · Spring 2026"),
            ("“Sofia sings a phrase, translates it, sings it again, and suddenly you hear the language differently. It is teaching at its highest form.”", "Nora W.", "Boston · L'Opera · Autumn 2025")
        ],
        "promise_headline": "Follow a <span class='gold-ital'>Verdi</span> aria in real time.",
        "promise_lede": "A six-session capsule on the Italian of the libretto — Verdi, Puccini, Rossini — hosted by a former La Scala correspondent.",
        "different_headline": "What makes <span class='gold-ital'>L'Opera</span> different",
        "different_lede": "Three reasons opera is the shortest path to Italian at its most beautiful.",
        "city_eyebrow": "La Scala is the classroom",
        "city_headline": "Why <span class='gold-ital'>l'opera</span> teaches the language",
        "city_lede": "Opera is Italian at its most concentrated. To follow it is to hold the language whole.",
        "sample_eyebrow": "Listen in",
        "sample_headline": "The brindisi from <span class='gold-ital'>La Traviata</span>",
        "final_headline": "Hear Italian as <span class='gold-ital'>opera</span>.",
        "final_sub": "Six live sessions with Sofia, hosted from Milan and La Scala. Any level. Lifetime recordings.",
        "start_date": "3 November 2026",
    },
}

# ============================================================
# HTML BUILDING
# ============================================================

NAV = """<header class="site-header">
  <div class="wrap nav">
    <a class="nav-logo" href="{up}/index.html" aria-label="Club Italia — home">
      <span class="logo-text">
        <span class="lt-main">Club Italia</span>
        <span class="lt-sub">by eTeacher</span>
      </span>
    </a>
    <nav class="nav-menu" aria-label="Primary">
      <span class="nav-item"><a class="nav-link" href="{up}/courses.html">Courses</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/how-it-works.html">How It Works</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/method.html">Method</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/teachers.html">Teachers</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/culture.html">Culture</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/biagio.html">AI Tutor</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/pricing.html">Pricing</a></span>
      <span class="nav-item"><a class="nav-link" href="{up}/blog.html">Blog</a></span>
    </nav>
    <button class="btn btn-3d btn-3d-primary nav-cta" data-advisor type="button">Talk to an Advisor</button>
    <button class="nav-toggle" aria-label="Open menu" aria-controls="navDrawer" type="button">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<aside class="nav-drawer" id="navDrawer" aria-label="Mobile menu">
  <button class="nav-drawer-close" aria-label="Close menu" type="button">&times;</button>
  <a href="{up}/courses.html">Courses</a>
  <a href="{up}/how-it-works.html">How It Works</a>
  <a href="{up}/method.html">Method</a>
  <a href="{up}/teachers.html">Teachers</a>
  <a href="{up}/culture.html">Culture</a>
  <a href="{up}/capsules.html">Culture Capsules</a>
  <a href="{up}/biagio.html">AI Tutor</a>
  <a href="{up}/pricing.html">Pricing</a>
  <a href="{up}/blog.html">Blog</a>
  <a href="{up}/faq.html">FAQ</a>
  <a href="{up}/about.html">About</a>
  <a href="{up}/contact.html">Contact</a>
  <button class="btn btn-3d btn-3d-primary" data-advisor type="button" style="width:100%;margin-top:1.6rem">Talk to an Advisor</button>
</aside>"""

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="logo-text" style="margin-bottom:1rem"><span class="lt-main" style="color:var(--on-dark)">Club Italia</span><span class="lt-sub">by eTeacher</span></div>
        <p>Live Italian, taught inside Italian cities. Small groups, master teachers, lifetime recordings. Certified by eTeacher Group.</p>
      </div>
      <div class="footer-col">
        <h4>Courses</h4>
        <a href="{up}/pages/courses/ci1.html">CI Principiante</a>
        <a href="{up}/pages/courses/ci2.html">CI Elementare</a>
        <a href="{up}/pages/courses/ci3.html">CI Intermedio</a>
        <a href="{up}/pages/courses/ci4.html">CI Avanzato</a>
        <a href="{up}/courses.html">All Courses</a>
      </div>
      <div class="footer-col">
        <h4>Spoken &amp; Capsules</h4>
        <a href="{up}/pages/spoken/ps1.html">Al Caffè</a>
        <a href="{up}/pages/spoken/ps2.html">A Tavola</a>
        <a href="{up}/pages/spoken/ps3.html">In Viaggio</a>
        <a href="{up}/pages/spoken/ps4.html">Chiacchierando</a>
        <a href="{up}/capsules.html">Culture Capsules</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="{up}/about.html">About</a>
        <a href="{up}/method.html">Method</a>
        <a href="{up}/pricing.html">Pricing</a>
        <a href="{up}/faq.html">FAQ</a>
        <a href="{up}/contact.html">Contact</a>
        <a href="{up}/terms.html">Terms</a>
        <a href="{up}/privacy.html">Privacy</a>
      </div>
    </div>
    <div class="footer-bottom">
      <p>Presented by eTeacher Group &nbsp;·&nbsp; advisor@clubitalia.com &nbsp;·&nbsp; +1-888-230-5110</p>
    </div>
    <p style="color:var(--on-dark-faint);font-size:.78rem;text-align:center;margin-top:1.6rem">Copyright eTeacher Group © 2026. All Rights Reserved.</p>
  </div>
</footer>"""

ADVISOR_MODAL = """<div class="advisor-modal" id="advisorModal" role="dialog" aria-modal="true" aria-labelledby="advisorTitle">
  <div class="advisor-card">
    <button class="advisor-modal-close" aria-label="Close" type="button">&times;</button>
    <div class="advisor-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">Placement conversation</p>
      <h3 id="advisorTitle">Speak to a Club Italia advisor</h3>
      <p>A 15-minute conversation to place you in the right level and answer everything about the course.</p>
    </div>
    <form class="advisor-form" novalidate>
      <div class="field"><label for="af-name">Your name</label><input id="af-name" name="name" required><span class="err-msg"></span></div>
      <div class="field"><label for="af-email">Email</label><input id="af-email" name="email" type="email" required><span class="err-msg"></span></div>
      <div class="field"><label for="af-phone">Phone (optional)</label><input id="af-phone" name="phone" type="tel"></div>
      <div class="field"><label for="af-level">Current Italian level</label><select id="af-level" name="level"><option>Complete beginner</option><option>A1 · basics</option><option>A2 · confident</option><option>B1 or higher</option></select></div>
      <button class="btn btn-3d btn-3d-primary" type="submit">Reserve My Placement Call</button>
    </form>
    <div class="advisor-success"><h3>Grazie mille.</h3><p>An advisor will call within one business day. Look for a call from Roma.</p></div>
  </div>
</div>"""

# --- Page-level style block (extra components used only in course pages) ---
PAGE_STYLE = """<style>
/* ===== Course-page extras (page-local; ci.css is READ ONLY) ===== */
.hero-badges{display:flex;gap:.55rem;flex-wrap:wrap;margin-bottom:1.6rem}
.h-badge{display:inline-flex;align-items:center;gap:.5rem;padding:.4rem .8rem;border:1px solid var(--gold-line);color:var(--on-dark);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;border-radius:2px;background:rgba(34,8,11,.35);backdrop-filter:blur(6px)}
.h-badge.lvl{background:rgba(201,162,75,.14);color:var(--gold-soft);border-color:var(--gold-soft)}
.hero-meta-strip{display:grid;grid-template-columns:repeat(5,1fr);gap:1.4rem;margin-top:3rem;padding-top:2rem;border-top:1px solid var(--gold-line-soft);max-width:900px}
.hero-meta-strip .hm{}
.hero-meta-strip .hm-k{font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-soft);margin-bottom:.4rem}
.hero-meta-strip .hm-v{font-family:var(--serif);font-size:1.15rem;color:var(--on-dark)}
@media (max-width:820px){.hero-meta-strip{grid-template-columns:repeat(2,1fr);gap:1rem}}

/* Promise editorial two-column */
.promise-grid{display:grid;grid-template-columns:1fr 1.1fr;gap:5rem;align-items:start}
@media (max-width:900px){.promise-grid{grid-template-columns:1fr;gap:2.5rem}}
.promise-head h2{font-size:clamp(2.4rem,4.4vw,4rem);letter-spacing:-.015em}
.promise-outcomes{display:grid;grid-template-columns:1fr 1fr;gap:1.4rem}
@media (max-width:640px){.promise-outcomes{grid-template-columns:1fr}}
.promise-outcomes li{display:flex;gap:.9rem;font-size:1.02rem;line-height:1.5;color:var(--on-light)}
.promise-outcomes .n{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:1.35rem;line-height:1;flex-shrink:0;min-width:1.8rem}

/* Pillar cards */
.pillar-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6rem}
@media (max-width:900px){.pillar-grid{grid-template-columns:1fr}}
.pillar-card{background:rgba(255,255,255,.05);border:1px solid var(--dark-line);padding:2.4rem 1.9rem;position:relative;transition:border-color .3s var(--ease),transform .3s var(--ease)}
.pillar-card:hover{border-color:var(--gold-soft);transform:translateY(-3px)}
.pillar-card .p-num{font-family:var(--serif);font-style:italic;font-size:2.2rem;color:var(--gold-soft);line-height:1;margin-bottom:1.2rem;opacity:.85}
.pillar-card h3{font-family:var(--serif);font-size:1.55rem;line-height:1.15;margin-bottom:.8rem;color:var(--on-dark)}
.pillar-card p{font-size:.98rem;color:var(--on-dark-soft);line-height:1.6}

/* City band cinematic */
.city-band{position:relative;padding:0;min-height:82vh;display:flex;align-items:center;color:var(--on-dark);overflow:hidden}
.city-band .cb-bg{position:absolute;inset:0;z-index:0}
.city-band .cb-bg img{width:100%;height:100%;object-fit:cover}
.city-band .cb-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(34,8,11,.85) 0%,rgba(34,8,11,.5) 60%,rgba(34,8,11,.2) 100%),linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.55))}
.city-band .cb-content{position:relative;z-index:2;padding:6rem clamp(1.4rem,5vw,5rem);max-width:900px}
.city-band h2{font-family:var(--serif);font-weight:500;font-size:clamp(2.6rem,5vw,4.4rem);color:var(--on-dark);line-height:1.05;margin:.8rem 0 2rem}
.city-band .cb-paragraphs p{font-size:1.06rem;line-height:1.75;color:var(--on-dark-soft);margin-bottom:1.2rem;max-width:60ch}

/* Teacher block (course-page) */
.teacher-block{display:grid;grid-template-columns:.9fr 1.1fr;gap:4rem;align-items:center}
@media (max-width:900px){.teacher-block{grid-template-columns:1fr;gap:2rem}}
.teacher-photo{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--navy-mid);border:1px solid var(--gold-line);max-width:440px}
.teacher-photo img{width:100%;height:100%;object-fit:cover}
.teacher-photo .tp-badge{position:absolute;bottom:1rem;left:1rem;background:rgba(34,8,11,.75);color:var(--gold-soft);font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;padding:.5rem .9rem;border:1px solid var(--gold-line)}
.teacher-info .ti-role{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.15rem;margin:.4rem 0 1.2rem}
.teacher-info h3{font-family:var(--serif);font-size:clamp(2.2rem,3.6vw,3rem);line-height:1.05;margin-bottom:.2rem;color:var(--on-dark)}
.teacher-info p{color:var(--on-dark-soft);font-size:1.02rem;line-height:1.7;margin-bottom:1.4rem}
.teacher-quote{font-family:var(--serif);font-style:italic;font-size:1.35rem;line-height:1.35;color:var(--on-dark);padding-left:1.4rem;border-left:2px solid var(--gold);margin:1.6rem 0}
.teacher-creds{font-size:.78rem;letter-spacing:.06em;color:var(--on-dark-faint);padding-top:1rem;border-top:1px solid var(--dark-line-soft)}

/* Syllabus timeline / unit cards */
.unit-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1.4rem}
@media (max-width:820px){.unit-grid{grid-template-columns:1fr}}
.unit-card{display:grid;grid-template-columns:64px 1fr;gap:1.2rem;padding:1.6rem 1.6rem 1.6rem 0;border-top:1px solid var(--gold-line-soft);position:relative;transition:background .2s var(--ease)}
.unit-card:hover{background:rgba(201,162,75,.04)}
.unit-card .u-no{font-family:var(--serif);font-style:italic;color:var(--gold-deep);font-size:2rem;line-height:1;padding-left:.6rem}
.unit-card .u-body h4{font-family:var(--serif);font-size:1.25rem;line-height:1.22;margin-bottom:.35rem;color:var(--on-light)}
.unit-card .u-body p{font-size:.92rem;color:var(--on-light-soft);line-height:1.55;max-width:none}

/* Week rhythm cards */
.week-grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;margin-top:2.6rem}
@media (max-width:900px){.week-grid-4{grid-template-columns:repeat(2,1fr)}}
@media (max-width:520px){.week-grid-4{grid-template-columns:1fr}}
.week-card-lg{background:var(--paper);border:1px solid var(--gold-line-soft);padding:1.8rem 1.6rem;transition:transform .3s var(--ease),border-color .3s var(--ease)}
.week-card-lg:hover{transform:translateY(-3px);border-color:var(--gold-soft)}
.wc-day{font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:.6rem}
.wc-title{font-family:var(--serif);font-size:1.4rem;line-height:1.12;margin-bottom:.5rem;color:var(--on-light)}
.wc-note{font-size:.9rem;color:var(--on-light-soft);line-height:1.55}

/* Sample dialogue card */
.sample-card{background:var(--navy-mid);border:1px solid var(--gold-line);padding:clamp(2rem,4vw,3.4rem);color:var(--on-dark);position:relative;overflow:hidden}
.sample-card::before{content:"";position:absolute;top:-50px;right:-40px;width:220px;height:220px;background:radial-gradient(circle,rgba(201,162,75,.16),transparent 70%);pointer-events:none}
.sample-head{display:flex;justify-content:space-between;align-items:flex-start;gap:1.6rem;margin-bottom:1.4rem;padding-bottom:1.4rem;border-bottom:1px solid var(--dark-line-soft);flex-wrap:wrap}
.sample-head h3{font-family:var(--serif);font-size:1.8rem;color:var(--on-dark);line-height:1.15}
.sample-head .listen-btn{display:inline-flex;align-items:center;gap:.6rem;padding:.7rem 1.2rem;border:1px solid var(--gold-line);color:var(--gold-soft);font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;background:rgba(201,162,75,.06);cursor:pointer;transition:background .2s var(--ease)}
.sample-head .listen-btn:hover{background:rgba(201,162,75,.14)}
.sample-head .listen-btn::before{content:"";width:12px;height:12px;border-radius:50%;background:var(--gold-soft);box-shadow:0 0 12px var(--gold-soft)}
.sample-setting{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:1.1rem;line-height:1.5;margin-bottom:1.8rem;max-width:60ch}
.sample-dialogue{display:grid;gap:1rem;margin-bottom:1.8rem}
.sample-line{display:grid;grid-template-columns:120px 1fr;gap:1.2rem;padding:.9rem 0;border-bottom:1px solid var(--dark-line-soft)}
@media (max-width:600px){.sample-line{grid-template-columns:1fr;gap:.3rem}}
.sample-line .sp{font-family:var(--serif);font-style:italic;color:var(--gold-soft);font-size:.98rem}
.sample-line .txt{font-family:var(--serif);font-size:1.2rem;line-height:1.4;color:var(--on-dark)}
.sample-note{background:rgba(201,162,75,.08);border-left:2px solid var(--gold);padding:1rem 1.4rem;font-size:.94rem;color:var(--on-dark-soft);line-height:1.6}

/* Sibling nav */
.sibling-nav{display:grid;grid-template-columns:repeat(2,1fr);gap:1.4rem}
@media (max-width:820px){.sibling-nav{grid-template-columns:1fr}}
.sib-card{background:rgba(255,255,255,.05);border:1px solid var(--dark-line);padding:2rem;display:flex;flex-direction:column;gap:.4rem;transition:border-color .3s var(--ease),transform .3s var(--ease);color:var(--on-dark)}
.sib-card:hover{border-color:var(--gold-soft);transform:translateY(-3px)}
.sib-dir{font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-soft)}
.sib-title{font-family:var(--serif);font-size:1.7rem;color:var(--on-dark)}
.sib-cefr{font-size:.86rem;color:var(--on-dark-soft)}

/* Section head (course pages) */
.sec-head{max-width:820px;margin:0 auto 3.4rem;text-align:center}
.sec-head h2{margin:.6rem 0 1rem}
.sec-head p{margin:0 auto;color:var(--on-light-soft)}
.on-dark .sec-head p{color:var(--on-dark-soft)}
.gold-rule{border:0;height:1px;background:var(--gold);opacity:.7;width:60px;margin:1.6rem auto 0}

/* Section-terra (warm terracotta accent) */
.section-terra{background:linear-gradient(180deg,var(--paper) 0%,var(--cream) 100%)}
.section-navy-grad{background:linear-gradient(180deg,var(--navy) 0%,var(--navy-deep) 100%);color:var(--on-dark)}
.section-navy-grad h2,.section-navy-grad h3,.section-navy-grad h4{color:var(--on-dark)}

/* Final CTA */
.final-cta{text-align:center;padding:clamp(5rem,9vw,9rem) 0}
.final-cta h2{font-size:clamp(2.8rem,5vw,4.6rem);line-height:1.05;margin-bottom:1.4rem;color:var(--on-dark)}
.final-cta p{max-width:52ch;margin:0 auto 2.4rem;color:var(--on-dark-soft);font-size:1.15rem;line-height:1.55}
.final-cta .hero-ctas{justify-content:center}
</style>"""


def esc(s):
    return html.escape(str(s), quote=True)


def build_hero(meta, data):
    up = meta["up"]
    return f"""<section class="hero" style="min-height:88vh">
  <div class="hero-bg">
    <img src="{up}/assets/img/{meta['hero_video_poster']}" alt="{esc(data['city'])} — {esc(data['title'])}">
  </div>
  <div class="hero-content">
    <div style="max-width:820px">
      <div class="hero-badges">
        <span class="h-badge lvl">CEFR {esc(data['cefr'])}</span>
        <span class="h-badge"><span class="live-dot"></span>Live from Italia</span>
        <span class="h-badge">{esc(meta['code'])}</span>
        <span class="h-badge">Certified by eTeacher</span>
      </div>
      <p class="hero-tag">{esc(data['tag'])}</p>
      <h1>{data['title']} <span class="gold-ital">·</span> {esc(data['city'])}</h1>
      <p class="hero-sub">{esc(data['promise'])}</p>
      <div class="hero-ctas">
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
        <a class="btn btn-3d btn-3d-ghost" href="{up}/pdf/{meta['slug']}-syllabus.pdf" download>Download Syllabus PDF</a>
      </div>
      <div class="hero-meta-strip">
        <div class="hm"><div class="hm-k">Format</div><div class="hm-v">{esc(data['hours'])}</div></div>
        <div class="hm"><div class="hm-k">Group size</div><div class="hm-v">10&ndash;12 learners</div></div>
        <div class="hm"><div class="hm-k">CEFR</div><div class="hm-v">{esc(data['cefr'])}</div></div>
        <div class="hm"><div class="hm-k">Setting</div><div class="hm-v">{esc(data['city'])}</div></div>
        <div class="hm"><div class="hm-k">Next start</div><div class="hm-v">{esc(meta['start_date'])}</div></div>
      </div>
    </div>
  </div>
</section>"""


def build_proof_row(meta, data):
    # Fold 2 — Proof stat row
    lessons = "20" if meta['slug'].startswith(('ci','ps')) else "6"
    return f"""<section class="section-cream" style="padding:0">
  <div class="wrap" style="padding-top:2.2rem;padding-bottom:2.2rem">
    <div class="proof-row">
      <div class="proof-item"><div class="pi-num">{lessons}</div><div class="pi-label">Live lessons</div></div>
      <div class="proof-item"><div class="pi-num">85</div><div class="pi-label">Minutes each</div></div>
      <div class="proof-item"><div class="pi-num">10&ndash;12</div><div class="pi-label">Learners per group</div></div>
      <div class="proof-item"><div class="pi-num">{esc(data['cefr'].split(' → ')[-1])}</div><div class="pi-label">CEFR on completion</div></div>
    </div>
  </div>
</section>"""


def build_promise(meta, data):
    outs = data["outcomes"]
    items = "".join(
        f'<li><span class="n">0{i+1}</span><span>{esc(o)}</span></li>'
        for i, o in enumerate(outs)
    )
    return f"""<section class="section-paper">
  <div class="wrap">
    <div class="promise-grid">
      <div class="promise-head">
        <p class="eyebrow eyebrow-line">The promise</p>
        <h2 class="display-lg">{meta['promise_headline']}</h2>
        <p class="lead" style="margin-top:1.4rem">{esc(meta['promise_lede'])}</p>
      </div>
      <div>
        <ul class="promise-outcomes">{items}</ul>
      </div>
    </div>
  </div>
</section>"""


def build_pillars(meta, data):
    pillars = meta["pillars"]
    cards = "".join(
        f"""<div class="pillar-card"><div class="p-num">0{i+1}</div><h3>{esc(t)}</h3><p>{esc(b)}</p></div>"""
        for i, (t, b) in enumerate(pillars)
    )
    return f"""<section class="section-navy-grad">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">The DNA of this course</p>
      <h2 class="display-lg">{meta['different_headline']}</h2>
      <p>{esc(meta['different_lede'])}</p>
      <hr class="gold-rule">
    </div>
    <div class="pillar-grid">{cards}</div>
  </div>
</section>"""


def build_city(meta, data):
    up = meta["up"]
    paras = "".join(f"<p>{esc(p)}</p>" for p in meta["city_paragraphs"])
    return f"""<section class="city-band">
  <div class="cb-bg"><img src="{up}/assets/img/{meta['region_photo']}" alt="{esc(meta['city_name'])}"></div>
  <div class="wrap cb-content">
    <p class="eyebrow" style="color:var(--gold-soft)">{esc(meta['city_eyebrow'])}</p>
    <h2>{meta['city_headline']}</h2>
    <p class="lead" style="color:var(--on-dark);margin-bottom:2rem;max-width:56ch">{esc(meta['city_lede'])}</p>
    <div class="cb-paragraphs">{paras}</div>
  </div>
</section>"""


def build_teacher(meta, data):
    up = meta["up"]
    t = meta["teacher"]
    return f"""<section class="section-dark" style="background:linear-gradient(160deg,var(--navy-deep) 0%,var(--navy) 60%,var(--navy-soft) 130%)">
  <div class="wrap">
    <div class="teacher-block">
      <div class="teacher-photo">
        <img src="{up}/assets/img/{t['img']}" alt="{esc(t['name'])} — Club Italia master teacher">
        <span class="tp-badge">{esc(t['region'])}</span>
      </div>
      <div class="teacher-info">
        <p class="eyebrow">Meet your teacher</p>
        <h3>{esc(t['name'])}</h3>
        <div class="ti-role">{esc(t['role'])}</div>
        <p>{esc(t['bio'])}</p>
        <blockquote class="teacher-quote">&ldquo;{esc(t['quote'])}&rdquo;</blockquote>
        <div class="teacher-creds">{esc(t['creds'])}</div>
      </div>
    </div>
  </div>
</section>"""


def build_syllabus(meta, data):
    lessons = data["syllabus"]
    cards = ""
    for i, entry in enumerate(lessons):
        n = f"{i+1:02d}"
        title, body = entry[0], entry[1]
        cards += f"""<div class="unit-card">
      <div class="u-no">{n}</div>
      <div class="u-body">
        <h4>{esc(title)}</h4>
        <p>{esc(body)}</p>
      </div>
    </div>"""
    total = len(lessons)
    label = "twenty" if total == 20 else "six"
    return f"""<section class="section-paper" id="syllabus">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">The full curriculum</p>
      <h2 class="display-lg">{label.capitalize()} live lessons, one <span class="gold-ital">journey</span></h2>
      <p>A structured {esc(data['cefr'])} curriculum, each 85-minute live class themed to the setting of the course.</p>
      <hr class="gold-rule">
    </div>
    <div class="unit-grid">{cards}</div>
  </div>
</section>"""


def build_week(meta, data):
    cards = "".join(
        f"""<div class="week-card-lg"><div class="wc-day">{esc(d)}</div><div class="wc-title">{esc(t)}</div><div class="wc-note">{esc(n)}</div></div>"""
        for d, t, n in meta["week_rhythm"]
    )
    return f"""<section class="section-cream">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">The rhythm</p>
      <h2 class="display-lg">A <span class="gold-ital">week</span> in this course</h2>
      <p>Every week is designed to make Italian a daily habit, not a weekly appointment.</p>
      <hr class="gold-rule">
    </div>
    <div class="week-grid-4">{cards}</div>
  </div>
</section>"""


def build_sample(meta, data):
    s = meta["sample"]
    lines = "".join(
        f"""<div class="sample-line"><div class="sp">{esc(sp)}</div><div class="txt">{esc(tx)}</div></div>"""
        for sp, tx in s["dialogue"]
    )
    return f"""<section class="section-paper">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">{esc(meta['sample_eyebrow'])}</p>
      <h2 class="display-lg">{meta['sample_headline']}</h2>
      <p>A short excerpt from a real lesson. Press listen to hear the pronunciation.</p>
      <hr class="gold-rule">
    </div>
    <div class="sample-card">
      <div class="sample-head">
        <h3>{esc(s['title'])}</h3>
        <button class="listen-btn" type="button" aria-label="Play the audio for this dialogue">Play audio · 0:42</button>
      </div>
      <p class="sample-setting">{esc(s['setting'])}</p>
      <div class="sample-dialogue">{lines}</div>
      <p class="sample-note"><strong>Teacher's note.</strong> {esc(s['note'])}</p>
    </div>
  </div>
</section>"""


def build_testimonials(meta, data):
    cards = "".join(
        f"""<div class="t-card"><div class="t-stars">★ ★ ★ ★ ★</div><p class="t-quote">{q}</p><p class="t-name">{esc(n)}</p><p class="t-loc">{esc(loc)}</p></div>"""
        for q, n, loc in meta["testimonials"]
    )
    return f"""<section class="section-cream">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">Voices from this course</p>
      <h2 class="display-lg">Students of <span class="gold-ital">{esc(data['title'].split()[-1])}</span></h2>
      <p>Three past learners of this exact course, in their own words.</p>
      <hr class="gold-rule">
    </div>
    <div class="testimonials">{cards}</div>
  </div>
</section>"""


def build_pricing(meta, data):
    # Course-specific pricing (values consistent with $1,240 annual for full courses; capsules different)
    if meta['slug'].startswith('cap'):
        annual = "$480"
        annual_note = "$480 for the six-session capsule"
        term = "$180"
        term_sub = "$180 / two sessions"
        monthly = "$99"
        monthly_sub = "$99 / month · six months max"
    else:
        annual = "$62"
        annual_note = "$1,240 billed yearly · full 20-lesson programme"
        term = "$78"
        term_sub = "From $780 / ten-lesson term"
        monthly = "$84"
        monthly_sub = "From $336 / month · cancel anytime"
    return f"""<section class="section-dark" id="pricing" style="background:linear-gradient(180deg,var(--navy) 0%,var(--navy-deep) 100%)">
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow eyebrow-line" style="justify-content:center">Tuition</p>
      <h2 class="display-lg" style="color:var(--on-dark)">One investment. One <span class="gold-ital">Italia</span>.</h2>
      <p style="color:var(--on-dark-soft)">Every plan includes live teaching from Italy, lifetime access to lesson recordings, and your Club Italia certificate.</p>
      <hr class="gold-rule">
    </div>
    <div class="pricing-grid">
      <div class="price-card featured">
        <span class="pc-badge">Best value</span>
        <h3>Annual</h3>
        <div class="pc-perweek">{annual}<small>&nbsp;/ week</small></div>
        <p class="pc-total">{annual_note}</p>
        <ul>
          <li>All live lessons with the master teacher</li>
          <li>Small live groups of 10&ndash;12 learners</li>
          <li>Lifetime access to every lesson recording</li>
          <li>Biagio, your 24/7 AI Italian tutor</li>
          <li>Club Italia certificate on completion</li>
          <li>$100 in Club Italia learning credits</li>
        </ul>
        <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Seat</button>
      </div>
      <div class="price-card">
        <h3>Term</h3>
        <div class="pc-perweek">{term}<small>&nbsp;/ week</small></div>
        <p class="pc-total">{term_sub}</p>
        <ul>
          <li>Pay per term, no long commitment</li>
          <li>Same live small-group classes</li>
          <li>Lifetime recordings included</li>
          <li>Upgrade to Annual anytime</li>
        </ul>
        <button class="btn btn-3d btn-3d-navy" data-advisor type="button">Start with a Term</button>
      </div>
      <div class="price-card">
        <h3>Monthly</h3>
        <div class="pc-perweek">{monthly}<small>&nbsp;/ week</small></div>
        <p class="pc-total">{monthly_sub}</p>
        <ul>
          <li>Pay month to month, cancel anytime</li>
          <li>Same live small-group classes</li>
          <li>Lifetime recordings included</li>
          <li>Convert to Annual at any point</li>
        </ul>
        <button class="btn btn-3d btn-3d-navy" data-advisor type="button">Start Monthly</button>
      </div>
    </div>
    <p style="text-align:center;color:var(--on-dark-faint);font-size:.82rem;margin-top:2rem">Club Italia is presented by eTeacher Group. All amounts in USD. Tuition includes VAT where applicable.</p>
  </div>
</section>"""


def build_sibling_and_final(meta, data):
    up = meta["up"]
    parts = []
    if meta.get("prev") or meta.get("next"):
        cards = []
        if meta["prev"]:
            s, t, cfr = meta["prev"]
            # figure out folder
            folder = "courses" if s.startswith("ci") else ("spoken" if s.startswith("ps") else "culture")
            cards.append(f"""<a class="sib-card" href="{up}/pages/{folder}/{s}.html">
        <span class="sib-dir">&larr; Previous</span>
        <span class="sib-title">{esc(t)}</span>
        <span class="sib-cefr">{esc(cfr)}</span>
      </a>""")
        if meta["next"]:
            s, t, cfr = meta["next"]
            folder = "courses" if s.startswith("ci") else ("spoken" if s.startswith("ps") else "culture")
            cards.append(f"""<a class="sib-card" href="{up}/pages/{folder}/{s}.html">
        <span class="sib-dir">Next &rarr;</span>
        <span class="sib-title">{esc(t)}</span>
        <span class="sib-cefr">{esc(cfr)}</span>
      </a>""")
        parts.append(f"""<section class="section-dark" style="background:var(--navy-deep);padding:3rem 0"><div class="wrap"><div class="sibling-nav">{''.join(cards)}</div></div></section>""")
    parts.append(f"""<section class="section-dark final-cta" style="background:linear-gradient(180deg,var(--navy) 0%,var(--navy-deep) 100%)">
  <div class="wrap-narrow">
    <p class="eyebrow eyebrow-line" style="justify-content:center">Live Italian. Live.</p>
    <h2>{meta['final_headline']}</h2>
    <p>{esc(meta['final_sub'])}</p>
    <div class="hero-ctas">
      <button class="btn btn-3d btn-3d-primary" data-advisor type="button">Reserve My Placement Call</button>
      <a class="btn btn-3d btn-3d-ghost" href="{up}/how-it-works.html">See how it works</a>
    </div>
  </div>
</section>""")
    return "\n".join(parts)


def build_page(slug):
    meta = COURSE_META[slug]
    data = DATA[slug]
    up = meta["up"]

    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(data['title'])} &mdash; {esc(data['cefr'])} &middot; {esc(data['city'])} &middot; Club Italia</title>
<meta name="description" content="{esc(data['promise'][:180])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{up}/css/ci.css">
{PAGE_STYLE}
</head>
<body>
{NAV.format(up=up)}

{build_hero(meta, data)}
{build_proof_row(meta, data)}
{build_promise(meta, data)}
{build_pillars(meta, data)}
{build_city(meta, data)}
{build_teacher(meta, data)}
{build_syllabus(meta, data)}
{build_week(meta, data)}
{build_sample(meta, data)}
{build_testimonials(meta, data)}
{build_pricing(meta, data)}
{build_sibling_and_final(meta, data)}

{FOOTER.format(up=up)}
{ADVISOR_MODAL}
<script src="{up}/js/ci.js" defer></script>
</body>
</html>
"""
    return head


def main():
    for slug, meta in COURSE_META.items():
        html_out = build_page(slug)
        out_path = os.path.join(ROOT, meta["path"])
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"wrote {out_path}  ({len(html_out):,} bytes)")


if __name__ == "__main__":
    main()
