"""Testy modułu window"""

import unittest

from game_module import window
from game_module import constants


class TestGame(unittest.TestCase):

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów"""
        self.window = window.Window()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów"""
        pass

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych"""
        self.assertEqual(self.window.width, constants.WINDOW_WIDTH)
        self.assertEqual(self.window.height, constants.WINDOW_HEIGHT)

    def test_draw(self):
        pass

    def test_main_menu(self):
        pass

    def test_options_menu(self):
        pass

    def test_pause_menu(self):
        pass

    def test_win_menu(self):
        pass

    def test_print_headline(self):
        pass


class TestElse(unittest.TestCase):
    def test_check_which_button(self):
        pass
