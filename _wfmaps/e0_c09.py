import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_00342",
    ("<FF1B>Black-suited man<FF03>", "<FF1B>Hombre de traje negro<FF03>"),
    ("She'd be sad if he got gunned down!", "Se pondria triste si lo balean!"),
    ("No trespassing, kiddos!", "Prohibido el paso, ninos!"),
    ("This ain't no place for kids! Go find<FF03>yourselves a nice playground!",
     "No es lugar para ninos! Vayan a<FF03>buscar un parque!"),
)
repl("e0_00343", ("What is that dude up to?", "Que trama ese tipo?"))
repl("e0_00344",
    ("What's Kandori's game?", "Que planea Kandori?"),
    ("I don't like this", "Esto no me gusta"),
)
repl("e0_00345",
    ("This isn't how<FF03>an ordinary corporation acts!", "Asi no actua<FF03>una empresa normal!"),
    ("What could this mean? I heard SEBEC<FF03>was a Fortuna 500 company",
     "Que significa? Oi que SEBEC<FF03>era empresa Fortuna 500"),
)
repl("e0_00346",
    ("<FF1B>Black-suited man<FF03>", "<FF1B>Hombre de traje negro<FF03>"),
    ("But this may as well be a Mafia<FF03>front operation!", "Pero esto bien podria ser fachada<FF03>de la Mafia!"),
    ("Mm? Isn't he that transfer student?", "Mm? No es ese estudiante nuevo?"),
    ("Huh? Oh, hey, yeah, it's Reiji!<FF03>What's he doing here?", "Eh? Oh, si, es Reiji!<FF03>Que hace aqui?"),
    ("<0029>Nickname<0006> Reiji<002A>", "<0029>Apodo<0006> Reiji<002A>"),
    ("A quiet loner who transferred to<FF03>St! Hermelin High six months ago!",
     "Un solitario callado que llego a<FF03>St! Hermelin hace seis meses!"),
    ("Who're youse?", "Quienes son?"),
    ("Past here is SEBEC territory!<FF03>No entry!", "Aqui es zona SEBEC!<FF03>Prohibido pasar!"),
    ("Hey, doesn't Maki's mom work for SEBEC?<FF03>What in the world's going on",
     "Oye, la mama de Maki no trabaja en SEBEC?<FF03>Que esta pasando"),
)
repl("e0_00351", ("Here we are! Maki's mother should be<FF03>here", "Llegamos! La mama de Maki debe<FF03>estar aqui"))
repl("e0_00352",
    ("Oh, what an exquisite butterfly.", "Oh, que mariposa tan bella."),
    ("Hey", "Oye"),
)
repl("e0_00353",
    ("Is it me, or is there something<FF03>strange about that butterfly?",
     "Sera idea mia, o hay algo<FF03>raro en esa mariposa?"),
    ("Wh", "Qu"),
)
repl("e0_00354", ("What's up with this thing.?", "Que pasa con esto.?"))
repl("e0_00363", ("<0028>Truth is stranger than fiction", "<0028>La realidad supera la ficcion"))
repl("e0_00364",
    ("Evidently!", "Claramente!"),
    ("To be present for another once-in-a-<FF03>lifetime event", "Presenciar otro evento unico<FF03>en la vida"),
)
repl("e0_00365",
    ("<FF1B>Maki's mother<FF03>", "<FF1B>Madre de Maki<FF03>"),
    ("How magnificent.", "Que magnifico."),
)
repl("e0_00367",
    ("Maki's mother! She works at SEBEC as<FF03>an engineering specialist!",
     "Madre de Maki! Trabaja en SEBEC como<FF03>especialista en ingenieria!"),
    ("H-Hey. Did you forget about Maki's<FF03>mom here?", "O-Oye. Olvidaron a la mama<FF03>de Maki?"),
    ("Lady? Are you okay?", "Senora? Esta bien?"),
    ("This is a gunshot wound", "Es una herida de bala"),
)
repl("e0_00368",
    ("Who did<FF03>this to you?", "Quien te<FF03>hizo esto?"),
    ("Kandori's", "De Kandori"),
)
repl("e0_00370",
    ("Kandori.? The president of SEBEC?", "Kandori.? El presidente de SEBEC?"),
    ("The alterations to this town", "Las alteraciones del pueblo"),
)
repl("e0_00371", ("Kandori's behind them all", "Kandori esta tras todo"))
repl("e0_00372", ("<FF1B>Setsuko Sonomura<FF03>I", "<FF1B>Setsuko Sonomura<FF03>"))  # pro-drop; 373 lleva el verbo
repl("e0_00373", ("was involved in the development<FF03>of a certain device", "participe en el desarrollo<FF03>de cierto aparato"))
repl("e0_00374", ("A device", "Aparato"))
repl("e0_00375",
    ("And you're saying this<FF03>machine is causing the changes?", "Y dices que esta<FF03>maquina causa los cambios?"),
    ("It's the <FF18><0700>Deva System<FF18> ", "Es el <FF18><0700>Deva System<FF18> "),
)
repl("e0_00376",
    ("It's engineered to affect reality!<FF03>But I didn't think it could do this",
     "Fue creada para afectar la realidad!<FF03>No crei que pudiera hacer esto"),
)
repl("e0_00377", ("Kandori said", "Kandori dijo"))
dump(os.path.join(os.path.dirname(__file__), "e0_c09.json"))
