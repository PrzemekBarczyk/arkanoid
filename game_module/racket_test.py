"""Testy modułu racket."""
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

from game_module import constants
from game_module import racket
import game


class RacketTest(unittest.TestCase):

    def setUp(self):

        self.racket = racket.Racket()
        self.game = game.Game()

    def test_default_vaules(self):

        self.assertEqual(self.racket.width, constants.RACKET_WIDTH)
        self.assertEqual(self.racket.height, constants.RACKET_HEIGHT)
        self.assertEqual(self.racket.x_cord, 0)
        self.assertEqual(self.racket.y_cord, constants.RESOLUTIONS[0][1] - 40)
        self.assertEqual(self.racket.color, constants.RACKET_COLOR)


if __name__ == '__main__':
    unittest.main()
