import sys; sys.path.insert(0,"/home/josechavez/persona_es/scripts")
from wf_chunk_e0 import put,repl,dump

# --- dup block (= e0_00130/131 + S124-S129 from d04) ---
E130=" Asi no actua<FF03>una corporacion normal!<FF02><FF01> <FF1B>Elly<FF03>Que significa esto? Oi que SEBEC<FF03>era una empresa Fortuna 500"
E131="<FF02><FF04><FF1B>Elly<FF03>Pero esto bien podria ser una<FF03>fachada de la Mafia!<FF02><FF01><FF1B>Elly<FF03>Mm? No es ese el de intercambio?<FF02><FF01> <FF1B>Mark<FF03>Huh? Oh, oye, si, es Reiji!<FF03>Que hace aqui?<FF02><FF01>   <FF18><0200><0044> Reiji Kido <0029>Apodo<0006> Reiji<002A><FF03>Un solitario callado que llego a<FF03>St! Hermelin hace seis meses!<FF18> <FF02><FF01> <FF1B>Hombre de negro<FF03>Quienes son?<FF02><FF04><FF1B>Hombre de negro<FF03>De aqui es territorio SEBEC!<FF03>No entren!<FF02><FF01><FF1B>Mark<FF03>Oye, la mama de Maki no trabaja en SEBEC?<FF03>Que rayos pasa"
S124=" entonces preparate para morir!<FF02><FF01><FF1B>Hombre de negro<FF03>No me hagas repetirlo!<FF02><FF04><FF1B>Hombre de negro<FF03>De aqui es territorio SEBEC! Si no<FF03>oyes, quiza te maten a tiros!<FF02><FF01><FF1B>Mark<FF03>Ese idiota. Va a hacer que lo<FF03>maten.<FF02><FF01><FF1B>Mark<FF03>Hahaha, perdon por meterme! Este<FF03>no esta bien de la cabeza, sabes?<FF02><FF04><FF1B>Mark<FF03>Vamos, tarado, hora de irse!<FF02><FF01>   <FF1B>Reiji<FF03>Tch"
S125=" Ustedes otra vez!<FF02><FF01> <FF1B>Nanjo<FF03>Asi que hasta tu ayudas a otros"
S126="<FF03>Interesante! No lo habria pensado!<FF02><FF01>   <FF1B>Mark<FF03>Idiota. Hasta tipos asi tienen mama"
S127="<FF03>Estaria triste si lo balean!<FF02><FF01>  <FF1B>Hombre de negro<FF03>Prohibido el paso, ninos!<FF02><FF01> <FF1B>Hombre de negro<FF03>No es lugar para ninos! Vayan a<FF03>buscar un buen parque!<FF02><FF01> <FF1B>Mark<FF03>Cielos"
S128=" Que trama ese tipo?<FF02><FF01>  <FF1B>Nanjo<FF03>SEBEC"
S129=" Que trama Kandori?<FF02><FF01><FF1B>Yukino<FF03>Esto no me gusta"

put("e0_00153",E130)
put("e0_00154",E131)
put("e0_00157",S124)
put("e0_00158",S125)
put("e0_00159",S126)
put("e0_00160",S127)
put("e0_00161",S128)
put("e0_00162",S129)
put("e0_00163",E130)
put("e0_00164","<FF02><FF04><FF1B>Elly<FF03>Pero esto bien podria ser una<FF03>fachada de la Mafia!<FF02><FF01><FF1B>Elly<FF03>Mm? No es ese el de intercambio?<FF02><FF01> <FF1B>Mark<FF03><FF1B>Mark<FF03>Huh? Oh, oye, si, es Reiji!<FF03>Que hace aqui?<FF02><FF01> <FF18><0200><0044> Reiji Kido <0029>Apodo<0006> Reiji<002A><FF03>Un solitario callado que llego a<FF03>St! Hermelin hace seis meses!<FF18> <FF02><FF01> <FF1B>Hombre de negro<FF03>Quienes son?<FF02><FF04><FF1B>Hombre de negro<FF03>De aqui es territorio SEBEC!<FF03>No entren!<FF02><FF01><FF1B>Mark<FF03>Oye, la mama de Maki no trabaja en SEBEC?<FF03>Que rayos pasa")

# --- new casino scene ---
put("e0_00169","<FF02><FF04><FF1B>Nanjo<FF03>No logro comprender en absoluto tus<FF03>motivos para estar aqui!<FF02><FF01><FF1B>Mark<FF03>Ignora a esos tipos! Se aburriran<FF03>y se iran en un rato!<FF02><FF01>   <FF1B>Mark<FF03>Me gustan los slots, pero<FF03>juguemos tras la revision.<FF02><FF01>   <FF1B>Mark<FF03>Me da pena el resto de los<FF03>Tailors, pero tengo cosas que hacer!<FF02><FF01>  <FF1B>Yukino<FF03>Los amigos de Masao siguen raros!<FF02><FF01>   <FF1B>Yukino<FF03>El Santuario Alaya, chicos! Odio insistir,<FF03>pero no lo olviden!<FF02><FF01> <FF1B>Elly<FF03>El aire aqui es desagradable!<FF02><FF01>   <FF1B>Hombre muy alegre<FF03>Jeje")
put("e0_00170"," Sson amigosh de Mark?<FF03>Jeejeejeeee.<FF02><FF04><FF1B>Hombre muy alegre<FF03>Parecsse que no sson losh que busco.<FF02><FF01><FF1B>Hombre muy alegre<FF03>Jeje")
put("e0_00173"," Te habriamos golpeado<FF03>si lo fueras.<FF02><FF04><FF1B>Hombre muy alegre<FF03>Y luego los pondria a todos a<FF03>trabajar para mi. Jeee.<FF02><FF01><FF1B>Hombre rubio<FF03>Sabes, ha habido un fuereno<FF03>rondando nuestro lugar!<FF02><FF04><FF1B>Hombre rubio<FF03>Dicen que tiene cicatriz en la<FF03>cabeza! No debe meterse con los Tailors.<FF02><FF01> <FF1B>Hombre rubio<FF03>Rayos, que hare? No sirvo<FF03>para pelear demonios!<FF02><FF04><FF1B>Hombre rubio<FF03>Y Mark tampoco estara!<FF03>La verdad, tengo miedo!<FF02><FF01>   <FF1B>Mark<FF03>Men, no te asustes por<FF03>algo asi!<FF02><FF04><FF1B>Mark<FF03>Te dejo los Tailors a cargo<FF03>mientras no estoy, sabes!<FF02><FF01>  <FF1B>Ludopata<FF03>Maldicion. Estoy quebrado de nuevo.<FF02><FF04><FF1B>Ludopata<FF03>Tras tantas perdidas, el proximo que<FF03>juegue esta maquina deberia ganar")
put("e0_00174","<FF02><FF04><FF1B>Ludopata<FF03>Espera, sigues tu? Aww, que mal.<FF02><FF01> <FF1B>Cajero<FF03>Holaaa. QUE gusto verte.<FF02><FF04><FF1B>Cajero<FF03>Si buscas cambiar dinero por<FF03>fichas, soy tu hombre!<FF02><FF04><FF1B>Cajero<FF03>No quieres comprar fichas? Hmmmm?<FF0E> <FF01> <FF1B>Cajero<FF03>Puedo cambiar tus fichas por items, si<FF03>es lo que se te antoja")

# --- Reiji confrontation outside studio ---
put("e0_00187"," Masao, el tambien es de tu <0028>banda<0028><FF03>?<FF02><FF01><FF1B>Mark<FF03>Que dijiste.? Huh")
put("e0_00188","<FF02><FF04><FF1B>Mark<FF03>Asi que eres el de la cicatriz en la<FF03>cabeza")
put("e0_00189"," Que haces aqui?<FF02><FF01>   <FF1B>Reiji<FF03>Mejor alejense todos de aqui!<FF03>A menos que quieran morir, claro")
put("e0_00190","<FF02><FF01> <FF1B>Mark<FF03>Que se supone que significa?<FF03>Oye, espera.<FF02><FF01>  <FF1B>Yukino<FF03>Me pregunto por que anda<FF03>rondando")
put("e0_00191","<FF02><FF01><FF1B>Mark<FF03>Tienes algo en nuestro estudio, men?<FF03>Creo que hoy no hay nadie")
repl("e0_00192",
  ("<0029>Nickname<0006>","<0029>Apodo<0006>"),
  ("A quiet loner who transferred to<FF03>St! Hermelin High six months ago!","Un solitario callado que llego a<FF03>St! Hermelin hace seis meses!"))
put("e0_00195","<FF02><FF01>   <FF1B>Nanjo<FF03>Terminaste aqui? Podemos ir<FF03>al hospital ya?<FF02><FF01>   <FF1B>Nanjo<FF03>Hah")
put("e0_00196"," Es cierto, uno consigue cosas<FF03>diarias en la tienda!<FF02><FF01>  <FF1B>Mark<FF03>Asi que esa es la mama de Reiji")
dump("/home/josechavez/persona_es/translated_text/_wfmaps/e0_d05.json")
