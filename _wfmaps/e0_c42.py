import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_01525", ("No particular reason", "Sin razon especial"))
repl("e0_01526",
    ("Why? Did it<FF03>seem like an odd question?", "Por que? Parecio<FF03>pregunta rara?"),
    ("This place seems pretty dangerous!", "Este lugar parece peligroso!"),
    ("That girl asked some pretty heavy stuff!<FF03>I'm still kinda sorting it all out!", "Esa chica pregunto cosas pesadas!<FF03>Aun lo estoy procesando!"),
    ("It's been a while since I saw this many<FF03>trees in one place!", "Hace mucho no veia tantos<FF03>arboles juntos!"),
    ("Did you know this smell is called ozone?", "Sabias que este olor se llama ozono?"),
)
repl("e0_01527",
    ("Hey <FF07>, have you ever like,<FF03>thought seriously about your future?", "Oye <FF07>, alguna vez has<FF03>pensado en serio en tu futuro?"),
    ("I've", "He"),
)
repl("e0_01528", ("Eh, never mind! Let's not talk<FF03>about that stuff", "Eh, olvidalo! Mejor no hablar<FF03>de eso"))
repl("e0_01529", ("Just forget it!", "Olvidalo!"))
repl("e0_01533",
    ("<FF1B>Girl in white<FF03>", "<FF1B>Chica de blanco<FF03>"),
    ("Wh-Who's there?", "Q-Quien anda ahi?"),
    ("Hey, isn't that the ghost who showed up<FF03>at the Historical Society?", "Oye, no es el fantasma que aparecio<FF03>en la Sociedad Historica?"),
    ("Is she friends with that brat in black.?", "Es amiga de esa mocosa de negro.?"),
)
repl("e0_01534",
    ("<FF1B>Girl in white<FF03>", "<FF1B>Chica de blanco<FF03>"),
    ("Waaaaaaaaah.", "Buaaaaaah."),
    ("Hey now, don't cry! Are you little Mai?", "Oye, no llores! Eres la pequena Mai?"),
    ("Yes", "Si"),
)
repl("e0_01535", ("Whoa", "Whoa"))
repl("e0_01536",
    ("She has a half-moon-shaped<FF03>compact.", "Tiene una polvera<FF03>de media luna."),
    ("It looks a lot like mine", "Se parece mucho a la mia"),
)
repl("e0_01537", ("That must be the castle's key! But who<FF03>are these children", "Esa es la llave! Pero quienes<FF03>son estos ninos"))
repl("e0_01538",
    ("Hey Mai, you know that girl Aki?", "Oye Mai, conoces a esa chica Aki?"),
    ("Is she a friend of yours?", "Es amiga tuya?"),
    ("No. She's not my friend.", "No. No es mi amiga."),
    ("She's Mai", "Es Mai"),
)
repl("e0_01539", ("She's the bad Mai! Waaaaaah", "Es la Mai mala! Buaaaah"))
repl("e0_01540",
    ("What.? What does that mean?", "Que.? Que significa eso?"),
    ("I was lonely", "Estaba sola"),
)
repl("e0_01541",
    ("That's when<FF03>Kandori came!", "Ahi fue cuando<FF03>llego Kandori!"),
    ("Then she came out of me and left with<FF03>Kandori!", "Salio de mi y se fue con<FF03>Kandori!"),
    ("She knows Kandori isn't our real Daddy", "Sabe que Kandori no es nuestro Papa real"),
)
repl("e0_01543", ("So she's a separate personality<FF03>that split off", "Asi que es una personalidad<FF03>que se separo"))
repl("e0_01544",
    ("What is that compact?", "Que es esa polvera?"),
    ("It's my treasure! It grants wishes!", "Es mi tesoro! Cumple deseos!"),
    ("I used it to make this town!", "La use para crear este pueblo!"),
    ("No way. That's", "Imposible. Eso"),
)
repl("e0_01545", ("Unbelievable", "Increible"))
repl("e0_01546", ("This small child was the<FF03>creator of an entire world", "Esta nina fue la<FF03>creadora de un mundo entero"))
repl("e0_01547",
    ("Yes! This little girl was this world's<FF03>creator!", "Si! Esta nina fue la creadora<FF03>de este mundo!"),
    ("Wow. You're like a magical girl! I could<FF03>use one of those compacts myself.", "Vaya. Eres como chica magica! Yo<FF03>usaria una de esas polveras."),
    ("Seriously.? Can I have that.?", "En serio.? Me la das.?"),
    ("Can't you use the compact to catch Aki<FF03>and Kandori, or send everyone home?", "No puedes usar la polvera para atrapar<FF03>a Aki y Kandori, o mandarnos a casa?"),
)
repl("e0_01548",
    ("Aki took half of it!", "Aki tomo la mitad!"),
    ("I know she's using the other half to<FF03>do mean things", "Se que usa la otra mitad para<FF03>hacer maldades"),
)
repl("e0_01549",
    ("My wishes just get canceled out! That's<FF03>how come I'm hiding here!", "Mis deseos se anulan! Por eso<FF03>me escondo aqui!"),
    ("But we can't get to Kandori without it!<FF03>Can't we borrow it for a while?", "Pero no llegamos a Kandori sin ella!<FF03>Nos la prestas un rato?"),
    ("No. You can't. That's what Kandori wants.", "No. No pueden. Eso quiere Kandori."),
)
repl("e0_01550", ("You shouldn't hide like this!", "No deberias esconderte asi!"))
dump(os.path.join(os.path.dirname(__file__), "e0_c42.json"))
