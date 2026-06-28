import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from wf_chunk_e0 import repl, dump

repl("e0_00135",
    ("You have <FF11> coins!", "Tienes <FF11> monedas!"),
    ("It's a video poker machine!", "Es una maquina de video poker!"),
    ("What will you do?", "Que haras?"),
    ("What would you like explained?", "Que quieres que te explique?"),
    ("In this version of poker, you can", "En esta version de poker, puedes"),
    ("change your hand once!", "cambiar tu mano una vez!"),
    ("You will be dealt five cards at the", "Se te reparten cinco cartas al"),
    ("outset!", "inicio!"),
    ("Use the directional buttons to move to", "Usa los botones de direccion para ir a"),
    ("a card, and press the ", "una carta, y pulsa el "),
)
dump(os.path.join(os.path.dirname(__file__), "e0_c01.json"))
