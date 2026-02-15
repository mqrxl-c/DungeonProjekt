from monster import Monster
from utils import print_line, check_input_number, randomize_name
from room import Room

from rich import print

class Controller:
    def __init__(self, player):
        self.room_list = []
        self.player = player

    def init_game(self):
        print("Welcome to Dungeon Run")
        print_line()

        room_amount = check_input_number("How many rooms do you want to play? ")

        input("Press enter to init game with " + str(room_amount) + " rooms.")

        for i in range(room_amount):
            print_line()
            print("Room " + str(i + 1))
            print("Enter a name for the monster. If left empty the game will select a random name.")

            name = input()

            if name == "":
                name = randomize_name()

            monster = Monster(name)

            self.room_list.append(Room(i, monster, self.player))

        print("Setup for " + str(room_amount) + " rooms finished.")

    def run_game(self):
        for room in self.room_list:
            room.run_room()

        print_line()
        print("You Won!")
        print("You finished " + str(len(self.room_list)) + " rooms and made " + str(self.player.damage_done) + " damage!")