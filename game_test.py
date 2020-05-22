"""Testy modułu game"""

import unittest

import game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = game.Game()

    def test_run(self):
        pass

    def test_handle_events(self):
        pass

    def test_reset(self):
        pass


class MainTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
