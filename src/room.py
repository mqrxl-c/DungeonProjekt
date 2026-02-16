from utils import print_line
from rich import print
from time import sleep


class Room:
    def __init__(self, index, monster, player):
        self.name = "Room " + str(index + 1)

        ## Class References
        self.monster = monster
        self.player = player

    def run_room(self):
        run = True
        while run:

            ## Print Room Info
            print_line()
            print(self.name)
            print(self.monster.health_bar())
            print(self.player.health_bar())

            print(self.monster.image)

            print_line()

            ## Print Possible Actions
            print(r"[A]ttack")
            print(r"[F]lee")

            ## Check if Player Input is valid
            selection = input()
            invalid = True
            while invalid:
                if selection.lower() in ["a", "f", "flee", "attack"]:
                    invalid = False

                    ## handle player input
                    if selection.lower() == "a":
                        self.player_attack()
                    elif selection.lower() == "f":
                        self.player_flee()
                        run = False
                else:
                    invalid = True
                    print("Please enter a valid option")
                    selection = input()

            ## check if the monster is alive and do its action
            if self.monster.health > 0 and not selection.lower() == "f":
                self.monster_attack()

            elif self.monster.health <= 0:
                ## if the monster died set the loop to false
                run = False

                ## heal player and output info
                self.player.damage_done += self.monster.max_health
                self.player.regain_health(round(self.monster.max_health / 2))
                print(self.player.name + " regenerated " +
                      str(round(self.monster.max_health / 2)) + " health!")

    def player_attack(self):
        ## print players attack info
        print_line()
        self.monster.take_damage(self.player.strength)
        print(self.monster.name + " took " + str(self.player.strength)
              + " damage!")
        print(self.monster.__str__())

        ## wait for next frame
        sleep(2)

    def player_flee(self):
        ## print player flee info
        print_line()
        self.player.take_damage(10)
        print(self.player.name + " escaped and took 10 damage!")
        print(self.player.__str__())

        ## wait for next frame
        sleep(2)

    def monster_attack(self):
        ## print monster attack info
        print_line()
        self.player.take_damage(self.monster.strength)
        print("The Monster, " + self.monster.name + " attacked!")
        print(self.player.name + " took " + str(self.monster.strength)
              + " damage!")
        print(self.player.__str__())

        ## wait for next frame
        sleep(2)
