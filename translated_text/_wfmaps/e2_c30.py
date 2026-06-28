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
put("e2_01394"," Muy extrano!<FF02><FF01>  <FF1B>Ayase<FF03>Tienen pistolas con, o sea, lindos<FF03>patrones de flores?<FF02><FF01><FF1B>Mark<FF03>Japon estaria perdido si empezaran a vender<FF03>armas en tiendas de verdad!<FF02><FF01>   <FF1B>Elly<FF03>No importa cuantas veces venga,<FF03>no me acostumbro a esta tienda!<FF02><FF01>  <FF1B>Elly<FF03>Esta tienda me sigue pareciendo rara<FF03>sin importar cuanto vengamos!<FF02><FF01> <FF1B>Reiji<FF03>Compra algo si vas a hacerlo!")
put("e2_01398"," Amo las gemas mas que<FF03>nada en este mundo!<FF02><FF04><FF1B>Khamenturun<FF03>Cambio mis tesoros especiales por<FF03>tus gemas! Quieres comerciar?<FF02><FF01>   <FF1B>Vecino<FF03>Este pueblo era tan agradable")
put("e2_01399","<FF03>Que paso? Es todo una pesadilla?<FF02><FF01> <FF1B>Maki<FF03>Un pueblo agradable, eh")
put("e2_01400"," Tambien debo<FF03>disculparme con la gente del pueblo!<FF02><FF01>   <FF1B>Mark<FF03>Esta sigue siendo una tienda sospechosa!<FF02><FF01> <FF1B>Nanjo<FF03>Noto que las tiendas comunes tienen<FF03>cosas exoticas")
put("e2_01401"," Este pueblo es la excepcion!<FF02><FF01>  <FF1B>Ayase<FF03>Tengo mucha hambre!<FF02><FF04><FF1B>Ayase<FF03>Pero lo aguantare! Digo, Maki esta<FF03>pasando algo mucho peor!<FF02><FF01>   <FF1B>Mark<FF03>Estoy harto de caminar! Aunque, no es<FF03>momento de quejarse, no?<FF02><FF01>  <FF1B>Elly<FF03>Terminaste de comprar?<FF02><FF01>  <FF1B>Elly<FF03>Ya acabaste tus compras?<FF02><FF01><FF1B>Reiji<FF03>Cuanto mas vas a tardar?")
repl("e2_01403",
 ("Yikes, things are getting crazy! Well,<FF03>my store will stay open!","Vaya, esto se pone loco! Bueno,<FF03>mi tienda seguira abierta!"),
 ("I feel like someone's going around and<FF03>destroying this town","Siento que alguien anda<FF03>destruyendo este pueblo"),
 ("Clerk","Mozo"),
 ("Area man","Vecino"))
put("e2_01404","<FF02><FF01>  <FF1B>Maki<FF03>Perdon, Sr! Tadashi")
put("e2_01405","<FF02><FF01>   <FF1B>Mark<FF03>Esta cancion siempre suena cuando venimos!<FF03>Me esta volviendo loco!<FF02><FF01>  <FF1B>Nanjo<FF03>Ja. Al fin me acostumbre. Adelante,<FF03>intenta lavarme el cerebro--es inutil.<FF02><FF01><FF1B>Ayase<FF03>Oooooh, este panal tiene ranitas<FF03>lindas. Es taaan tierno.<FF02><FF01>  <FF1B>Mark<FF03>Oye, crees que aqui haya pociones<FF03>de amor.?<FF02><FF01>   <FF1B>Elly<FF03>No tiene este lugar medicinas normales<FF03>para cosas diarias?<FF02><FF01><FF1B>Elly<FF03>Esta tienda no tiene medicina regular<FF03>para situaciones diarias?<FF02><FF01> <FF1B>Reiji<FF03>Que? Es raro que mire<FF03>cosas de bebe?<FF02><FF01>  <FF1B>Mozo<FF03>Hm? Oye, el mostrador esta aqui")
put("e2_01408","<FF02><FF01><FF1B>Maki<FF03>Tal como era")
put("e2_01409"," Pero por bonito<FF03>que fuera, seguia siendo falso!<FF02><FF01><FF1B>Mark<FF03>La verdadera vendedora se desmayaria<FF03>si viera esto!<FF02><FF01><FF1B>Nanjo<FF03>Podriamos comprar por mucho<FF03>tiempo si insistimos en lo mejor")
put("e2_01410","<FF02><FF04><FF1B>Nanjo<FF03>Pero al menos deberiamos llevar<FF03>lo minimo necesario!<FF02><FF01>   <FF1B>Ayase<FF03>No tienen armadura con, o sea,<FF03>animales y eso?<FF02><FF01> <FF1B>Mark<FF03>Lo que necesito es armadura que se<FF03>vea ruda")
put("e2_01411"," La tienen aqui?<FF02><FF01> <FF1B>Elly<FF03>Supongo que no puedo quejarme si nos<FF03>mantiene vivos")
put("e2_01412","<FF02><FF04><FF1B>Elly<FF03>Pero esto no es de mi gusto!<FF02><FF01><FF1B>Elly<FF03>Supongo que no debo quejarme, ya que<FF03>nos protege del dano")
put("e2_01413","<FF02><FF04><FF1B>Elly<FF03>Pero no puedo evitar sentir que esto<FF03>choca un poco con mi estilo!<FF02><FF01><FF1B>Reiji<FF03>Compra algo si vas a hacerlo!")
put("e2_01416"," No puedo reabastecer mi mercancia.<FF02><FF01>   <FF1B>Nina<FF03>Siempre tuve la sensacion de que algo<FF03>no estaba bien con este pueblo!<FF02><FF04><FF1B>Nina<FF03>Quiza es natural que cosas raras<FF03>asi pasen aqui!<FF02><FF01>   <FF1B>Maki<FF03>Hmm")
put("e2_01417"," Tiene razon! Si no fuera natural<FF03>que pasaran cosas raras aqui")
put("e2_01418","<FF02><FF04><FF1B>Maki<FF03>No habria entendido nada!<FF02><FF01>   <FF1B>Mark<FF03>Vamos al bosque.<FF02><FF01><FF1B>Mark<FF03>Vamos al templo.<FF02><FF01><FF1B>Mark<FF03>Vamos a la escuela.<FF02><FF01><FF1B>Nanjo<FF03>Reabastecer")
put("e2_01419"," Oye, de donde reabastece este<FF03>pueblo sus suministros?<FF02><FF04><FF1B>Nanjo<FF03>Aunque, es inutil darle vueltas a<FF03>cosas que no necesariamente tienen sentido!<FF02><FF01><FF1B>Ayase<FF03>Tengo muuucha hambre. Solo debo<FF03>aguantarme, supongo")
put("e2_01420","<FF02><FF01> <FF1B>Mark<FF03>Aqui exageran un poco con lo de dar<FF03>gracias, no? Jijiji.<FF02><FF01>   <FF1B>Elly<FF03>Hay que apurarnos, <FF07>!<FF02><FF01><FF1B>Elly<FF03>No tenemos mucho tiempo que perder,<FF03><FF07>!<FF02><FF01><FF1B>Reiji<FF03>Estoy seguro que no teniamos<FF03>nada que hacer aqui!<FF02><FF04><FF1B>Reiji<FF03>En serio")
put("e2_01421"," Eres un valiente<FF03>o un idiota! No te entiendo!<FF02><FF04><FF1B>Reiji<FF03>Aunque, lo mires como lo mires,<FF03>eres un tipo interesante!")
repl("e2_01425", *(docmenu("1,500")+[
 ("Don't let Maki get hurt, got it? She's<FF03>like a local hero here.","No dejes que lastimen a Maki, si? Es<FF03>como una heroina local aqui."),
 ("Nurse","Enfermera"),
 ("Oh, you go to the same school as<FF03>Maki Sonomura!","Oh, vas a la misma escuela que<FF03>Maki Sonomura!"),
 ("Huh? You're friends with her.? Oooh,<FF03>I'm so jealous.","Eh? Eres su amigo.? Oooh,<FF03>que envidia."),
 ("Hey, could you get me her autograph?","Oye, me consigues su autografo?"),
 ("I'm no hero or anything","No soy heroina ni nada")]))
put("e2_01426"," Solo hacen<FF03>creer eso a todos")
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c30.json")
