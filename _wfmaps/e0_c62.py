import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_02191", ("The compact brought<FF03>us here", "La polvera nos<FF03>trajo aqui"))
repl("e0_02193",
    ("Where are we.?", "Donde estamos.?"),
    ("Looks like it worked", "Parece que funciono"),
)
repl("e0_02194", ("This looks like the forest where that<FF03>girl in white was", "Parece el bosque donde estaba<FF03>esa chica de blanco"))
repl("e0_02195",
    ("the child-Maki!", "la Maki nina!"),
    ("Bingo. This is child-Maki's forest.", "Bingo. Es el bosque de la Maki nina."),
    ("Hey, it worked. Isn't this the forest<FF03>where that little Maki was.?", "Oye, funciono. No es el bosque<FF03>de esa Maki nina.?"),
    ("Wow, talk about luck. Isn't this that<FF03>little Maki's forest.?", "Vaya suerte. No es el bosque<FF03>de esa Maki nina.?"),
    ("Why have you all come back.?<FF03>What about Kandori.?", "Por que volvieron.?<FF03>Y Kandori.?"),
    ("Same to you, lady. Why're YOU here?", "Igual usted, senora. Por que esta AQUI?"),
)
repl("e0_02196", ("don't really know", "no se bien"))
repl("e0_02197", ("After I transported you all, I thought<FF03>I heard Maki's voice again", "Tras transportarlos, crei<FF03>oir la voz de Maki otra vez"))
repl("e0_02198", ("And when I came to, I was here", "Y al despertar, estaba aqui"))
repl("e0_02199",
    ("But why have you all come back?", "Pero por que volvieron?"),
    ("Allow me to explain! You should know<FF03>the truth", "Dejame explicar! Debe saber<FF03>la verdad"),
)
repl("e0_02200", ("No", "No"))
repl("e0_02202",
    ("What about Maki.? What's going to<FF03>happen to her.?", "Y Maki.? Que le va<FF03>a pasar.?"),
    ("If we leave her be, she'll stay that way<FF03>for the rest of her life! Or worse", "Si la dejamos, quedara asi<FF03>el resto de su vida! O peor"),
)
repl("e0_02203", ("No", "No"))
repl("e0_02204", ("Can't you do something.?<FF03>My Maki", "No pueden hacer algo.?<FF03>Mi Maki"))
repl("e0_02205",
    ("Cool it, lady. That's why we came back!", "Calma, senora. Por eso volvimos!"),
    ("Don't worry", "Tranquila"),
)
repl("e0_02206",
    ("We won't let it end<FF03>like this!", "No dejaremos que acabe<FF03>asi!"),
    ("Don't worry! We definitely won't leave<FF03>Maki hanging.", "Tranquila! No abandonaremos<FF03>a Maki."),
    ("Relax. Just have fate in us--you can<FF03>forget all about it.", "Calma. Solo ten fete en nosotros--<FF03>olvidalo."),
    ("That's <0028>faith,<0028> you cretin.", "Es <0028>fe,<0028> cretino."),
    ("Yeah, faith, exactly. It'll be fine.<FF03>Hahahahaha.", "Si, fe, exacto. Estara bien.<FF03>Jajaja."),
    ("The dude shows his true colors! After<FF03>all that stuff about pretending", "Muestra su verdadera cara! Tras<FF03>todo eso de fingir"),
)
repl("e0_02207", ("Indeed! He's innately imbecilic", "En efecto! Imbecil nato"))
repl("e0_02208",
    ("not<FF03>a man to be ashamed of soiling himself!", "no<FF03>se avergonzaria de ensuciarse!"),
    ("Don't worry, Maki-Mom. I'm more<FF03>competent than I look, y'know.", "Tranquila, mama de Maki. Soy mas<FF03>capaz de lo que parezco."),
    ("Thank you, everyone", "Gracias a todos"),
)
repl("e0_02209",
    ("<FF1B>Mai's voice<FF03>", "<FF1B>Voz de Mai<FF03>"),
    ("Waaah", "Buaah"),
)
repl("e0_02210",
    ("Was that Maki's voice.? She must be<FF03>just past here.", "Esa era la voz de Maki.? Debe estar<FF03>justo mas alla."),
    ("Let's go. That li'l Maki might know<FF03>something.", "Vamos. Esa Maki nina quiza sepa<FF03>algo."),
    ("Wait. Please", "Espera. Por favor"),
)
repl("e0_02211",
    ("take me with you.", "llevenme con ustedes."),
    ("She's my daughter. I can't leave her<FF03>suffering like this.", "Es mi hija. No puedo dejarla<FF03>sufrir asi."),
)
repl("e0_02212",
    ("Very well!", "Muy bien!"),
    ("However, this forest is hazardous!<FF03>Your survival is far from assured!", "Pero este bosque es peligroso!<FF03>Su supervivencia no esta asegurada!"),
    ("I don't care about that.", "No me importa eso."),
    ("Then that settles that! Come on,<FF03><FF0F>!", "Entonces decidido! Vamos,<FF03><FF0F>!"),
    ("Let's reunite a mother with her child!", "Reunamos a una madre con su hija!"),
)
repl("e0_02213",
    ("She's one super mom!<FF03>Good looking, too.", "Es una super mama!<FF03>Y guapa."),
    ("My mom", "Mi mama"),
)
repl("e0_02214",
    ("she's just a loud nag!<FF03>But she better still be alive.", "es solo una reganona!<FF03>Pero mas le vale seguir viva."),
    ("I don't think she'd die that easy", "No creo que muera tan facil"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c62.json"))
