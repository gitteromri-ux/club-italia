#!/usr/bin/env python3
"""Club Italia — 11 blog posts + syllabus PDFs."""
from pathlib import Path
import re, json
ROOT = Path("/home/user/workspace/club-italia")
NAV = open(ROOT/"_partials/nav.html").read()
FOOTER = open(ROOT/"_partials/footer.html").read()

def page(title, desc, body, rel=""):
    nav, footer = NAV, FOOTER
    if rel:
        def prefix(m):
            attr, val = m.group(1), m.group(2)
            if val.startswith(('http','#','mailto:','tel:','/', rel)): return m.group(0)
            return f'{attr}="{rel}{val}"'
        nav = re.sub(r'(href|src)="([^"]+)"', prefix, nav)
        footer = re.sub(r'(href|src)="([^"]+)"', prefix, footer)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{rel}css/ci.css"></head><body>
{nav}
{body}
{footer}
<script src="{rel}js/ci.js"></script></body></html>
"""

POSTS = [
    ("italian-golden-age","Cinema","The Golden Age of Italian Cinema","How Fellini, Visconti and Rossellini rewrote what film could be","10 Sep 2026","pillar-cinema.jpg",[
        ("The invention of neorealism","In the shattered aftermath of World War II, a small group of Roman filmmakers walked out of the studios and into the streets. Roberto Rossellini's Roma, Città Aperta (1945) — shot on scrap film stock in the ruins of a Rome that had barely finished being occupied — showed the world what cinema could be when it stopped pretending. Vittorio De Sica's Ladri di biciclette (1948), Luchino Visconti's La terra trema (1948), and Rossellini's Paisà (1946) followed in swift succession, and Italian neorealism was born."),
        ("A cinema of ordinary people","What made these films revolutionary was not their technique but their gaze. They filmed factory workers, fishermen, war widows and orphans with the seriousness that Hollywood reserved for kings. They filmed real neighbourhoods, real markets, real light. When the young Federico Fellini apprenticed with Rossellini on Roma, Città Aperta, he was learning a method that would carry Italian cinema for the next half-century."),
        ("Fellini's transformation of the everyday","By 1960, Fellini had transformed neorealism into something entirely his own. La dolce vita gave the West a phrase and a mood that has never faded. 8½ (1963) gave every filmmaker for two generations a template for the film-about-a-filmmaker. Amarcord (1973) gave Italian cinema its warmest, saddest, most tender self-portrait."),
        ("Visconti's operatic scale","Where Fellini went inward, Luchino Visconti went outward and upward. Il Gattopardo (1963), Morte a Venezia (1971), Ludwig (1973) — each is a three-hour meditation on beauty, class and death, filmed with the operatic scale of a Verdi finale. Visconti was, not coincidentally, one of the great opera directors of his century as well."),
        ("The inheritors","Paolo Sorrentino's La Grande Bellezza (2013) — a film Fellini would have recognised as his own grandchild — won the Academy Award for Best Foreign Language Film. Roberto Benigni's La vita è bella (1997) and Giuseppe Tornatore's Nuovo Cinema Paradiso (1988) had already done the same. Italian cinema, more than any other national cinema in Europe, still gives the world films that people carry with them for the rest of their lives."),
        ("Why this matters for Italian learners","To learn Italian is to inherit the vocabulary of one of the most beloved cinematic traditions on earth. Every Italian learner discovers, at some point, that they are not just decoding a language — they are earning access to films that changed the world. And once you can follow La grande bellezza without subtitles, you have arrived somewhere real.")
    ]),
    ("americans-italy","Travel","7.5 Million Americans, One Italy","Why U.S. travellers made Italy their second-most-visited country","24 Aug 2026","pillar-travel.jpg",[
        ("The numbers","In 2023, according to ISTAT, 7.55 million U.S. travellers spent at least one night in Italy — a figure that made the United States Italy's second-largest source market after Germany, and its largest overseas one. AARP's annual travel survey confirms the deeper trend: Italy is the number-one European bucket-list destination for American travellers over 50, edging out France, Greece, Spain and the United Kingdom."),
        ("Why Italy, why now","The reasons are not new. Italy has more UNESCO World Heritage sites than any country on earth. It contains the greatest concentration of Renaissance art in the world. It produced the most beloved cuisine of the twentieth century. And it is small enough that a two-week trip can genuinely cross five distinct cultural regions — Rome, Tuscany, Emilia, the Lakes and Venice — without ever repeating itself."),
        ("The language gap","And yet — for the American traveller who wanted to travel Italy well, in Italian, the language provision was remarkably thin. Duolingo's Italian tree is brief. University adult-education Italian tends toward slow, textbook grammar. High-end language schools are Rome-based and in-person. There was no serious, live, small-group, American-facing Italian school built for adult learners with real cultural ambition."),
        ("What Club Italia set out to solve","Club Italia was built for that gap. A live-online school with native Italian teachers in Italian cities, small groups of 10 to 12, and a cultural method that treats travel Italian not as a phrasebook but as an entry point into the language of one of the most beloved cultures on earth. The traveller who takes CI Principiante in the spring and lands in Rome in the summer is not a different tourist. They are, in a small but real way, a different person.")
    ]),
    ("passato-prossimo","Language","The Passato Prossimo Is Not the Enemy","Why the Italian past tense is the friendliest tense you will meet","12 Aug 2026","course-ci2.jpg",[
        ("The reputation","Ask any American Italian learner what they fear, and the answer comes back with alarming consistency: the past tense. The word passato prossimo is used, in the first weeks of study, with the reverence Americans reserve for tax forms and dentist appointments."),
        ("The reality","And yet the passato prossimo — the Italian equivalent of the English present perfect and simple past combined — is arguably the friendliest tense in the language. It is formed with just two ingredients: the present tense of avere or essere, and the past participle. That is it. There are no subjunctive triggers to worry about, no sequence-of-tense rules to memorise, no exotic irregular endings to survive."),
        ("The one real question","The only real question the passato prossimo asks you is: which auxiliary — avere or essere? And the answer is far more predictable than English learners are led to believe. If the verb takes a direct object (mangiare, leggere, comprare), use avere. If the verb describes motion or a change of state (andare, venire, diventare, nascere, morire), use essere. Reflexive verbs always take essere. That is 95% of the rule."),
        ("A worked example","Ieri ho mangiato una pizza margherita — yesterday I ate a margherita pizza. Sono andato a Roma il weekend scorso — I went to Rome last weekend. Mi sono svegliato alle sette — I woke up at seven. Once you see these patterns in a real Italian conversation, the fear evaporates within a week."),
        ("The Club Italia way","At Club Italia, the passato prossimo is introduced in the second half of CI Principiante — not as a decontextualised drill but inside a real Roman weekend narrative. By the end of CI Elementare in Florence, learners are narrating full weekends, past holidays, and childhood memories in Italian. The past tense stops being an obstacle. It becomes the tense in which most of your Italian life is actually told.")
    ]),
    ("ragu-alla-bolognese","Cuisine","The Real Ragù alla Bolognese","And the eight things it is not","28 Jul 2026","pillar-food.jpg",[
        ("The dish","Ragù alla bolognese, the meat sauce of Bologna, is one of the most misunderstood dishes in the world. In 1982, the Italian Academy of Cuisine deposited the official recipe with the Bologna Chamber of Commerce, in what remains the most Italian bureaucratic act of the twentieth century."),
        ("The official recipe","The deposited recipe calls for beef cartella (thin skirt), pancetta, onion, carrot, celery, tomato paste, meat broth, dry white wine and milk. No garlic. No herbs. No olive oil. No red wine. No cream at the end. No tomato passata as a base. And absolutely, categorically, no spaghetti."),
        ("The eight things ragù is not","One: it is not spaghetti bolognese, which is a dish invented in mid-twentieth-century America and served today across the English-speaking world. In Bologna, ragù is served with tagliatelle — the flat, porous, egg-based pasta that catches sauce the way spaghetti never can. Two: it is not brown. A proper ragù has just enough tomato to blush the meat, no more. Three: it is not quick. The minimum simmer time is two hours, and four is closer to right. Four: it does not contain garlic. Five: it does not contain oregano, basil or bay leaves. Six: the milk is not optional. Seven: the wine is white, not red. Eight: it is finished with a small ladle of broth, not with cream."),
        ("The philosophy","What the deposited recipe protects is not a formula but a philosophy — that a great Italian dish is built by patience, by the right cut of the right meat, by the sofrito of onion, carrot and celery, and by the willingness of the cook to spend an afternoon at the stove for a Sunday lunch that lasts three hours. Ragù is not fast food. It is the slow, ritual food of a very serious culture."),
        ("The Club Italia connection","In the Parliamo Italiano course A Tavola, learners spend a full 85-minute session on the language of ragù — the vocabulary of cuts, of pastas, of simmering, of the family Sunday. By the end of the session, you can order it, cook it, and argue about it in Italian. Which is, if you think about it, all the Italian you really need.")
    ]),
    ("dual-citizenship","Culture","Italian Dual Citizenship, 2026","What the March 2025 reform means for Italian-descent Americans","15 Jul 2026","pillar-tradition.jpg",[
        ("The old rule","For more than a century, Italy has recognised jure sanguinis — citizenship by right of blood. If you could document an unbroken male line from an Italian ancestor who left Italy after 17 March 1861, you were, in the eyes of Italian law, already Italian. You just needed to prove it."),
        ("The March 2025 reform","On 28 March 2025, the Italian Parliament passed the most substantial reform of the citizenship-by-descent law in fifty years. The reform tightened the eligibility line to two generations (parents and grandparents), introduced a mandatory Italian language certification at CEFR B1 for most applicants, and streamlined the consular process to reduce the notorious multi-year wait times."),
        ("The language requirement","For Italian-descent Americans this last change is the one that matters most in practice. B1 is a solid conversational level — the level at which you can hold your own in an Italian bureaucratic office, understand a full Italian film without subtitles, and read Corriere della Sera comfortably. It is not a trivial certification. But it is also entirely reachable, in a structured live-classroom setting, in roughly 18 to 24 months of consistent study."),
        ("The Club Italia pathway","Club Italia's full sequence — CI Principiante (A0→A1.1), CI Elementare (A1.1→A1.2), CI Intermedio (A1.2→A2.1), CI Avanzato (A2.1→A2.2) — plus supplementary Parliamo Italiano conversation courses and cultural capsules, is designed to bring an absolute beginner to CEFR B1 in about two years of once-a-week live study. Every learner who completes the full sequence is ready to sit for the CILS or CELI B1 external exam that Italian consulates accept as proof."),
        ("Why now","With the reform now firmly in effect, U.S. consulates have reported a 40% increase in citizenship-application inquiries in the first six months. The Italian-descent Americans who begin their language study today will hold their certification, and their new Italian passport, well before those who wait.")
    ]),
    ("verdi-life","Opera","Verdi in a Life","Six operas that shaped a nation and still shape Italian","01 Jul 2026","pillar-opera.jpg",[
        ("A national poet","Giuseppe Verdi (1813–1901) is not, for Italians, only a composer. He is a national poet, a political figure, a folk hero, and the man whose surname was scrawled on Milanese walls in 1859 as an acronym for Vittorio Emanuele Re d'Italia — a coded call for Italian unification. When he died, the largest funeral in Italian history brought Milan to a standstill. Two hundred thousand mourners spontaneously sang Va, pensiero from Nabucco as his coffin was carried through the streets."),
        ("Nabucco (1842)","The first of the great political operas, and the source of Va, pensiero — the chorus of the Hebrew slaves in Babylon, sung in the accents of Italians under Austrian rule. To this day, it functions as a second national anthem, sung at moments of national grief and pride."),
        ("Rigoletto (1851)","La donna è mobile — the tenor aria that became the first true opera single, whistled in every Venetian street the morning after the premiere. Verdi kept it secret from the tenor until the final rehearsal because he knew the moment it was heard once, it would be sung by everyone."),
        ("La traviata (1853)","Libiamo ne' lieti calici. The drinking song of the courtesan and the young provincial who loves her. Two centuries later, still the aria most Italian children learn first."),
        ("Aida (1871)","Commissioned by the Khedive of Egypt for the opening of the Suez Canal. The triumphal march is arguably the most famous piece of orchestral music in the world outside of Beethoven's Ninth."),
        ("Otello (1887) and Falstaff (1893)","Verdi's late Shakespeare operas — one a tragedy of jealousy, the other a comedy of a fat English knight — are the two works in which he transcends even himself. Falstaff, completed at eighty, closes with a fugue whose final line is: Tutto nel mondo è burla. Everything in the world is a joke."),
        ("Why this matters for Italian learners","In the Club Italia Capsula Culturale L'Opera, learners spend six 60-minute sessions reading Verdi and Puccini libretti in Italian — following the arias, understanding the recitatives, and hearing the language of a poet who, more than almost anyone, made modern Italian into the language it is.")
    ]),
    ("tuscan-italian","Language","Why Italian Is Really Tuscan","Dante, Boccaccio, Petrarch and the accident of the standard","18 Jun 2026","course-ci2.jpg",[
        ("An accident of geography","The Italian you learn at Club Italia — the Italian spoken on the Rai evening news, taught in Milanese schools, and printed in Corriere della Sera — is not, in any strict historical sense, the language of Italy. It is the language of Florence, of Siena, of Arezzo — the Tuscan dialect of the fourteenth century, elevated to national status by the accident of three writers."),
        ("Dante, Boccaccio, Petrarch","Dante Alighieri's Divine Comedy (finished 1321), Giovanni Boccaccio's Decameron (finished 1353), and Petrarch's Canzoniere (finished 1374) established, between them, the literary prestige of Tuscan so firmly that when Italian unification came five centuries later, no serious question remained about which dialect would become the standard."),
        ("Why this matters for the learner","This history is not just antiquarian. It means that a serious Italian learner is, in a very real sense, learning the language of Dante — a language whose lexical core has changed remarkably little in seven hundred years. Passages of the Inferno are readable, with a little help, by any B1 Italian speaker today. That is a strange and beautiful thing."),
        ("Florence as the site of study","It is also why CI Elementare, the second course in the Club Italia structured mastery track, is set in Florence. To learn Italian in Florence is to learn it where it was made — walking the streets Dante walked, past the Baptistery where he was baptised, along the Arno he watched from his exile.")
    ]),
    ("neapolitan-humour","Culture","Neapolitan Humour, Explained","The philosophy underneath the world's most laughed-in city","02 Jun 2026","course-ci4.jpg",[
        ("A city that laughs","Naples is, by most sociological measures, one of the harder cities in Europe to live in. It is dense, chaotic, poor by northern-European standards, historically underserved by its own state. It is also, by the near-unanimous testimony of every visitor and every Neapolitan, the funniest city on earth."),
        ("The philosophy","The Neapolitan philosopher Benedetto Croce, born just outside the city, wrote that Neapolitan humour is not a decoration on Neapolitan life but its structural foundation. Laughter, in this reading, is not what you do after your problems are solved. Laughter is how you organise your relationship to problems that cannot be solved."),
        ("The registers","Neapolitan humour has three registers. The first is verbal wit — the pun, the double meaning, the swift verbal punch that ends a discussion. The second is physical comedy — the exaggerated gesture, the deadpan face, the sudden shift from apparent seriousness to obvious absurdity. The third, and most sophisticated, is what Neapolitans call sfottò — the affectionate mockery of a friend, delivered with such precision that the friend himself laughs harder than anyone."),
        ("For the learner","Understanding Neapolitan humour requires understanding Naples — its history, its dialects, its centuries of Spanish, French, Bourbon and Piedmontese rule. This is why CI Avanzato, the fourth course in the Club Italia structured mastery track, spends its Neapolitan sessions on the humour, the theatre, the songs and the language of a city that laughs at everything, including its own laughter.")
    ]),
    ("italian-coffee","Cuisine","Italian Coffee Is Not What You Think","A history of espresso, from Naples 1901 to your kitchen","18 May 2026","cap-food.jpg",[
        ("The invention","Espresso as we know it was invented in 1901 by the Milanese engineer Luigi Bezzera, whose steam-pressure machine reduced coffee preparation time from five minutes to thirty seconds. Bezzera sold the patent to Desiderio Pavoni in 1903, and the modern espresso bar was born."),
        ("The moka pot","In 1933 the Piedmontese engineer Alfonso Bialetti patented the moka pot — the octagonal aluminium coffee-maker that would sit on every Italian stovetop for the rest of the century. The Bialetti Moka Express is arguably the most successful piece of consumer industrial design in Italian history. Roughly 300 million have been sold. Two-thirds of Italian households still own one."),
        ("The rules","Italian coffee is governed by unwritten rules that every Italian knows and that most tourists violate. Cappuccino is a morning drink and is never ordered after eleven. Espresso is drunk standing at the counter and is called simply un caffè. The word cappuccio is the Milanese diminutive and is used only in the north. In Naples, you may be given a small glass of water first — this is meant to be drunk before the coffee, not with it, to prepare the palate."),
        ("The vocabulary","Un caffè normale is a standard espresso. Un caffè lungo is longer, weaker. Un caffè ristretto is shorter, stronger. Un caffè macchiato is with a small drop of milk foam. Un caffè corretto is corrected — with grappa, with sambuca, with cognac. Un caffè shakerato is iced and shaken. A latte, in Italian, is a glass of milk — if you order una latte in an Italian bar you will get exactly that."),
        ("For the learner","In Parliamo Italiano · Al Caffè, every one of the twenty spoken conversation sessions is set at an Italian bar. By the end of the course, you can order every one of these variations without thinking, understand the fast reply of a Roman barista, and hold a five-minute conversation about your morning with the person standing next to you at the counter. Which is, in Italy, the essential form of civil communion.")
    ]),
    ("uffizi-italian","Art","How to Read an Uffizi Wall Label","The five Italian words that unlock the museum","05 May 2026","cap-art.jpg",[
        ("The problem","A visitor to the Uffizi Gallery in Florence stands in front of Botticelli's Primavera, wall label at eye height, and reads: Tempera su tavola. Firenze, Galleria degli Uffizi. Attribuito a Sandro Botticelli, ca. 1480. And that visitor, if they do not read Italian, understands almost none of it."),
        ("The five words","But five Italian words, learned and remembered, unlock ninety per cent of every wall label in every Italian museum. They are: tempera (a paint made with egg yolk as the binder, used before the invention of oil paint), tavola (a wood panel, the standard surface before the sixteenth century), olio (oil paint, invented in Flanders and perfected in Venice), tela (canvas, the standard surface from the sixteenth century onward), and affresco (fresh — a mural painted directly onto wet plaster, so the pigment becomes part of the wall itself)."),
        ("The rest of the label","The word attribuito means the painting is generally believed to be by the named artist but there is scholarly doubt. The word cerchia di means the workshop or circle of. The word bottega di means directly from the workshop, probably with the master's supervision but not by his own hand. The word firma means the work is signed."),
        ("The transformation","Once these words are in place, the Uffizi transforms. You are not looking at a beautiful object with a small Italian riddle beneath it. You are looking at a beautiful object whose Italian caption is telling you exactly what it is, how it was made, and how sure the museum is about who made it."),
        ("For the learner","This is exactly what the Capsula Culturale L'Arte at Club Italia does. Six 60-minute cultural sessions, structured around the vocabulary of Italian art history, so that by the end you can walk into any Italian museum in the world and read the walls.")
    ]),
    ("aperitivo","Culture","The Milanese Aperitivo, Decoded","When it started, what it costs, what you actually eat","22 Apr 2026","spoken-ps4.jpg",[
        ("The invention","The Milanese aperitivo — a lightly alcoholic drink taken between six and eight in the evening, accompanied by a spread of small savoury bites — is a nineteenth-century Piedmontese invention that Milan adopted and made its own. The Piedmontese Antonio Benedetto Carpano invented vermouth in Turin in 1786; the Milanese, a century later, invented the ritual that put it at the centre of their evening."),
        ("The drink","The three canonical Milanese aperitivi are the Aperol Spritz (Aperol, Prosecco, soda), the Campari Spritz (Campari, Prosecco, soda) and the Negroni (Campari, gin, sweet vermouth). All three share the same DNA: a bitter Italian herbal liqueur, cut with something lighter, garnished with a slice of orange."),
        ("The food","What distinguishes the Milanese aperitivo from anywhere else in Italy is the food. In a proper Milanese bar, the price of your drink includes access to a small buffet — olives, focaccia, small pieces of pizza, cured meats, cheese, sometimes pasta salads. In the more elaborate versions (called apericena, a portmanteau of aperitivo and cena) the buffet becomes an entire light dinner."),
        ("The rules","Aperitivo is a shared, social ritual. It is taken standing, with friends, in a bar. It is not a solitary sitting-and-scrolling drink. The price is displayed openly and typically ranges from 8 to 15 euros in Milan proper, less outside the centre. Tipping is not expected; a small rounding-up of the bill is polite."),
        ("For the learner","In Parliamo Italiano · Chiacchierando, the fourth course in the spoken track, learners spend a full session on the Milanese aperitivo — the vocabulary, the ritual, the small-talk register that goes with it. By the end, you can hold a full 40-minute aperitivo conversation in Italian without flagging.")
    ]),
]

def post_page(slug, cat, title, sub, date, img, sections):
    rel = "../../"
    body = f"""
<section class="hero" style="min-height:60vh"><div class="hero-bg"><img src="{rel}assets/img/{img}" alt=""></div>
<div class="hero-content"><div style="max-width:64ch"><p class="hero-tag">{cat} · {date}</p><h1>{title}</h1><p class="hero-sub">{sub}</p></div></div></section>

<article class="section-paper"><div class="wrap-narrow">
{"".join(f'<h2 class="display-sm mt-4">{h}</h2><p class="lead" style="margin-top:1rem">{p}</p>' for h,p in sections)}
</div></article>

<section class="section-dark tagline-band"><div class="wrap-narrow"><p class="tag-script">Leggi. Poi parla.</p>
<div class="hero-ctas mt-3" style="justify-content:center;display:flex"><a class="btn btn-3d btn-3d-primary" href="{rel}courses.html">Explore the Courses</a></div></div></section>
"""
    out = ROOT / f"pages/blog/{slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(f"{title} — Cultural Journal · Club Italia", sub, body, rel=rel))
    print(f"wrote {out}")

for p in POSTS: post_page(*p)

# ------- SYLLABUS PDFs (via reportlab) -------
try:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    HAS_RL = True
except ImportError:
    HAS_RL = False
    print("reportlab missing, install...")

if HAS_RL:
    course_data = json.loads((ROOT/"research/course-data.json").read_text())
    (ROOT/"pdf").mkdir(exist_ok=True)
    styles = getSampleStyleSheet()
    title_s = ParagraphStyle('t', parent=styles['Title'], fontName='Times-Bold', fontSize=28, textColor=colors.HexColor('#3A0E12'), spaceAfter=12)
    subt_s = ParagraphStyle('s', parent=styles['Normal'], fontName='Times-Italic', fontSize=14, textColor=colors.HexColor('#A88536'), spaceAfter=20)
    h2_s = ParagraphStyle('h2', parent=styles['Heading2'], fontName='Times-Bold', fontSize=16, textColor=colors.HexColor('#3A0E12'), spaceAfter=8, spaceBefore=12)
    body_s = ParagraphStyle('b', parent=styles['Normal'], fontName='Times-Roman', fontSize=11, textColor=colors.HexColor('#2A0A0D'), leading=15, spaceAfter=6)
    less_s = ParagraphStyle('l', parent=styles['Normal'], fontName='Times-Bold', fontSize=12, textColor=colors.HexColor('#3A0E12'), spaceAfter=4, spaceBefore=8)
    less_body = ParagraphStyle('lb', parent=styles['Normal'], fontName='Times-Roman', fontSize=10.5, textColor=colors.HexColor('#2A0A0D'), leading=14, spaceAfter=4)
    small = ParagraphStyle('sm', parent=styles['Normal'], fontName='Times-Italic', fontSize=9, textColor=colors.HexColor('#8B4E52'), spaceAfter=4)
    for cid, c in course_data.items():
        pdf_path = ROOT / f"pdf/{cid}-syllabus.pdf"
        doc = SimpleDocTemplate(str(pdf_path), pagesize=LETTER, leftMargin=0.9*inch, rightMargin=0.9*inch, topMargin=0.9*inch, bottomMargin=0.9*inch, title=f"{c['title']} Syllabus")
        story = []
        story.append(Paragraph("CLUB ITALIA BY ETEACHER", small))
        story.append(Paragraph(c['title'], title_s))
        story.append(Paragraph(f"{c['tag']} &nbsp;&middot;&nbsp; {c['cefr']} &nbsp;&middot;&nbsp; {c['hours']}", subt_s))
        story.append(Paragraph("The Promise", h2_s))
        story.append(Paragraph(c['promise'], body_s))
        story.append(Spacer(1,10))
        story.append(Paragraph("On Completion, You Can:", h2_s))
        for o in c['outcomes']:
            story.append(Paragraph(f"&#8250; {o}", body_s))
        story.append(Spacer(1,10))
        story.append(Paragraph("The Syllabus — Week by Week", h2_s))
        for i,(t,g) in enumerate(c['syllabus'],1):
            story.append(Paragraph(f"Lesson {i:02d} &nbsp;&middot;&nbsp; {t}", less_s))
            story.append(Paragraph(g, less_body))
        story.append(Spacer(1,14))
        story.append(Paragraph(f"&copy; 2026 eTeacher Group. Club Italia is a trading style of eTeacher Group. Live from Italy. Certified by eTeacher. clubitalia.live &nbsp;&middot;&nbsp; advisor@eTeacherGroup.com", small))
        doc.build(story)
        print(f"pdf: {pdf_path}")
    print("PDFs done.")
