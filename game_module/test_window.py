"""Testy modułu window"""

import unittest

from game_module import window
from game_module import constants


class TestGame(unittest.TestCase):
    """Testy klasy Window"""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów"""

        self.window = window.Window()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów"""

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych"""

        self.assertEqual(self.window.width, constants.WINDOW_WIDTH)
        self.assertEqual(self.window.height, constants.WINDOW_HEIGHT)

    def test_update(self):
        """Testy metody update()"""

    def test_draw(self):
        """Testy metody draw()"""
