import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR) + "/src")

import unittest

from utils import *


class UtilsTest(unittest.TestCase):
    def test_randomized_name(self):
        assert randomize_name() in name_list
    
    def test_check_input_number(self):
        assert type(check_input_number(text="input1 ")) is int

        assert check_input_number(text="input2 ", min_value=1) >= 1

        assert check_input_number(text="input3 ", max_value = 1) <= 1


if __name__ == "__main__":
    unittest.main()
