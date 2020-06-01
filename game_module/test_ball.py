"""Testy modułu ball."""

import unittest

from game_module import ball
from game_module import constants
import game


class TestBall(unittest.TestCase):
    """Testy klasy Ball."""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów."""

        self.ball = ball.Ball()
        self.game = game.Game()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów."""

        del self.ball, self.game

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych."""

        # sprawdzam czy w trakcie inicjalizacji utworzono obiekty o odpowiednich wartościach
        self.assertEqual(self.ball.width, int(constants.BALL_WIDTH))
        self.assertEqual(self.ball.height, int(constants.BALL_HEIGHT))
        self.assertEqual(self.ball.start_x_cord, int(constants.BALL_START_X))
        self.assertEqual(self.ball.start_y_cord, int(constants.BALL_START_Y))
        self.assertEqual(self.ball.x_cord, int(self.ball.start_x_cord))
        self.assertEqual(self.ball.y_cord, int(self.ball.start_y_cord))
        self.assertEqual(self.ball.color, constants.BALL_COLOR)
        self.assertEqual(self.ball.speed, constants.BALL_SPEED)
        self.assertEqual(self.ball.direction, 150)

    def test_reset(self):
        """Test metody reset()."""

        self.ball.reset()  # wywołanie testowanej metody

        # sprawdzenie poprawności wyników
        self.assertEqual(self.ball.x_cord, self.ball.start_x_cord)
        self.assertEqual(self.ball.y_cord, self.ball.start_y_cord)
        self.assertEqual(self.ball.direction, 150)

    def test_bounce(self):
        """Test metody bounce()."""

        self.ball.bounce(0)
        self.assertEqual(self.ball.direction, 30)

        self.ball.direction = 150
        self.ball.bounce(10)
        self.assertEqual(self.ball.direction, 40)

        self.ball.direction = 150
        self.ball.bounce(20)
        self.assertEqual(self.ball.direction, 50)

    def test_move(self):
        """Test metody move()."""

        self.ball.move(self.game.player, self.game.level.blocks, self.game.window,
                       self, self.game.judge)

    def test_draw(self):
        """Testy metody draw()."""

        self.ball.draw(self.game.window)


if __name__ == '__main__':
    unittest.main()
