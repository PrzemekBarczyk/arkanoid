"""Testy moduły game."""
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import unittest

import game
from game_module import ball
from game_module import judge
from game_module import level
from game_module import racket
from game_module import window


class GameTest(unittest.TestCase):

    def setUp(self):

        self.game = game.Game()

    def test_default_vaules(self):

        # sprawdzam czy w trakcie inicjalizacji utworzono obiekty odpowiednich klas
        self.assertIsInstance(self.game.window, window.Window)
        self.assertIsInstance(self.game.ball, ball.Ball)
        self.assertIsInstance(self.game.player, racket.Racket)
        self.assertIsInstance(self.game.judge, judge.Judge)
        self.assertIsInstance(self.game.level, level.Level)

    def test_update(self):

        # sprawdzam czy dane zostały poprawnie zaaktualizowane
        self.game.update()  # wywołanie testowanej metody
        self.assertEqual(self.game.player.y_cord, self.game.window.height - 40)
        self.assertEqual(self.game.player.rect,
                         self.game.player.surface.get_rect(x=int(self.game.player.x_cord),
                                                           y=int(self.game.player.y_cord)))

    def test_reset(self):

        # sprawdzam czy wartości są odpowiednie po resecie gry
        self.game.reset()  # wywołanie testowanej metody
        self.assertEqual(self.game.ball.x_cord, self.game.ball.start_x_cord)
        self.assertEqual(self.game.ball.y_cord, self.game.ball.start_y_cord)
        self.assertEqual(self.game.ball.direction, 150)
        self.assertEqual(self.game.judge.lives, 3)


if __name__ == '__main__':
    unittest.main()
