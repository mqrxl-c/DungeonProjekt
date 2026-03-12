from rich import print

from monster import Monster
from utils import print_line, check_input_number, randomize_name
from room import Room


class Controller:
    def __init__(self, player):
        self.room_list = []
        self.player = player

    def run_menu(self):
        print_line()
        print("Welcome " + self.player.name + " to Dungeon Run!")
        print_line()

        print("[S]tart")
        print("[H]ow to play")
        ##print("[O]ptions")
        print("[Q]uit")

        ## Check if Player Input is valid
        selection = input()
        invalid = True
        while invalid:
            if selection.lower() in ["s", "h", "o", "q", "quit", "option",
                                     "start", "how to play"]:
                invalid = False

                ## handle player input
                if selection.lower() == "s":
                    self.init_game()
                elif selection.lower() == "h":
                    self.print_description()
                elif selection.lower() == "q":
                    break
            else:
                invalid = True
                print("Please enter a valid option")
                selection = input()

    def print_description(self):
        print_line()
        print("Game Info / Tut")
        input("Press enter to back")
        self.run_menu()

    def init_game(self):
        '''initializes the rooms from user input'''

        print_line()

        room_amount = check_input_number("How many rooms do you want to play?")

        input("Press enter to init game with " + str(room_amount) + " rooms.")

        for i in range(room_amount):
            print_line()
            print("Room " + str(i + 1))
            print("Enter a name for the room. Default: Room " + str(i + 1) )
            room_name = input()

            if room_name == "":
                room_name = "Room " + str(i + 1)
            else:
                room_name = "Room: " + room_name

            print("Enter a name for the monster. "
                  "If left empty the game will select a random name.")

            monster_name = input()

            if monster_name == "":
                monster_name = randomize_name()

            monster = Monster(monster_name)
            self.room_list.append(Room(room_name, monster, self.player))

        print("Setup for " + str(room_amount) + " rooms finished.")
        self.run_game()

    def run_game(self):
        '''runs all rooms and handles win and Lose'''
        for room in self.room_list:
            if self.player.health > 0:
                input("Press Enter to continue to the next room...")
                room.start_room()
            else:
                break

        if self.player.health > 0:
            ## print Win message and stats
            print_line()
            print("You Won!")
            print("You finished " + str(len(self.room_list)) +
                " rooms and made " + str(self.player.damage_done) + " damage!")    

        else:
            ## if player is dead print Lose message and stats
            print_line()
            print("You Lost!")
            print("You finished " + str(len(self.room_list)) +
                " rooms and made " + str(self.player.damage_done) + " damage!")
        
        input("Press Enter to return to Menu...")
        self.run_menu()