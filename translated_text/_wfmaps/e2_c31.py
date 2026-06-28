import sys; sys.path.insert(0,"/home/josechavez/persona_es/scripts")
from wf_chunk import put,repl,dump
def docmenu(fee):
    return [(f"My fee is {fee} yen! Well?",f"Cobro {fee} yenes! Bien?"),
     ("Hm! Then let's get you patched up!","Hm! Entonces a curarte!"),
     ("There, that should do it!","Listo, con eso basta!"),
     ("Anything else you need?","Necesitas algo mas?"),
     ("Well, I can't treat patients who can't<FF03>pay! Come back when you have the fee!","No atiendo a quien no puede<FF03>pagar! Vuelve cuando tengas el dinero!"),
     ("I hope you don't run into trouble later<FF03>because you cheaped out on treatment!","Espero que no tengas problemas luego<FF03>por ahorrarte el tratamiento!"),
     ("All right! If anything else comes up,<FF03>I recommend you see me immediately!","Bien! Si surge algo mas,<FF03>te recomiendo verme de inmediato!"),
     ("My time is valuable! If you don't have<FF03>any business here, then take a hike!","Mi tiempo vale! Si no tienes<FF03>nada que hacer aqui, largate!")]
put("e2_01427","<FF02><FF01> <FF1B>Mark<FF03>Maki es heroina local, eh? Que genial.<FF03>No?<FF02><FF01> <FF1B>Nanjo<FF03>")
put("e2_01428","Esto debe ser tedioso para Maki<FF03>ahora que sabe la verdad!<FF02><FF01>  <FF1B>Ayase<FF03>Por que los doctores siempre actuan tan<FF03>creidos?<FF02><FF01><FF1B>Mark<FF03>Olvida mis heridas, necesito pastillas para el cerebro!<FF02><FF01><FF1B>Elly<FF03>Es duro cuando te idolatran!<FF03>Hay mucho que cumplir!<FF02><FF01>   <FF1B>Elly<FF03>Es dificil ser idolatrada asi")
repl("e2_01429",
 ("You end up having to put on an act!","Acabas teniendo que actuar!"),
 ("What's wrong? Hope you're not tired,<FF03>'cause we got a long ways to go!","Que pasa? Espero que no estes cansado,<FF03>nos falta mucho camino!"))
repl("e2_01467",
 ("I suggest gems for obtaining a higher-<FF03>or lower-ranked fusion within an order!","Sugiero gemas para lograr una fusion de<FF03>rango mayor o menor dentro de un orden!"),
 ("As for the other items' effects, you<FF03>should experiment for yourself!","En cuanto a los otros objetos, deberias<FF03>experimentar por ti mismo!"))
repl("e2_01470",
 ("Hi. I'm Trish and this is my fountain<FF03>of healing.","Hola. Soy Trish y esta es mi fuente<FF03>de curacion."),
 ("This world runs on give-and-take. Give<FF03>me money and I'll take away your pain.","El mundo es de toma y daca. Dame<FF03>dinero y te quito el dolor."),
 ("What do you say?","Que dices?"),
 ("Okay.","Bien."),
 ("Umm, with the going rate for healing","Umm, con la tarifa actual de curacion"))
put("e2_01472","<FF02><FF01> <FF1B>Trish<FF03>Seran 3,000 yenes!<FF03>Esta bien, no?<FF02><FF0E> <FF01>  <FF1B>Trish<FF03>Genial. Aqui va.<FF03>Dolor, dolor, vete.<FF02><FF01><FF1B>Trish<FF03>Uf")
repl("e2_01473",
 ("That should do it.<FF03>You're all good to go.","Con eso basta.<FF03>Ya estas listo."),
 ("Need anything else?","Necesitas algo mas?"),
 ("You don't have enough.? Boo to that.<FF03>There's nothing I hate like poor people.","No te alcanza.? Que mal.<FF03>Nada odio mas que a los pobres."),
 ("Come back when your wallet's fuller!<FF03>Bye-bye.","Vuelve con la cartera mas llena!<FF03>Adios."),
 ("Boo to that. You mangy, dirty bum.<FF03>Don't blame me if you wind up dead.","Que mal. Vago sucio y sarnoso.<FF03>No me culpes si acabas muerto."),
 ("Well, come again! I'll be waiting.<FF03>Bye-bye.","Bueno, vuelve! Te espero.<FF03>Adios."),
 ("You called me out for no reason.?<FF03>Boo to that. Get outta here.","Me llamaste sin razon.?<FF03>Que mal. Largate."))
repl("e2_01475",
 ("Are you finished here? Can we leave yet?","Terminaste aqui? Ya podemos irnos?"),
 ("Psychological wounds are difficult to<FF03>treat, since they can't be seen!","Las heridas psicologicas son dificiles<FF03>de tratar, porque no se ven!"),
 ("Oh, I didn't mean anything in particular!<FF03>It just crossed my mind!","Oh, no quise decir nada en particular!<FF03>Solo se me ocurrio!"),
 ("What're we waiting for? Let's get patched<FF03>up and go.","Que esperamos? Curemonos<FF03>y vamos."),
 ("I do want to drive out the demons, but","Si quiero echar a los demonios, pero"))
repl("e2_01476",
 ("I think I'll regret it, just a bit!","Creo que me arrepentire, un poco!"),
 ("When's the time come when I'm considered<FF03>a local hero? No, a national hero.","Cuando me consideraran<FF03>heroe local? No, heroe nacional."),
 ("I just wanna hurry up and get back to<FF03>normal life.","Solo quiero volver pronto a<FF03>la vida normal."),
 ("I want to get this all over with as soon<FF03>as I can!","Quiero terminar con todo esto<FF03>cuanto antes!"),
 ("Don't you have someone waiting for you<FF03>to come home, too?","No tienes a alguien esperando<FF03>que vuelvas a casa tambien?"),
 ("It's dangerous outside, so don't go<FF03>wandering around too much.","Es peligroso afuera, asi que no<FF03>deambules mucho."),
 ("I hope the demons go away soon","Ojala los demonios se vayan pronto"),
 ("Nurse","Enfermera"))
put("e2_01477","<FF02><FF04><FF1B>Doctor<FF03>Aunque, eso podria dejarnos sin<FF03>trabajo! Jaja.<FF02><FF01>   <FF1B>Doctor<FF03>Bien, en que te ayudo?<FF02><FF0E><1100><FF01> <FF1B>Doctor<FF03>Bien")
repl("e2_01479", *docmenu("1,500"))
repl("e2_01481",
 ("Are you finished here? Can we leave yet?","Terminaste aqui? Ya podemos irnos?"),
 ("Psychological wounds are difficult to<FF03>treat, since they can't be seen!","Las heridas psicologicas son dificiles<FF03>de tratar, porque no se ven!"),
 ("Oh, I didn't mean anything in particular!<FF03>It just crossed my mind!","Oh, no quise decir nada en particular!<FF03>Solo se me ocurrio!"),
 ("What're we waiting for? Let's get patched<FF03>up and go.","Que esperamos? Curemonos<FF03>y vamos."),
 ("I want to drive out the demons and return<FF03>this town to normal","Quiero echar a los demonios y volver<FF03>este pueblo a la normalidad"))
put("e2_01482","<FF02><FF01><FF1B>Mark<FF03>Cuando me consideraran<FF03>heroe local? No, heroe nacional.<FF02><FF01><FF1B>Ayase<FF03>Solo quiero volver pronto a<FF03>la vida normal.<FF02><FF01> <FF1B>Reiji<FF03>Quiero terminar con todo esto<FF03>cuanto antes!<FF02><FF04><FF1B>Reiji<FF03>No tienes a alguien esperando<FF03>que vuelvas a casa tambien?<FF02><FF01>   <FF1B>Doctor<FF03>Este era un pueblito maravilloso,<FF03>pero ahora esta devastado!<FF02><FF04><FF1B>Doctor<FF03>Pero basta de eso")
repl("e2_01483",
 ("How are you feeling?","Como te sientes?"),
 ("This town's going entirely to pieces!<FF03>I'm not holding out much hope!","Este pueblo se cae a pedazos!<FF03>No tengo muchas esperanzas!"),
 ("I even find myself sometimes wishing<FF03>it would all disappear!","A veces hasta deseo<FF03>que todo desaparezca!"),
 ("Nurse","Enfermera"))
put("e2_01486"," de Lovecraft, creo!<FF02><FF01>  <FF1B>Maki<FF03>El Espejo Expel esta aqui, no?<FF02><FF01><FF1B>Nanjo<FF03>No confias en Tsutomu? Parece mucho<FF03>mas confiable que el que conocemos!<FF02><FF01> <FF1B>Nanjo<FF03>Dios mio, que peste")
put("e2_01487","<FF02><FF01> <FF1B>Nanjo<FF03>Asi es! El Espejo Expel estaba<FF03>exhibido aqui!<FF02><FF01><FF1B>Mark<FF03>Siento que estamos de excursion.<FF03>Algo es diferente en este lugar?<FF02><FF01>  <FF1B>Mark<FF03>Que dijo ese monstruo? <0028>Yog Sothuh<0028>?<FF03>Que fue eso?<FF02><FF01>   <FF1B>Mark<FF03>Ese tipo sospechoso otra vez")
put("e2_01488","<FF02><FF01>   <FF1B>Elly<FF03>Ojala tuvieran mas exhibiciones sobre<FF03>demonios aqui!<FF02><FF01><FF1B>Elly<FF03>Ese demonio que vimos fue maravilloso. Me<FF03>conmovio mucho verlo")
put("e2_01489","<FF02><FF01><FF1B>Elly<FF03>Podemos pelear al demonio del metro si<FF03>tenemos el Espejo Expel, verdad?<FF02><FF01>  <FF1B>Mark<FF03>Esto no es lo mio!<FF02><FF01>  <FF1B>Mark<FF03>Vamos a pelear ese demonio?<FF03>En serio")
put("e2_01490","<FF02><FF01><FF1B>Mark<FF03>Una vez con el Espejo Expel, podemos")
put("e2_01491","<FF03>pelear ese demonio")
repl("e2_01497",
 ("Young ones","Jovenes"))
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c31.json")
