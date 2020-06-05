"""Testy modułu window."""
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

import unittest
import pygame

from game_module import constants
from game_module import window


class WindowTest(unittest.TestCase):

    def setUp(self):

        self.window = window.Window()

    def test_default_vaules(self):

        self.assertEqual(self.window.width, constants.RESOLUTIONS[0][0])  # 800
        self.assertEqual(self.window.height, constants.RESOLUTIONS[0][1])  # 600
        self.assertEqual(self.window.width, 800)
        self.assertEqual(self.window.height, 600)

    def test_update(self):

        # metoda aktualizuję dane w poprawny sposób
        self.window.update((1920, 1080), 0)
        self.assertEqual(self.window.width, 1920)
        self.assertEqual(self.window.height, 1080)
        self.window.update((1366, 768), 1)
        self.assertEqual(self.window.width, 1366)
        self.assertEqual(self.window.height, 768)

        # metoda rzuca odpowiedni wyjątek dla błędych danych
        with self.assertRaises(pygame.error):
            self.window.update((-100, -50), 1)
        with self.assertRaises(TypeError):
            self.window.update(("", 100), 0)

        # metoda nie rzuca wyjątków dla poprawnych danych
        try:
            self.window.update((1366, 768), 1)
            self.window.update((30, 400), 0)
            self.window.update((100, 100), 1)
        except:
            self.assertTrue(False)

    def test_draw(self):

        self.assertIsNone(self.window.draw())  # funkcja nic nie zwraca

        # metoda wykorzystana w testowanej metodzie zwraca obiekt który jest instancją klasy Rect
        self.assertIsInstance(self.window.surface.fill((255, 0, 0)), pygame.Rect)

        # metoda rzuca wyjątki dla błędych danych
        with self.assertRaises(TypeError):
            constants.BACKGROUND_COLOR = (-255, 0, 0)  # stała wykorzystywana wewnątrz metody
            self.window.draw()
        with self.assertRaises(TypeError):
            constants.BACKGROUND_COLOR = (0, "0")
            self.window.draw()
        with self.assertRaises(TypeError):
            constants.BACKGROUND_COLOR = (0, 0, 4324123)
            self.window.draw()

        # metoda nie rzuca wyjątku dla poprawnych danych
        try:
            constants.BACKGROUND_COLOR = (255, 0, 0)  # stała wykorzystywana wewnątrz metody
            self.window.draw()
            constants.BACKGROUND_COLOR = (123, 255, 12)
            self.window.draw()
            constants.BACKGROUND_COLOR = (5, 0, 43)
            self.window.draw()
        except:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
