import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_01886",
    ("can't you<FF03>somehow rescue Sonomura's daughter?", "no puedes<FF03>rescatar a la hija de Sonomura?"),
    ("I'll do my best to adjust the system so<FF03>you can go rescue her whenever you wish.", "Ajustare el sistema para que<FF03>puedan ir a salvarla cuando quieran."),
    ("And once that's done, I'll go to whatever<FF03>fate awaits me! I beg you, young man.", "Y luego ire al destino que<FF03>me espere! Te lo ruego, joven."),
    ("<FF07>. Where are you going.?<FF03>We have to defeat Kandori.", "<FF07>. A donde vas.?<FF03>Hay que vencer a Kandori."),
    ("<FF07>. Where you goin", "<FF07>. A donde vas"),
)
repl("e0_01896",
    ("Kandori. This is it. I hope you're ready.", "Kandori. Es la hora. Espero que listo."),
    ("We finally found you", "Al fin te encontramos"),
)
repl("e0_01897",
    ("You're not going<FF03>anywhere this time.", "No iras a ningun<FF03>lado esta vez."),
    ("You guys are so aggravating. I won't<FF03>let you get in my Daddy's way.", "Que fastidiosos. No dejare<FF03>que estorben a mi Papa."),
)
repl("e0_01898",
    ("That's enough, Aki! Stay back!", "Basta, Aki! Atras!"),
    ("But, Daddy", "Pero, Papa"),
)
repl("e0_01899", ("Wait in the other room! I'll be with<FF03>you soon!", "Espera en otro cuarto! Pronto<FF03>estare contigo!"))
repl("e0_01900",
    ("Okay, Daddy!", "Bien, Papa!"),
    ("Stop causin' all this pain. Turn everyone<FF03>back to normal.", "Deja de causar dolor. Vuelve a todos<FF03>a la normalidad."),
)
repl("e0_01901", ("Don't worry! I won't do anything<FF03>further!", "Tranquilos! No hare nada<FF03>mas!"))
repl("e0_01902",
    ("What the hell.? What, all of a sudden<FF03>you're not in the mood anymore?", "Que rayos.? De pronto<FF03>ya no estas de humor?"),
    ("What a bunch of crap", "Que basura"),
)
repl("e0_01903",
    ("After all we<FF03>did to get here.", "Despues de todo lo<FF03>que hicimos por llegar."),
    ("What.? Something seems peculiar<FF03>about this", "Que.? Algo raro hay<FF03>en esto"),
)
repl("e0_01904",
    ("Hey. Did you finally snap or something?<FF03>Apologizing now won't help.", "Oye. Por fin te volviste loco?<FF03>Disculparte ya no ayuda."),
    ("I'm too pissed off now.", "Estoy muy enojada ahora."),
)
repl("e0_01905", ("What the hell's with you? Decided to<FF03>beg for your life all of a sudden?", "Que te pasa? De pronto decides<FF03>rogar por tu vida?"))
repl("e0_01906",
    ("What are you living for?", "Para que vives?"),
    ("Huh.?", "Eh.?"),
    ("People aren't strong enough to live<FF03>without a goal! Everyone wants something!", "La gente no es fuerte para vivir<FF03>sin meta! Todos quieren algo!"),
    ("No matter how small the desire", "Por pequeno que sea el deseo"),
)
repl("e0_01907",
    ("It gives them the strength to carry on!", "Les da fuerza para seguir!"),
    ("But", "Pero"),
)
repl("e0_01908",
    ("if every desire is fulfilled,<FF03>what's left to strive for?", "si todo deseo se cumple,<FF03>por que luchar?"),
    ("When one's wishes have been granted,<FF03>the only thing that awaits", "Cuando los deseos se cumplen,<FF03>lo unico que espera"),
)
repl("e0_01910",
    ("is a bottomless solitude<0007> an eternal<FF03>emptiness!", "es una soledad sin fondo<0007> un vacio<FF03>eterno!"),
    ("Then wouldn't it be better if one chose<FF03>not to ascend the stairs of desire?", "No seria mejor elegir<FF03>no subir la escalera del deseo?"),
    ("That way", "Asi"),
)
repl("e0_01911", ("one's dreams are kept alive!", "los suenos siguen vivos!"))
repl("e0_01912", ("kept ascending that stair to destroy<FF03>this worthless world", "segui subiendo escalera para<FF03>destruir este mundo inutil"))
repl("e0_01913", ("But it no longer matters! Right now", "Pero ya no importa! Ahora"))
repl("e0_01914",
    ("nothing is beyond my grasp!", "nada esta fuera de mi alcance!"),
    ("Hah! The winds of solitude and emptiness<FF03>blow within me", "Ja! Los vientos de soledad y vacio<FF03>soplan en mi"),
)
repl("e0_01915", ("Such is a god's lot!", "Destino de un dios!"))
repl("e0_01916", ("Boy", "Tu"))
repl("e0_01917",
    ("I allowed you to come here in<FF03>order to ask you this<0006>", "Te deje venir aqui<FF03>para preguntarte esto<0006>"),
    ("Why do you cling to life?", "Por que te aferras a la vida?"),
    ("What are you living for?", "Para que vives?"),
    ("That's right. Our reason for living", "Asi es. Nuestra razon de vivir"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c53.json"))
