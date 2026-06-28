import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_00828", ("Ungh", "Agh"))
repl("e0_00829", ("Where am I", "En donde"))
repl("e0_00830",
    ("Oh, <FF07>! You're all right!", "Oh, <FF07>! Estas bien!"),
    ("Owwww", "Ayyy"),
)
repl("e0_00832",
    ("Y-Yes. We're alive, <FF08>.", "S-Si. Vivos, <FF08>."),
    ("Go me. I'm the luckiest.", "Que suerte la mia."),
)
repl("e0_00833", ("Where am I? Ah, <FF07>!<FF03>Are you hurt anywhere?", "Donde estoy? Ah, <FF07>!<FF03>Estas herido?"))
repl("e0_00834",
    ("Owww. I've had it. I'm going home.<FF03>Like, why is this happening to me.?", "Ayy. Ya basta. Me voy a casa.<FF03>Por que me pasa esto.?"),
    ("Looks like everyone's unhurt!<FF03>We certainly have the devil's luck!", "Parece que nadie esta herido!<FF03>Tenemos suerte del diablo!"),
)
repl("e0_00835", ("This is our school's gym! But it's<FF03>the one from six months ago", "Es el gimnasio de la escuela! Pero el<FF03>de hace seis meses"))
repl("e0_00836", ("Hey", "Oye"))
repl("e0_00837", ("is this the gym.? But it's the<FF03>old one from six months ago", "es el gimnasio.? Pero el<FF03>viejo de hace seis meses"))
repl("e0_00838", ("Hey, uh", "Oye, eh"))
repl("e0_00839",
    ("This is the gym, right?", "Es el gimnasio, no?"),
    ("Didn't they tear this one down six<FF03>months ago", "No demolieron este hace seis<FF03>meses"),
)
repl("e0_00841", ("We've gone back", "Retrocedimos"))
repl("e0_00842",
    ("Gone back? To six months ago.?<FF03>C'mon, Maki, snap out of it.", "Retroceder? A hace seis meses.?<FF03>Vamos, Maki, reacciona."),
    ("You mean a time slip? That's rather<FF03>different than what your mother said!", "Un salto en el tiempo? Eso es<FF03>distinto a lo que dijo tu madre!"),
)
repl("e0_00843",
    ("I've told you before, I don't have<FF03>a real mom!", "Ya te dije, no tengo<FF03>una madre real!"),
    ("I never thought the stuff Yosuke was<FF03>saying was", "Nunca crei que lo que decia<FF03>Yosuke fuera"),
)
repl("e0_00844", ("actually true", "cierto"))
repl("e0_00845",
    ("<FF1B>Harried girl<FF03>", "<FF1B>Chica agitada<FF03>"),
    ("Oh. There you are. It's really bad,<FF03>Maki. Yosuke got seriously hurt.", "Oh. Ahi estas. Es muy malo,<FF03>Maki. Yosuke se hirio grave."),
    ("That girl in black came back again", "Esa chica de negro volvio otra vez"),
)
repl("e0_00846",
    ("No way. Th-That's impossible. Yosuke.", "Imposible. E-Eso no puede ser. Yosuke."),
    ("H-Hey. Maki.", "O-Oye. Maki."),
    ("Could this <0028>Yosuke<0028> be Yosuke Naito?", "Sera este <0028>Yosuke<0028> Yosuke Naito?"),
    ("As I recall, he went missing along with<FF03>Chisato Kasai roughly two months ago!", "Si recuerdo, desaparecio con<FF03>Chisato Kasai hace dos meses!"),
    ("Y'think <0028>Yosuke<0028> is Yosuke Naito?", "Crees que <0028>Yosuke<0028> es Yosuke Naito?"),
    ("He ran away with his girlfriend Chisato<FF03>two months back, didn't he?", "Huyo con su novia Chisato<FF03>hace dos meses, no?"),
    ("Could <0028>Yosuke<0028> be that guy Yosuke Naito?", "Sera <0028>Yosuke<0028> ese Yosuke Naito?"),
    ("Didn't he, like, run off with Chisato<FF03>a couple months ago?", "No huyo con Chisato<FF03>hace unos meses?"),
)
repl("e0_00847",
    ("That dolt! I can't believe she took<FF03>off on her own at a time like this!", "Que tonta! No creo que se fuera<FF03>sola en un momento asi!"),
    ("Come, <FF07>! We'd better go<FF03>after Maki!", "Ven, <FF07>! Mejor vamos<FF03>tras Maki!"),
)
repl("e0_00848",
    ("<FF07>! Don't you think Maki is<FF03>acting oddly for an amnesia victim?", "<FF07>! No crees que Maki actua<FF03>raro para tener amnesia?"),
    ("Is this really six months ago? That girl<FF03>did come here looking for Maki", "De verdad es hace seis meses? Esa chica<FF03>vino buscando a Maki"),
)
repl("e0_00849",
    ("But Maki was hospitalized six months<FF03>ago as well!", "Pero Maki estaba internada hace<FF03>seis meses!"),
    ("Yosuke, huh", "Yosuke, eh"),
)
repl("e0_00851",
    ("Oh, uh, what's up, <FF07>?", "Oh, que hay, <FF07>?"),
    ("A time slip", "Salto temporal"),
)
repl("e0_00852",
    ("Do you think it's true,<FF03><FF07>?", "Crees que es verdad,<FF03><FF07>?"),
    ("Something tells me that isn't the<FF03>case here!", "Algo me dice que no es<FF03>el caso aqui!"),
    ("Is this place really our school?<FF03>Doesn't it look like somewhere else?", "De verdad es nuestra escuela?<FF03>No parece otro lugar?"),
    ("Oh, duh. It's all a dream. Of course.<FF03>Hahaha", "Oh, claro. Es un sueno. Obvio.<FF03>Jaja"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c23.json"))
