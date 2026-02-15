from utils import print_line
from rich import print
from time import sleep

class Room:
    def __init__(self, index, monster, player):
        self.name = "Room " + str(index + 1)

        self.monster = monster
        self.player = player

    def run_room(self):
        while self.monster.health >= 0:

            print_line()
            print(self.monster.health_bar())
            print(self.player.health_bar())

            print(self.monster.image)

            print_line()

            print(r"[A]ttack")
            print(r"[F]lee")

            selection = input()
            if selection.lower() == "a":
                self.player_attack()
            elif selection.lower() == "f":
                self.player_flee()
                pass

            if self.monster.health >= 0 and not selection.lower() == "f":
                self.monster_attack()

        input("Press Enter to continue to the next room...")

    def player_attack(self):
        print_line()
        self.monster.take_damage(self.player.strength)
        print(self.monster.name + " took " + str(self.player.strength) + " damage!")
        print(self.monster.__str__())
        sleep(2)

    def player_flee(self):
        print_line()
        self.player.take_damage(10)
        print(self.player.name + " escaped and took 10 damage!")
        print(self.player.__str__())
        sleep(2)

    def monster_attack(self):
        print_line()
        self.player.take_damage(self.monster.strength)
        print("The Monster, " + self.monster.name + " attacked!")
        print(self.player.name + " took " + str(self.monster.strength) + " damage!")
        print(self.player.__str__())
        sleep(2)
