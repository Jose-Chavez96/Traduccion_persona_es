import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_02105",
    ("It's 'cause I crapped myself!", "Es porque me cague!"),
    ("See? Isn't that funny? Man, it was<FF03>embarrassing", "Ves? No es gracioso? Fue<FF03>vergonzoso"),
)
repl("e0_02106", ("I spent most of middle school as the<FF03>butt of every joke in the class", "Pase la secundaria siendo el<FF03>blanco de toda burla"))
repl("e0_02107",
    ("I was sick of myself! I came to Hermelin<FF03>'cause I couldn't take the local schools!", "Me harte de mi! Vine a Hermelin<FF03>porque no soportaba las de aqui!"),
    ("So when I got to high school, I did my<FF03>best to act like Mr! Cool", "Asi que en la prepa, me<FF03>esforce por hacerme el Sr! Genial"),
)
repl("e0_02108",
    ("But I was lying to myself all this time!", "Pero me mentia todo este tiempo!"),
    ("No more, though! I realized how dumb I<FF03>was being from watching you", "Ya no! Vi lo tonto que era<FF03>al verte a ti"),
)
repl("e0_02109", ("So there it is! Now c'mon", "Ahi esta! Ahora vamos"))
repl("e0_02110", ("give us<FF03>a smile", "danos<FF03>sonrisa"))
repl("e0_02111",
    ("Wakey wakey, Maki.", "Despierta, Maki."),
    ("I still have your handkerchief! Anything<FF03>you wanna talk about, I'll listen", "Aun tengo tu panuelo! Lo que<FF03>quieras hablar, te escucho"),
)
repl("e0_02112", ("I get how you feel! I used to think the<FF03>same way", "Te entiendo! Yo pensaba<FF03>igual"))
repl("e0_02113", ("I would like, wish there would be no<FF03>future", "Yo deseaba que no hubiera<FF03>futuro"))
repl("e0_02114", ("I worry about the future a lot! I think<FF03>that's why I party so hard", "Me preocupa mucho el futuro! Creo<FF03>que por eso parrandeo tanto"))
repl("e0_02115",
    ("'Cause the future's too depressing to<FF03>think about, right?", "Porque el futuro es muy deprimente<FF03>para pensarlo, no?"),
    ("So I made up my mind to live only for<FF03>now, and ran away from the future", "Asi que decidi vivir solo<FF03>el ahora, y hui del futuro"),
)
repl("e0_02116",
    ("But it doesn't work like that!", "Pero asi no funciona!"),
    ("It's my future! I have to come up with<FF03>it myself", "Es mi futuro! Debo crearlo<FF03>yo misma"),
)
repl("e0_02117",
    ("So I've made my choice!", "Asi que ya elegi!"),
    ("I'm gonna snag a great guy so I can live<FF03>on easy street. So, Maki", "Atrapare un buen tipo para vivir<FF03>comoda. Asi que, Maki"),
)
repl("e0_02118", ("I wanna hear your dreams for the future,<FF03>too! Please, Maki", "Quiero oir tus suenos del futuro<FF03>tambien! Por favor, Maki"))
repl("e0_02120",
    ("A <FF18><0700>shard of the Chaos Mirror<FF18>  is on<FF03>the floor!", "Un <FF18><0700>shard of the Chaos Mirror<FF18>  en<FF03>el piso!"),
    ("Pick it up?", "Recogerlo?"),
    ("Is that a shard of Kandori's mirror.?", "Es un fragmento del espejo de Kandori.?"),
    ("This size and shape", "Este tamano y forma"),
)
repl("e0_02121",
    ("I think it may<FF03>fit Maki's compact.", "Creo que encaja<FF03>en la polvera de Maki."),
    ("Seriously.? Maybe we can use this to<FF03>go back.", "En serio.? Quiza con esto<FF03>volvamos."),
    ("Lemme see that, <FF07>.", "Dejame ver, <FF07>."),
    ("It's a perfect fit.", "Encaja perfecto."),
    ("Obtained <FF19><0300><FF18><0500>Chaos Mirror Shard<FF18> !", "Obtuviste <FF19><0300><FF18><0500>Chaos Mirror Shard<FF18> !"),
    ("The real Maki won't wake up", "La Maki real no despierta"),
)
repl("e0_02122", ("She sleeps as though dead", "Duerme como muerta"))
repl("e0_02123",
    ("Where are you going? Are you going to<FF03>leave Maki this way?", "A donde vas? Vas a dejar<FF03>a Maki asi?"),
    ("Obtained <FF19><0300><FF18><0500>Green Compact<FF18> !", "Obtuviste <FF19><0300><FF18><0500>Green Compact<FF18> !"),
    ("Obtained <FF19><0300><FF18><0500>Broken Compact<FF18> !", "Obtuviste <FF19><0300><FF18><0500>Broken Compact<FF18> !"),
    ("The Mirror of Chaos is cracked", "El Mirror of Chaos esta agrietado"),
)
repl("e0_02124", ("What could have happened to the town<FF03>inside Maki's heart", "Que habra pasado en el pueblo<FF03>dentro del corazon de Maki"))
repl("e0_02125", ("It's Maki's painting, the <0028>Gate to<FF03>Paradise!<0028> You wonder how she felt when<FF03>she painted this", "Es la pintura de Maki, <0028>Puerta al<FF03>Paraiso!<0028> Te preguntas como se sintio al<FF03>pintarla"))
repl("e0_02126", ("It's a holographic model of the Deva<FF03>System! It seems Maki is connected<FF03>directly to the machine!", "Es un modelo holografico del Deva<FF03>System! Maki parece conectada<FF03>directo a la maquina!"))
repl("e0_02190",
    ("Huh?", "Eh?"),
    ("I get it", "Ya veo"),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c61.json"))
