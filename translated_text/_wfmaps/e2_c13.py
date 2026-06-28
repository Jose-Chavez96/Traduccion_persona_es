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
put("e2_00671","<FF02><FF01> <FF1B>Elly<FF03>Una vez curadas las heridas, debemos<FF03>apurarnos a la fabrica abandonada!<FF02><FF04><FF1B>Elly<FF03>Pero de verdad crees que podemos<FF03>acceder a SEBEC desde ahi?<FF02><FF01> <FF1B>Elly<FF03>Debemos apurarnos tras el Sr! Kandori.<FF02><FF01><FF1B>Mark<FF03>Sabes, casi me rayan la cara<FF03>bonita en batalla hace rato.<FF02><FF04><FF1B>Mark<FF03>50,000 fans de Mark en el mundo<FF03>caerian en total desesperacion.<FF02><FF04><FF1B>Mark<FF03>Como pude ser tan descuidado.?<FF02><FF01>   <FF1B>Ayase<FF03>No nos dara una inyeccion, verdad?<FF03>ODIO las inyecciones!<FF02><FF01><FF1B>Enfermera<FF03>Oi que una mujer herida andaba<FF03>por aqui hace poco!<FF02><FF04><FF1B>Enfermera<FF03>Me pregunto si cayo ante los demonios")
put("e2_00673","<FF03>interesante como siempre!<FF02><FF01> <FF1B>Doctor<FF03>Bien, en que te ayudo?<FF02><FF0E><1100><FF01> <FF1B>Doctor<FF03>Bien")
put("e2_00674"," Para todos ustedes")
repl("e2_00675", *docmenu("800"))
repl("e2_00677",
 ("I really don't want to stay here long!","De verdad no quiero quedarme mucho aqui!"),
 ("Is there anywhere I could be more active?<FF03>I dunno if I'm standing out enough","Hay un lugar donde destaque mas?<FF03>No se si resalto lo suficiente"),
 ("Brown","Mark"))
put("e2_00678","<FF02><FF01><FF1B>Nanjo<FF03>Seria genial si algun dia pudiera curar<FF03>mis heridas solo con voluntad!<FF02><FF01><FF1B>Mark<FF03>Hay tanto silencio aqui")
repl("e2_00679",
 ("I feel like<FF03>nothin' ever happened!","Siento como si<FF03>nunca hubiera pasado nada!"),
 ("The demons appearing in town must be<FF03>SEBEC's doing!","Los demonios que aparecen deben ser<FF03>obra de SEBEC!"),
 ("Ugh, I hate this sterile medical smell!","Ugh, odio este olor a medicina!"),
 ("I heard a bear appeared! Was it brown?<FF03>White? Plump and hairy?","Oi que aparecio un oso! Era cafe?<FF03>Blanco? Gordo y peludo?"),
 ("Nurse","Enfermera"),
 ("It's another nice day out!","Otro buen dia afuera!"),
 ("Do bears appear even in this town","Aparecen osos hasta en este pueblo"))
put("e2_00680","<FF02><FF01> <FF1B>Doctor<FF03>Bien, en que te ayudo?<FF02><FF0E><1100><FF01> <FF1B>Doctor<FF03>Bien")
put("e2_00681"," Para todos ustedes")
repl("e2_00682", *docmenu("1,000"))
put("e2_00687"," que es SEBEC?<FF02><FF04><FF1B>Maki<FF03>Es una empresa? No recuerdo que<FF03>hubiera algo asi")
put("e2_00688","<FF02><FF01><FF1B>Maki<FF03>Vamos tras Kandori.<FF02><FF01> <FF1B>Mark<FF03>Je, me estoy emocionando! Desde ahora,<FF03>veras lo que puedo hacer.<FF02><FF01>   <FF1B>Nanjo<FF03>Hidehiko ya olvido que<FF03>nosotros lo rescatamos!<FF02><FF01>   <FF1B>Nanjo<FF03>No crees que hay algo raro<FF03>en Maki? Hmmm")
put("e2_00689","<FF02><FF01>  <FF1B>Mark<FF03>Esta bien que estas tiendas esten abiertas?<FF02><FF04><FF1B>Mark<FF03>No me hago responsable si los demonios<FF03>las destrozan.<FF02><FF01><FF1B>Elly<FF03>Eso me recuerda")
put("e2_00690"," He oido de esta<FF03>tienda rara antes!<FF02><FF01> <FF1B>Ayase<FF03>Es raro que las tiendas sigan abiertas<FF03>en un momento asi!<FF02><FF01>   <FF1B>Cliente<FF03>Esa tienda rara del centro al parecer<FF03>abrira pronto!<FF02><FF04><FF1B>Cliente<FF03>Me pregunto que tipo de tienda es")
put("e2_00691","<FF02><FF01> <FF1B>Cliente<FF03>Oi de una tienda rara abriendo<FF03>aqui en el centro")
put("e2_00692","<FF02><FF04><FF1B>Cliente<FF03>Puedo oir musica occidental<FF03>desde adentro")
put("e2_00693"," Sera solo para miembros!<FF02><FF04><FF1B>Cliente<FF03>Me gustaria ver que tienen")
repl("e2_00694",
 ("Clerk","Mozo"),
 ("My, I'm grateful you came all this way!<FF03>Things must be hard for all of you!","Vaya, gracias por venir hasta aqui!<FF03>Debe ser dificil para ustedes!"))
repl("e2_00698",
 ("Are TVs and radios that important?<FF03>I've never thought they were necessary!","Son tan importantes las TVs y radios?<FF03>Nunca crei que fueran necesarias!"),
 ("All one can trust is one's own strength!<FF03>It's the only way!","Solo se puede confiar en la propia<FF03>fuerza! Es el unico modo!"),
 ("Kids these days sure know what's what","Los chicos de hoy si saben"))
put("e2_00699","<FF02><FF01><FF1B>Elly<FF03>Me gustaria resolver este misterio!<FF02><FF04><FF1B>Elly<FF03>Es mi oportunidad de poner en practica<FF03>lo que he estudiado todo este tiempo!<FF02><FF01>   <FF1B>Mark<FF03>Asi que primero la fabrica abandonada,<FF03>luego SEBEC, y vencemos a Kandori?<FF02><FF04><FF1B>Mark<FF03>Problema resuelto. Sere un heroe.<FF02><FF04><FF1B>Mark<FF03>Cierto")
put("e2_00700","<FF02><FF01> <FF1B>Mark<FF03>Tenemos que perseguir a Kandori?<FF03>Bueno")
put("e2_00701"," si toca, supongo")
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c13.json")
