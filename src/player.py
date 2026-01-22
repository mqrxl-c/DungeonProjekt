from random import randint


class Player:
    def __init__(self, name : str="Name"):
        self.name = name
        self.health = 100
        self.strength = randint(40, 81)
        self.max_health = self.health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            ## die
            pass

    def __str__(self):
        return (self.name + " has strength: " + str(self.strength)
                + " and health: " + str(self.health))

    def regain_health(self, health_regain):
        self.health += health_regain
        if self.health > self.max_health:
            self.health = self.max_health

    def return_strength(self):
        return self.strength