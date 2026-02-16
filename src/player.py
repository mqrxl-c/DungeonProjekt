from random import randint


class Player:
    def __init__(self, name : str="Name"):
        self.name = name
        self.health = 100
        self.strength = randint(40, 81)
        self.max_health = self.health

        self.damage_done = 0

    def take_damage(self, damage):
        self.health -= damage

    def __str__(self):
        if self.health <= 0:
            return "The Player, " + self.name + ", is dead."
        return (self.name + " has strength: " + str(self.strength)
                + " and health: " + str(self.health))

    def regain_health(self, health_regain):
        self.health += health_regain
        if self.health > self.max_health:
            self.health = self.max_health

    def health_bar(self):
        '''returns the string for a visual health bar'''
        full = round(self.max_health / 10)
        amount = round(self.health / 10)

        string = (str(self.name) + " HP: "+ ":red_heart-emoji: " * amount
                  + ":black_heart-emoji: " * (full - amount) + str(self.health)
                  + "/" + str(self.max_health))
        return string