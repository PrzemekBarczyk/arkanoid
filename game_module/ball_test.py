"""Testy modułu ball."""
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

from game_module import ball
from game_module import constants


class BallTest(unittest.TestCase):

    def setUp(self):

        self.ball = ball.Ball()

    def test_default_vaules(self):

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

        self.ball.reset()  # wywołanie testowanej metody

        # sprawdzenie poprawności wyników
        self.assertEqual(self.ball.x_cord, self.ball.start_x_cord)
        self.assertEqual(self.ball.y_cord, self.ball.start_y_cord)
        self.assertEqual(self.ball.direction, 150)

    def test_bounce(self):

        self.ball.bounce(0)
        self.assertEqual(self.ball.direction, 30)

        self.ball.direction = 150
        self.ball.bounce(10)
        self.assertEqual(self.ball.direction, 40)

        self.ball.direction = 150
        self.ball.bounce(20)
        self.assertEqual(self.ball.direction, 50)


if __name__ == '__main__':
    unittest.main()
