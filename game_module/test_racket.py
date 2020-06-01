"""Testy modułu racket."""

import unittest

from game_module import constants
from game_module import racket
import game


class TestRacket(unittest.TestCase):
    """Testy klasy Racket."""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów."""

        self.racket = racket.Racket()
        self.game = game.Game()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów."""

        del self.racket, self.game

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych."""

        self.assertEqual(self.racket.width, constants.RACKET_WIDTH)
        self.assertEqual(self.racket.height, constants.RACKET_HEIGHT)
        self.assertEqual(self.racket.x_cord, 0)
        self.assertEqual(self.racket.y_cord, constants.RESOLUTIONS[0][1] - 40)
        self.assertEqual(self.racket.color, constants.RACKET_COLOR)

    def test_move(self):
        """Test metody move()."""

    def test_draw(self):
        """Test metody draw()."""

        self.racket.draw(self.game.window)


if __name__ == '__main__':
    unittest.main()
