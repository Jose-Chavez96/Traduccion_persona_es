import sys; sys.path.insert(0,"/home/josechavez/persona_es/scripts")
from wf_chunk import put,repl,dump
# doctor menu reusable pairs (fee param)
def docmenu(fee):
    return [
     (f"My fee is {fee} yen! Well?",f"Cobro {fee} yenes! Bien?"),
     ("Hm! Then let's get you patched up!","Hm! Entonces a curarte!"),
     ("There, that should do it!","Listo, con eso basta!"),
     ("Anything else you need?","Necesitas algo mas?"),
     ("Well, I can't treat patients who can't<FF03>pay! Come back when you have the fee!","No atiendo a quien no puede<FF03>pagar! Vuelve cuando tengas el dinero!"),
     ("I hope you don't run into trouble later<FF03>because you cheaped out on treatment!","Espero que no tengas problemas luego<FF03>por ahorrarte el tratamiento!"),
     ("All right! If anything else comes up,<FF03>I recommend you see me immediately!","Bien! Si surge algo mas,<FF03>te recomiendo verme de inmediato!"),
     ("My time is valuable! If you don't have<FF03>any business here, then take a hike!","Mi tiempo vale! Si no tienes<FF03>nada que hacer aqui, largate!"),
    ]
put("e2_00302","<FF03>interesante como siempre!<FF02><FF01> <FF1B>Doctor<FF03>Bien, en que te ayudo?<FF02><FF0E><1100><FF01> <FF1B>Doctor<FF03>Bien")
put("e2_00303"," Para todos ustedes")
repl("e2_00304", *docmenu("800"))
repl("e2_00306",
 ("I can't speak to what went on at the<FF03>haunted mansion<0007> I've never been!","No puedo hablar de lo que paso en la<FF03>mansion embrujada<0007> nunca fui!"),
 ("It would be nice if I could someday cure<FF03>my wounds through willpower alone!","Seria genial si algun dia pudiera curar<FF03>mis heridas solo con voluntad!"),
 ("The <0028>haunted mansion<0028> was just some old,<FF03>abandoned dump! We liked it there, is all!","La <0028>mansion embrujada<0028> era un viejo<FF03>basurero! Solo nos gustaba ahi!"),
 ("It's so quiet here","Hay tanto silencio aqui"))
put("e2_00307"," Siento como si<FF03>nunca hubiera pasado nada!<FF02><FF01><FF1B>Yukino<FF03>Admito que yo tambien jugaba en la<FF03>mansion embrujada!<FF02><FF01>  <FF1B>Yukino<FF03>Lo que sea que haya alla afuera")
put("e2_00308","<FF05><1000><FF03>No sera un oso, verdad?<FF02><FF01> <FF1B>Elly<FF03>Me pregunto")
repl("e2_00309",
 ("what prompted the sudden<FF03>appearance of these demons?","que provoco la repentina<FF03>aparicion de estos demonios?"),
 ("Nurse","Enfermera"),
 ("Did you play in the haunted mansion when<FF03>you were little? Lots of kids did!","Jugabas en la mansion embrujada de<FF03>pequeno? Muchos ninos lo hacian!"),
 ("I heard a bear appeared! Was it brown?<FF03>White? Plump and hairy?","Oi que aparecio un oso! Era cafe?<FF03>Blanco? Gordo y peludo?"),
 ("It's another nice day out!","Otro buen dia afuera!"),
 ("Do bears appear even in this town","Aparecen osos hasta en este pueblo"))
put("e2_00310","<FF02><FF01> <FF1B>Doctor<FF03>Bien, en que te ayudo?<FF02><FF0E><1100><FF01> <FF1B>Doctor<FF03>Bien")
put("e2_00311"," Para todos ustedes")
repl("e2_00312", *docmenu("1,000"))
repl("e2_00314",
 ("The only clothing I require is this<FF03>uniform","La unica ropa que necesito es este<FF03>uniforme"))
put("e2_00315"," y mi bufanda, claro!<FF02><FF01><FF1B>Mark<FF03>Hablando de ropa, que onda con la<FF03>bufanda de Nanjo? Siempre la trae!<FF02><FF01> <FF1B>Yukino<FF03>Tch, Yuka te pidio que fueras de<FF03>compras por ella?<FF02><FF04><FF1B>Yukino<FF03>Bueno, cuando termines aqui, iremos<FF03>directo al hospital.<FF02><FF01> <FF1B>Mozo<FF03>La gente de este pueblo tiene muy mal<FF03>gusto para la moda.<FF02><FF04><FF1B>Mozo<FF03>El unico con algo de gusto es<FF03>un chico castano que veo a veces")
put("e2_00320","<FF02><FF04><FF1B>Nanjo<FF03>Mientras el hospital este en nuestros<FF03>planes en algun momento!<FF02><FF01> <FF1B>Nanjo<FF03>Asi que se niega a cerrar su negocio aun<FF03>con la llegada de los demonios")
put("e2_00321","<FF02><FF04><FF1B>Nanjo<FF03>La gente comun puede tener mas voluntad<FF03>de la que yo creia!<FF02><FF01>   <FF1B>Mark<FF03>Musica")
put("e2_00322"," Tipo pianos y canto?<FF02><FF04><FF1B>Mark<FF03>Eh? Creo que oi algo asi<FF03>en algun lado tambien")
put("e2_00323","<FF02><FF01> <FF1B>Mark<FF03>Esta bien que estas tiendas esten abiertas?<FF02><FF04><FF1B>Mark<FF03>No me hago responsable si los demonios<FF03>las destrozan.<FF02><FF01><FF1B>Elly<FF03>Eso me recuerda, alguien en la escuela<FF03>decia algo parecido!<FF02><FF01>   <FF1B>Yukino<FF03>Una tienda rara? Que crees<FF03>que hay dentro")
put("e2_00324","<FF02><FF01>  <FF1B>Yukino<FF03>No has tenido suficiente diversion?<FF03>Podemos ir al Templo Alaya ahora?<FF02><FF01><FF1B>Mozo<FF03>Vaya, gracias por venir hasta aqui!<FF03>Bueno, mira con confianza!<FF02><FF01><FF1B>Mozo<FF03>Vaya, gracias por venir hasta aqui!<FF03>Debe ser dificil para ustedes!<FF02><FF01><FF1B>Cliente<FF03>Hay una tienda rara en este<FF03>centro comercial")
put("e2_00325","<FF02><FF04><FF1B>Cliente<FF03>Cada vez que voy a mirar, esta cerrada,<FF03>y nunca vi a nadie entrar o salir!<FF02><FF04><FF1B>Cliente<FF03>Pero de vez en cuando, se oye<FF03>musica adentro")
repl("e2_00326",
 ("It's a funny old world, isn't it?","Es un mundo curioso, no?"),
 ("That strange store in this mall will<FF03>apparently be open soon!","Esa tienda rara del centro al parecer<FF03>abrira pronto!"),
 ("Don't ask me when, though!","Pero no me preguntes cuando!"),
 ("Customer","Cliente"))
put("e2_00329"," Tu presencia es bienvenida!<FF02><FF01> <FF1B>Atastya Tree<FF03>Inscribiras tu historia en mi?<FF02><FF0E> <FF01>   <FF1B>Atastya Tree<FF03>Cuidate en tu viaje, joven")
put("e2_00334","cuando te sientas mal, entonces<FF03>toma un Dis-Sick")
put("e2_00335","<FF02><FF04><FF1B>Nanjo<FF03>Gah, esta cancion insidiosa. Me estan<FF03>lavando el cerebro.<FF02><FF01>  <FF1B>Nanjo<FF03>Solo se puede confiar en la propia fuerza!<FF03>Es el unico modo!<FF02><FF01><FF1B>Mark<FF03>Asi que esta es la tienda del tio de Tadashi!<FF03>Dijo que vive en la del Sun Mall?<FF02><FF01>   <FF1B>Mark<FF03>Los chicos de hoy si saben")
put("e2_00336","<FF02><FF01><FF1B>Yukino<FF03>Me intriga este arbol que no<FF03>estaba antes!<FF02><FF01> <FF1B>Yukino<FF03>Me sorprende que la mama de Maki llegara<FF03>al templo!<FF02><FF04><FF1B>Yukino<FF03>Si se hubiera desmayado antes")
repl("e2_00337",
 ("I don't<FF03>like to think what might've happened!","No quiero<FF03>pensar que habria pasado!"),
 ("I'm giving some thought to the mystery<FF03>as well!","Yo tambien pienso en<FF03>el misterio!"),
 ("This is my chance to put into practice<FF03>the things I've studied all this time!","Es mi oportunidad de poner en practica<FF03>lo que he estudiado todo este tiempo!"),
 ("Are you friends with my nephew? Then I'll<FF03>give you extra special service.","Son amigos de mi sobrino? Entonces les<FF03>dare un servicio muy especial."),
 ("I'm not the least bit scared of demons!","No le tengo nada de miedo a los demonios!"),
 ("I'm sure it was just a trick, or maybe<FF03>I was seeing things!","Seguro fue un truco, o quiza<FF03>vi visiones!"),
 ("I went to the park and saw a tree that<FF03>wasn't there before! You should go look!","Fui al parque y vi un arbol que no<FF03>estaba antes! Deberias ir a ver!"),
 ("You can't go in there. It's private.","No puedes entrar ahi. Es privado."),
 ("The TV and radio don't work, and my<FF03>parents are hiding under their futons!","La tele y la radio no sirven, y mis<FF03>padres se esconden bajo sus futones!"),
 ("I guess in the end, you have to take<FF03>matters into your own hands!","Supongo que al final, uno debe<FF03>tomar las riendas!"),
 ("Clerk","Mozo"),
 ("Customer","Cliente"))
repl("e2_00377",
 ("Is no one home? Hmm","No hay nadie en casa? Hmm"))
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e2_c08.json")
