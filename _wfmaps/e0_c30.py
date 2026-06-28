import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_01011",
    ("Maybe he knows where Kandori is.", "Quiza sabe donde esta Kandori."),
    ("This door", "Esta puerta"),
)
repl("e0_01012", ("I don't like the way<FF03>it feels", "No me gusta<FF03>como se siente"))
repl("e0_01013",
    ("Dammit. I'll settle this, just you wait.", "Maldicion. Esto lo arreglo, espera."),
    ("For heaven's sake. Thanks to this idiot,<FF03>I forgot what I was going to ask.", "Por Dios. Por este idiota,<FF03>olvide que iba a preguntar."),
)
repl("e0_01014",
    ("I told you to leave me alone!", "Te dije que me dejes en paz!"),
    ("This world's Devil-Boy seems reliable!<FF03>Though he could work on his looks", "El Chico Diablo de este mundo es<FF03>confiable! Aunque podria mejorar su look"),
)
repl("e0_01015", ("Devil-Boy, huh? This is pretty funny,<FF03>actually", "Chico Diablo, eh? Es gracioso,<FF03>la verdad"))
repl("e0_01016",
    ("But I can't get used to it!", "Pero no me acostumbro!"),
    ("Whaaaat? We're going ALREADY.?", "Queee? Nos vamos YA.?"),
    ("You're the first guy who's ever dragged<FF03>me around this much!", "Eres el primero que me arrastra<FF03>tanto!"),
    ("With your stamina, I'm sure you'll be<FF03>fine no matter what you face!", "Con tu energia, estaras bien<FF03>ante lo que sea!"),
    ("Though you're a rather unruly crowd", "Aunque son un grupo rebelde"),
)
repl("e0_01017",
    ("The Alaya Shrine is right where it was<FF03>in our world! Find a way home!", "El Alaya Shrine esta donde estaba<FF03>en nuestro mundo! Hallen el camino!"),
    ("And", "Y"),
)
repl("e0_01018", ("If you happen to see Chisato,<FF03>save her for me! I'm begging you", "Si ves a Chisato,<FF03>salvala por mi! Te lo ruego"))
repl("e0_01019", ("You can hear an eerie beating from<FF03>the other side of the door", "Oyes un latido inquietante del<FF03>otro lado de la puerta"))
repl("e0_01020",
    ("You're curious too, I see! This door<FF03>appeared during the incident last month!", "Tu tambien curioso! Esta puerta<FF03>aparecio en el incidente del mes pasado!"),
    ("I've tried everything, but it won't<FF03>budge!", "Lo intente todo, pero no<FF03>cede!"),
    ("Though if the threads of fate lead<FF03>there, even this door must open!", "Pero si los hilos del destino llevan<FF03>alli, esta puerta debe abrir!"),
    ("Supposed to be an occult obsessive with<FF03>dodgy information, but", "Supuesto obseso del ocultismo con<FF03>datos dudosos, pero"),
)
repl("e0_01037",
    ("It'll be 2,500 yen!<FF03>That's okay, right?", "Seran 2,500 yenes!<FF03>Esta bien, no?"),
    ("Great. Then here goes.<FF03>Pain, pain, go away.", "Bien. Aqui voy.<FF03>Dolor, dolor, vete."),
    ("Phew", "Uf"),
)
repl("e0_01141",
    ("I wonder who he is!", "Quien sera el!"),
    ("Oh yes, that's right! Maki said that<FF03>she'd met the masked man, too!", "Ah si, cierto! Maki dijo que<FF03>tambien conocio al enmascarado!"),
    ("Wonder why there's always a butterfly<FF03>flying around", "Por que siempre hay una mariposa<FF03>volando"),
)
repl("e0_01142",
    ("This world is completely fascinating!", "Este mundo es fascinante!"),
    ("There's nothing nice about meeting<FF03>a creepy guy like that.", "Nada lindo en conocer<FF03>a un tipo raro asi."),
    ("I had a dream about that butterfly<FF03>man, too!", "Yo tambien sone con ese<FF03>hombre mariposa!"),
    ("We're sure that butterfly has nothing<FF03>to do with Kandori, right?", "Seguro que esa mariposa no tiene<FF03>que ver con Kandori, no?"),
    ("No one's here", "No hay nadie"),
)
repl("e0_01143",
    ("Did Tsutomu pull<FF03>a fast one on us?", "Tsutomu nos<FF03>engano?"),
    ("But this world's Tsutomu seemed<FF03>reliable", "Pero el Tsutomu de este mundo<FF03>parecia confiable"),
)
repl("e0_01144",
    ("What's that?", "Que es eso?"),
    ("Say, Masao", "Oye, Masao"),
)
repl("e0_01145", ("isn't that butterfly", "no es esa mariposa"))
repl("e0_01146",
    ("Oh. It's that butterfly from when we<FF03>found Maki's mother collapsed here!", "Oh. Es esa mariposa de cuando<FF03>hallamos a la mama de Maki aqui!"),
    ("What a pretty butterfly", "Que linda mariposa"),
)
repl("e0_01147",
    ("What say<FF03>we catch it and keep it as a pet?", "Que tal si<FF03>la atrapamos de mascota?"),
    ("You're into butterflies, Nanjo?", "Te gustan las mariposas, Nanjo?"),
    ("What, are you the kind of guy who gloats<FF03>over his room full of specimens?", "Que, eres de los que presume<FF03>un cuarto lleno de especimenes?"),
    ("Could this be one of his traps", "Sera una de sus trampas"),
)
repl("e0_01148",
    ("One false move and I'll catch it<FF03>and crush it!", "Un mal paso y la atrapo<FF03>y la aplasto!"),
    ("No", "No"),
)
repl("e0_01149", ("feel faint", "me mareo"))
repl("e0_01158",
    ("So he's in this town, too!", "Asi que el tambien esta aqui!"),
    ("Kandori's here, too? Aw man, I have,<FF03>like, a really bad feeling about this.", "Kandori tambien? Ay, tengo,<FF03>o sea, muy mal presentimiento."),
    ("Kandori, huh? Even a total stud like me<FF03>would rather not deal with that guy", "Kandori, eh? Hasta un galan como yo<FF03>preferiria no lidiar con el"),
)
put("e0_01159", O("e0_01159"))  # solo nombre (Kandori)
dump(os.path.join(os.path.dirname(__file__), "e0_c30.json"))
