from rich import print
from time import sleep

from utils import print_line


class Room:
    def __init__(self, name, monster, player):
        self.name = name

        ## Class References
        self.monster = monster
        self.player = player
    
    def handle_input(self):
        '''Handles Player input in fight'''
        selection = input()
        invalid = True
        while invalid:
            if selection.lower() in ["a", "attack"]:
                invalid = False

                ## handle player input
                if selection.lower() in ["a", "attack"]:
                    self.player_attack()
                return selection
            else:
                invalid = True
                print("Please enter a valid option")
                selection = input()
    
    def print_room(self):
        '''Prints Room Info'''
        print_line()
        print(self.name)
        print(self.monster.health_bar())
        print(self.player.health_bar())

        print(self.monster.image)

        print_line()

    def start_room(self):
        
        self.print_room()

        ## Print Possible Actions
        print(r"[F]ight")
        print(r"[R]un")

        selection = input()
        invalid = True
        while invalid:
            if selection.lower() in ["r", "f", "fight", "run"]:
                invalid = False

                    ## handle player input
                if selection.lower() == "f":
                    self.monster_attack()
                    self.run_room()
                elif selection.lower() == "r":
                    self.player_flee()
            else:
                invalid = True
                print("Please enter a valid option")
                selection = input()

    def run_room(self):
        run = True
        while run:
            
            self.print_room()

            ## Print Possible Actions
            print(r"[A]ttack")

            self.handle_input()

            ## check if the monster is alive and do its action
            if self.monster.health > 0:
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
