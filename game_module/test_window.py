"""Testy modułu window."""

import unittest

from game_module import constants
from game_module import window


class TestGame(unittest.TestCase):
    """Testy klasy Window."""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów."""

        self.window = window.Window()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów."""

        del self.window

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych."""

        self.assertEqual(self.window.width, constants.RESOLUTIONS[0][0])
        self.assertEqual(self.window.height, constants.RESOLUTIONS[0][1])

    def test_update(self):
        """Testy metody update()."""

        self.window.update((1920, 1080), 0)
        self.assertEqual(self.window.width, 1920)
        self.assertEqual(self.window.height, 1080)

    def test_draw(self):
        """Testy metody draw()."""

        self.window.draw()


if __name__ == '__main__':
    unittest.main()
