from random import randint

from src.utils import ascii_image_list


class Monster:
    def __init__(self, name):
        self.name = name
        self.health = randint(40, 80)
        self.max_health = self.health
        self.strength = randint(20, 40)

        int = randint(0, len(ascii_image_list) - 1)
        self.image = ascii_image_list[int]

    def __str__(self):
        if self.health <= 0:
            return "The Monster, " + self.name + ", is dead."
        return ("The Monster, " + self.name + ", has " + str(self.health)
                + " health")

    def take_damage(self, damage):
        self.health -= round(damage)

    def return_damage_taken(self):
        ## return health to player
        return int(self.max_health / 2)

    def health_bar(self):
        '''returns the string for a visual health bar'''
        full = round(self.max_health / 10)
        amount = round(self.health / 10)

        string = (str(self.name) + " HP: "+ ":red_heart-emoji: " * amount
                  + ":black_heart-emoji: " * (full - amount)
                  + str(self.health) + "/" + str(self.max_health))
        return string