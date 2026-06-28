import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_01969", ("Meet your true self", "Conoce tu yo real"))
repl("e0_01970", ("She is here, in this castle", "Esta aqui, en este castillo"))
repl("e0_01971", ("But I'm me. This", "Soy yo. Esto"))
repl("e0_01972",
    ("this is too much.", "esto es demasiado."),
    ("<FF07>. We have to go after her.", "<FF07>. Hay que ir tras ella."),
    ("This is bad, <FF08>", "Esto esta mal, <FF08>"),
)
repl("e0_01973",
    ("We should go after her.", "Vamos tras ella."),
    ("Uh oh", "Oh oh"),
)
repl("e0_01974",
    ("Well, <FF07>.?<FF03>Aren't you gonna go after her?", "Y bien, <FF07>.?<FF03>No vas a ir tras ella?"),
    ("Aren't you going after her? You're the<FF03>only one who can save her, you know!", "No iras tras ella? Eres el<FF03>unico que puede salvarla!"),
)
repl("e0_01975",
    ("she needs to discover<FF03>her true self!", "ella debe descubrir<FF03>su verdadero yo!"),
    ("If she doesn't, she'll share my fate", "Si no, correra mi suerte"),
)
repl("e0_01976", ("Go to her", "Ve a ella"))
repl("e0_01977", ("Don't let her go down that<FF03>lonely path", "No la dejes por ese<FF03>camino solitario"))
repl("e0_01979", ("What a pitiful man", "Pobre hombre"))
repl("e0_01980",
    ("<FF07>. We gotta look for Maki.", "<FF07>. Hay que buscar a Maki."),
    ("It's gotta be a lie. It's too much<FF03>for Maki", "Debe ser mentira. Es demasiado<FF03>para Maki"),
)
repl("e0_01981", ("I've been thinking it over all this time,<FF03>and my conclusions still surprised me!", "Lo he pensado todo este tiempo,<FF03>y mis conclusiones me sorprenden!"))
repl("e0_01982", ("I finally killed the bastard", "Al fin mate al infeliz"))
repl("e0_01983", ("Then why this empty feeling", "Por que este vacio entonces"))
repl("e0_01984", ("Poor Maki", "Ay, Maki"))
repl("e0_01985",
    ("We need to help her!", "Hay que ayudarla!"),
    ("Is this for real? What's going to<FF03>happen to Maki?", "Es en serio? Que le<FF03>pasara a Maki?"),
    ("I can't believe this", "No puedo creerlo"),
)
repl("e0_01986",
    ("Hey. What's gonna<FF03>happen to Maki, huh.?", "Oye. Que le<FF03>pasara a Maki, eh.?"),
    ("Kandori looks peaceful in death", "Kandori luce en paz al morir"),
)
repl("e0_01987", ("There's an inscription on the wall", "Hay una inscripcion en el muro"))
repl("e0_01988", ("A man's life of fifty years is a<FF03>fleeting dream next to the age of the<FF03>universe! Does anything last forever?", "Cincuenta anos de vida humana son<FF03>sueno fugaz ante la edad del<FF03>universo! Algo dura para siempre?"))
repl("e0_01997",
    ("You idiot. Why did you kill Daddy.?", "Idiota. Por que mataste a Papa.?"),
    ("Don't you know what you did.?", "No sabes lo que hiciste.?"),
    ("Waaaaaaaaaaaah.", "Buaaaaaah."),
    ("This is me", "Esta soy yo"),
)
repl("e0_01998", ("I made everyone<FF03>suffer", "Hice sufrir<FF03>a todos"))
repl("e0_01999",
    ("You killed the only one the real me<FF03>could rely on.", "Mataste al unico en quien la<FF03>verdadera yo confiaba."),
    ("No one will save us now. It's all over.", "Nadie nos salvara ya. Se acabo."),
    ("There's three Makis", "Hay tres Makis"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c56.json"))
