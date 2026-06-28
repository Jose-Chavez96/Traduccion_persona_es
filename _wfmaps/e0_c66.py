import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_02287",
    ("Try saying it backwards!", "Pruebalo al reves!"),
    ("That girl's still my treasure", "Esa chica sigue siendo mi tesoro"),
)
repl("e0_02290",
    ("Maki, it's me. Your mother. Let's go<FF03>back together.", "Maki, soy yo. Tu madre. Volvamos<FF03>juntas."),
    ("Look. These people came all this way<FF03>because they were worried about you.", "Mira. Estos vinieron hasta aqui<FF03>porque se preocupaban por ti."),
    ("Don't come near me. Why", "No te acerques. Por que"),
)
repl("e0_02291",
    ("Why did you all come here.?", "Por que vinieron aqui.?"),
    ("Don't you know what kind of girl I am?", "No saben que clase de chica soy?"),
)
repl("e0_02292", ("I know you feel like you can't<FF03>just let it go", "Se que sientes que no puedes<FF03>dejarlo ir"))
repl("e0_02293",
    ("But doesn't everyone get jealous now<FF03>and then, one way or another?", "Pero no todos sienten envidia<FF03>de vez en cuando?"),
    ("I know I do!", "Yo si!"),
    ("And on top of that, you were just being<FF03>used! It's Kandori's fault, not yours!", "Y ademas, solo te estaban<FF03>usando! Es culpa de Kandori, no tuya!"),
    ("How often did I try to kill everyone.?<FF03>How can you be so nice to me.?", "Cuantas veces trate de matarlos.?<FF03>Como pueden ser tan amables.?"),
    ("I don't want pity! It just makes me more<FF03>miserable", "No quiero lastima! Solo me hace<FF03>mas miserable"),
)
repl("e0_02294",
    ("I deserve to die.", "Merezco morir."),
    ("That's not true.", "No es cierto."),
    ("What a petulant child", "Que nina tan caprichosa"),
)
put("e0_02296", O("e0_02296"))  # solo nombre (Maki)
repl("e0_02297", ("Dude, Maki", "Oye, Maki"))
repl("e0_02298", ("Aw, Maki", "Ay, Maki"))
repl("e0_02299",
    ("You know it, don't you, <FF07>.?", "Lo sabes, verdad, <FF07>.?"),
    ("You know I'm the worst girl alive.", "Sabes que soy la peor chica."),
    ("Get a grip. You've sown these seeds<FF03>and now it's time to reap them.", "Reacciona. Sembraste esto<FF03>y ahora lo cosechas."),
    ("If you want to die, then why sit around<FF03>and mope about it?", "Si quieres morir, por que te<FF03>quedas lamentandote?"),
    ("Don't make empty threats if you don't<FF03>have the courage of your convictions.", "No hagas amenazas vacias si no<FF03>tienes el valor de tus convicciones."),
)
repl("e0_02300",
    ("You spoke of pity? Don't make me laugh!", "Hablaste de lastima? No me hagas reir!"),
    ("We came here of our own will because<FF03>we could sympathize with you!", "Vinimos por voluntad propia porque<FF03>te entendiamos!"),
    ("But even before that", "Pero aun antes de eso"),
)
repl("e0_02301",
    ("Did you think<FF03>you were alone in this world?", "Creiste que<FF03>estabas sola en el mundo?"),
    ("We live at the sufferance of others!<FF03>Each is responsible for each!", "Vivimos gracias a otros!<FF03>Cada quien responde por el otro!"),
    ("Your careless decision would have left<FF03>behind wounds that would never heal!", "Tu decision descuidada dejaria<FF03>heridas que nunca sanarian!"),
    ("If you still want to die, even now,<FF03>go ahead! Put it all behind you!", "Si aun quieres morir, ahora,<FF03>adelante! Deja todo atras!"),
    ("But you're our friend, and we can never<FF03>put you behind us!", "Pero eres nuestra amiga, y nunca<FF03>te dejaremos atras!"),
    ("Now let's get back! We still have to<FF03>rescue Maki on our own!", "Volvamos! Aun debemos<FF03>salvar a Maki nosotros!"),
    ("I don't leave things undone!", "No dejo cosas sin terminar!"),
    ("Wait.", "Espera."),
    ("I'm sorry, everyone", "Perdon a todos"),
)
repl("e0_02303",
    ("Please let me come along!", "Dejenme ir con ustedes!"),
    ("Hehe", "Jeje"),
)
repl("e0_02304",
    ("Of course you can come.<FF03>Welcome back, Maki.", "Claro que puedes venir.<FF03>Bienvenida, Maki."),
)
repl("e0_02305",
    ("Welcome back aboard, Maki.", "Bienvenida de vuelta, Maki."),
    ("Woo-hoo. Good to have you back, Maki.", "Woo-hoo. Que bueno tenerte, Maki."),
    ("Yay. Welcome back, Maki.", "Yei. Bienvenida, Maki."),
    ("I'm back, guys.", "Volvi, amigos."),
    ("Thank you, all of you", "Gracias a todos"),
)
repl("e0_02306", ("Thank you so much", "Muchas gracias"))
repl("e0_02308", ("I'm sorry! I've been bad", "Perdon! Me porte mal"))
repl("e0_02309",
    ("I remember it all now!", "Ahora lo recuerdo todo!"),
    ("I was so lonely being by myself", "Estaba tan sola"),
)
repl("e0_02311", ("I wanted to see you", "Queria verte"))
repl("e0_02312", ("I forgot you were working for my sake,<FF03>and held a grudge", "Olvide que trabajabas por mi,<FF03>y te guarde rencor"))
repl("e0_02313",
    ("I'm so sorry!", "Lo siento mucho!"),
    ("It's okay! It's all right, Maki", "Esta bien! Tranquila, Maki"),
)
repl("e0_02314",
    ("I'm sorry, too!", "Yo tambien lo siento!"),
    ("I'm sorry, Nanjo, and you too,<FF03><FF07>", "Perdon, Nanjo, y tu,<FF03><FF07>"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c66.json"))
