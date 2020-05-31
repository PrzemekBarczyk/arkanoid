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

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych."""

        self.assertEqual(self.window.width, constants.RESOLUTIONS[0][0])
        self.assertEqual(self.window.height, constants.RESOLUTIONS[0][1])

    def test_update(self):
        """Testy metody update()."""

    def test_draw(self):
        """Testy metody draw()."""
