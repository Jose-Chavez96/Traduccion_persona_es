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
put("e2_01207"," <FF05><3000>Encaja bien<FF03>en este pueblo sin ley!<FF02><FF01>  <FF1B>Mark<FF03>Que bueno ver que el doctor no ha<FF03>cambiado nada!<FF02><FF01>   <FF1B>Elly<FF03>Me alivia que el doctor sea igual<FF03>que siempre!<FF02><FF01>   <FF1B>Mark<FF03>Asi que el doc sigue igual")
put("e2_01208","<FF02><FF04><FF1B>Mark<FF03>Me preocupaba que hacer si resultaba<FF03>ser un pelon con parche en el ojo.<FF02><FF01> <FF1B>Ayase<FF03>El es")
put("e2_01209"," <FF05><2000>No nos va a poner inyecciones,<FF03>verdad")
put("e2_01210","<FF02><FF01>  <FF1B>Reiji<FF03>Eh! Esperaba que el doctor fuera")
repl("e2_01211",
 ("stranger, I guess!","mas raro, supongo!"),
 ("The reason I'm so happy is all because<FF03>of the Harem Queen!","Soy tan feliz todo gracias a<FF03>la Reina del Haren!"),
 ("Let's all give thanks to the Queen.<FF03>Hooray for the Queen.","Demos gracias a la Reina.<FF03>Viva la Reina."),
 ("It was never the Queen who made me happy.","Nunca fue la Reina quien me hizo feliz."),
 ("But now who am I supposed to thank?","Pero ahora a quien le doy gracias?"),
 ("What, did you catch a cold? Then go<FF03>sleep it off.","Que, te resfriaste? Pues ve<FF03>a dormirlo."),
 ("Now, what can I do for you?","Bien, en que te ayudo?"),
 ("Alright","Bien"),
 ("Nurse","Enfermera"))
repl("e2_01213", *docmenu("1,500"))
put("e2_01216","<FF02><FF01>  <FF1B>Nanjo<FF03>Este mercado parece carecer de tiendas normales!<FF02><FF01>  <FF1B>Mark<FF03>Supongo que el Sennen Mannen-Do de aqui<FF03>no vende dulces!<FF02><FF01>  <FF1B>Elly<FF03>Que exotico. Que tienda tan maravillosa.<FF02><FF01> <FF1B>Mark<FF03>Este jarron es lindo! Oye <FF08>,<FF03>me lo compras de regalo?<FF02><FF01><FF1B>Ayase<FF03>Hablaste con los mozos de aqui?<FF03>Su maquillaje es muy raro.<FF02><FF01>   <FF1B>Reiji<FF03>")
put("e2_01217","Este lugar esta embrujado?<FF02><FF01>  <FF1B>Turunkhamen<FF03>Jojojo")
put("e2_01219"," Amo las gemas mas que<FF03>nada en este mundo!<FF02><FF04><FF1B>Khamenturun<FF03>Cambio mis tesoros especiales por<FF03>tus gemas! Quieres comerciar?<FF02><FF01>   <FF1B>Cliente<FF03>Si fuera un bello joven que pareciera<FF03>un perro callejero, le gustaria a la Reina.<FF02><FF04><FF1B>Cliente<FF03>Asi podria descansar en el palacio<FF03>en vez de vivir en este basurero!<FF02><FF01>   <FF1B>Cliente<FF03>Los hombres del haren tenian que jurar<FF03>lealtad a la Reina, no?<FF02><FF04><FF1B>Cliente<FF03>Que patetico")
repl("e2_01220",
 ("I'm gonna live the way I want, without<FF03>submitting to anyone!","Vivire como quiera, sin<FF03>someterme a nadie!"),
 ("Customer","Cliente"))
repl("e2_01222",
 ("This store's owned by the uncle of a<FF03>friend of mine named Tadashi!","Esta tienda es del tio de un<FF03>amigo mio llamado Tadashi!"),
 ("Tadashi doesn't get along with Tamaki,<FF03>this transfer student!","Tadashi no se lleva con Tamaki,<FF03>la estudiante nueva!"),
 ("He won't speak even one word to her!","No le dice ni una palabra!"))
put("e2_01223","Si quieres recuperar HP usa")
put("e2_01224","<FF02><FF04><FF1B>Nanjo<FF03>Bien. Me rindo. Toma, <FF07>,<FF03>canta tu tambien.<FF02><FF01>   <FF1B>Mark<FF03>El tio de Tadashi, eh? Este lugar no<FF03>se ve tan distinto del nuestro!<FF02><FF01>  <FF1B>Elly<FF03>No quiero ser grosera, pero me pregunto<FF03>que tan eficaz es la medicina aqui")
put("e2_01225","<FF02><FF01>  <FF1B>Mark<FF03>Oye")
put("e2_01226"," El pelo de ese tipo")
put("e2_01227"," No es<FF03>una peluca, verdad?<FF02><FF01> <FF1B>Ayase<FF03>Las cosas de bebe son tan lindas! Solo<FF03>me gusta mirarlas!<FF02><FF01>  <FF1B>Reiji<FF03>Que maniaco")
repl("e2_01228",
 ("Welcome to Satomi Tadashi. Feel free to<FF03>call me <0028>the Satster<0028>.","Bienvenido a Satomi Tadashi. Llamame<FF03><0028>el Satster<0028>."),
 ("Now, on to business.","Bien, al negocio."),
 ("I'm a little down in the dumps today!","Hoy estoy algo decaido!"),
 ("At times like these, all I can do is go<FF03>to the bar and discuss the Queen's art!","En momentos asi, solo puedo ir al<FF03>bar a hablar del arte de la Reina!"),
 ("The Queen's finally gone. This calls for<FF03>a drink or five.","La Reina al fin se fue. Esto pide<FF03>un trago o cinco."),
 ("You can't go in there! Nope, not even<FF03>a peek.","No puedes entrar ahi! No, ni<FF03>una mirada."),
 ("Clerk","Mozo"),
 ("Customer","Cliente"))
put("e2_01232"," A decir verdad,<FF03>yo")
put("e2_01234"," Hace falta divertirse<FF03>a veces, supongo!<FF02><FF01>   <FF1B>Mark<FF03>Bien. Preparate para deslumbrarte con<FF03>mis dotes de poker.<FF02><FF01>  <FF1B>Elly<FF03>Detesto este tipo de lugar. El aire<FF03>es asqueroso.<FF02><FF01> <FF1B>Mark<FF03>Jeje. Todo se trata de casinos.<FF02><FF04><FF1B>Mark<FF03>Por cierto, <FF08>")
put("e2_01235"," Que opinas<FF03>de esos tipos del mostrador")
put("e2_01236","<FF02><FF01> <FF1B>Ayase<FF03>Oye, <FF07>. Junta fichas y<FF03>comprame aretes.<FF02><FF04><FF1B>Ayase<FF03>Queee.? Solo tienen cosas como<FF03>Para Stones? Que decepcion.<FF02><FF01>  <FF1B>Reiji<FF03>Hmph")
put("e2_01237"," Ridiculo!<FF02><FF01><FF1B>Mozo<FF03>Holaaa. Que gusto verte.<FF02><FF04><FF1B>Mozo<FF03>Si buscas cambiar dinero por<FF03>fichas, soy tu hombre!<FF02><FF04><FF1B>Mozo<FF03>No quieres comprar fichas? Hmmmm?<FF02><FF0E> <FF01><FF1B>Mozo<FF03>Cambio tus fichas por objetos, si<FF03>es lo que se te antoja")
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c26.json")
