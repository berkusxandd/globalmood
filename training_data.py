from sentiment_engine import analyze_sentiment
LABEL_INDEX = {"negative": 1, "neutral": 2, "positive": 3}
import pandas as pd
sentences = ["After a multi-year battle with my mental health, I'm finally in a position to get back to work. Had my first interview in years today, with three more this week.",
             "Good for you dude! Good luck with in interviews!",
             "Wife cheated but now I get to live on my own terms. Got an apartment, thrifted my living room for under $300. YouTube, Chicken tacos, and whiskey/coke zero. Life is good",
             "Over 90% of global renewable power projects are now cheaper than fossil fuels. Solar power costs 41% less than the cheapest fossil fuel option, and onshore wind is under half the price, per an International Renewable Energy Agency report.",
             "Give it up to her as she’s CANCER FREE",
             "This is true partnership ❣️",
             "2025 YKS sorularını çalanların konuşmaları ortaya çıktı",
             "Karaman'da sevgi evlerinde görevli bakıcı annelerin, devlet koruması altındaki annesiz, babasız çocuklarla ilgili; çocuklara verilen yemeklere taş atılması, yiyeceklerin kasıtlı olarak aşırı acılı yapılması, mide rahatsızlığına yol açabilecek maddeler katılması gibi yazışmaları ortaya çıktı",
             "If they want you to sign something, they probably don't have a valid reason to fire you and just try to pressure you into quitting voluntarily. Get a lawyer.",
             "Hello. My partner and I are thinking of moving to Germany from the US with our dog and cat. I am writing here to get a better understanding of what dog and cat culture is like over there. I read up on the banned dog breeds, strict dog training culture, housing shortages with pets, and required dog tax. But I really want to get to know the more nuanced parts of dog culture and especially how our dog with separation anxiety would factor into all of it.",
             "So i got a call about a contract in the farming field in germany and as he said its a modern farming So i have a diploma in industrial maintenance with 3 years of experience in my country And this is the only way i found to start a career in germany Will it be helpful for my career to start with a farming job in germany The good thing is he said that im gonna learn until b2 level of german there and then i can pass the test and start looking for a job in maintenance field So any ideas guys I really need help",
             "Is this alcoholic beverage available for purchase in Poland? If so, where can I buy it?",
             "The brand exists and its quite popular and available everywhere (as others said) but they definitely changed the recipe. You wont find the 40% version, nowadays its 24-26% maximum. It will also be probably much sweeter now. Generally, classic example of enshittification.",
             "Hey guys! Me and the family have a few free days and I always wanted to visit Gdansk. I wanted to ask some guidance from the locals whats worth seeing, places to stay, eat etc... travelling by car with kids, 8yo and 2yo.We're planing on leaving Kaunas either today or tomorrow morning. Back to Lithuania on thrusday/ friday. Maybe a with a stop at Mikolajki.Thanks! Best wishes ;)",
             "Tips for south of Wroclaw and towards Krakow",
             "also the most visited area in Stołowe Mountains is the Błędne Skały complex (a rock labyrtinth) and it's just a few hours hike I guess you have to pay for an entry) btw is the palace in Kamieniec Ząbkowicki worth a visit? what about the Kłodzko fortress complex?",
             "I am planning a bikepacking trip from Ostrava to Hel. Any recommendations?",
             "A Polish grocery shop opened in my town. Are these good picks? I know nothing of Polish snacks and drinks.",
             "Nigeria’s never-complete highway has barely begun",
             "was recently mugged around agege and it got me thinking,do white people get mugged at all on Lagos or even harassed by agberos. Ive seen some of them around that area.",
             "Waris Kareem, an 11 year-old ART PRODIGY from Nigeria showcasing his amazing talent.",
             "An 80 year-old woman being arrested on terrorism charges in London today",
             "Look who's making the arrests. You think they'd have anything to do with the phone thieves?",
             "the met are such a fucking joke",
             "Music bringing people together on the London Underground.",
             "We are now experiencing smog for the first time.",
             "2 years ago today, Google Photos reminded me. It was a very good time. Rovaniemi",
             "Need help/advice with package sent to Finland. Stuck in customs.",
             "There's been a recent change regarding some information needed for shipping packages from outside or the EU to the EU. This has led to a delay for packages coming in particular from the USA and China to Finland. I had the same situation recently with a package coming from my mother-in-law in the States. It sat at customs for some extra weeks awaiting processing, but then I finally got a message that it was ready to be declared and it arrived quite quickly after I completed the declaration.",
             "The town of Telč, Czechia",
             "Znojmo, CZECHIA - My hometown",
             "Work American hours, earn European wages: Why Canada has the worst of both worlds",
             "This man planted a 3.2 km linear park in the heart of São Paulo",
             "Meet the Austrian carpenter safeguarding precious flutes with his new 'smart case' invention - Professional flutists know that many cases don't hold the flutes in place, making them vulnerable to damage. But a carpenter from a small Austrian town may have changed that...",
             "LA Houselessness Drops for Second Year - Los Angeles County’s houseless population fell for a second straight year, suggesting recent state and local policies are beginning to show results in a region that has been beset by houselessness for decades.",
             "Esther Mahlangu, an 89 year old Ndebele woman celebrates her culture with traditional painting",
             "Rabbits in Colorado spotted with tentacle-like growths on their heads from rare virus",
             "That’s some nightmare/alien/zombie sort of thing",
             "En 1993, l'électricien français Émile Lerey s'est retrouvé coincé dans le désert africain alors qu'il conduisait une vieille Citroën 2CV depuis le Maroc.",
             "Direkt imha edilmesi yada toplumdan uzaklaştırılması lazım",
             "“Chat Control” ilitiga najgori zakon koji sam vidio u životu!",
             "O ovom treba pričati i treba slati mailove. Nek političari budu svjesni da na lak način mogu dobiti veliku podršku javnosti ako se bore protiv ovakvih gluposti. Ak iko misli odgovorit sa niš se neće postić i mi ćemo ionak glasat kak nam se kaže, poštedite me. Sve sam čuo, a pametovanjem u podkomentarima na redditu se tek ništa neće postić.",
             ]

labels = [
        2,
        2,
        2,
        2,
        2,
        2,
        0,
        0,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        0,
        0,
        2,
        0,
        0,
        0,
        2,
        2,
        2,
        0,
        1,
        2,
        2,
        2,
        2,
        0,
        2,
        2,
        2,
        2,
        0,
        0,
        1,
        0,
        0,
        0
        ]

data = []

def prep_data():
    rows = []
    label = 0
    for sentence in sentences:
        res = analyze_sentiment(sentence)
        neg = 0
        neu = 0
        pos = 0
        for r in res:
            if r["label"] == "negative":
                neg = r["score"]
            elif r["label"] == "positive":
                pos = r["score"]
            else:
                neu = r["score"]
        rows.append({"sentence": sentence, "neg": neg, "neu": neu, "pos": pos, "label": labels[label]})
        label += 1
    df = pd.DataFrame(rows)
    df.to_csv("training_data.csv",index=0)
    