import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_00280", ("I will always<FF03>be", "Siempre<FF03>estare"))
repl("e0_00281", ("in your heart", "en tu corazon"))
repl("e0_00282", ("Hey", "Oye"))
repl("e0_00284", ("I'm begging you", "Te lo ruego"))
put("e0_00285", O("e0_00285"))  # solo nombres (Yamaoka./Nanjo)
repl("e0_00286", ("Let him alone", "Dejalo en paz"))
repl("e0_00288",
    ("Could you hear their voices?", "Oiste sus voces?"),
    ("That thing said it was me!", "Esa cosa dijo que era yo!"),
    ("I heard it, too", "Yo tambien la oi"),
)
repl("e0_00289",
    ("Think it was that<FF03>Persona thing?", "Sera esa cosa<FF03>Persona?"),
    ("It said it would lend us power, so I<FF03>kinda doubt it's hostile!",
     "Dijo que nos daria poder, asi que<FF03>dudo que sea hostil!"),
    ("If we're lucky, maybe it'll listen to<FF03>what we tell it",
     "Con suerte, quiza escuche<FF03>lo que digamos"),
)
repl("e0_00290",
    ("I guess we might as well go on calling<FF03>it <0028><FF18><0700>Persona<FF18> !<0028>",
     "Mejor sigamos llamandola<FF03><0028><FF18><0700>Persona<FF18> !<0028>"),
    ("That's how it felt to me, too", "Asi lo senti yo tambien"),
)
repl("e0_00291",
    ("I have<FF03>a bad feeling about this! Let's go!", "Tengo<FF03>mal presentimiento! Vamos!"),
    ("I'm wondering if the school's safe!<FF03>We should get outdoors, <FF07>!",
     "Estara segura la escuela?<FF03>Salgamos afuera, <FF07>!"),
    ("Nanjo seemed like a little boy in front<FF03>of that old guy",
     "Nanjo parecia un nino frente<FF03>a ese viejo"),
)
repl("e0_00292", ("Failing to protect the ones you love", "No proteger a quienes amas"))
repl("e0_00293", ("Nothing hurts worse than that!", "Nada duele mas que eso!"))
repl("e0_00295", ("Without you, I'm all alone", "Sin ti, estoy solo"))
repl("e0_00296", ("No one<FF03>is here to encourage me", "Nadie<FF03>esta para animarme"))
repl("e0_00297", ("No one", "Nadie"))
repl("e0_00298", ("will stand by me", "estara a mi lado"))
repl("e0_00299", ("I didn't think he was gonna cry", "No crei que iba a llorar"))
repl("e0_00300",
    ("He must've really loved that old guy!", "De verdad amaba a ese viejo!"),
    ("I feel bad for Nanjo, but we gotta<FF03>worry about the living now!",
     "Me da pena Nanjo, pero hay que<FF03>pensar en los vivos ahora!"),
    ("Let's hurry and rescue Maki's mom!", "Vamos a rescatar a la mama de Maki!"),
    ("So that's what happened", "Asi que eso paso"),
)
repl("e0_00301",
    ("Losing one's<FF03>beloved can profoundly affect one!", "Perder a un ser<FF03>amado afecta mucho!"),
    ("He's already gone", "Ya se fue"),
)
repl("e0_00307",
    ("<FF07>. This one's still alive.<FF03>Gimme a hand here.", "<FF07>. Esta sigue viva.<FF03>Ayudame aqui."),
    ("We haven't time to waste here, <FF07>.<FF03>It's too late for her, but not for us.",
     "No hay tiempo que perder, <FF07>.<FF03>Es tarde para ella, no para nosotros."),
    ("Yo, <FF07>. The monsters are just<FF03>around the corner.", "Oye, <FF07>. Los monstruos estan<FF03>a la vuelta."),
    ("<FF1B>Severely wounded nurse<FF03>I", "<FF1B>Enfermera muy herida<FF03>Yo"),
)
repl("e0_00308", ("I'm not going to make it", "No lo voy a lograr"))
repl("e0_00310", ("g-get out of here", "v-vayanse de aqui"))
dump(os.path.join(os.path.dirname(__file__), "e0_c07.json"))
