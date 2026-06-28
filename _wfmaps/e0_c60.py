import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_02083",
    ("Gimme that, Nanjo.", "Dame eso, Nanjo."),
    ("Please. Send us back into Maki's heart.", "Por favor. Vuelvenos al corazon de Maki."),
)
repl("e0_02084",
    ("The compact couldn't possibly have such<FF03>powers in the real world!", "La polvera no tendria tales<FF03>poderes en el mundo real!"),
    ("If only the ideal Maki's compact was<FF03>complete, then maybe", "Si la polvera de la Maki ideal<FF03>estuviera completa, quiza"),
)
put("e0_02085", O("e0_02085"))  # solo nombre (Maki)
repl("e0_02086",
    ("Everyone wants to see you,<FF03>y'know? There's no need to suffer alone!", "Todos quieren verte,<FF03>sabes? No sufras sola!"),
    ("Just call on us, please", "Solo llamanos, por favor"),
)
repl("e0_02087", ("I'd go<FF03>anywhere for you", "Iria<FF03>a donde sea por ti"))
repl("e0_02088",
    ("The ideal Maki is the manifestation of<FF03>Maki wanting to change herself!", "La Maki ideal es la manifestacion de<FF03>Maki queriendo cambiar!"),
    ("But if her ideal self denied its own<FF03>existence", "Pero si su yo ideal niega su<FF03>propia existencia"),
)
put("e0_02089", O("e0_02089"))  # solo nombre (Maki)
repl("e0_02090",
    ("have you really lost hope?", "de verdad perdiste la esperanza?"),
    ("If there's even a fragment left,<FF03>call out to us", "Si queda un fragmento,<FF03>llamanos"),
)
repl("e0_02091", ("Quit sticking your head in a hole,<FF03>Maki. It's the easy way out", "Deja de esconderte,<FF03>Maki. Es la salida facil"))
repl("e0_02092",
    ("My mom was Kandori's dad's old mistress!<FF03>She got thrown away like an old rag!", "Mi mama fue amante del padre de Kandori!<FF03>La tiraron como trapo viejo!"),
    ("But even knowing that would happen", "Pero aun sabiendo que pasaria"),
)
repl("e0_02093",
    ("She still gave birth to me!", "Aun asi me dio a luz!"),
    ("Know why she did that?", "Sabes por que?"),
    ("She told me she couldn't neglect her own<FF03>child's life", "Me dijo que no podia abandonar la<FF03>vida de su hijo"),
)
repl("e0_02094",
    ("You have a mom too! No parent alive<FF03>doesn't love their child!", "Tu tambien tienes mama! No hay padre<FF03>que no ame a su hijo!"),
    ("You're gonna see your mom again, so hurry<FF03>and wake up.", "Veras a tu mama de nuevo, asi que<FF03>despierta ya."),
    ("Maki. Please wake up. Please", "Maki. Despierta, por favor"),
)
repl("e0_02095", ("You're not the only one who suffers from<FF03>having multiple aspects of yourself", "No eres la unica que sufre por<FF03>tener varios aspectos de si misma"))
repl("e0_02096",
    ("Everyone says how elegant and beautiful<FF03>I am, but it's not true at all!", "Todos dicen que soy elegante y bella,<FF03>pero no es cierto!"),
    ("I've always acted like someone I'm not!<FF03>I hate seeing boys talk to other girls", "Siempre actue como quien no soy!<FF03>Odio ver chicos hablar con otras"),
)
repl("e0_02097", ("That's why I always wear a fake smile!<FF03>It was so stifling", "Por eso siempre finjo una sonrisa!<FF03>Era tan asfixiante"))
repl("e0_02098",
    ("I'm no good, am I?", "No sirvo, verdad?"),
    ("But I understand now!", "Pero ahora entiendo!"),
    ("What I really needed are friends I can<FF03>trust! The ones I have with me here", "Lo que necesitaba eran amigos de<FF03>confianza! Los que tengo aqui"),
)
repl("e0_02099", ("I like someone now! You probably like<FF03>him too, Maki", "Me gusta alguien ahora! Quiza a ti<FF03>tambien, Maki"))
repl("e0_02100", ("Please wake up", "Despierta"))
repl("e0_02101", ("I wish I could talk to you again, about<FF03>things like him! Okay? So wake up", "Quisiera hablar contigo otra vez, de<FF03>cosas como el! Si? Despierta"))
repl("e0_02102",
    ("Rise and shine, Maki, and I'll tell you<FF03>the funniest story I know.", "Despierta, Maki, y te cuento<FF03>la historia mas graciosa que se."),
    ("Y'know how they call me Brown? It's a<FF03>nickname I picked up in middle school", "Sabes por que me dicen Brown? Es un<FF03>apodo de la secundaria"),
)
repl("e0_02103", ("People think it's about my brown hair", "Creen que es por mi pelo castano"))
repl("e0_02104", ("But really", "Pero no"))
dump(os.path.join(os.path.dirname(__file__), "e0_c60.json"))
