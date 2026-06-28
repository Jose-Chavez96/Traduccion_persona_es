import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_01776", ("I'd hope for one as<FF03>kind and caring as you", "Esperaria una tan<FF03>amable y atenta como tu"))
repl("e0_01777",
    ("We'll beat Kandori and save your Maki<FF03>while we're at it.", "Venceremos a Kandori y salvaremos a<FF03>tu Maki de paso."),
    ("Yes", "Si"),
)
repl("e0_01778", ("Please do! Thank you", "Por favor! Gracias"))
repl("e0_01780", ("Now get going, all of you.<FF03>And be careful.", "Ahora vayan, todos.<FF03>Y tengan cuidado."))
repl("e0_01789", ("Oh, it's the haunted mansion! I was just<FF03>having a dream about this place", "Oh, es la mansion embrujada! Estaba<FF03>sonando con este lugar"))
repl("e0_01790", ("See? Maki's mom doesn't exist in this<FF03>world, so", "Ves? La mama de Maki no existe<FF03>aqui, asi que"))
repl("e0_01791", ("This has to be her. But what's she<FF03>doing here", "Tiene que ser ella. Pero que<FF03>hace aqui"))
repl("e0_01792",
    ("You okay, lady?", "Bien, senora?"),
    ("Yes", "Si"),
)
repl("e0_01794", ("Maki was constantly getting lost at this<FF03>haunted mansion when she was little", "Maki se perdia siempre en esta<FF03>mansion de pequena"))
repl("e0_01795",
    ("I'm used to looking for her here!", "Estoy acostumbrada a buscarla aqui!"),
    ("I was just dreaming about those days", "Sonaba con aquellos dias"),
)
repl("e0_01796", ("I was searching for her in this huge<FF03>mansion, and I heard Maki call to me", "La buscaba en esta enorme<FF03>mansion, y oi a Maki llamarme"))
repl("e0_01797",
    ("I don't remember anything after that!", "No recuerdo nada despues de eso!"),
    ("Um, Miss? I'm", "Em, senora? Yo"),
)
repl("e0_01798", ("not your real child<FF03>after all", "no soy tu hija real<FF03>al final"))
repl("e0_01799", ("What", "Que"))
repl("e0_01800",
    ("Allow me to explain!", "Dejame explicar!"),
    ("So that's it", "Asi que es eso"),
)
repl("e0_01801",
    ("You're the Maki of<FF03>this world!", "Eres la Maki de<FF03>este mundo!"),
    ("But why don't I exist here", "Pero por que no existo aqui"),
)
repl("e0_01802", ("Uh-oh. The dimensional passageway is<FF03>about to disappear", "Oh-oh. El pasaje dimensional<FF03>va a desaparecer"))
repl("e0_01803",
    ("I'm sorry, lady, but we have to chase<FF03>down Kandori!", "Perdon, senora, pero hay que perseguir<FF03>a Kandori!"),
    ("Alright! Just give me one moment.", "Bien! Dame un momento."),
    ("The dimensional passageway is very<FF03>unstable right now!", "El pasaje dimensional esta muy<FF03>inestable ahora!"),
    ("Someone has to stay here and operate<FF03>the machine!", "Alguien debe quedarse a operar<FF03>la maquina!"),
    ("What? No", "Que? No"),
)
repl("e0_01804",
    ("We can't leave anyone here.", "No dejamos a nadie aqui."),
    ("I'll do it. Don't worry", "Yo lo hare. Tranquilos"),
)
repl("e0_01805",
    ("Go ahead<FF03>on your own!", "Vayan<FF03>ustedes solos!"),
    ("Though I'd be grateful if you came to<FF03>get me when this is all over with!", "Aunque agradeceria que vinieran por<FF03>mi cuando todo termine!"),
    ("Miss", "Senora"),
)
repl("e0_01806", ("Yes? Speak quickly", "Si? Habla rapido"))
repl("e0_01807", ("There isn't<FF03>much time!", "No hay<FF03>mucho tiempo!"))
dump(os.path.join(os.path.dirname(__file__), "e0_c50.json"))
