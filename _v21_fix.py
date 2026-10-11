# QA text fixes applied to visible text nodes only
from bs4 import BeautifulSoup, NavigableString, Comment
FIXT=[
("The sound system of Italian, open vowels and double consonants, from the first lesson.","Lesson one: the difference between «nono» and «nonno». You will hear it by the end of the hour."),
("Each unit is set in a real Roman place, from Fiumicino to a bar in Prati.","Unit 1 lands at Fiumicino. Unit 4 is a cappuccino at a bar in Prati, before 11am."),
("The course is a journey through Rome. Arrival, the bar, the market, the piazza, the trattoria: your Italian grows with every stop.","Arrivals hall, a standing bar, Campo de’ Fiori at nine, a trattoria in Testaccio. Twenty stops, one city."),

("Live Italian courses for adults, taught by DITALS certified teachers in seven Italian cities.","Live Italian for adults. Your teacher is in Rome, Florence, Bologna, Venice, Milan, Naples or Palermo, and holds the DITALS certificate."),
("Two collections of CEFR aligned courses, each taught live by one teacher from one Italian city.","Eight courses, A0 to B1. One teacher and one city per course."),
("One clear route, from your first lesson to a documented CEFR level.","Five steps, from a placement call to a certificate with your level on it."),
("Six pillars of Italian life run through every course, taught by people who live them.",""),
("Between live lessons, Biagio works inside the platform on exactly what your teacher covered that week.","At 11pm, when the class is asleep, Biagio replays this week’s lesson with you and listens to your «gl»."),
("Join a live class broadcasting from Italy and begin with your first lesson.","Your first lesson is an evening in Italy. Bring a coffee."),

("Club Italia by eTeacher. Live Italian courses for adults, taught by DITALS certified teachers from seven Italian cities.","Live Italian courses for adults, taught by DITALS certified teachers in seven Italian cities."),
("28 contact hours per level","28 h 20 min of live teaching"),
("Monthly and term plans are also available.","A monthly plan is also available."),
("Your first Italian, taught in Rome, the city where the language began.","Your first Italian, taught live from Rome."),
("Real Italian for real life, between the warmth of Naples and the sharpness of Milan.","Real Italian for real life, taught from Naples."),
("for people who actually travel Italy, trains, hotels, museums, mountain refuges, sailing the Amalfi coast.","for real journeys: trains, hotels, museums, mountain refuges and the Amalfi coast."),
("on the four things Italians actually do all day: opinion, humour, disagreement and storytelling.","on what Italians do all day: opinion, humour, disagreement and storytelling."),
("Twelve adults, eighty five minutes, and everyone speaks.","Ten to twelve adults, 85 minutes, and everyone speaks."),
("Eighty five minute live lessons","Live 85 minute lessons"),
("Everything worth asking before you enroll","Everything worth asking before you enrol"),
("to be contacted by our enrollment team.","to be contacted by our enrolment team."),
("Grazie. Your request has been received, we will reach out within one business day.","Grazie. Your request has been received. We will reply within one working day."),
("Upper-intermediate (B2)","Upper intermediate (B2)"),
("Native Italian teachers, live from Italy · Certified · CEFR-aligned","Native Italian teachers, live from Italy · DITALS certified · CEFR aligned"),
("Talk to an Advisor","Talk to an advisor"),("Request a Call","Request a call"),
("We’ll be in touch shortly to plan your Italian journey.","An advisor will reply within one working day."),
("from your first buongiorno to confident conversation.","from your first «buongiorno» to confident conversation."),
("says buongiorno back to me","says «buongiorno» back to me"),
("Italian begins in Roma.","Italian begins in Rome."),("Filmed in Roma","Filmed in Rome"),("Live from Roma","Live from Rome"),
("Every plan includes the live lessons from Roma,","Every plan includes the live lessons from Rome,"),
("Twenty live lessons in Roma, with Marco.","Twenty live lessons from Rome, with Marco."),
("CI Principiante takes a true beginner from A0 to A1.1. Understands and uses familiar everyday expressions and very basic phrases. Introduces themselves and interacts simply when the other person speaks slowly.","CI Principiante takes a true beginner from A0 to A1.1. At A1.1, the CEFR describes a learner who understands and uses familiar everyday expressions, introduces themselves, and interacts simply when the other person speaks slowly."),
("Review, mini test, oral presentation. Half-way milestone.","Review, progress check and a short oral presentation. The halfway milestone."),
("Weekend plans, imperfetto introduced, contrastive with passato.","Weekend plans. The imperfetto introduced and contrasted with the passato prossimo."),
("Full oral CEFR A1.1 assessment, farewell dialogue, next steps.","Final spoken and written A1.1 assessment, farewell dialogue, next steps."),
("Feedback in every lesson, a progress check at unit 10, and a final spoken and written task in unit 20.","Feedback in every lesson, a progress check in unit 15, and a final spoken and written assessment in unit 20."),
("A dialogue at a Roman café.","A dialogue at a Roman bar."),
]
def fix_html(out):
    S=BeautifulSoup(out,'html.parser')
    for t in S.find_all(string=True):
        if isinstance(t,Comment) or t.parent.name in ('script','style'): continue
        s=str(t);n=s
        for a,b in FIXT: n=n.replace(a,b)
        if n!=s: t.replace_with(NavigableString(n))
    return str(S)
