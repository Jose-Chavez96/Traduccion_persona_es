import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_01946", ("but I feel<FF03>remarkably content!", "pero me siento<FF03>muy en paz!"))
repl("e0_01947", ("Where is the real Maki?", "Donde esta Maki real?"))
repl("e0_01948", ("you've solved the mystery of the<FF03>two worlds", "resolviste el misterio de los<FF03>dos mundos"))
repl("e0_01949", ("I'm not surprised!", "No me sorprende!"))
repl("e0_01950",
    ("What do you mean?", "A que te refieres?"),
    ("You and the people of your world were<FF03>mere figments of a certain imagination!", "Tu y la gente de tu mundo eran<FF03>meras figuras de cierta imaginacion!"),
    ("Maki Sonomura's", "De Maki Sonomura"),
)
repl("e0_01951",
    ("Huh? What're you saying.? What does<FF03>that mean.?", "Eh? Que dices.? Que<FF03>significa.?"),
    ("You're", "Eres"),
)
repl("e0_01952",
    ("probably the idealized self<FF03>of the Maki Sonomura we know!", "seguro el yo idealizado<FF03>de la Maki que conocemos!"),
    ("And the town you live in is the world<FF03>inside Maki Sonomura's heart", "Y el pueblo donde vives es el mundo<FF03>dentro del corazon de Maki Sonomura"),
)
repl("e0_01953",
    ("Am I correct, Kandori?", "Tengo razon, Kandori?"),
    ("Yes", "Si"),
)
repl("e0_01954",
    ("and not only her!", "y no solo ella!"),
    ("Mai and Aki are also shadows within<FF03>Maki Sonomura's heart", "Mai y Aki son sombras en<FF03>el corazon de Maki Sonomura"),
)
repl("e0_01955",
    ("All of you are nothing more than aspects<FF03>of her!", "Todos ustedes solo son aspectos<FF03>de ella!"),
    ("No", "No"),
)
put("e0_01957", O("e0_01957"))  # solo nombres (Maki, Mai, Aki) identicos
repl("e0_01958",
    ("Simple anagrams!", "Simples anagramas!"),
    ("Maki must have conceived of her own<FF03>paradise in her heart", "Maki debio concebir su propio<FF03>paraiso en su corazon"),
)
repl("e0_01959",
    ("One modeled off her memories of Mikage<FF03>until the day she was hospitalized!", "Modelado de sus recuerdos de Mikage<FF03>hasta el dia que la internaron!"),
    ("No way", "Imposible"),
)
repl("e0_01960", ("Then there was no police<FF03>station or hospital because", "Por eso no habia<FF03>comisaria ni hospital porque"))
repl("e0_01961", ("They have no place in paradise! She only<FF03>had room for what was useful", "No tienen lugar en el paraiso! Solo<FF03>tenia espacio para lo util"))
repl("e0_01962",
    ("It's a common sentiment!", "Es un sentir comun!"),
    ("Chisato and Yosuke were no doubt drawn<FF03>in by Maki's unconscious desires!", "Chisato y Yosuke sin duda fueron<FF03>atraidos por los deseos de Maki!"),
    ("When it came to her crush and her best<FF03>friend, she wanted the genuine article!", "Con su amor y su mejor<FF03>amiga, queria los autenticos!"),
    ("The trial run of the Deva System<FF03>succeeded roughly a month ago!", "La prueba del Deva System<FF03>tuvo exito hace un mes!"),
    ("But", "Pero"),
)
repl("e0_01963",
    ("she was linked to the system<FF03>even before then!", "ella estaba ligada al sistema<FF03>desde antes!"),
    ("Her wavelength must have synchronized<FF03>with the system's!", "Su frecuencia debio sincronizar<FF03>con la del sistema!"),
    ("Once she had internalized the power to<FF03>interfere with the dimensions", "Al internalizar el poder de<FF03>alterar las dimensiones"),
)
repl("e0_01964",
    ("The paradise within her heart seems to<FF03>have grown beyond our imaginations!", "El paraiso en su corazon parece<FF03>haber crecido mas de lo imaginado!"),
    ("And you came into contact with Mai,<FF03>caretaker of that paradise", "Y entraste en contacto con Mai,<FF03>guardiana de ese paraiso"),
)
put("e0_01965", O("e0_01965"))  # solo nombre (Mai)
repl("e0_01966", ("No! That Maki was isolated!<FF03>She had her role for the ideal Maki", "No! Esa Maki estaba aislada!<FF03>Tenia su papel para la Maki ideal"))
repl("e0_01967",
    ("To provide the world she'd always wanted<FF03>as comfort for Maki in the real world!", "Dar el mundo que siempre quiso<FF03>como consuelo para la Maki real!"),
    ("You know the rest", "Sabes el resto"),
)
repl("e0_01968",
    ("You're lying. None of that makes sense.", "Mientes. Nada de eso tiene sentido."),
    ("Then go", "Entonces ve"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c55.json"))
