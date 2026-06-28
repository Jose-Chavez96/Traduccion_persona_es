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
repl("e2_00297",
 ("I'm rather surprised that the townspeople<FF03>know so much about St! Hermelin!","Me sorprende que la gente del pueblo<FF03>sepa tanto de St! Hermelin!"),
 ("I'd like to refrain from seeing the<FF03>doctor for a while","Preferiria evitar ver al<FF03>doctor por un tiempo"))
put("e2_00298","<FF02><FF01>  <FF1B>Mark<FF03>No te molesta que aun no hayamos<FF03>ido al hospital?<FF02><FF01> <FF1B>Mark<FF03>Rayos, esto me esta enojando")
put("e2_00299"," Debemos<FF03>apurarnos al templo!<FF02><FF01><FF1B>Yukino<FF03>La Srta! Saeko es nuestra superior!<FF03>Me lo dijo una vez!<FF02><FF01>   <FF1B>Yukino<FF03>Crees que la mujer que vio la enfermera<FF03>era la mama de Maki?<FF02><FF01>  <FF1B>Elly<FF03>Vamos al Templo Alaya cuando nos<FF03>curen! Esta a la vuelta!<FF02><FF01>  <FF1B>Elly<FF03>Una vez curadas las heridas, apuremonos<FF03>a la fabrica abandonada!<FF02><FF04><FF1B>Elly<FF03>Aunque de verdad crees que se puede<FF03>acceder a SEBEC desde ahi?<FF02><FF01>  <FF1B>Enfermera<FF03>Vaya, ese uniforme trae recuerdos.<FF03>Yo me gradue de St! Hermelin!<FF02><FF04><FF1B>Enfermera<FF03>Una vieja companera, Saeko Takami,<FF03>ensena ahi ahora! La conocen?<FF02><FF04><FF1B>Enfermera<FF03>Jaja, esa Saeko")
put("e2_00300"," Nunca la imagine<FF03>como maestra.<FF02><FF01>  <FF1B>Enfermera<FF03>Oi que una mujer herida andaba<FF03>por aqui! Se la llevaron los demonios")
put("e2_00596","<FF02><FF01>  <FF1B>Elly<FF03>Que sensacion tan curiosa")
put("e2_00597"," Es como si<FF03>todo fuera un sueno cuando estoy aqui!<FF02><FF01>   <FF1B>Ayase<FF03>Oye, y SEBEC? Solo vamos a<FF03>dejar esa idea?<FF02><FF01>  <FF1B>Ayase<FF03>Vamos, persigamos a Kandori.<FF02><FF01> <FF1B>Mozo<FF03>Estare bien si me quedo aqui")
put("e2_00598"," Mantenerla<FF03>abierta")
put("e2_00599"," Nunca cerramos")
repl("e2_00600",
 ("Welcome.","Bienvenido."),
 ("Clerk","Mozo"))
put("e2_00603"," No vamos a estar<FF03>aqui mucho, verdad?<FF02><FF01> <FF1B>Mark<FF03>De verdad tenemos que ir a esa fabrica?<FF03>Es muy sucia para alguien con clase.<FF02><FF01>  <FF1B>Mark<FF03>De verdad hay que vencer a Kandori? Escapo.<FF03>Mejor dejemoslo asi.<FF02><FF01>   <FF1B>Nanjo<FF03>")
put("e2_00604","<FF05><1000>Oh, perdon, <FF07>! Estaba<FF03>pensando!<FF02><FF01> <FF1B>Mark<FF03>Asi que Kandori estaba detras de todo")
put("e2_00605"," <FF05><2000>Seguimos<FF03>yendo a la fabrica abandonada?<FF02><FF01>  <FF1B>Mark<FF03>Debemos apurarnos y atrapar a Kandori.<FF02><FF01>  <FF1B>Elly<FF03>El ambiente alegre de esta clinica<FF03>siempre relaja, me parece!<FF02><FF01>   <FF1B>Ayase<FF03>Por que SEBEC tiene seguridad<FF03>tan estricta?<FF02><FF01><FF1B>Ayase<FF03>Wow")
put("e2_00606"," SEBEC si era tan malo como<FF03>dicen")
repl("e2_00607",
 ("I hear things are going haywire outside!<FF03>If I wasn't on the job, I'd go look.","Oi que afuera esta todo loco!<FF03>Si no trabajara, iria a ver."),
 ("Nurse","Enfermera"),
 ("Wish I could find a nurse who was less<FF03>of a ditz!","Ojala hallara una enfermera menos<FF03>despistada!"),
 ("Now, what can I do for you?","Bien, en que te ayudo?"),
 ("Alright","Bien"))
put("e2_00608"," Para todos ustedes")
repl("e2_00609", *docmenu("800"))
put("e2_00612"," no ibamos a la fabrica<FF03>abandonada?<FF02><FF01>   <FF1B>Maki<FF03>Debemos apurarnos tras Kandori.<FF02><FF01> <FF1B>Mark<FF03>Vaya, que tienda tan mala. Si fuera mia,<FF03>la haria un cafe al aire libre.<FF02><FF01>   <FF1B>Nanjo<FF03>Ese mozo parece sospechar de nosotros!<FF02><FF04><FF1B>Nanjo<FF03>Pero seguimos siendo humanos con<FF03>este poder? Que opinas?<FF02><FF01> <FF1B>Mark<FF03>Ojala fuera tan relajado como tu,<FF03><FF07>!<FF02><FF01>   <FF1B>Elly<FF03>Me sorprende que algunos puedan<FF03>mantener la calma! Es admirable!<FF02><FF01><FF1B>Ayase<FF03>No sabia que te gustaba esto,<FF03><FF07>. Awww, que tierno.<FF02><FF01>   <FF1B>Tendero<FF03>Estas")
repl("e2_00615",
 ("The owner here really knows how to sell<FF03>his product!","El dueno aqui si sabe vender<FF03>su producto!"),
 ("That was my first time in a jail cell.","Fue mi primera vez en una celda."),
 ("I was kinda nervous at first","Estaba algo nervioso al inicio"),
 ("Brown","Mark"))
put("e2_00616"," pero<FF03>fue muy divertido.<FF02><FF01>   <FF1B>Nanjo<FF03>Hombre prevenido vale por dos.<FF03>")
put("e2_00617","Eso decia siempre Yamaoka!<FF02><FF01> <FF1B>Mark<FF03>Tengo mucho que decirle a Kandori")
put("e2_00618","<FF03>No dejare a ese tipo en paz!<FF02><FF01>   <FF1B>Elly<FF03>Vamos a la fabrica abandonada,<FF03>si?<FF02><FF04><FF1B>Elly<FF03>Nunca le di una buena mirada<FF03>antes, pero")
put("e2_00619","<FF02><FF01>   <FF1B>Elly<FF03>Debemos perseguir al Sr!Kandori")
put("e2_00620"," No podemos<FF03>dejarlo hacer lo que quiera.<FF02><FF01>  <FF1B>Ayase<FF03>Tienes razon")
put("e2_00621"," Si vamos a entrar<FF03>a SEBEC, necesitamos medicina.<FF02><FF01> <FF1B>Ayase<FF03>Debemos ir tras Kandori")
put("e2_00622"," Tipo, quien<FF03>sabe que hara?<FF02><FF01>   <FF1B>Mozo<FF03>Ah, bienvenido.<FF02><FF04><FF1B>Mozo<FF03>Oye, has visto a Tamaki?<FF02><FF04><FF1B>Mozo<FF03>Estoy muy preocupada por ella")
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c11.json")
