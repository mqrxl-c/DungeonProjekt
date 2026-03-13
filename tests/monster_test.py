## Wegen Probleme mit Import wird der Dateipfad zu src vor die Imports
# angehängt. In Doku genaueres
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR) + "/src")

import unittest

from monster import Monster


class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster = Monster("Name")
    
    def test_take_damage(self):
        self.monster.health = 100

        self.monster.take_damage(20)
        assert self.monster.health == 80

        ## check for float input
        self.monster.take_damage(9.9)
        assert self.monster.health == 70

        self.monster.take_damage(9.1)
        assert self.monster.health == 61

        self.monster.take_damage(-10)
        assert self.monster.health == 71

    def test_health_bar(self):
        self.monster.health = 100
        self.monster.max_health = 100
        expected = "Name HP: "+ ":red_heart-emoji: " * 10 + "100/100"
        self.assertEqual(self.monster.health_bar(), expected)
        assert type(self.monster.health_bar()) is str
    
    def test_monster_string(self):
        ## checkt ob __str__ richig ausgibt
        expected = "The Monster, Name, has 100 health"
        self.monster.health = 100
        self.monster.strength = 40
        self.assertEqual(self.monster.__str__(), expected)

        self.monster.health = 0
        expected = "The Monster, Name, is dead."
        self.assertEqual(self.monster.__str__(), expected)

        assert type(self.monster.__str__()) is str
    
    def test_return_damage_taken(self):
        assert type(self.monster.return_damage_taken()) is int


if __name__ == "__main__":
    unittest.main()

    