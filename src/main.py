from controller import Controller
from player import Player
from utils import print_line

if __name__ == "__main__":

    print("Game Starting..")

    name = input("Enter your name: ")
    player = Player(name)
    controller = Controller(player)

    print_line()

    controller.init_game()
    controller.run_game()