import sys; sys.path.insert(0,"/home/josechavez/persona_es/scripts")
from wf_chunk import put,repl,dump
K1="<FF02><FF01>   <FF1B>Mark<FF03>Solo hay que encargarse de Kandori,<FF03>y el pueblo volvera a la normalidad!<FF02><FF01>   <FF1B>Mark<FF03>Apuremonos tras Kandori.<FF02><FF01>  <FF1B>Nanjo<FF03>No hay tiempo que perder aqui!<FF02><FF01> <FF1B>Nanjo<FF03>No hay tiempo que perder aqui!<FF02><FF01> <FF1B>Ayase<FF03>Vamos a darle a Kandori. Vamos, rapido.<FF02><FF01><FF1B>Ayase<FF03>Esto significa que Kandori tambien<FF03>tuvo el sueno de la mariposa?<FF02><FF01>   <FF1B>Mark<FF03>Conmigo en accion, Kandori no tiene<FF03>futuro! Muajaja"
K2="<FF02><FF01>  <FF1B>Mark<FF03>Asi que esto significa que Kandori tambien<FF03>tuvo el sueno de la mariposa!<FF02><FF01> <FF1B>Elly<FF03>Apuremonos!<FF02><FF01><FF1B>Elly<FF03>Crees que Kandori tambien tuvo ese<FF03>sueno de la mariposa?<FF02><FF01> <FF1B>Reiji<FF03>"
for i in ("e2_00851","e2_00857","e2_00863"): put(i,K1)
for i in ("e2_00852","e2_00858","e2_00864"): put(i,K2)
repl("e2_00868",
 ("This is kinda exciting.","Esto es algo emocionante."),
 ("It looks like we can enter the SEBEC<FF03>building now!","Parece que ya podemos entrar al<FF03>edificio SEBEC!"),
 ("If you're frightened, <FF07>,<FF03>I won't blame you for backing out!","Si tienes miedo, <FF07>,<FF03>no te culpare por echarte atras!"),
 ("I'll defeat that man alone if that's<FF03>what it takes.","Vencere a ese hombre solo si<FF03>es necesario."),
 ("I feel like Maki's different somehow","Siento que Maki es diferente de algun modo"))
put("e2_00869","<FF02><FF01> <FF1B>Elly<FF03>Kandori esta en SEBEC, si?<FF02><FF01><FF1B>Elly<FF03>Nos hemos topado con algo<FF03>increible")
put("e2_00870"," Esto podria ser interesante.<FF02><FF01> <FF1B>Mark<FF03>Amigo, me estoy impacientando. Solo<FF03>dejame ir ya.<FF02><FF01><FF1B>Ayase<FF03>Oye, o sea, solo somos chicos normales<FF03>de prepa, verdad?<FF02><FF04><FF1B>Ayase<FF03>Asi que ni SEBEC le dispararia a unos<FF03>pobres como nosotros, o si")
repl("e2_00871",
 ("You're such a liar, <FF07>.<FF03>Kandori was totally gonna kill us.","Que mentiroso eres, <FF07>.<FF03>Kandori si nos iba a matar."))
repl("e2_00875",
 ("Hi. I'm Trish and this is my fountain<FF03>of healing.","Hola. Soy Trish y esta es mi fuente<FF03>de curacion."),
 ("This world runs on give-and-take. Give<FF03>me money and I'll take away your pain.","El mundo es de toma y daca. Dame<FF03>dinero y te quito el dolor."),
 ("What do you say?","Que dices?"),
 ("Okay.","Bien."),
 ("Umm, with the going rate for healing","Umm, con la tarifa actual de curacion"))
put("e2_00880","<FF21> <FF1B>Agastya Tree<FF03>Jovenes")
put("e2_00885","<FF02><FF04><FF1B>Maki<FF03>Pero yo no tengo madre.<FF02><FF01><FF1B>Nanjo<FF03>Esos cientificos")
put("e2_00886"," Que clase de investigacion<FF03>ocurre aqui?<FF02><FF01><FF1B>Mark<FF03>Este lugar es muy sospechoso!<FF02><FF04><FF1B>Mark<FF03>Eh")
put("e2_00887"," parece que los rumores de SEBEC<FF03>tenian algo de verdad.<FF02><FF01> <FF1B>Elly<FF03>Sea lo que investigaban, debian<FF03>mantenerlo en secreto!<FF02><FF01> <FF1B>Mark<FF03>Que lugar tan aburrido. No tienen<FF03>nada genial aqui?<FF02><FF01>   <FF1B>Ayase<FF03>Hmm")
put("e2_00888"," esta caja es muy sospechosa!<FF02><FF01> <FF1B>Cientifico<FF03>Este no es el sotano")
put("e2_00889"," Por que esta<FF03>sala esta sobre el suelo.?<FF02><FF01><FF1B>Cientifico<FF03>Disculpa, viste a una mujer en tu<FF03>camino aqui? Pelo corto y lentes!<FF02><FF04><FF1B>Cientifico<FF03>Oh, Sonomura")
put("e2_00890"," por favor estate a salvo.<FF02><FF01>   <FF1B>Cientifico<FF03>Kandori debio usar esa maquina")
put("e2_00891","<FF02><FF01> <FF1B>Cientifico<FF03>No puedo creerlo. <FF02><FF04><FF1B>Cientifico<FF03>No pudimos calcular que cambiaria<FF03>hasta la estructura del edificio")
put("e2_00892","<FF02><FF01>  <0044> La puerta no parece que<FF03>vaya a abrir")
put("e2_00895"," Fue demasiado lejos.<FF02><FF01> <FF1B>Mark<FF03>Estos tipos no sienten culpa<FF03>por lo que hicieron?<FF02><FF01>  <FF1B>Elly<FF03>Kandori les hizo construir una maquina<FF03>que crea demonios?<FF02><FF01>   <FF1B>Mark<FF03>No se si me gusta lo complicado<FF03>que se esta poniendo esto")
put("e2_00896","<FF02><FF04><FF1B>Mark<FF03>Hay cosas que ni yo puedo<FF03>entender, sabes.<FF02><FF01>   <FF1B>Ayase<FF03>Quien es ese Dr! Nicholai?<FF02><FF01>   <FF1B>Cientifico<FF03>Era ese chico de prepa amigo<FF03>tuyo? Lamento decir que el estaba")
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c16.json")
