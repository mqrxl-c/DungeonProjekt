from random import randint


class Monster:
    def __init__(self, name):
        self.name = name
        self.health = randint(40, 81)
        self.max_health = self.health
        self.strength = randint(20, 41)

    def __str__(self):
        return ("The Monster: " + self.name + " has strength: "
                + str(self.strength) + " and health: " + str(self.health))

    def take_damage(self, damage):
        '''give the monster damage and returns if it is still alive'''
        self.health -= damage
        if self.health <= 0:
            return False
        return True

    def return_damage_taken(self):
        ## return health to player
        return int(self.max_health / 2)
