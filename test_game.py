"""Testy modułu game"""

import unittest

import game
from game_module import ball
from game_module import judge
from game_module import level
from game_module import window
from game_module import racket


class TestGame(unittest.TestCase):
    """Testy klasy Game"""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów"""
        self.game = game.Game()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów"""
        pass

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych"""
        self.assertIsInstance(self.game.window, window.Window)
        self.assertIsInstance(self.game.ball, ball.Ball)
        self.assertIsInstance(self.game.player, racket.Racket)
        self.assertIsInstance(self.game.judge, judge.Judge)
        self.assertIsInstance(self.game.level, level.Level)

    def test_run(self):
        """Test działania funkcji run()"""
        self.game.run()

    def test_handle_events(self):
        """Test działania funkcji handle_events()"""
        self.game.handle_events()

    def test_reset(self):
        """Test działania funkcji reset()"""
        self.game.reset()


class TestElse(unittest.TestCase):
    """Testy pozostałych funkcji"""

    def test_main(self):
        """Test działania funkcji main()"""
        pass


if __name__ == '__main__':
    unittest.main()
