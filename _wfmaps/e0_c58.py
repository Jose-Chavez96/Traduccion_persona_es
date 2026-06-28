import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_02023", ("My jealousy and loathing grew", "Mi envidia y odio crecieron"))
repl("e0_02024", ("I made<FF03>up an ideal town to comfort myself", "Invente<FF03>un pueblo ideal para consolarme"))
repl("e0_02025", ("Now do you understand? I'm hopeless", "Ya entiendes? No tengo remedio"))
repl("e0_02026", ("I don't deserve to live.", "No merezco vivir."))
repl("e0_02027",
    ("Y-You.?", "T-Tu.?"),
    ("It's all over for you, too!<FF03>Kandori is gone!", "Tambien se acabo para ti!<FF03>Kandori ya no esta!"),
    ("N-No. Noooo.", "N-No. Noooo."),
    ("Now this quiet town will go back to how<FF03>it was", "Ahora este pueblo<FF03>volvera a ser como era"),
)
repl("e0_02028",
    ("Thank you, mister!", "Gracias, senor!"),
    ("You're", "Vas a"),
)
repl("e0_02029",
    ("You're going to keep living<FF03>there.?", "Vas a seguir viviendo<FF03>ahi.?"),
    ("Yes", "Si"),
)
repl("e0_02030", ("If I don't, I'll feel sorry<FF03>for myself", "Si no, me dare<FF03>lastima"))
repl("e0_02031",
    ("You're going back, too! I want you to<FF03>keep acting as my ideal self!", "Tu tambien vuelves! Quiero que sigas<FF03>siendo mi yo ideal!"),
    ("No. I don't want to go back there.", "No. No quiero volver ahi."),
)
repl("e0_02033", ("You like this boy now", "Te gusta este chico"))
repl("e0_02034",
    ("Okay! I'll make him, too!", "Bien! Tambien lo hare!"),
    ("It's easy", "Es facil"),
)
repl("e0_02035",
    ("Bye bye, mister!", "Adios, senor!"),
    ("Yes, it's all over. Everyone should<FF03>just disappear.", "Si, se acabo. Todos deberian<FF03>desaparecer."),
    ("Disappear, everyone.", "Desaparezcan, todos."),
    ("Maki. Come over here, okay?", "Maki. Ven aca, si?"),
)
repl("e0_02036", ("I can't be with you all anymore", "Ya no puedo estar con ustedes"))
repl("e0_02037", ("Please", "Porfa"))
repl("e0_02038",
    ("send me back into my heart.", "regresame a mi corazon."),
    ("You", "Tu"),
)
repl("e0_02039",
    ("you idiot. Why, dammit.?", "idiota. Por que, maldicion.?"),
    ("<FF07>. Let's go back into Maki's<FF03>heart.", "<FF07>. Volvamos al corazon<FF03>de Maki."),
)
repl("e0_02040",
    ("Wait, Masao! Do you know the story of<FF03>the foolish girl named Pandora?", "Espera, Masao! Conoces la historia<FF03>de la tonta llamada Pandora?"),
    ("Huh?", "Eh?"),
    ("The legend says she opened the gods' box,<FF03>releasing all sorts of evils", "La leyenda dice que abrio la caja<FF03>de los dioses, liberando males"),
)
repl("e0_02041",
    ("It applies to Maki! This town owes its<FF03>miserable condition to her wishes!", "Aplica a Maki! Este pueblo debe su<FF03>miserable estado a sus deseos!"),
    ("Rather than save her, we should focus<FF03>on destroying the Deva System!", "En vez de salvarla, hay que<FF03>destruir el Deva System!"),
    ("Y-You asshole", "M-Maldito"),
)
repl("e0_02042",
    ("How can you talk that<FF03>way about a friend.?", "Como hablas asi<FF03>de una amiga.?"),
    ("If we destroy that thing, what's gonna<FF03>happen to Maki?", "Si destruimos eso, que le<FF03>pasara a Maki?"),
    ("From the looks of it, the system is<FF03>keeping Maki alive", "Por lo visto, el sistema<FF03>mantiene viva a Maki"),
)
repl("e0_02043",
    ("If we destroy it, Maki will most likely<FF03>die as a result!", "Si lo destruimos, Maki<FF03>probablemente morira!"),
    ("But as long as the system is intact, the<FF03>fundamental problem remains unsolved!", "Pero mientras el sistema siga, el<FF03>problema de fondo no se resuelve!"),
    ("Don't let your personal feelings sway<FF03>you", "No dejes que tus sentimientos te<FF03>desvien"),
)
repl("e0_02044", ("A small sacrifice for the greater<FF03>good", "Un sacrificio por el<FF03>bien mayor"))
repl("e0_02045",
    ("The choice is obvious!", "La eleccion es obvia!"),
    ("I hope you're ready for this.", "Espero que estes listo."),
    ("I had you all wrong", "Te juzgue mal"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c58.json"))
