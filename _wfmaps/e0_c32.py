import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_01189", ("You shouldn't", "No debes"))
repl("e0_01190", ("You shouldn't", "No debes"))
repl("e0_01191", ("What was that", "Que fue eso"))
repl("e0_01192",
    ("It looked like a little girl's face,<FF03>but she was saying not to take <0028>this!<0028>", "Parecia cara de una nina,<FF03>pero decia no tomar <0028>esto!<0028>"),
    ("Did she mean the Expel Mirror?", "Se referia al Expel Mirror?"),
    ("Who gives a damn? We gotta have it,<FF03>or else!", "A quien le importa? Hay que tenerlo,<FF03>o si no!"),
    ("That face just now", "Esa cara de hace rato"),
)
repl("e0_01193", ("It looked<FF03>like Mai", "Parecia<FF03>Mai"))
repl("e0_01194",
    ("Here, <FF07>!", "Toma, <FF07>!"),
    ("We can fight the monster in the subway<FF03>once we have this, right?", "Podemos pelear al monstruo del metro<FF03>con esto, no?"),
    ("Obtained the <FF19><0300><FF18><0500>Expel Mirror<FF18> .", "Obtuviste el <FF19><0300><FF18><0500>Expel Mirror<FF18> ."),
)
repl("e0_01205", ("<FF1B>Monster<FF03>", "<FF1B>Bestia<FF03>"))
repl("e0_01209", ("Hold it. That thing looks really<FF03>strong", "Espera. Eso se ve muy<FF03>fuerte"))
repl("e0_01210",
    ("<FF1B>Monster<FF03>", "<FF1B>Bestia<FF03>"),
    ("Shouldn't we go to the shrine like<FF03>Tsutomu said? We might find something.", "No deberiamos ir al templo como<FF03>dijo Tsutomu? Quiza hallemos algo."),
    ("I am the key and the guardian of the<FF03>gate", "Soy la llave y el guardian de la<FF03>puerta"),
)
repl("e0_01211", ("Yog-Sothoth's son", "Yog-Sothoth menor"))
repl("e0_01212", ("<FF1B>Monster<FF03>", "<FF1B>Bestia<FF03>"), ("The gate will not open", "La puerta no se abrira"))
repl("e0_01213", ("For those<FF03>without credentials", "Para los<FF03>sin credenciales"))
repl("e0_01216", ("I think I've lost my taste for fish!<FF03>The stench of the thing", "Creo que perdi el gusto por el pez!<FF03>El hedor de la cosa"))
repl("e0_01217",
    ("I'm sorry, <FF07>, but we haven't<FF03>a prayer against this thing at present!", "Perdon, <FF07>, pero no tenemos<FF03>chance contra esto ahora!"),
    ("Just this once, we'll have to heed<FF03>the advice of that dubious young man!", "Solo por esta vez, haremos caso<FF03>al dudoso joven!"),
    ("You hold", "Tienes"),
)
repl("e0_01218", ("the Expel Mirror", "el Expel Mirror"))
repl("e0_01219", ("But you cannot pass", "No puedes pasar"))
repl("e0_01220", ("until you have<FF03>defeated me", "hasta que me<FF03>derrotes"))
repl("e0_01221",
    ("I knew it was gonna say that.<FF03>Let's do this, <FF07>.", "Sabia que diria eso.<FF03>Hagamoslo, <FF07>."),
    ("If we leave this creature be, it could<FF03>grow to be larger than a farmhouse", "Si dejamos a esta criatura, podria<FF03>crecer mas que una granja"),
)
repl("e0_01222",
    ("We must defeat it now.", "Hay que vencerla ya."),
    ("Are we really fighting this thing", "De verdad pelearemos con esto"),
)
repl("e0_01224", ("nasty-looking", "se ve feo"))
repl("e0_01225", ("What a tasteless creature", "Que criatura sin gusto"))
repl("e0_01226",
    ("And ugh,<FF03>that horrible smell. Frickin' gross.", "Y uf,<FF03>ese olor horrible. Que asco."),
    ("Now's not the time to bitch and moan!", "No es momento de quejarse!"),
    ("If we don't beat this thing, we'll<FF03>never get our hands on that bastard.", "Si no vencemos esto, nunca<FF03>atraparemos a ese desgraciado."),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c32.json"))
