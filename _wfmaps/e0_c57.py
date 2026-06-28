import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_02000",
    ("Are they all her?", "Son todas ella?"),
    ("Three's", "Tres"),
)
repl("e0_02001", ("three of her", "tres de ella"))
repl("e0_02002", ("Jesus Christ!<FF03>They're all Maki", "Cielos!<FF03>Todas son Maki"))
repl("e0_02003", ("There's three Makis? No way", "Hay tres Makis? Imposible"))
repl("e0_02004",
    ("This is<FF03>some sick joke, right?", "Es una<FF03>broma enferma, no?"),
    ("They're all Maki? Seriously?<FF03>That's just", "Todas son Maki? En serio?<FF03>Eso es"),
)
repl("e0_02005", ("No", "No"))
repl("e0_02006", ("Don't come near me", "No te acerques"))
repl("e0_02007",
    ("Don't look<FF03>at me.", "No me<FF03>mires."),
    ("Calm down, Maki. This has to be some<FF03>kinda mistake", "Calma, Maki. Esto debe ser<FF03>un error"),
)
repl("e0_02008",
    ("right?", "no?"),
    ("Stop saying that. That's a lie.<FF03>This is me, I can tell.", "Deja de decir eso. Es mentira.<FF03>Esta soy yo, lo se."),
    ("I messed up the town and made everyone<FF03>suffer. I did that", "Arruine el pueblo e hice sufrir<FF03>a todos. Yo lo hice"),
)
repl("e0_02009",
    ("Don't take it so hard! He was using you.", "No te culpes! El te usaba."),
    ("Calm down, Maki.", "Calma, Maki."),
    ("You were being used", "Te estaban usando"),
)
repl("e0_02010",
    ("There's no need<FF03>to let it get to you, okay?", "No hace falta<FF03>que te afecte, si?"),
    ("Calm down. You were being used, and it<FF03>sucks, but that's all it was!", "Calma. Te usaron, y es<FF03>feo, pero eso es todo!"),
    ("Okay? C'mon, get over here!", "Si? Vamos, ven aca!"),
    ("Maki. You don't have to take it so hard.<FF03>It was all Kandori's fault anyways.", "Maki. No te culpes tanto.<FF03>Fue culpa de Kandori igual."),
)
repl("e0_02012", ("Please don't be nice to me", "No me trates bien"))
repl("e0_02013",
    ("I understand everything now!", "Ahora entiendo todo!"),
    ("I was jealous of everyone", "Tenia envidia de todos"),
)
repl("e0_02014", ("Wearing cute clothes, walking<FF03>around town", "Usar ropa linda, pasear<FF03>por el pueblo"))
repl("e0_02015", ("Gossiping about each other's<FF03>boyfriends", "Chismear sobre los<FF03>novios de cada quien"))
repl("e0_02016", ("Laughing and joking", "Reir y bromear"))
repl("e0_02017", ("I envied everyone who went to school<FF03>and had fun with their friends", "Envidiaba a todos los que iban a clase<FF03>y se divertian con amigos"))
repl("e0_02018", ("I wished", "Desee"))
repl("e0_02019", ("that school and the town<FF03>would all be swallowed up", "que la escuela y el pueblo<FF03>fueran tragados"))
put("e0_02020", O("e0_02020"))  # solo nombre (Maki)
repl("e0_02021", ("Even if I wanted to do something about it,<FF03>I couldn't", "Aunque quisiera hacer algo,<FF03>no podia"))
repl("e0_02022", ("I cried and cried", "Llore y llore"))
dump(os.path.join(os.path.dirname(__file__), "e0_c57.json"))
