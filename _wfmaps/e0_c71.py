import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump, O, put

repl("e0_02511",
    ("Let's go back to the others.", "Volvamos con los demas."),
    ("Obtained <FF19><0300><FF18><0500>Blue Compact<FF18> !", "Obtuviste <FF19><0300><FF18><0500>Blue Compact<FF18> !"),
)
repl("e0_02516",
    ("Sorry to keep you all waiting.", "Perdon por la espera."),
    ("'Bout time. I was getting tired of<FF03>sitting around!", "Ya era hora. Me cansaba de<FF03>estar sentado!"),
    ("It seems to have gone well, mm?", "Parece que salio bien, mm?"),
    ("Now then, let's head to the school<FF03>and meet this Pandora!", "Ahora, vamos a la escuela<FF03>a ver a Pandora!"),
    ("They seem to have been pretty bored<FF03>while we were gone", "Parece que se aburrieron<FF03>mientras no estabamos"),
)
repl("e0_02517",
    ("Yo <FF07>, you didn't try anything<FF03>funny, did you?", "Oye <FF07>, no intentaste nada<FF03>raro, verdad?"),
    ("What's the matter? Did something happen<FF03>inside?", "Que pasa? Paso algo<FF03>dentro?"),
    ("Looks like you made it back in one<FF03>piece! When this is all over", "Parece que volviste de una<FF03>pieza! Cuando todo acabe"),
)
repl("e0_02518",
    ("What would you say to some sparring<FF03>to see who's stronger? You up for it?", "Que tal un combate<FF03>para ver quien es mas fuerte? Te animas?"),
    ("<FF07>. I'm so glad you're back.<FF03>You're not hurt anywhere, are you?", "<FF07>. Que bueno que volviste.<FF03>No estas herido, verdad?"),
    ("Oh, <FF07>. It's good to have you<FF03>back", "Oh, <FF07>. Que bueno tenerte<FF03>de vuelta"),
)
repl("e0_02519",
    ("Are you hurt anywhere?", "Estas herido?"),
    ("Tch", "Tch"),
)
repl("e0_02520",
    ("You're pretty tough!", "Eres bien duro!"),
    ("I kinda thought you'd eat it! Then I<FF03>could rush in and rescue the princess.", "Crei que caerias! Asi yo<FF03>rescataria a la princesa."),
    ("Yeesh, <FF07>, you were in there so<FF03>long I thought you'd died!", "Cielos, <FF07>, tardaste tanto<FF03>que te crei muerto!"),
    ("Yeesh, <FF08>, you were in there so<FF03>long I thought you'd died!", "Cielos, <FF08>, tardaste tanto<FF03>que te crei muerto!"),
    ("There isn't much time until this world<FF03>vanishes completely! You must hurry!", "No queda mucho antes de que el mundo<FF03>desaparezca! Apurense!"),
)
repl("e0_02541",
    ("Chisato. Yosuke. I'm so glad to see you<FF03>both safe and sound.", "Chisato. Yosuke. Que alegria verlos<FF03>sanos y salvos."),
    ("Maki. Oh good, you're safe, too.", "Maki. Que bueno, tu tambien estas bien."),
    ("Hey Yosuke, what happened here? There's<FF03>no one around but you guys!", "Oye Yosuke, que paso aqui? No hay<FF03>nadie mas que ustedes!"),
    ("I'm not sure", "No estoy seguro"),
)
repl("e0_02542",
    ("It was like this when we got back!<FF03>The east side of town's vanished, too!", "Estaba asi al volver!<FF03>El lado este tambien desaparecio!"),
    ("I want to know what's going on just as<FF03>much as you do.", "Quiero saber que pasa tanto<FF03>como tu."),
    ("This must be the work of Pandora", "Esto debe ser obra de Pandora"),
)
repl("e0_02543",
    ("Pandora?", "Pandora?"),
    ("I'm sorry, both of you", "Perdon, ustedes dos"),
)
repl("e0_02544", ("I'm at fault for all of this", "Todo es culpa mia"))
repl("e0_02545", ("It's the<FF03>real reason behind everything", "Es la<FF03>verdadera causa de todo"))
repl("e0_02547", ("So that's it", "Es eso"))
repl("e0_02548",
    ("I promise I'll return everyone to their<FF03>original world!", "Prometo devolver a todos a su<FF03>mundo original!"),
    ("I know there's no forgiving me for what<FF03>I did", "Se que no hay perdon por lo<FF03>que hice"),
)
repl("e0_02549",
    ("but I'm really, really sorry!", "pero lo siento de verdad!"),
    ("If you want to hit me, Chisato, I'll<FF03>understand! Go right ahead!", "Si quieres pegarme, Chisato,<FF03>lo entendere! Adelante!"),
    ("You're such an idiot, Maki.", "Que tonta eres, Maki."),
    ("You're just as thick as you've always<FF03>been", "Eres tan terca como<FF03>siempre"),
)
repl("e0_02550", ("Hey, Chisato, c'mon", "Oye, Chisato, vamos"))
repl("e0_02551",
    ("It's me who needs to apologize!", "Yo soy la que debe disculparse!"),
    ("You called me to this world because you<FF03>thought of me as your best friend, right?", "Me trajiste a este mundo porque<FF03>me veias como tu mejor amiga, no?"),
    ("And I", "Y yo"),
)
repl("e0_02552", ("I betrayed you", "te traicione"))
repl("e0_02553", ("You've got it backwards, Maki! It's me<FF03>who needs your forgiveness", "Lo tienes al reves, Maki! Soy yo<FF03>quien necesita tu perdon"))
put("e0_02554", O("e0_02554"))  # solo nombre (Chisato)
repl("e0_02556",
    ("Now go on! We'll wait here so we don't<FF03>get in your way!", "Ve! Esperaremos aqui para no<FF03>estorbar!"),
    ("Once things settle down", "Cuando todo se calme"),
)
repl("e0_02557",
    ("let's all go<FF03>to an amusement park together.", "vamos todos<FF03>a un parque de diversiones."),
    ("Sound good?", "Te parece?"),
)
repl("e0_02558", ("An amusement park, huh? Heheh", "Un parque, eh? Jeje"))
dump(os.path.join(os.path.dirname(__file__), "e0_c71.json"))
