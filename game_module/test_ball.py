"""Testy modułu ball"""

import unittest

from game_module import ball
from game_module import constants


class TestBall(unittest.TestCase):
    """Testy klasy Ball"""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów"""

        self.ball = ball.Ball()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów"""

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych"""

        self.assertEqual(self.ball.width, int(constants.BALL_WIDTH))
        self.assertEqual(self.ball.height, int(constants.BALL_HEIGHT))
        self.assertEqual(self.ball.start_x_cord, int(constants.BALL_START_X))
        self.assertEqual(self.ball.start_y_cord, int(constants.BALL_START_Y))
        self.assertEqual(self.ball.x_cord, int(self.ball.start_x_cord))
        self.assertEqual(self.ball.y_cord, int(self.ball.start_y_cord))
        self.assertEqual(self.ball.color, constants.COLOR_BALL)
        self.assertEqual(self.ball.speed, constants.BALL_SPEED)
        self.assertEqual(self.ball.direction, 150)

    def test_reset(self):
        """Test metody reset()"""

        self.ball.reset()  # wywołanie testowanej funkcji

        # sprawdzenie poprawności wyników
        self.assertEqual(self.ball.x_cord, self.ball.start_x_cord)
        self.assertEqual(self.ball.y_cord, self.ball.start_y_cord)
        self.assertEqual(self.ball.direction, 150)

    def test_bounce(self):
        """Test metody bounce()"""

        self.ball.bounce(0)
        self.assertEqual(self.ball.direction, 30)

        self.ball.direction = 150
        self.ball.bounce(10)
        self.assertEqual(self.ball.direction, 40)

        self.ball.direction = 150
        self.ball.bounce(20)
        self.assertEqual(self.ball.direction, 50)

    def test_move(self):
        """Test metody move()"""

        # self.ball.move()

    def test_draw(self):
        """Testy metody draw()"""


if __name__ == '__main__':
    unittest.main()
