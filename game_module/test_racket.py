"""Testy modułu racket"""

import unittest

from game_module import racket
from game_module import constants


class TestRacket(unittest.TestCase):
    """Testy klasy Racket"""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów"""

        self.racket = racket.Racket()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów"""

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych"""

        self.assertEqual(self.racket.width, constants.RACKET_WIDTH)
        self.assertEqual(self.racket.height, constants.RACKET_HEIGHT)
        self.assertEqual(self.racket.x_cord, constants.RACKET_X)
        self.assertEqual(self.racket.y_cord, constants.RACKET_Y)
        self.assertEqual(self.racket.color, constants.COLOR_RACKET)

    def test_move(self):
        """Test metody move()"""

    def test_draw(self):
        """Test metody draw()"""
