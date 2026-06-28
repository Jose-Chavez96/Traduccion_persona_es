import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_01411", ("It's Maki's painting", "Pintura de Maki"))
repl("e0_01412", ("The mirror's power has faded", "El poder del espejo se fue"))
repl("e0_01413",
    ("Hey. How weak are you, losing to nobodies<FF03>like them.?", "Oye. Que debil, perder ante<FF03>nadies como ellos.?"),
    ("If you can't win, I'm not gonna fix<FF03>your face.", "Si no ganas, no te arreglo<FF03>la cara."),
    ("Though I was never gonna do that anyway.<FF03>Pbbbbt.", "Aunque igual nunca lo iba a hacer.<FF03>Pbbbt."),
    ("Huh? Hey, wait", "Eh? Oye, espera"),
)
repl("e0_01414",
    ("What do you mean.?", "Que quieres decir.?"),
    ("Daddy called you a <0028>ginnee pig<0028> and a<FF03><0028>useless pon<0028>.", "Papa te llamo <0028>conejilla<0028> y<FF03><0028>peon inutil<0028>."),
    ("He said, <0028>Even if Chisato loses, she's<FF03>not worth our trouble!<0028>", "Dijo, <0028>Aunque Chisato pierda, no<FF03>vale la pena!<0028>"),
    ("So you can have fun staying that way as<FF03>long as you live. Bye-bye.", "Diviertete quedando asi<FF03>el resto de tu vida. Adios."),
    ("W-Wait. Am I going to be like this<FF03>forever", "E-Espera. Voy a quedar asi<FF03>para siempre"),
)
put("e0_01415", O("e0_01415"))  # solo nombre (Chisato)
repl("e0_01416",
    ("Just wait here for us!<FF03>We'll go catch that girl!", "Espera aqui!<FF03>Iremos por esa chica!"),
    ("And when we do, we'll make her put your<FF03>face back the way it was.", "Y cuando lo hagamos, le haremos<FF03>devolverte tu cara."),
)
repl("e0_01417",
    ("You're lying. Don't feed me that crap.<FF03>I know you think I deserve all this.", "Mientes. No me vengas con eso.<FF03>Se que crees que merezco esto."),
    ("I'm not lying, Chisato! I still like<FF03>you", "No miento, Chisato! Aun me<FF03>caes bien"),
)
repl("e0_01418", ("even now!", "aun hoy!"))
repl("e0_01420",
    ("Yep. You're energetic, beautiful,<FF03>fashionable, and self-possessed!", "Si. Eres energica, hermosa,<FF03>con estilo y segura!"),
    ("I can tell what Yosuke sees in you!", "Veo lo que Yosuke ve en ti!"),
    ("No. I'm", "No. Estoy"),
)
repl("e0_01421", ("sure Yosuke still has a<FF03>thing for you, Maki!", "segura de que Yosuke aun<FF03>gusta de ti, Maki!"))
repl("e0_01422",
    ("I'm sorry!", "Perdon!"),
    ("I was so jealous of you, Maki!", "Tenia tanta envidia de ti, Maki!"),
    ("You say I'm self-possessed, but it's<FF03>just an act!", "Dices que soy segura, pero es<FF03>solo actuacion!"),
    ("The real me is helpless!", "La verdadera yo es inutil!"),
    ("I have to act out and look pretty or<FF03>everyone will ignore me", "Tengo que actuar y verme linda o<FF03>todos me ignoran"),
)
repl("e0_01423", ("That's why I envied you! You just had to<FF03>be yourself, and everyone loved you!", "Por eso te envidiaba! Solo<FF03>siendo tu, todos te querian!"))
repl("e0_01424", ("Yosuke will hate me now! Then, you and<FF03>him will", "Yosuke me odiara ahora! Entonces tu<FF03>y el"))
repl("e0_01427",
    ("Ohhhh, you're so stubborn. Deep down,<FF03>you really like Yosuke!", "Ahhh, que terca. En el fondo,<FF03>de verdad te gusta Yosuke!"),
    ("But you don't have to worry about me<FF03>getting in the way! See", "Pero no te preocupes por mi<FF03>estorbando! Mira"),
)
repl("e0_01428", ("Ack. What the", "Ack. Pero que"))
repl("e0_01429", ("Chisato. I finally found you. I've been<FF03>looking for you all this time.", "Chisato. Al fin te encuentro. Te he<FF03>buscado todo este tiempo."))
repl("e0_01430",
    ("What happened to your face.?<FF03>Did you get hurt.?", "Que paso con tu cara.?<FF03>Te lastimaste.?"),
    ("No. Don't look at me.", "No. No me mires."),
    ("Umm, what happened was, Aki put a curse<FF03>on her, and", "Em, lo que paso es que Aki la<FF03>maldijo, y"),
)
repl("e0_01431",
    ("Maki. Are you trying to cover for me?", "Maki. Intentas encubrirme?"),
    ("No", "No"),
)
repl("e0_01432",
    ("Not this time.", "No esta vez."),
    ("Look, Yosuke. This is my face now.", "Mira, Yosuke. Esta es mi cara ahora."),
    ("I did terrible things", "Hice cosas terribles"),
)
repl("e0_01433",
    ("I was so cruel<FF03>to Maki!", "Fui tan cruel<FF03>con Maki!"),
    ("This is my punishment.", "Es mi castigo."),
)
repl("e0_01434",
    ("I don't deserve you, Yosuke.", "No te merezco, Yosuke."),
    ("I'm a terrible person", "Soy una persona terrible"),
)
repl("e0_01435",
    ("Even the face<FF03>I was so proud of shows it!", "Hasta la cara<FF03>de la que presumia lo muestra!"),
    ("If people see you with me, they'll<FF03>laugh at you, too!", "Si te ven conmigo, se reiran<FF03>de ti tambien!"),
    ("That's why it's okay if you want Maki<FF03>instead. You always liked her, right?", "Por eso esta bien si prefieres a Maki.<FF03>Siempre te gusto, no?"),
    ("Hey, hey, don't get me wrong.", "Oye, oye, no me malentiendas."),
    ("Yeah, I did like Maki", "Si, me gustaba Maki"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c39.json"))
