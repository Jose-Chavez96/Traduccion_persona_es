import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_00247", ("But it seems", "Pero parece"))
repl("e0_00249",
    ("It's the painting called <0028>Gate To<FF03>Paradise<0028> that Maki won an award for!",
     "Es el cuadro <0028>Puerta al<FF03>Paraiso<0028> que a Maki dio un premio!"),
    ("You can sense Maki's pain just by<FF03>looking at it", "Se siente el dolor de Maki solo<FF03>con verlo"),
)
repl("e0_00251", ("I wonder if Maki's okay", "Estara bien Maki?"))
repl("e0_00253",
    ("Dammit.", "Maldicion."),
    ("Wh-What the--an earthquake.?", "Q-Que es--un temblor.?"),
    ("Whoa. It's a big one.", "Whoa. Es fuerte."),
)
repl("e0_00254",
    ("It seems to have stopped!", "Parece que paro!"),
    ("Maki. Wh-What the hell.?<FF03>Th-The room's gone.", "Maki. Q-Que demonios.?<FF03>E-El cuarto ya no esta."),
    ("What.? What's going on here? That was<FF03>definitely the ICU", "Que.? Que pasa aqui? Esa era<FF03>la UCI sin duda"),
)
repl("e0_00255",
    ("<FF1B>Woman's voice<FF03>", "<FF1B>Voz de mujer<FF03>"),
    ("Did you hear that? It came from<FF03>downstairs. Let's check it out.",
     "Oiste eso? Vino de<FF03>abajo. Vamos a ver."),
)
repl("e0_00256",
    ("Vacant-eyed man<FF03>", "Hombre vacio<FF03>"),
    ("F-Fresh meat", "C-Carne fresca"),
)
repl("e0_00257",
    ("<FF1B>Panicked nurse<FF03>", "<FF1B>Enfermera en panico<FF03>"),
    ("Meat is heeeeere.", "Carne aquiii."),
    ("Wh-What's with these guys?", "Q-Que les pasa a estos?"),
    ("Th-The dead patients suddenly got up and<FF03>walked",
     "L-Los muertos se levantaron y<FF03>caminaron"),
)
repl("e0_00258", ("That old man rescued me and", "Ese viejo me rescato y"))
repl("e0_00259",
    ("<FF1B>Panicked nurse<FF03>", "<FF1B>Enfermera en panico<FF03>"),
    ("What.? These guys were dead?<FF03>Is this for real.?", "Que.? Estos estaban muertos?<FF03>Es en serio.?"),
)
repl("e0_00261", ("Yamaoka. You bastards", "Yamaoka. Malditos"))
repl("e0_00267",
    ("You wouldn't<FF03>leave me behind, right?", "No me<FF03>dejarias atras, verdad?"),
    ("Right, Yamaoka?", "Verdad, Yamaoka?"),
    ("Oh, young master", "Oh, joven amo"),
)
repl("e0_00269", ("It spoils your handsome face", "Arruina tu apuesto rostro"))
repl("e0_00270", ("You're a fine Japanese man", "Eres un buen japones"))
repl("e0_00271", ("And a<FF03>man must stand on his own someday", "Y un<FF03>hombre debe valerse solo un dia"))
repl("e0_00272", ("It seems that this", "Parece que esto"))
repl("e0_00273", ("will be the last<FF03>service I can provide for you", "sera el ultimo<FF03>servicio que pueda darte"))
repl("e0_00274",
    ("No. No no no. I won't let you leave me.", "No. No no no. No dejare que te vayas."),
    ("Hang in there, Yamaoka.", "Aguanta, Yamaoka."),
    ("It's time I said farewell", "Es hora de despedirme"),
)
repl("e0_00275", ("Just one last thing", "Una ultima cosa"))
repl("e0_00276", ("Please promise<FF03>me, young master", "Prometeme<FF03>algo, joven amo"))
repl("e0_00277",
    ("Promise to become the No! 1 man in the<FF03>country and carry Japan on your back.",
     "Promete ser el hombre No! 1 del<FF03>pais y cargar a Japon en tu espalda."),
)
repl("e0_00279",
    ("Of course I will!<FF03>When that time comes, you'll see!", "Claro que si!<FF03>Cuando llegue, ya veras!"),
    ("So, until then--", "Asi que, hasta entonces--"),
    ("That's my young master", "Ese es mi joven amo"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c06.json"))
