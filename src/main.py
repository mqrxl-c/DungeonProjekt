from controller import Controller
from Player import Player
from utils import print_line

if __name__ == "__main__":

    print("Game Starting..")

    name = input("Enter your name: ")
    player = Player(name)
    controller = Controller(player)

    controller.run_menu()