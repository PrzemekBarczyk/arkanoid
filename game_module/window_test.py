"""Testy modułu window."""
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest

from game_module import constants
from game_module import window


class WindowTest(unittest.TestCase):

    def setUp(self):

        self.window = window.Window()

    def test_default_vaules(self):

        self.assertEqual(self.window.width, constants.RESOLUTIONS[0][0])
        self.assertEqual(self.window.height, constants.RESOLUTIONS[0][1])

    def test_update(self):

        self.window.update((1920, 1080), 0)
        self.assertEqual(self.window.width, 1920)
        self.assertEqual(self.window.height, 1080)


if __name__ == '__main__':
    unittest.main()
