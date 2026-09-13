#!/usr/bin/env python3
"""Port FA-style structure to Club Italia 11 course pages (4 CI, 4 PS, 3 CAP)."""
import os, pathlib, re

ROOT = pathlib.Path("/home/user/workspace/club-italia")
PARTIALS = ROOT / "_partials"

# ---- read partials + prefix ../.. ----
NAV = (PARTIALS / "nav.html").read_text()
FOOT = (PARTIALS / "footer.html").read_text()

def rebase(html: str, prefix: str) -> str:
    # rewrite href="foo.html" or href="pages/..." → prefix + path (but not absolute urls or anchors)
    def sub(m):
        q, url = m.group(1), m.group(2)
        if url.startswith(("http", "#", "mailto:", "tel:", "/", "..")):
            return m.group(0)
        return f'href={q}{prefix}{url}{q}'
    html = re.sub(r'href=(["\'])([^"\']+)\1', sub, html)
    # same for src=
    def sub2(m):
        q, url = m.group(1), m.group(2)
        if url.startswith(("http", "#", "data:", "/", "..")):
            return m.group(0)
        return f'src={q}{prefix}{url}{q}'
    html = re.sub(r'src=(["\'])([^"\']+)\1', sub2, html)
    return html

NAV_PP = rebase(NAV, "../../")
FOOT_PP = rebase(FOOT, "../../")

# ---- unit-cards for CI 01 (A0 to A1.1) ----
CI1_UNITS = [
 ("Salutare: buongiorno, ciao, arrivederci + tu/Lei",
  "Learn the essential Italian greetings and the crucial distinction between the familiar <em>tu</em> and the formal <em>Lei</em>. Practise arriving and leaving with <em>buongiorno, buonasera, ciao, arrivederci, a presto</em>."),
 ("Presentarsi: mi chiamo, sono di, ho... anni",
  "Introduce yourself in Italian. Use <em>mi chiamo Marco, sono di Chicago, ho quarantadue anni</em>. Ask back with <em>e tu, come ti chiami?</em>"),
 ("Nazionalita, professione: sono italiano/a, faccio il/la...",
  "Say where you are from and what you do. <em>Sono americano, sono italiana, faccio l'avvocato, sono insegnante</em>. Learn masculine and feminine adjective agreement in real sentences."),
 ("Numeri 0 a 100, eta, telefono",
  "Master the Italian numbers from zero to one hundred. Give your age, your phone number, a price at the shop: <em>ho trenta anni, il mio numero e...</em>"),
 ("Alfabeto italiano + fare lo spelling",
  "Learn the twenty-one letters of the Italian alphabet, the five extra imported letters, and how to spell your name out loud: <em>C come Como, A come Ancona</em>."),
 ("Verbo essere: presente indicativo",
  "Conjugate the fundamental verb <em>essere</em> across all six persons: <em>io sono, tu sei, lui/lei e, noi siamo, voi siete, loro sono</em>. Use it for identity, origin and description."),
 ("Verbo avere: presente indicativo",
  "Conjugate <em>avere</em>: <em>ho, hai, ha, abbiamo, avete, hanno</em>. Use it for age, possession and the essential idioms <em>ho fame, ho sete, ho freddo</em>."),
 ("Articoli determinativi il/lo/la/i/gli/le",
  "The six forms of the Italian definite article. Learn when to use <em>il libro, lo studente, la casa, i libri, gli studenti, le case</em>, with the sound-based rules native speakers use automatically."),
 ("Articoli indeterminativi un/uno/una",
  "The Italian indefinite article. <em>Un caffe, uno zucchero, una pizza, un'amica</em>. Practise picking the right form in five seconds."),
 ("Nomi maschili e femminili + plurali regolari",
  "The gender of Italian nouns and how to form regular plurals: <em>ragazzo/ragazzi, ragazza/ragazze, studente/studenti</em>. Learn the endings that always tell you gender."),
 ("Chiedere e indicare la direzione",
  "Ask where things are and understand the answer. <em>Scusi, dov'e il Colosseo? Sempre dritto, poi a destra. E qui a sinistra.</em>"),
 ("Ordinare al bar: un caffe, per favore",
  "Order like a Roman at the bar counter. <em>Un caffe, un cappuccino, un cornetto, per favore. Quanto costa? Il conto, grazie.</em>"),
 ("Verbi in -are (parlare, abitare, lavorare) presente",
  "Conjugate the first family of Italian verbs. <em>Io parlo italiano, tu abiti a Roma, noi lavoriamo insieme</em>. Learn the pattern that unlocks hundreds of verbs."),
 ("Aggettivi qualificativi (bello, grande, piccolo) + concordanza",
  "Italian adjectives change to match their noun. <em>Un bel ragazzo, una bella ragazza, i bei quadri, le belle piazze</em>. The rule of four endings that governs almost every adjective."),
 ("Espressioni di tempo: oggi, domani, la mattina, la sera",
  "Situate yourself in the Italian day and week. <em>Oggi, domani, dopodomani, la mattina, il pomeriggio, la sera, la notte</em>."),
 ("Che ore sono? + gli orari",
  "Tell the time in Italian. <em>Che ore sono? Sono le nove e mezza. Il ristorante apre alle otto. Chiude a mezzanotte.</em>"),
 ("I giorni della settimana e i mesi",
  "Name the days and months in Italian. <em>Lunedi, martedi, mercoledi... gennaio, febbraio... Oggi e giovedi, siamo a marzo.</em>"),
 ("Descrivere la propria casa: c'e, ci sono",
  "Describe where you live. <em>C'e una cucina, ci sono due camere, il bagno e piccolo, il salotto e grande</em>. Master the essential <em>c'e / ci sono</em> distinction."),
 ("La famiglia italiana: mio padre, mia madre + possessivi",
  "Introduce your family with Italian possessive adjectives. <em>Mio padre, mia madre, mio fratello, mia sorella, i miei nonni, le mie zie</em>."),
 ("Milestone: raccontare una giornata a Roma per 2 minuti",
  "A live oral milestone. Speak for two full minutes about a day in Rome, using at least ten grammatical structures from units one to nineteen. Marco gives you a written personal feedback note."),
]

# ---- CI 02 (A1.1 to A1.2) ----
CI2_UNITS = [
 ("Verbi in -ere (leggere, scrivere, prendere) presente",
  "Conjugate the second family of Italian verbs. <em>Leggo un libro, scrivi una mail, prendiamo il treno, prendete un caffe?</em>"),
 ("Verbi in -ire (dormire, capire, finire) presente",
  "Conjugate the third family, with the crucial <em>-isc-</em> subgroup. <em>Dormo bene, capisci l'italiano? Finiamo alle sette.</em>"),
 ("Chiedere e dare opinioni: il verbo piacere",
  "The most Italian of verbs, which behaves like nothing in English. <em>Mi piace la pasta, mi piacciono i film italiani, ti piace Firenze? Non mi piace il caldo.</em>"),
 ("Al ristorante: prenotare un tavolo, ordinare",
  "Book a table and order a full Italian meal. <em>Vorrei prenotare un tavolo per due, per stasera alle otto. Come antipasto prendiamo... come primo... come secondo... da bere...</em>"),
 ("I cibi italiani per regione: pasta, pizza, gelato",
  "The map of Italian food. Regional dishes and how to describe them: <em>orecchiette pugliesi, pizza napoletana, risotto milanese, tiramisu veneto, cannoli siciliani</em>."),
 ("Descrivere le persone: aspetto fisico + carattere",
  "Describe people in Italian. <em>E alto, biondo, con gli occhi verdi. E simpatica, intelligente, un po' timida. Assomiglia a sua madre.</em>"),
 ("Il tempo libero: sport, musica, cinema, arte",
  "Talk about your hobbies and interests. <em>Nel tempo libero gioco a tennis, ascolto musica classica, vado al cinema, visito i musei</em>."),
 ("Andare a / stare in / venire da + citta e paesi",
  "The Italian preposition system for movement and place. <em>Vado a Firenze, vado in Toscana, sto a Roma, sto in Italia, vengo dagli Stati Uniti</em>. The rules that trip up every learner."),
 ("Verbi modali: potere, volere, dovere presente",
  "The three verbs that build polite Italian. <em>Posso avere il conto? Vorrei un bicchiere di vino. Devo andare adesso. Vuoi venire con noi?</em>"),
 ("Fare la spesa al mercato: quantita",
  "Shop at a Tuscan market with proper quantities. <em>Un chilo di pomodori, mezzo chilo di zucchine, cento grammi di parmigiano, un litro di latte, una decina di uova</em>."),
 ("Comprare vestiti: taglia, colore, prezzo",
  "Shop for clothes in a Florence boutique. <em>Che taglia porta? Porto la 42. Posso provare questa giacca? Ce l'avete in nero? Quanto viene?</em>"),
 ("Prendere i mezzi pubblici: il biglietto, la fermata",
  "Navigate Italian public transport. <em>Un biglietto per il centro, per favore. Che autobus devo prendere? Dove scendo? La prossima fermata e Duomo.</em>"),
 ("Il futuro immediato: stare per + infinito",
  "Express what is about to happen. <em>Sto per uscire, il treno sta per partire, sta per piovere</em>. The elegant Italian equivalent of the English 'about to'."),
 ("Il passato prossimo con avere",
  "Speak in the past for the first time. <em>Ho mangiato una pizza, ho visto il David, ho parlato con Chiara, ieri ho lavorato molto</em>. Learn how the past participle is built."),
 ("Il passato prossimo con essere",
  "The other half of the past tense, with agreement of the past participle. <em>Sono andato a Firenze, sono andata a Siena, siamo partiti alle sei, sono nate due bambine</em>."),
 ("Raccontare il fine settimana: cosa hai fatto?",
  "Tell the story of your weekend. Use at least eight verbs in the past: <em>sabato sono andato al mercato, ho comprato del formaggio, poi sono passato dai miei amici, abbiamo cenato insieme</em>."),
 ("L'arte fiorentina: descrivere un quadro con Chiara",
  "A cultural bridge. Describe a Renaissance painting in Italian with Chiara. <em>Nel quadro vedo una donna, in primo piano c'e..., sullo sfondo si vede..., i colori sono caldi, l'atmosfera e serena</em>."),
 ("Le preposizioni articolate: al, dal, nel, sul",
  "The contracted prepositions that native Italians use without thinking. <em>Vado al mercato, torno dal medico, il libro e nel cassetto, il gatto e sul tavolo</em>. All fifteen forms in one session."),
 ("Il condizionale di cortesia: vorrei, potrei, mi piacerebbe",
  "Speak like a polite Italian in shops, restaurants and offices. <em>Vorrei un caffe, potrei avere il menu? Mi piacerebbe vedere Firenze di notte. Sarebbe possibile prenotare?</em>"),
 ("Milestone: 3 minuti di racconto delle vacanze in Toscana",
  "A live oral milestone. Three minutes narrating a Tuscan holiday in the past tense, with at least twelve past-tense verbs. Chiara delivers a full written feedback note."),
]

# ---- CI 03 (A1.2 to A2.1) Bologna ----
CI3_UNITS = [
 ("L'imperfetto: da bambino, io...",
  "The Italian past for descriptions and habits. <em>Da bambino, abitavo a Bologna, andavo a scuola in bicicletta, mia nonna cucinava il ragu ogni domenica</em>."),
 ("Imperfetto vs passato prossimo: mentre + narrazione",
  "The single hardest choice in Italian grammar, taught clearly. <em>Mentre camminavo per via dell'Indipendenza, ho incontrato un vecchio amico. Pioveva, allora sono entrato in un bar.</em>"),
 ("I pronomi diretti: lo, la, li, le",
  "Direct object pronouns replace the noun. <em>Il libro? Lo leggo stasera. La pasta? La preparo io. I bambini? Li porto io a scuola. Le chiavi? Le ho perse.</em>"),
 ("I pronomi indiretti: mi, ti, gli, le, ci, vi, gli",
  "Indirect object pronouns for the person receiving. <em>Le ho scritto una mail, gli ho telefonato ieri, ci hanno regalato un vino, vi mando la foto stasera</em>."),
 ("Il verbo piacere avanzato: mi piace / mi piacciono / mi piaceva",
  "The full grammar of <em>piacere</em> across persons and tenses. <em>Ti piaceva la scuola? Non gli piacciono le verdure. Ci piacerebbe vedere Bologna.</em>"),
 ("Ne partitivo: quanto ne vuoi?",
  "The particle <em>ne</em>, the missing piece of every Italian conversation. <em>Ne vuoi un po'? Ne prendo due etti. Quanti fratelli hai? Ne ho tre.</em>"),
 ("Al mercato di Bologna: quantita avanzate con Giulia",
  "Shop with a Bolognese chef. <em>Un etto di prosciutto crudo di Parma tagliato sottile, due etti di mortadella, mezzo chilo di tortellini freschi, una forma piccola di parmigiano stagionato ventiquattro mesi</em>."),
 ("La cucina emiliana: descrivere una ricetta",
  "Describe an Italian recipe step by step. <em>Prima si soffrigge la cipolla, poi si aggiunge la carne, si versa il vino rosso, si lascia cuocere per tre ore a fuoco lento</em>. The impersonal <em>si</em>."),
 ("Comparativi: piu... di, meno... di, cosi... come",
  "Compare things and people in Italian. <em>Bologna e piu antica di Milano, la pasta al ragu e piu ricca della pasta al pomodoro, non e cosi caro come sembra</em>."),
 ("Superlativi: il piu, il meno, bellissimo, buonissimo",
  "The Italian love for absolute superlatives. <em>La Basilica di San Petronio e la piu grande di Bologna. Il tiramisu era buonissimo, la giornata bellissima.</em>"),
 ("Il periodo ipotetico del primo tipo: se + presente + futuro",
  "Real conditions in Italian. <em>Se piove, resto a casa. Se hai tempo, vieni a cena. Se studi ogni giorno, imparerai velocemente.</em>"),
 ("I possessivi con la famiglia: mio fratello vs il mio amico",
  "The article-drop rule with family. <em>Mio padre, mia madre, mio fratello (no article) vs il mio migliore amico, la mia sorellina, i miei genitori (article)</em>."),
 ("Verbi riflessivi: alzarsi, vestirsi, divertirsi",
  "Talk about your daily routine and feelings. <em>Mi alzo alle sette, mi vesto, faccio colazione, mi diverto molto in Italia, ci siamo conosciuti a Bologna</em>."),
 ("Passato prossimo dei riflessivi: mi sono alzato",
  "Reflexive verbs in the past always take <em>essere</em>. <em>Mi sono alzata tardi, ci siamo divertiti, si sono sposati a giugno, vi siete conosciuti a Roma?</em>"),
 ("Esprimere accordo e disaccordo: sono d'accordo, non credo",
  "Have a real Italian conversation with opinions. <em>Sono d'accordo con te, non sono d'accordo, secondo me hai ragione, credo che sia una buona idea, non lo so davvero</em>."),
 ("Il gerundio: stare + gerundio",
  "The Italian present continuous. <em>Sto studiando italiano, sta piovendo, stiamo mangiando, cosa stai facendo? Stavo pensando a te.</em>"),
 ("Le espressioni di frequenza: sempre, spesso, qualche volta, mai",
  "Say how often you do things. <em>Vado sempre al mercato il sabato, mangio spesso la pasta, qualche volta esco con gli amici, non ho mai visto la neve a Bologna</em>."),
 ("Chiedere e dare consigli: dovresti, potresti",
  "Give advice in polite Italian. <em>Dovresti visitare le due torri, potresti provare le tagliatelle al ragu, ti consiglio di andare a piedi, se fossi in te andrei presto</em>."),
 ("A cena a casa di Giulia: la conversazione a tavola",
  "The full Italian dinner conversation. <em>Buonissimo, complimenti alla cuoca. Prendine ancora un po', ce n'e tantissimo. Sono sazio, ma il tiramisu non lo posso rifiutare. Alla salute!</em>"),
 ("Milestone: raccontare una cena bolognese in 4 minuti",
  "A live oral milestone. Four minutes narrating a Bolognese dinner, weaving past tenses, direct and indirect pronouns, comparatives and reflexives. Giulia gives you a detailed rubric-based review."),
]

# ---- CI 04 (A2.1 to A2.2) Naples ----
CI4_UNITS = [
 ("Il futuro semplice: parlero, saro, avro",
  "The Italian future tense in all persons. <em>Domani andro a Napoli, la settimana prossima prendero il traghetto per Capri, un giorno vivro sulla costa amalfitana</em>."),
 ("Il futuro anteriore: quando avro finito",
  "Talk about future actions completed before other future actions. <em>Quando avro finito il lavoro, partiro. Ti chiamero appena saro arrivato a Napoli.</em>"),
 ("Il condizionale semplice: vivrei, andrei, mangerei",
  "Express hypotheses and polite requests. <em>Vivrei volentieri a Napoli, andrei ogni sera a mangiare una pizza, ordinerei sempre una margherita, sarei felicissimo</em>."),
 ("Il condizionale composto: sarei andato, avrei voluto",
  "Express past regret or unrealised plans. <em>Sarei andato al concerto, ma ero troppo stanco. Avrei voluto vedere il Vesuvio da vicino. Ti avrei chiamato prima.</em>"),
 ("Il periodo ipotetico del secondo tipo: se avessi... andrei",
  "Real hypothetical conditions in Italian. <em>Se avessi tempo, verrei con te. Se abitassi a Napoli, mangerei pizza ogni giorno. Se fossi ricco, comprerei una villa a Positano.</em>"),
 ("Introduzione al congiuntivo presente: penso che tu sia",
  "The single feature that separates a beginner from a real Italian speaker. <em>Penso che tu sia molto brava, credo che sia una buona idea, spero che venga anche Luca, e importante che voi capiate</em>."),
 ("Il congiuntivo dopo espressioni impersonali: e importante che",
  "The impersonal expressions that always trigger the subjunctive. <em>E importante che tu studi ogni giorno, e necessario che partiamo presto, bisogna che ci pensiamo bene</em>."),
 ("Il si impersonale: a Napoli si mangia bene",
  "The Italian impersonal construction. <em>In Italia si mangia bene, a Napoli si parla il dialetto, in questo bar si prende un ottimo caffe, la sera si esce sempre tardi</em>."),
 ("I pronomi combinati: me lo, glielo, ce li",
  "The trickiest pronouns in Italian, combining direct and indirect. <em>Me lo dai? Te lo do. Glielo dico io. Ce li porta domani. Non ve lo ripeto piu.</em>"),
 ("Verbi riflessivi reciproci: ci vediamo, ci sentiamo",
  "Reciprocal reflexives for relationships. <em>Ci vediamo domani, ci sentiamo dopo, si sono conosciuti a Napoli, ci siamo lasciati bene, si scrivono ogni giorno</em>."),
 ("La forma passiva: la pizza e stata inventata a Napoli",
  "Build passive sentences in Italian. <em>La pizza margherita e stata inventata a Napoli, il Vesuvio e visitato da milioni di turisti, questa canzone e cantata in tutto il mondo</em>."),
 ("I pronomi relativi: che, cui, il quale",
  "Build complex sentences with relative pronouns. <em>L'uomo che ho visto, la citta in cui vivo, l'amico di cui ti ho parlato, il ristorante nel quale abbiamo cenato</em>."),
 ("Il discorso indiretto al presente: mi ha detto che...",
  "Report what other people said. <em>Luca mi ha detto che parte domani, mi ha chiesto se voglio venire, ha risposto che non lo sa, mi ha spiegato come si prepara la pizza napoletana</em>."),
 ("Connettivi logici: pero, tuttavia, quindi, invece",
  "Argue in real Italian. <em>Napoli e caotica, pero e affascinante. Volevo prendere il traghetto, tuttavia il mare era mosso. Non c'era il sole, quindi siamo restati a casa. Non mi piace il caffe, invece adoro il te.</em>"),
 ("Esprimere probabilita: forse, magari, chissa",
  "Speculate the Italian way. <em>Forse domani vado a Capri, magari partiamo insieme, chissa se piovera, sara stanco, avra dimenticato l'appuntamento</em>."),
 ("La costa amalfitana: descrivere un paesaggio",
  "Describe an Italian landscape with real vocabulary. <em>Un mare azzurrissimo, scogliere che cadono a picco sull'acqua, limoneti terrazzati sulle colline, case colorate arrampicate sulla montagna, un tramonto indimenticabile</em>."),
 ("Argomentare: secondo me... primo, secondo, infine",
  "Structure a real Italian argument. <em>Secondo me la cucina napoletana e la migliore d'Italia. Primo, perche usa ingredienti freschi. Secondo, perche ha una tradizione antichissima. Infine, perche la pizza e nata qui.</em>"),
 ("Narrazione estesa: raccontare un viaggio",
  "Tell a full Italian story using every tense. <em>L'estate scorsa sono partito per Napoli. Il primo giorno pioveva, allora ho visitato il museo. Il giorno dopo il sole splendeva. Ho preso il traghetto e sono andato a Capri, dove avrei voluto restare per sempre.</em>"),
 ("Un dibattito in italiano: la vita al Sud",
  "A guided live debate. <em>Ha ragione chi dice che al Sud si vive meglio? Da una parte..., dall'altra parte..., e vero che... ma bisogna considerare che...</em>"),
 ("Milestone: presentazione libera di 5 minuti in italiano",
  "A live oral milestone. Five minutes of prepared speech on a chosen topic, with Q&A from the class. Luca provides a full CEFR A2.2 evaluation and a written note on your path to B1."),
]

# ---- Spoken PS01 Al Caffe (Rome) ----
PS1_UNITS = [
 ("Il primo caffe della mattina", "Order your first Italian coffee correctly and read the room. <em>Un caffe, per favore. Al banco o al tavolino? Un cappuccino e un cornetto. Quanto le devo?</em>"),
 ("Al banco vs al tavolino", "Understand the price difference and etiquette. <em>Al banco costa un euro, al tavolino tre euro. Prendo al banco, grazie.</em>"),
 ("Il tabaccaio: sigarette, francobolli, biglietti", "The multi-purpose Italian tobacconist. <em>Un pacchetto di Marlboro, tre francobolli per gli Stati Uniti, un biglietto per l'autobus di novanta minuti</em>."),
 ("L'edicola: giornali e riviste", "Buy a newspaper at the classic Italian newsstand. <em>Il Corriere, per favore. Avete anche La Repubblica? Quanto costa? Ha un sacchettino?</em>"),
 ("Chiedere l'ora al passante", "Ask the time on the street. <em>Scusi, sa che ore sono? Le tre e un quarto, grazie. Sa dov'e Piazza Navona?</em>"),
 ("Perdersi in centro a Roma", "Ask for directions when lost. <em>Scusi, mi sono perso. Come arrivo al Pantheon? Sempre dritto, poi la seconda a destra, non puo sbagliare.</em>"),
 ("Prenotare un tavolo al telefono", "Book a table by phone. <em>Buonasera, vorrei prenotare un tavolo per due, per stasera alle otto e mezza. A nome Rinaldi. Grazie, arrivederci.</em>"),
 ("Ordinare la colazione al bar", "Full Italian breakfast at the bar. <em>Un cappuccino non troppo caldo, un cornetto alla crema, una spremuta d'arancia. Quanto viene tutto?</em>"),
 ("Chiacchierare con il barista", "Small talk with the barista, a Roman institution. <em>Buongiorno, come va? Che caldo oggi, eh! Il solito, per favore. A dopo!</em>"),
 ("Fare due chiacchiere con il vicino di casa", "Neighbourly exchanges in Italian. <em>Buongiorno signora Rossi, come sta? Ha visto che tempo? Salutami suo marito, mi raccomando!</em>"),
 ("Salutare in vari momenti della giornata", "Master when to say what. <em>Buongiorno fino a pranzo, buon pomeriggio, buonasera dalle sei, buonanotte prima di andare a letto</em>."),
 ("Ringraziare e rispondere: prego, di niente, figurati", "The five Italian ways to say 'you're welcome'. <em>Grazie mille! Prego. Grazie di tutto. Di niente. Grazie ancora! Figurati, e stato un piacere.</em>"),
 ("Chiedere scusa: mi scusi, scusami, mi spiace", "The full range of Italian apologies. <em>Mi scusi, non l'avevo vista. Scusami per il ritardo. Mi dispiace tanto, era importante per te?</em>"),
 ("Al bar dopo cena: un digestivo", "The Italian evening ritual. <em>Prendiamo un digestivo? Un amaro, un limoncello, una grappa. Offro io! No no, questa volta pago io.</em>"),
 ("Complimenti in italiano: che bello!", "React with real Italian enthusiasm. <em>Che bello! Che buono! Che carino! Complimenti! Bravissimo! Fantastico!</em>"),
 ("Reagire in italiano: davvero? non ci credo!", "The reactive interjections that make you sound Italian. <em>Davvero? Non ci credo! Ma dai! Ma pensa te! Che roba! Incredibile!</em>"),
 ("Piccole trattative: uno sconto al mercato", "Bargain gently at a Roman market. <em>Quanto viene? Dieci euro? Un po' caro, non le pare? Mi fa uno sconticino? Nove euro? Affare fatto.</em>"),
 ("Chiedere aiuto al passante", "Ask a stranger for help gracefully. <em>Scusi, mi puo aiutare? Non riesco a trovare... Le chiedo un favore... Grazie mille, e stato gentilissimo.</em>"),
 ("Chiamare un taxi", "Call and take a Roman taxi. <em>Pronto, un taxi in Via del Corso? Grazie. Mi porta all'aeroporto, per favore? Quanto viene? Tenga pure il resto.</em>"),
 ("Milestone: una mattinata a Roma da solo, in italiano", "Live milestone. Marco simulates a full Roman morning with five real interactions. You handle each one entirely in Italian with a detailed voice-note report at the end."),
]

# ---- PS02 A Tavola (Florence) ----
PS2_UNITS = [
 ("Prenotare un tavolo in trattoria", "Book a proper Tuscan trattoria. <em>Vorrei prenotare un tavolo per quattro persone, per venerdi sera alle otto. A nome Weller. Preferibilmente all'aperto.</em>"),
 ("Arrivare al ristorante e chiedere il tavolo", "The full arrival ritual. <em>Buonasera, abbiamo prenotato a nome Weller. Da questa parte, prego. Il vostro tavolo e questo. Va bene? Perfetto, grazie.</em>"),
 ("Leggere il menu: antipasto, primo, secondo, dolce", "Navigate the Italian menu correctly. <em>Come antipasto abbiamo bruschette e crostini, i primi sono pasta e risotti, i secondi carne e pesce, poi i contorni e i dolci</em>."),
 ("Ordinare un menu completo alla toscana", "Order a proper Florentine meal. <em>Come antipasto, crostini toscani. Come primo, pappa al pomodoro per me, ribollita per lui. Come secondo, la bistecca alla fiorentina per due. Da bere, un chianti classico.</em>"),
 ("Chiedere consiglio al cameriere", "Ask the waiter what to have. <em>Che cosa ci consiglia stasera? Qual e la specialita della casa? Il pesce e fresco? La pasta e fatta in casa? Cosa abbina con questo vino?</em>"),
 ("Ordinare il vino: la carta dei vini", "Order Italian wine like you know what you're doing. <em>La carta dei vini, per favore. Un chianti classico riserva. Un bicchiere di prosecco. Va bene un rosso corposo con la bistecca?</em>"),
 ("Preferenze e allergie: sono vegetariano, sono celiaco", "State dietary needs in Italian. <em>Sono vegetariano, non mangio carne ne pesce. Sono celiaco, ha piatti senza glutine? Sono allergico ai frutti di mare. Non tollero il lattosio.</em>"),
 ("Complimentarsi con lo chef", "Give real Italian compliments to the chef. <em>Complimenti allo chef! Era tutto squisito. La pasta era perfetta, al dente giusta. Il ragu buonissimo, come lo faceva mia nonna.</em>"),
 ("Al mercato di San Lorenzo", "Shop at the Florentine central market. <em>Un etto di prosciutto crudo dolce, due mozzarelle di bufala, mezzo chilo di pomodori maturi, un pane toscano, ecco qua signora</em>."),
 ("Comprare olio, aceto, tartufo", "Buy Tuscan luxuries. <em>Vorrei un olio extravergine, biologico se possibile. Un aceto balsamico invecchiato. Ha del tartufo bianco fresco? Mi fa assaggiare?</em>"),
 ("Invito a cena a casa: cosa porto?", "Handle an Italian dinner invitation. <em>Ti va di venire a cena venerdi? Con piacere! Cosa porto? Non serve niente, ma se vuoi un dolce e sempre benvenuto. A che ora? Verso le otto e mezza.</em>"),
 ("A tavola: passami il sale, prendine ancora", "The full Italian table conversation. <em>Mi passi il sale, per favore? Certo. Prendine ancora un po', ce n'e tantissimo. Sono sazio, ma era troppo buono per rifiutare.</em>"),
 ("Brindare in italiano: cin cin, salute, alla salute", "The Italian toast, done right. <em>Alziamo i calici! Cin cin! Alla salute! Alla nostra! Alla salute di Chiara, buon compleanno! Prosit!</em>"),
 ("Chiedere il conto: il conto per favore", "Pay the bill Italian style. <em>Ci porta il conto, per favore? Paghiamo alla romana, dividiamo per quattro. Coperto e servizio inclusi? Accettate carta? Tenga il resto.</em>"),
 ("Un caffe dopo cena", "The obligatory post-meal coffee. <em>Prendiamo un caffe? Un espresso e un ammazzacaffe. Un amaro. Un limoncello ghiacciato. Offre la casa? Grazie, gentilissimi.</em>"),
 ("Il dolce: gelato e tiramisu", "Order Italian dessert correctly. <em>Cosa avete di dolce? Fatto in casa? Un tiramisu, una panna cotta ai frutti di bosco. Un gelato: nocciola, pistacchio e stracciatella, per favore.</em>"),
 ("Reclamare educatamente: e freddo, e crudo", "Complain in polite Italian. <em>Mi scusi, la pasta e un po' fredda. La bistecca era al sangue, ma io l'avevo chiesta media. Ci puo cambiare il piatto? Grazie della comprensione.</em>"),
 ("Un aperitivo fiorentino: spritz e stuzzichini", "The Italian aperitivo. <em>Due spritz, per favore. Cosa ci portate come stuzzichini? Un tagliere di salumi e formaggi misto? Perfetto, grazie.</em>"),
 ("Dare la ricetta di un piatto italiano", "Explain how to cook an Italian dish. <em>Prima soffriggi la cipolla nell'olio, poi aggiungi la pancetta, dopo un minuto il pomodoro, sale, un pizzico di zucchero, lasci cuocere venti minuti a fuoco basso</em>."),
 ("Milestone: una cena intera in italiano con Chiara", "Live milestone. Chiara sets up a full Florentine dinner scenario in Zoom, and you handle the entire evening in Italian: greeting, ordering, conversation, bill, farewells."),
]

# ---- PS03 In Viaggio (Venice) ----
PS3_UNITS = [
 ("Arrivare a Venezia in treno", "Arrive at Santa Lucia and find your way. <em>Scusi, dove sono i vaporetti? Il numero uno per San Marco, per favore. Un biglietto ACTV di ventiquattro ore. Grazie, buon soggiorno!</em>"),
 ("Fare il check-in in albergo", "Check into an Italian hotel professionally. <em>Buongiorno, ho una prenotazione a nome Kim. Il documento, prego. Quante notti? Colazione inclusa? A che ora? Che tipo di camera? Con vista sul canale.</em>"),
 ("Chiedere informazioni turistiche", "Get real tourist information. <em>Scusi, dove posso prendere una gondola? Quanto costa un giro? A che ora chiude il Palazzo Ducale? Ci vuole la prenotazione per la Basilica di San Marco?</em>"),
 ("Prendere il vaporetto giusto", "Navigate Venice by water. <em>Scusi, questo vaporetto va a Murano? No, deve prendere il numero quattro punto uno. Da dove parte? Al pontile qui accanto. Quanto ci mette?</em>"),
 ("Comprare i biglietti dei musei", "Buy museum tickets in Italian. <em>Due biglietti interi per la Galleria dell'Accademia, per favore. Ci sono sconti per studenti? L'audioguida in inglese? Fino a che ora possiamo entrare?</em>"),
 ("Perdersi nelle calli di Venezia", "The real Venetian experience. <em>Scusi, mi sono perso. Come arrivo al Ponte di Rialto? Prosegua dritto, giri a sinistra al secondo campo, e poi sempre dritto fino al ponte, non puo sbagliare.</em>"),
 ("Al ristorante veneziano: cicchetti e ombre", "Order the local Venetian way. <em>Due ombre di rosso e un piatto di cicchetti misti, per favore. Prendo anche delle sarde in saor. E poi baccala mantecato su polenta. Grazie.</em>"),
 ("Prenotare un tour in gondola", "Book a real gondola tour. <em>Quanto costa un giro in gondola? Ottanta euro per trenta minuti? Possiamo fare mezz'ora? In quattro persone, va bene? Passiamo per il Canal Grande?</em>"),
 ("Comprare un souvenir di Murano", "Shop for authentic Murano glass. <em>Quanto viene questo bicchiere? E vetro di Murano vero? Ha il certificato? Mi fa uno sconto se ne prendo sei? Me li puo impacchettare bene?</em>"),
 ("Fare fotografie: mi puo fare una foto?", "Ask for a photo in Italian. <em>Scusi, ci puo fare una foto? Basta premere qui. Ancora una, per favore? Grazie mille. Vuole che gliela faccia anche a lei?</em>"),
 ("Alla stazione: cambiare treno", "Handle train changes in Italian. <em>Scusi, questo treno ferma a Bologna? A che ora arriva? Devo cambiare a Padova? Da che binario parte il regionale? Il biglietto va convalidato?</em>"),
 ("Comprare biglietti del treno online", "Buy Italian train tickets in real time. <em>Un biglietto Frecciarossa Venezia-Roma per domani mattina alle otto, seconda classe. Un posto vicino al finestrino. La prima colazione a bordo? Perfetto.</em>"),
 ("Chiedere consiglio a un veneziano", "Get insider tips from a local. <em>Scusi, lei e di Venezia? Un consiglio da veneziano: dove si mangia bene qui vicino, non da turisti? E per un aperitivo autentico? Grazie mille, e stato gentilissimo.</em>"),
 ("Il maltempo: acqua alta e passerelle", "Handle Venice-specific weather. <em>Domani c'e acqua alta? A che ora? Fino a dove arriva? Ci sono le passerelle? Meglio prendere gli stivali? Grazie del consiglio.</em>"),
 ("Prenotare una degustazione di vini in Veneto", "Book a Veneto wine tasting. <em>Vorrei prenotare una degustazione per due, sabato pomeriggio. Prosecco e amarone? Quanto dura? C'e anche un piccolo pranzo? Perfetto, confermo.</em>"),
 ("Un problema con la prenotazione", "Handle a booking problem calmly. <em>Buongiorno, ho un problema con la mia prenotazione. Non risulta a sistema. Ho una mail di conferma. Mi puo aiutare a sistemare la cosa? Grazie della disponibilita.</em>"),
 ("Il taxi acqueo per l'aeroporto", "Book a water taxi to Marco Polo airport. <em>Un taxi acqueo per l'aeroporto per domani alle sei del mattino. Da dove ci prende? Quanto viene? Un'ora e mezza prima del volo? D'accordo, grazie.</em>"),
 ("Fare shopping in Rialto", "Shop at Rialto markets. <em>Quanto viene il chilo di gamberi? Sono freschi? Del pesce spada, un trancio. Un'orata piccola. Me le pulisce? Grazie, buona giornata!</em>"),
 ("Raccontare il viaggio ai propri amici", "Tell friends about your trip. <em>Ho passato tre giorni fantastici a Venezia. Ho preso la gondola al tramonto, ho mangiato cicchetti divini, mi sono anche perso dieci volte nelle calli, ma e questo il bello.</em>"),
 ("Milestone: tre giorni in Veneto in italiano con Francesca", "Live milestone. Francesca guides you through a simulated three-day Veneto trip, and you handle every conversation in Italian: hotel, museums, restaurants, water taxi, farewells."),
]

# ---- PS04 Chiacchierando (Milan) ----
PS4_UNITS = [
 ("L'aperitivo milanese in Navigli", "The Milan aperitivo, done properly. <em>Due spritz e due negroni. Il buffet e libero? Fino a che ora? Cosa mi consigli tra i vini al calice? Un lombardo rosso.</em>"),
 ("Chiacchierare del lavoro: cosa fai di bello?", "Small talk about work in real Italian. <em>Tu che lavoro fai? Sono consulente, mi occupo di marketing digitale. Un lavoro impegnativo. Si, ma mi piace. E tu? Cosa fai di bello?</em>"),
 ("Parlare del proprio quartiere a Milano", "Talk about where you live. <em>Abito in zona Porta Romana, mi trovo benissimo. E' vivace ma tranquillo la sera. Ci sono tanti locali, ristoranti, e comodo per il centro. Tu di che zona sei?</em>"),
 ("Un colloquio informale in italiano", "Handle an informal Italian interview. <em>Mi parli un po' di lei. Sono di Chicago, vivo a Milano da tre anni, lavoro nel settore moda. Ha esperienza in questo campo? Si, ho lavorato cinque anni da Prada.</em>"),
 ("Fare un discorso a una cena tra amici", "Give an Italian toast among friends. <em>Vorrei fare un piccolo brindisi. A Chiara, che oggi compie quaranta anni. A tutti noi che siamo qui riuniti. Alla vita, all'amicizia, alla salute. Cin cin!</em>"),
 ("Discutere di politica italiana (con garbo)", "Discuss Italian politics tactfully. <em>Non voglio entrare troppo nel merito, ma secondo me... Ognuno ha le sue idee, no? Bisogna vedere le cose da piu punti di vista. Cambiamo discorso?</em>"),
 ("Parlare di calcio: Milan vs Inter", "Talk football in Milanese. <em>Tu per chi tifi? Milan da sempre. Che partita ieri sera! Il gol al novantesimo, incredibile. Il derby domenica prossima, non me lo perdo per nulla al mondo.</em>"),
 ("Raccontare un aneddoto divertente", "Tell a funny Italian anecdote. <em>Devo raccontarvi una cosa che mi e successa. L'altro giorno stavo salendo sul tram, quando all'improvviso... Non ci crederete mai! Vi giuro che e successo davvero.</em>"),
 ("Esprimere sentimenti: sono felice, arrabbiato, deluso", "Express real feelings in Italian. <em>Sono felicissimo per te. Sono un po' triste, sinceramente. Mi ha fatto arrabbiare tantissimo. Sono deluso da come si e comportato. Mi sento sollevato.</em>"),
 ("Consigliare una serie o un film", "Recommend Italian TV and film. <em>Hai visto La Grande Bellezza? Devi guardarlo. Ti consiglio Suburra su Netflix. Se ti piacciono i gialli, prova Petra. Guardalo assolutamente, non ti pentirai.</em>"),
 ("Un dibattito informale: sei d'accordo?", "Have a real Italian debate. <em>Ma tu sei d'accordo? Assolutamente si. In parte si e in parte no. Direi di no, non sono per nulla d'accordo. Vediamo di trovare un punto d'incontro.</em>"),
 ("Fare le condoglianze: mi dispiace tanto", "Offer Italian condolences properly. <em>Ho saputo di tua madre, mi dispiace tantissimo. Ti sono vicino in questo momento. Se hai bisogno di qualcosa, io ci sono. Coraggio, sara dura, ma passera.</em>"),
 ("Congratularsi: bravi! complimenti!", "Congratulate the Italian way. <em>Congratulazioni! Bravi voi! Ve lo siete meritato. Complimenti vivissimi per il traguardo. Sono fiero di te, davvero. Bravo, continua cosi.</em>"),
 ("Un litigio educato: non sono d'accordo", "Disagree without a fight. <em>Guarda, non sono affatto d'accordo. Rispetto la tua opinione, ma io la vedo diversamente. Non e questione di aver ragione, e questione di prospettive. Restiamo amici?</em>"),
 ("Discutere di arte contemporanea a Milano", "Talk contemporary art in Milanese. <em>Sei stato all'Hangar Bicocca? Che ne pensi? Personalmente lo trovo geniale. A me lascia freddo, sinceramente. E' arte o e provocazione? Bel dibattito.</em>"),
 ("Consigliare un ristorante a un amico", "Recommend an Italian restaurant convincingly. <em>Ti consiglio caldamente Da Cesare in via Marghera. Cucina milanese autentica, ambiente familiare, prezzi onesti. Prenota, altrimenti non trovi posto. Digli che ti mando io.</em>"),
 ("Parlare di moda: la settimana della moda", "Talk fashion in Milan. <em>La settimana della moda e sempre uno spettacolo. Quest'anno hanno sfilato Prada, Armani, Dolce e Gabbana. Le tendenze per l'autunno? Molto oro e nero. Che ne pensi?</em>"),
 ("Confrontare il Nord e il Sud d'Italia", "Compare North and South Italy. <em>Milano e piu veloce, piu europea, piu efficiente. Napoli e piu calda, piu passionale, piu autentica. Sono due Italie diverse, ma entrambe bellissime a modo loro.</em>"),
 ("Un discorso di presentazione al lavoro", "Give a business intro in Italian. <em>Buongiorno a tutti, mi presento. Mi chiamo Sarah Kim, sono la nuova responsabile marketing. Vengo dagli Stati Uniti, ho un'esperienza di dieci anni nel settore. Sono felice di lavorare con voi.</em>"),
 ("Milestone: una serata milanese completa in italiano", "Live milestone. Alessandro simulates a full evening in Milan: aperitivo, dinner, discussion, toast, farewells. You handle it all in fluid Italian with a written B1-readiness report."),
]

# ---- CAP 01 La Cucina (6 lessons) ----
CAP1_UNITS = [
 ("Al mercato di Bologna con Giulia", "Shop with a Bolognese chef at the Mercato delle Erbe. Learn to name every fruit and vegetable, request precise cuts, and understand butcher jargon. <em>Un etto di guanciale tagliato spesso, mezzo chilo di ossobuco, una gallina intera per il brodo</em>."),
 ("La pasta fresca: sfoglia, tagliatelle, tortellini", "The full grammar of fresh Italian pasta, kneaded on-camera. <em>La sfoglia, il mattarello, le tagliatelle larghe, i tortellini chiusi a mano, farina zero doppio zero, uova fresche di giornata</em>."),
 ("Il ragu alla bolognese autentico", "The one true ragu, taught with the official recipe deposited at the Bologna Chamber of Commerce. <em>Soffritto di sedano, carota e cipolla, macinato misto di manzo e maiale, pancetta, vino bianco secco, latte, tre ore di cottura a fuoco lento</em>."),
 ("Il pane e i lievitati italiani", "Italian bread and leavened bakes across the peninsula. <em>La pagnotta pugliese, la ciabatta veneta, il pane di Altamura DOP, la focaccia genovese, il panettone milanese, la biga e il lievito madre</em>."),
 ("I dolci italiani per stagione", "The Italian dessert calendar. <em>Il tiramisu, la panna cotta, la crostata di ricotta, il torrone natalizio, la colomba pasquale, i cannoli siciliani, la sfogliatella napoletana</em>. Each with a live demonstration."),
 ("Il menu di stagione: comporre una cena italiana completa", "Build a full seasonal Italian menu from antipasto to digestivo. <em>Antipasto della casa, primo di stagione, secondo con contorno, formaggi e miele, dolce, caffe, ammazzacaffe. La regola dei tempi, dei sapori, dei vini in abbinamento.</em>"),
]

# ---- CAP 02 L'Arte (6 lessons) ----
CAP2_UNITS = [
 ("Il vocabolario del Rinascimento", "The essential lexicon of Renaissance art in Italian. <em>La bottega, l'apprendista, la commissione, il mecenate, il fondo oro, la tempera, l'affresco, la prospettiva, il chiaroscuro, il disegno preparatorio</em>."),
 ("Michelangelo e Vasari raccontati in italiano", "Read Vasari's Vite in Italian, with Chiara guiding you through the story of Michelangelo. <em>Il divino Michelangelo, la Cappella Sistina, il David di Firenze, la Pieta vaticana, il non finito, il rapporto con Giulio II</em>."),
 ("La prospettiva: da Brunelleschi a Piero della Francesca", "The invention that changed Western art, explained in Italian. <em>Il punto di fuga, la linea d'orizzonte, la costruzione geometrica, la tavoletta di Brunelleschi, la Flagellazione di Urbino, la profondita illusoria</em>."),
 ("Affresco vs olio su tela: le tecniche", "The two great techniques of Italian painting. <em>L'affresco, l'intonaco fresco, la giornata di lavoro, la pittura a buon fresco. L'olio su tela, la preparazione, gli strati, le velature, i tempi di essiccazione</em>."),
 ("Firenze e i Medici: il potere e l'arte", "The Medici and the making of Florence, in Italian. <em>Cosimo il Vecchio, Lorenzo il Magnifico, il mecenatismo, la corte medicea, gli Uffizi, la cacciata dei Medici, il ritorno, il Granducato di Toscana</em>."),
 ("L'arte italiana contemporanea", "From Futurismo to today's biennale, in Italian. <em>Il Futurismo di Marinetti, la Metafisica di De Chirico, la Transavanguardia di Achille Bonito Oliva, l'Arte Povera, la Biennale di Venezia, i grandi collezionisti italiani</em>."),
]

# ---- CAP 03 L'Opera (6 lessons) ----
CAP3_UNITS = [
 ("Il libretto: leggere l'opera in italiano", "Read an opera libretto in real Italian. Understand recitative and aria markings, stage directions, and the poetic Italian of Da Ponte, Boito and Piave. <em>Andante, largo, aria, cavatina, cabaletta, duetto, coro, finale</em>."),
 ("Verdi: La Traviata al Teatro alla Scala", "Enter Verdi's most performed opera in Italian. <em>Libiamo ne' lieti calici, Sempre libera, Amami Alfredo, il finale d'atto secondo, il dramma di Violetta, la Milano borghese dell'Ottocento</em>."),
 ("Puccini: La Boheme, l'amore e Parigi", "Puccini's poetic realism in Italian. <em>Che gelida manina, Mi chiamano Mimi, Quando m'en vo', il quadro terzo alla Barriera d'Enfer, il finale straziante, il verismo pucciniano</em>."),
 ("Rossini: Il Barbiere di Siviglia", "Rossini's comic genius, sung in Italian. <em>Largo al factotum della citta, Una voce poco fa, il crescendo rossiniano, il patter, l'aria del sorbetto, il buffo napoletano, la brillantezza del canto</em>."),
 ("L'italiano operistico vs l'italiano moderno", "The linguistic bridge between operatic and modern Italian. <em>Le forme arcaiche (ei, ella, avvi), le inversioni, le desinenze, il perche di certe scelte poetiche, come Verdi e Puccini hanno modernizzato la lingua del melodramma</em>."),
 ("Andare a un concerto in italiano: alla Scala di Milano", "Attend a concert or opera at La Scala, entirely in Italian. <em>Il palchetto, la platea, il loggione, il programma di sala, l'intervallo, il fuoriprogramma, i bravo e i bis, gli applausi finali, l'atmosfera del gran teatro milanese</em>."),
]

# ---- teacher data ----
TEACHERS = {
 "marco": {"name":"Marco Rinaldi","city":"Roma","photo":"teacher-marco.jpg","role":"Native teacher · applied linguistics","bio":"A Roman with a passion for the vowels of his city, Marco specialises in absolute beginners. His classes are patient, precise and full of the daily culture of Rome, from Piazza Navona to the Testaccio market.","quote_it":"Il primo giorno un mio studente ordina un caffe in italiano al bar sotto casa mia · quel giorno l'italiano diventa suo.","quote_en":"The first day one of my students orders a coffee in Italian at the bar downstairs · that is the day Italian becomes theirs."},
 "chiara": {"name":"Chiara Ferretti","city":"Firenze","photo":"teacher-chiara.jpg","role":"Native teacher · art history","bio":"A Florentine with a doctorate in Italian art history, Chiara brings the Uffizi and the Duomo into every lesson. She makes grammar sing, and she teaches the leap from survival Italian to real conversation.","quote_it":"Quando uno studente mi descrive un quadro di Botticelli in italiano, senza tradurlo dall'inglese, l'italiano ha vinto.","quote_en":"When a student can describe a Botticelli painting in Italian, without translating from English, Italian has won."},
 "giulia": {"name":"Giulia Ricci","city":"Bologna","photo":"teacher-giulia.jpg","role":"Native teacher · gastronomy & B1 grammar","bio":"A Bolognese trained at the University of Bologna and at the ALMA culinary school of Colorno, Giulia teaches Italian through the daily grammar of the kitchen and the market. Her live classes always end with a real recipe.","quote_it":"Un ragu alla bolognese non si spiega in inglese. Bisogna imparare le parole, il ritmo, la pazienza · e allora si impara anche l'italiano.","quote_en":"A ragu alla bolognese cannot be explained in English. You have to learn the words, the rhythm, the patience · and then you learn Italian too."},
 "luca": {"name":"Luca De Luca","city":"Napoli","photo":"teacher-luca.jpg","role":"Native teacher · advanced grammar & argumentation","bio":"A Neapolitan with a linguistics degree from L'Orientale and years of teaching Italian at the highest level, Luca specialises in the leap from A2 to B1. His live classes are rigorous, warm and full of the passion of the South.","quote_it":"Quando uno studente comincia a discutere in italiano, e non solo a parlare, allora l'italiano e diventato pensiero.","quote_en":"When a student starts arguing in Italian, and not just speaking it, then Italian has become thought."},
 "francesca": {"name":"Francesca Marino","city":"Venezia","photo":"teacher-francesca.jpg","role":"Native teacher · travel Italian","bio":"A Venetian with a specialty in spoken Italian for travellers, Francesca teaches you to move through Italy with confidence. Her lessons are pure conversation, from the vaporetto to the pizzeria.","quote_it":"L'italiano vero si impara chiedendo la strada a una signora veneziana · non su un libro.","quote_en":"Real Italian is learned by asking directions from a Venetian lady · not from a book."},
 "alessandro": {"name":"Alessandro Ferri","city":"Milano","photo":"teacher-alessandro.jpg","role":"Native teacher · advanced conversation","bio":"A Milanese with a background in advanced Italian for professionals, Alessandro teaches confident conversation, business Italian and the leap to B1. His live classes cover politics, culture, work and Milan aperitivo talk.","quote_it":"Chiacchierare in italiano non e tradurre l'inglese piu velocemente. E cambiare mente.","quote_en":"Small talk in Italian is not translating English faster. It is changing your mind."},
}

# ---- course meta ----
COURSES = [
 # id, folder, dir, cefr, name_it, name_en_short, teacher_key, video, journey, subhead, hero_h1_first, hero_h1_accent, hero_h1_tail, hero_sub_1, hero_sub_2, learn_bullets, region_eyebrow, region_h2, region_p, siblings (prev, next as (href,title,cefr)), units, unit_count
 {
  "id":"ci1","folder":"courses","dir":"pages/courses","cid":"CI-01","cefr":"A0 → A1.1",
  "title":"CI Principiante · A0 → A1.1 · Roma · Club Italia",
  "desc":"CI Principiante: 20 live units (A0 → A1.1, CEFR) from Piazza Navona in Rome to the neighbourhood market. Build your first real Italian with Marco, a native teacher in Rome.",
  "teacher":"marco","video":"ag-rome-basilica",
  "h1_first":"From ", "h1_accent":"Piazza Navona", "h1_tail":" to the neighbourhood market",
  "sub_1":"You know how to say ciao · now learn to hold your first real Italian conversation.",
  "sub_2":"Twenty live lessons take you from ordering an espresso at the counter to describing your day in Rome for two full minutes, entirely in Italian.",
  "journey":"Rome to the market",
  "learn":[
    "Introduce yourself in Italian: name, age, origin, work, family",
    "Conjugate essere, avere and every regular -are, -ere and -ire verb in the present",
    "Master the six definite articles and the three indefinite articles by ear",
    "Order coffee, food and directions the way a Roman would",
    "Tell the time, the day, the month and describe your home and family",
    "Speak for two continuous minutes about a day in Rome",
  ],
  "region_eyebrow":"Filmed in Roma", "region_h2":"From the domes of Rome to the local bar",
  "region_p":"Principiante is a journey through Rome. From your first buongiorno in Piazza Navona to the coffee ritual at the corner bar, every unit is filmed live from Marco's Roman apartment.",
  "units":CI1_UNITS,
  "prev":None,
  "next":("ci2.html","CI Elementare","A1.1 → A1.2 · Firenze"),
 },
 {
  "id":"ci2","folder":"courses","dir":"pages/courses","cid":"CI-02","cefr":"A1.1 → A1.2",
  "title":"CI Elementare · A1.1 → A1.2 · Firenze · Club Italia",
  "desc":"CI Elementare: 20 live units (A1.1 → A1.2, CEFR) from the Ponte Vecchio to the Uffizi. Speak the Italian past tense and describe a Botticelli, with Chiara in Florence.",
  "teacher":"chiara","video":"ag-tuscany-drone",
  "h1_first":"From the ", "h1_accent":"Ponte Vecchio", "h1_tail":" to the Uffizi",
  "sub_1":"You can already introduce yourself in Italian · now learn to tell your story.",
  "sub_2":"Twenty live lessons take you from ordering a proper Tuscan meal to describing a Renaissance painting entirely in Italian, in the past, present and future tense.",
  "journey":"Ponte Vecchio to the Uffizi",
  "learn":[
    "Conjugate -ere and -ire verbs and master the modal verbs potere, volere, dovere",
    "Speak in the past with the passato prossimo, using both avere and essere",
    "Handle the Italian preposition system with articles: al, dal, nel, sul, dei",
    "Use piacere in every person and tense to talk about likes and dislikes",
    "Order a full meal, shop for clothes, take public transport in real Italian",
    "Describe a Renaissance painting for three minutes with Chiara",
  ],
  "region_eyebrow":"Filmed in Firenze & Toscana", "region_h2":"From the terracotta rooftops of Florence to the hills of Chianti",
  "region_p":"Elementare is a Tuscan journey. From the Ponte Vecchio at sunrise to the vineyards of Chianti, every unit is filmed live from Chiara's Florentine studio near Santa Croce.",
  "units":CI2_UNITS,
  "prev":("ci1.html","CI Principiante","A0 → A1.1 · Roma"),
  "next":("ci3.html","CI Intermedio","A1.2 → A2.1 · Bologna"),
 },
 {
  "id":"ci3","folder":"courses","dir":"pages/courses","cid":"CI-03","cefr":"A1.2 → A2.1",
  "title":"CI Intermedio · A1.2 → A2.1 · Bologna · Club Italia",
  "desc":"CI Intermedio: 20 live units (A1.2 → A2.1, CEFR) from the food markets of Bologna to a home dinner. Master the imperfetto and the pronomi with Giulia, a Bolognese chef-teacher.",
  "teacher":"giulia","video":"ag-market-produce",
  "h1_first":"From the food markets of ", "h1_accent":"Bologna", "h1_tail":" to a home dinner",
  "sub_1":"You can already speak in the past · now learn to weave the imperfetto and the pronouns of real Italian.",
  "sub_2":"Twenty live lessons take you from shopping at the Mercato delle Erbe to holding a full Bolognese dinner conversation, weaving imperfetto and passato prossimo with pronoun elegance.",
  "journey":"Bologna market to home dinner",
  "learn":[
    "Master the imperfetto and the passato prossimo, and the choice between them",
    "Use direct, indirect and combined pronouns (lo, le, glielo, ne) fluently",
    "Handle reflexive verbs in every tense, including the past",
    "Compare and superlativise: piu, meno, il piu bello, buonissimo, ottimo",
    "Speak in the present continuous with stare + gerundio",
    "Hold a full Italian dinner conversation for four minutes",
  ],
  "region_eyebrow":"Filmed in Bologna & Emilia", "region_h2":"From the porticoes of via dell'Indipendenza to a Bolognese kitchen",
  "region_p":"Intermedio is a Bolognese journey. From the two towers and the ancient portici to Giulia's family kitchen, every unit is filmed live from Emilia · the region where Italian food and Italian grammar both live at their most refined.",
  "units":CI3_UNITS,
  "prev":("ci2.html","CI Elementare","A1.1 → A1.2 · Firenze"),
  "next":("ci4.html","CI Avanzato","A2.1 → A2.2 · Napoli"),
 },
 {
  "id":"ci4","folder":"courses","dir":"pages/courses","cid":"CI-04","cefr":"A2.1 → A2.2",
  "title":"CI Avanzato · A2.1 → A2.2 · Napoli · Club Italia",
  "desc":"CI Avanzato: 20 live units (A2.1 → A2.2, CEFR) from the port of Naples to the Amalfi coast. Enter the futuro, the condizionale and the congiuntivo with Luca in Naples.",
  "teacher":"luca","video":"ag-camogli-coast",
  "h1_first":"From the port of ", "h1_accent":"Napoli", "h1_tail":" to the Amalfi coast",
  "sub_1":"You can already tell a story · now learn to argue, hypothesise and imagine in real Italian.",
  "sub_2":"Twenty live lessons take you from the futuro semplice to the introduction of the congiuntivo, closing with a full five-minute prepared speech, all under the Neapolitan sun.",
  "journey":"Napoli to the Amalfi coast",
  "learn":[
    "Speak in the futuro semplice and the futuro anteriore",
    "Use the condizionale semplice and composto for hypothesis and regret",
    "Introduce the congiuntivo presente after opinion and impersonal expressions",
    "Handle the si impersonale, the passive voice and relative pronouns che, cui, il quale",
    "Combine direct and indirect pronouns fluidly (me lo, glielo, ce li)",
    "Give a five-minute prepared speech in Italian with live class Q&A",
  ],
  "region_eyebrow":"Filmed in Napoli & Costiera Amalfitana", "region_h2":"From the shadow of Vesuvius to the terraces of Positano",
  "region_p":"Avanzato is a southern journey. From Luca's Neapolitan library to the ferry along the Amalfi coast, every unit is filmed live from the South · where Italian is at its most passionate and its most complex.",
  "units":CI4_UNITS,
  "prev":("ci3.html","CI Intermedio","A1.2 → A2.1 · Bologna"),
  "next":None,
 },
 # spoken
 {
  "id":"ps1","folder":"spoken","dir":"pages/spoken","cid":"PS-01","cefr":"Spoken · A0 → A1",
  "title":"Parliamo · Al Caffe · Roma · Club Italia",
  "desc":"Parliamo Al Caffe: 20 real spoken scenarios in Rome at the bar, at the tabaccaio, on the street. Live conversation practice with Marco in Rome, no grammar drills.",
  "teacher":"marco","video":"ag-roma-statue",
  "h1_first":"At the ", "h1_accent":"caffe", "h1_tail":" in Rome",
  "sub_1":"Twenty spoken scenarios, zero grammar drills · real Italian, in real Roman places.",
  "sub_2":"From ordering your first espresso to bargaining at a market, every unit is a live dialogue you rehearse until it becomes yours.",
  "journey":"20 real Roman scenarios",
  "learn":[
    "Order and pay at any Italian bar without hesitation",
    "Handle the daily rituals: greetings, small talk, thanks, apologies",
    "Ask for directions and understand fast Roman answers",
    "Book a restaurant, call a taxi, ask the time on the street",
    "Complain politely, ask a favour, react like an Italian",
    "Survive a full Roman morning entirely in Italian",
  ],
  "region_eyebrow":"Filmed in Roma", "region_h2":"Live from the bars, tobacconists and piazzas of Rome",
  "region_p":"Al Caffe is spoken Italian in the real places. Every unit is filmed live from Marco's Roman neighbourhood · the bar downstairs, the tabaccaio, the newsstand, the market.",
  "units":PS1_UNITS,
  "prev":None,
  "next":("ps2.html","Parliamo · A Tavola","Spoken · A1 → A2 · Firenze"),
 },
 {
  "id":"ps2","folder":"spoken","dir":"pages/spoken","cid":"PS-02","cefr":"Spoken · A1 → A2",
  "title":"Parliamo · A Tavola · Firenze · Club Italia",
  "desc":"Parliamo A Tavola: 20 real spoken scenarios at the Italian table. Book, order, toast and pay in real Italian with Chiara, live from Florence.",
  "teacher":"chiara","video":"ag-chefs-street",
  "h1_first":"At the Italian ", "h1_accent":"tavola", "h1_tail":" in Florence",
  "sub_1":"Twenty spoken scenarios at the heart of Italian life: the table.",
  "sub_2":"From booking a Florentine trattoria to giving compliments to the chef, every unit is a full live dialogue you rehearse with Chiara.",
  "journey":"20 spoken scenarios at the table",
  "learn":[
    "Book, arrive, be seated at any Italian restaurant",
    "Order antipasto, primo, secondo, contorno, dolce, caffe correctly",
    "Choose wine and match it with the dish in real Italian",
    "State dietary needs and allergies clearly and politely",
    "Handle the invitation to a friend's dinner, from arrival to farewell",
    "Give a proper Italian toast and pay the bill the Italian way",
  ],
  "region_eyebrow":"Filmed in Firenze", "region_h2":"Live from the trattorias, markets and kitchens of Florence",
  "region_p":"A Tavola is spoken Italian at the table. Every unit is filmed live from Florence · from the Mercato di San Lorenzo to a real Florentine trattoria near Santo Spirito.",
  "units":PS2_UNITS,
  "prev":("ps1.html","Parliamo · Al Caffe","Spoken · A0 → A1 · Roma"),
  "next":("ps3.html","Parliamo · In Viaggio","Spoken · A2 · Venezia"),
 },
 {
  "id":"ps3","folder":"spoken","dir":"pages/spoken","cid":"PS-03","cefr":"Spoken · A2",
  "title":"Parliamo · In Viaggio · Venezia · Club Italia",
  "desc":"Parliamo In Viaggio: 20 real travel scenarios across Italy. Hotel, vaporetto, train, museum, gondola · live spoken practice with Francesca in Venice.",
  "teacher":"francesca","video":"ag-venice-gondola",
  "h1_first":"On the road through ", "h1_accent":"Italia",
  "sub_1":"Twenty spoken scenarios for the Italy trip you actually want to take.",
  "sub_2":"From arriving at Santa Lucia to booking a gondola tour and calling a water taxi to the airport, every unit is a real Italian conversation Francesca guides you through.",
  "journey":"20 spoken travel scenarios",
  "learn":[
    "Check into any Italian hotel professionally",
    "Ask for tourist information and get real, useful answers",
    "Navigate Venice by vaporetto and any Italian city by public transport",
    "Buy museum tickets, book tours, ask for insider tips from locals",
    "Handle problems: bad weather, lost reservations, wrong tickets",
    "Book Italian train tickets and change trains without stress",
  ],
  "region_eyebrow":"Filmed in Venezia & Veneto", "region_h2":"Live from the calli, canals and ferries of Venice",
  "region_p":"In Viaggio is spoken Italian on the move. Every unit is filmed live from Venice · from the vaporetto stop at San Marco to the ferry to Murano and back, with Francesca.",
  "units":PS3_UNITS,
  "prev":("ps2.html","Parliamo · A Tavola","Spoken · A1 → A2 · Firenze"),
  "next":("ps4.html","Parliamo · Chiacchierando","Spoken · A2 → B1 · Milano"),
 },
 {
  "id":"ps4","folder":"spoken","dir":"pages/spoken","cid":"PS-04","cefr":"Spoken · A2 → B1",
  "title":"Parliamo · Chiacchierando · Milano · Club Italia",
  "desc":"Parliamo Chiacchierando: 20 confident spoken scenarios in Milan · aperitivo, work, politics, football, fashion. Live with Alessandro in Milan.",
  "teacher":"alessandro","video":"ag-wine-bottles",
  "h1_first":"Chiacchierando in ", "h1_accent":"Milano",
  "sub_1":"Twenty confident conversation scenarios, from a Milanese aperitivo to a real Italian debate.",
  "sub_2":"From talking work at a Navigli spritz to giving an Italian toast at a friend's birthday dinner, every unit closes the gap between speaking Italian and living in it.",
  "journey":"20 confident conversation scenarios",
  "learn":[
    "Handle the full Milan aperitivo, drink to work talk",
    "Talk about your job, your neighbourhood, your daily life in fluid Italian",
    "Give a proper toast, tell an anecdote, offer condolences and congratulations",
    "Discuss politics, football, art, fashion with tact",
    "Recommend restaurants, films and TV series convincingly",
    "Give a business self-introduction and a short prepared speech",
  ],
  "region_eyebrow":"Filmed in Milano", "region_h2":"Live from the Navigli, the aperitivo bars and the offices of Milan",
  "region_p":"Chiacchierando is spoken Italian at its most confident. Every unit is filmed live from Milan · the aperitivo bars of the Navigli, the fashion district, Alessandro's studio near Porta Nuova.",
  "units":PS4_UNITS,
  "prev":("ps3.html","Parliamo · In Viaggio","Spoken · A2 · Venezia"),
  "next":None,
 },
 # capsules
 {
  "id":"cap-food","folder":"culture","dir":"pages/culture","cid":"CAP-01","cefr":"Cultural · 6 lessons",
  "title":"Capsule · La Cucina · Bologna · Club Italia",
  "desc":"Culture Capsule La Cucina: 6 lessons in Italian at the Bologna markets and kitchen with Giulia. Fresh pasta, ragu alla bolognese, seasonal Italian menus.",
  "teacher":"giulia","video":"ag-pizza-oven",
  "h1_first":"La ", "h1_accent":"Cucina", "h1_tail":" italiana",
  "sub_1":"Six live capsule lessons in Italian, cooking with Giulia in Bologna.",
  "sub_2":"From the Mercato delle Erbe to the fresh pasta board to the official Bolognese ragu, every lesson is a live cooking class in Italian with a written recipe you keep for life.",
  "journey":"6 cooking-in-Italian lessons",
  "learn":[
    "Shop an Italian market with the right vocabulary and quantities",
    "Roll fresh Italian pasta by hand, in Italian",
    "Cook the official Bolognese ragu, deposited at the Chamber of Commerce",
    "Understand Italian bread, focaccia, panettone and the biga starter",
    "Build the Italian dessert calendar from tiramisu to panettone",
    "Compose a full seasonal Italian menu from antipasto to digestivo",
  ],
  "region_eyebrow":"Filmed in Bologna", "region_h2":"Live from a Bolognese kitchen and the Mercato delle Erbe",
  "region_p":"La Cucina is Italian food taught in Italian. Every capsule is filmed live from Giulia's home kitchen in Bologna and from the Mercato delle Erbe across the street.",
  "units":CAP1_UNITS,
  "prev":None,
  "next":("cap-art.html","Capsule · L'Arte","Cultural · Firenze"),
 },
 {
  "id":"cap-art","folder":"culture","dir":"pages/culture","cid":"CAP-02","cefr":"Cultural · 6 lessons",
  "title":"Capsule · L'Arte · Firenze · Club Italia",
  "desc":"Culture Capsule L'Arte: 6 lessons in Italian on Renaissance and modern Italian art with Chiara in Florence. Vasari, Michelangelo, the Medici and the Biennale.",
  "teacher":"chiara","video":"ag-catania-statues",
  "h1_first":"L' ", "h1_accent":"Arte", "h1_tail":" italiana",
  "sub_1":"Six live capsule lessons in Italian, in front of the greatest paintings ever made.",
  "sub_2":"From Brunelleschi's perspective to Achille Bonito Oliva's Transavanguardia, every capsule is a live art history lesson taught in Italian by Chiara in Florence.",
  "journey":"6 art-in-Italian lessons",
  "learn":[
    "Read and speak the Italian vocabulary of the Renaissance",
    "Follow Vasari's Vite in Italian, with Michelangelo as your guide",
    "Understand perspective from Brunelleschi to Piero della Francesca",
    "Know when to say affresco and when to say olio su tela",
    "Understand the Medici and the making of Florence",
    "Move through Italian modern and contemporary art from Futurismo to the Biennale",
  ],
  "region_eyebrow":"Filmed in Firenze", "region_h2":"Live from the Uffizi, the Accademia and Chiara's Florentine studio",
  "region_p":"L'Arte is Italian art history taught in Italian. Every capsule is filmed live from Florence · inside the Uffizi and the Accademia when possible, from Chiara's studio near Santa Croce when not.",
  "units":CAP2_UNITS,
  "prev":("cap-food.html","Capsule · La Cucina","Cultural · Bologna"),
  "next":("cap-opera.html","Capsule · L'Opera","Cultural · Milano"),
 },
 {
  "id":"cap-opera","folder":"culture","dir":"pages/culture","cid":"CAP-03","cefr":"Cultural · 6 lessons",
  "title":"Capsule · L'Opera · Milano · Club Italia",
  "desc":"Culture Capsule L'Opera: 6 lessons in Italian on Verdi, Puccini, Rossini and the opera language, with Alessandro at La Scala in Milan.",
  "teacher":"alessandro","video":"ag-medieval-aerial",
  "h1_first":"L' ", "h1_accent":"Opera", "h1_tail":" italiana",
  "sub_1":"Six live capsule lessons in Italian, from the Teatro alla Scala.",
  "sub_2":"From reading a libretto to attending a real opera in Italian, every capsule opens the door of Italy's greatest cultural export: the melodramma, sung and taught in its own language.",
  "journey":"6 opera-in-Italian lessons",
  "learn":[
    "Read an Italian opera libretto with confidence",
    "Follow Verdi's La Traviata scene by scene, in Italian",
    "Understand Puccini's La Boheme, aria by aria",
    "Enter Rossini's comic Italian with Il Barbiere di Siviglia",
    "Bridge operatic Italian and modern Italian, and hear both",
    "Attend a full concert or opera at La Scala, entirely in Italian",
  ],
  "region_eyebrow":"Filmed in Milano", "region_h2":"Live from La Scala and Alessandro's Milanese studio",
  "region_p":"L'Opera is Italian opera taught in Italian. Every capsule is filmed live from Milan · from the Teatro alla Scala when possible, from Alessandro's studio near Porta Nuova otherwise, with a live piano and singer for each aria.",
  "units":CAP3_UNITS,
  "prev":("cap-art.html","Capsule · L'Arte","Cultural · Firenze"),
  "next":None,
 },
]

# ---- template ----
TICK_SVG = '<span class="tick"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>'

def render_page(c):
    t = TEACHERS[c["teacher"]]
    accent_tail = c.get("h1_tail","")
    h1_html = f'{c["h1_first"]}<span class="gold-ital">{c["h1_accent"]}</span>{accent_tail}'
    # learn list
    learn_html = ""
    for b in c["learn"]:
        learn_html += f'<li>{TICK_SVG}<span>{b}</span></li>'
    # unit cards
    units_html = ""
    for i, (it_h4, en_p) in enumerate(c["units"], 1):
        n = f"{i:02d}"
        units_html += f'<div class="unit-card"><div class="u-no">{n}</div><div class="u-body"><h4>{it_h4}</h4><p>{en_p}</p></div></div>'
    # sibling nav
    sibs = []
    if c["prev"]:
        href, title, cefr = c["prev"]
        sibs.append(f'<a class="sib-card" href="{href}"><span class="sib-dir">← Previous level</span><span class="sib-title">{title}</span><span class="sib-cefr">{cefr}</span></a>')
    if c["next"]:
        href, title, cefr = c["next"]
        sibs.append(f'<a class="sib-card" href="{href}"><span class="sib-dir">Next level →</span><span class="sib-title">{title}</span><span class="sib-cefr">{cefr}</span></a>')
    sibs_html = "".join(sibs) if sibs else ""

    # FAQs (6 per page)
    unit_count = len(c["units"])
    faqs = [
      ("Is this really live?",
       "Every session is a live class taught by a native teacher in Italy, at the scheduled hour, in a group of ten to twelve. If you cannot attend live, the class is recorded for you to review the same evening."),
      (f"How many units in the course?",
       f"{unit_count} live units, {'90' if unit_count == 20 else '85'} minutes each. Every unit is filmed live from Italy and is broadcast on the same day, at the same time each week."),
      ("What if I have never learned Italian before?",
       "If our advisor places you in this course, it is the right starting point for your level. If you are not sure, book a free placement call and we will listen to your Italian for ten minutes and give you an honest answer."),
      ("Who is the teacher?",
       f"{t['name']}, native Italian teacher from {t['city']}. Every unit of this course is taught by {t['name'].split()[0]} personally, from the same city, broadcasting live to your small group of ten to twelve."),
      ("Will I get a certificate?",
       "Yes. On completion you receive a CEFR-aligned certificate issued by eTeacher confirming the target level, plus lifetime access to every recording and one hundred dollars in learning credits."),
      ("What comes next after this course?",
       "Your teacher will personally recommend your next step. Most learners continue into the next CEFR level in our ladder; some pause and take a Culture Capsule to consolidate. Nothing is automatic."),
    ]
    faq_html = "".join(
      f'<details class="faq-item"><summary><span class="faq-q">{q}</span><span class="faq-toggle">＋</span></summary><div class="faq-a">{a}</div></details>'
      for q, a in faqs
    )

    # meta strip values
    lesson_min = "90 min" if unit_count == 20 else "60 min"
    format_v = f"{unit_count} units · {lesson_min}"

    # video src
    v = c["video"]
    video_src = f"../../assets/video/{v}.mp4"
    poster_src = f"../../assets/img/{v}-poster.jpg"

    out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{c["title"]}</title>
<meta name="description" content="{c["desc"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Inter:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="../../css/ci.css">
</head>
<body class="ci-body" id="ci" data-course="{c["id"]}">
{NAV_PP}
<section class="course-hero">
  <div class="hero-media">
    <video autoplay muted loop playsinline poster="{poster_src}">
      <source src="{video_src}" type="video/mp4">
    </video>
  </div>
  <div class="hero-scrim"></div>
  <div class="cw">
    <div class="hero-badges">
      <span class="h-badge lvl">CEFR {c["cefr"]}</span>
      <span class="h-badge"><span class="live-dot"></span>Live from Italy</span>
      <span class="h-badge">Accredited by eTeacher</span>
      <span class="h-badge">Biagio · 24/7 AI tutor</span>
    </div>
    <h1>{h1_html}</h1>
    <p class="hero-sub">{c["sub_1"]} {c["sub_2"]}</p>
    <div class="hero-ctas">
      <a class="btn btn-gold btn-lg" href="../../pricing.html">Enrol Now</a>
      <a class="btn btn-outline btn-lg" href="#syllabus">Explore the {unit_count} units</a>
    </div>
    <div class="hero-meta-strip">
      <div class="hm"><div class="hm-k">Format</div><div class="hm-v">{format_v}</div></div>
      <div class="hm"><div class="hm-k">Live groups</div><div class="hm-v">10 to 12 students</div></div>
      <div class="hm"><div class="hm-k">Journey</div><div class="hm-v">{c["journey"]}</div></div>
      <div class="hm"><div class="hm-k">Certificate</div><div class="hm-v">CEFR by eTeacher</div></div>
    </div>
  </div>
</section>

<section class="section section-travertine">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow eyebrow-line">What you'll learn</span><h2 class="h2-editorial">By unit {unit_count}, you will…</h2><p class="section-lede">Every learning outcome below is measured in a live oral check with {t['name'].split()[0]} at the end of your term.</p></div>
    <ul class="learn-list">{learn_html}</ul>
  </div>
</section>

<section class="region-band">
  <video autoplay muted loop playsinline poster="{poster_src}">
    <source src="{video_src}" type="video/mp4">
  </video>
  <div class="rb-scrim"></div>
  <div class="cw">
    <span class="eyebrow" style="color:var(--sistine-gold-soft)">{c["region_eyebrow"]}</span>
    <h2>{c["region_h2"]}</h2>
    <p>{c["region_p"]}</p>
  </div>
</section>

<section class="section section-cream" id="syllabus">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow eyebrow-line">The full curriculum</span><h2 class="h2-editorial">{'Twenty' if unit_count == 20 else 'Six'} live units. One journey.</h2><p class="section-lede">A structured {c["cefr"]} curriculum. Every h4 in Italian is the real Italian topic of the unit, taught live by {t['name'].split()[0]} from {t['city']}.</p></div>
    <div class="unit-grid">{units_html}</div>
  </div>
</section>

<section class="section section-ink">
  <div class="wrap">
    <div class="teacher-block">
      <div class="teacher-photo">
        <img src="../../assets/img/{t['photo']}" alt="{t['name']}, native Italian teacher" loading="lazy">
        <span class="tp-badge">{t['city']} · Italia</span>
      </div>
      <div class="teacher-info">
        <span class="eyebrow">Your teacher</span>
        <h3>{t['name']}</h3>
        <div class="ti-role">{t['role']}</div>
        <p>{t['bio']}</p>
        <blockquote class="teacher-quote"><em>"{t['quote_it']}"</em><br><span class="tq-en">"{t['quote_en']}"</span></blockquote>
      </div>
    </div>
  </div>
</section>

<section class="section section-travertine">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow eyebrow-line">Tuition</span><h2 class="h2-editorial">Choose a plan. Reserve your seat.</h2><p class="section-lede">One live curriculum. Three ways to pay. Every plan is fully refundable for seven days after your first live class.</p></div>
    <div class="pricing-grid">
      <article class="price-card"><span class="pc-name">Monthly</span><span class="pc-price"><em>$84</em> <span class="pc-unit">/ week</span></span><p class="pc-note">Pay month to month. Cancel anytime.</p><ul class="pc-list"><li>All live lessons on your track</li><li>Full access to Biagio, the AI coach</li><li>Culture library and cinema club</li><li>Advisor support</li></ul><a class="btn btn-ghost btn-gold" href="../../pricing.html">Start Monthly</a></article>
      <article class="price-card price-card-featured"><span class="pc-chip">Best value · Save $440</span><span class="pc-name">Annual</span><span class="pc-price"><em>$62</em> <span class="pc-unit">/ week</span></span><p class="pc-note">Billed once for the year. Save twenty six percent.</p><ul class="pc-list"><li>Everything in monthly</li><li>Two free capsule sessions of your choice</li><li>Priority placement with a preferred teacher</li><li>Free CEFR certificate at year end</li></ul><a class="btn btn-primary" href="../../pricing.html">Enrol Annual</a></article>
      <article class="price-card"><span class="pc-name">Term</span><span class="pc-price"><em>$73</em> <span class="pc-unit">/ week</span></span><p class="pc-note">Twelve weeks. One CEFR stage. Try before the full year.</p><ul class="pc-list"><li>All live lessons of one term</li><li>Biagio access for the whole term</li><li>Placement interview included</li><li>End-of-stage certificate</li></ul><a class="btn btn-ghost btn-gold" href="../../pricing.html">Start a Term</a></article>
    </div>
    <p class="pc-refund">Seven day full refund on every plan.</p>
  </div>
</section>

<section class="section section-cream">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow eyebrow-line">Questions</span><h2 class="h2-editorial">Everything you might be wondering</h2></div>
    <div class="faq-list">{faq_html}</div>
  </div>
</section>

{'''<section class="section section-ink closing-nav">
  <div class="wrap">
    <div class="sibling-nav">''' + sibs_html + '''</div>
  </div>
</section>''' if sibs_html else ''}

<section class="section section-verona final-cta" id="reserve">
  <div class="wrap final-inner">
    <div class="fc-copy">
      <h2 class="h2-huge">Reserve your placement call.</h2>
      <p class="fc-lede">Thirty minutes with an academic advisor. Spoken in English, honest about your level, ending with a clear next step.</p>
    </div>
    <form class="fc-form paper-glass" novalidate>
      <div class="ff-row"><label>Your name<input type="text" name="name" required placeholder="Full name"></label></div>
      <div class="ff-row"><label>Email<input type="email" name="email" required placeholder="you@email.com"></label></div>
      <div class="ff-row"><label>Phone<input type="tel" name="phone" required placeholder="+1 555 000 0000"></label></div>
      <div class="ff-row"><label>Your Italian right now
        <select name="level" required><option value="">Choose your level</option><option>I have not started</option><option>A few words · A1</option><option>Some basics · A2</option><option>Conversational · B1 or higher</option></select></label></div>
      <button class="btn btn-primary btn-block" type="submit">Reserve My Placement Call</button>
      <p class="ff-note">We reply within one working day. No sales script, no pressure.</p>
    </form>
  </div>
</section>

{FOOT_PP}
<script src="../../js/ci.js" defer></script>
</body>
</html>
'''
    return out

for c in COURSES:
    out_dir = ROOT / c["dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{c['id']}.html"
    out_path.write_text(render_page(c))
    print(f"Wrote {out_path}  ({len(c['units'])} units, teacher={c['teacher']})")

print("Done.")
