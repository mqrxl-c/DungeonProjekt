

class Room:
    def __init__(self, count, monster, player):
        self.name = "Room " + str(count)
        self.monster = monster
        self.player = player

    def room_loop(self):
        ## erste room info

        while self.monster.health > 0:
            ## angreifen oder fliehen
            pass

        ## monster tot
        self.player.regain_health(self.monster.return_damage_taken())