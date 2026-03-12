
"""
Wegen fehler bei den Imports für die Test Dateien.
Code nimmt den Absoluten Pfad des Projektes und hängt es vorne an die Imports an.
Dadurch sind die Eigenen dateien auch nicht relativ sondern mit src... eingebunden.
Genaueres in der Doku
"""

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.controller import Controller
from src.Player import Player
from src.utils import print_line

if __name__ == "__main__":

    print("Game Starting..")

    name = input("Enter your name: ")
    player = Player(name)
    controller = Controller(player)

    controller.run_menu()