
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.player import Player
import unittest


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_regain_health(self):

        self.player.health = 50

        ## checkt nach health increase, der nicht über 100 kommen kann
        self.player.regain_health(25)
        assert self.player.health == 75

        ## checkt ob health overfilled
        self.player.regain_health(50)
        assert self.player.health == 100

        self.player.health = 50
        
        ## check for float input
        self.player.regain_health(9.9)
        assert self.player.health == 60

        self.player.regain_health(9.1)
        assert self.player.health == 69
    
    def test_take_damage(self):
        self.player.health = 100

        self.player.take_damage(20)
        assert self.player.health == 80

        ## check for float input
        self.player.take_damage(9.9)
        assert self.player.health == 70

        self.player.take_damage(9.1)
        assert self.player.health == 61

    def test_health_bar(self):
        self.player.health = 100
        expected = "Name HP: "+ ":red_heart-emoji: " * 10 + ":black_heart-emoji: " * (10 - 10) + "100/100"
        self.assertEqual(self.player.health_bar(), expected)
    
    def test_player_string(self):
        ## checkt ob __str__ richig ausgibt
        expected = "Name has strength: 40 and health: 100"
        self.player.health = 100
        self.player.strength = 40
        self.assertEqual(self.player.__str__(), expected)


if __name__ == "__main__":
    unittest.main()

    