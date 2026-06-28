import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_00581", ("shut up.", "callate."))
repl("e0_00582",
    ("Why're you here?", "Por que estas aqui?"),
    ("It must've been a long trip", "Debio ser un viaje largo"),
)
repl("e0_00583",
    ("Are you<FF03>feelin' okay.?", "Estas<FF03>bien.?"),
    ("C'mon, Masao, why're you joking around<FF03>like that? I'm totally fine.", "Vamos, Masao, por que bromeas<FF03>asi? Estoy perfecta."),
    ("S-So I see", "Y-Ya veo"),
)
repl("e0_00584", ("Okay, then! Anyways--", "Bien! En fin--"))
repl("e0_00585",
    ("<FF1B>Lieutenant<FF03>", "<FF1B>Teniente<FF03>"),
    ("Who's there.?", "Quien va.?"),
)
repl("e0_00586",
    ("<FF1B>Policeman<FF03>", "<FF1B>Policia<FF03>"),
    ("You're not allowed out on<FF03>your owwwn!", "No puedes salir<FF03>soloooo!"),
    ("It's against the ruuules!", "Va contra las reglaaas!"),
    ("Look, Baldy, this is goin' too damn far,<FF03>even for a joke! I haven't done anything.",
     "Mira, Calvo, esto ya es demasiado,<FF03>aun de broma! No hice nada."),
    ("Wait", "Espera"),
)
repl("e0_00587", ("something's wrong!<FF03>Masao, they're", "algo anda mal!<FF03>Masao, ellos"))
repl("e0_00588",
    ("<FF1B>Policeman<FF03>", "<FF1B>Policia<FF03>"),
    ("<FF1B>Lieutenant<FF03>", "<FF1B>Teniente<FF03>"),
    ("Lieutenaaant, this kid broke out of<FF03>priiison!", "Tenienteee, este chico escapo<FF03>de prisioon!"),
    ("I seeee", "Ya veooo"),
)
repl("e0_00589",
    ("Vicious criminals must be<FF03>execuuuted!", "Los criminales deben ser<FF03>ejecutadooos!"),
    ("Ugh, that stink", "Ugh, que peste"),
)
repl("e0_00591",
    ("<FF1B>Demon policeman<FF03>", "<FF1B>Policia demonio<FF03>"),
    ("<FF1B>Demon lieutenant<FF03>", "<FF1B>Teniente demonio<FF03>"),
    ("Execute, execute, ex, ec, ute,<FF03>eheheheeeexecuuuute.", "Ejecutar, ejecutar, eje, cu, tar,<FF03>jejejeeeejecutaaar."),
    ("That's riiiight. Men", "Asi eees. Hombres"),
)
repl("e0_00592",
    ("kiiill theeeem.", "mateeenlooos."),
    ("Used the <FF19><0300><FF18><0500>Prison Key<FF18> ", "Usaste la <FF19><0300><FF18><0500>Prison Key<FF18> "),
)
repl("e0_00597", ("Alright, lemme explain it to you!<FF03>Listen up", "Bien, dejame explicarte!<FF03>Escucha"))
repl("e0_00598",
    ("Awesome. I really am a superhero.", "Genial. De verdad soy un superheroe."),
    ("Ever since I was a kid", "Desde nino"),
)
repl("e0_00599", ("I suspected<FF03>something was different about me", "Sospechaba<FF03>que algo era distinto en mi"))
repl("e0_00600", ("I don't think he really gets it", "No creo que de verdad entienda"))
repl("e0_00601",
    ("Oh well!", "En fin!"),
    ("Anyways, I'm comin' too, <FF07>!", "En fin, yo tambien voy, <FF07>!"),
    ("I'd be nervous for you guys if you were<FF03>on your own!", "Me preocuparian si fueran<FF03>solos!"),
    ("We could say the same about you!", "Lo mismo decimos de ti!"),
    ("You should leave the security card in<FF03><FF07>'s care, Masao!", "Deja la security card al<FF03>cuidado de <FF07>, Masao!"),
    ("Alright", "Bien"),
)
repl("e0_00602", ("Here's the security card, man! Better<FF03>not lose that thing", "Aqui la security card! Mejor<FF03>no la pierdas"))
repl("e0_00603",
    ("We have a firearm for you, Masao!<FF03>Just don't shoot us by mistake!", "Tenemos un arma para ti, Masao!<FF03>No nos dispares por error!"),
    ("Hey, hey, think I should come with<FF03>you guys?", "Oye, oye, deberia ir<FF03>con ustedes?"),
    ("Without me, you fools don't have any<FF03>star power, y'know?", "Sin mi, tontos no tienen<FF03>estrella, sabes?"),
    ("You guys need me to whip you into<FF03>shape. How about it, <FF07>.?", "Me necesitan para ponerlos en<FF03>forma. Que dices, <FF07>.?"),
)
repl("e0_00604",
    ("It's your call, <FF07>!", "Tu decides, <FF07>!"),
    ("Are you certain that you want to bring<FF03>Hidehiko along?", "Seguro que quieres traer<FF03>a Hidehiko?"),
    ("Are you certain that you don't want to<FF03>bring Hidehiko along?", "Seguro que no quieres traer<FF03>a Hidehiko?"),
    ("Great. I'm down--not like I have a<FF03>choice. Hahahahaha.", "Genial. Me apunto--no es que tenga<FF03>opcion. Jajajaja."),
    ("Then here's a firearm for you, too,<FF03>Hidehiko! Don't be careless with it!", "Entonces un arma para ti tambien,<FF03>Hidehiko! No seas descuidado!"),
)
repl("e0_00605", ("What's that look for", "Por que esa cara"))
repl("e0_00606", ("Oh? Is that", "Oh? Es eso"))
repl("e0_00607",
    ("Really? You're sure<FF03>you won't regret it?", "De veras? Seguro<FF03>que no te arrepentiras?"),
    ("Alright", "Bien"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c16.json"))
