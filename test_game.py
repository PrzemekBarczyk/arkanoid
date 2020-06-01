"""Testy modułu game."""
# pylint: disable=no-member

import unittest

import pygame

import game
from game_module import ball
from game_module import judge
from game_module import level
from game_module import racket
from game_module import window


class TestGame(unittest.TestCase):
    """Testy klasy Game."""

    def setUp(self):
        """Uruchamia się przed wykonaniem każdego z testów."""

        self.game = game.Game()

    def tearDown(self):
        """Uruchamia się po wykonaniu każdego z testów."""

        del self.game

    def test_default_vaules(self):
        """Test poprawności iniicjalizacji danych."""

        # sprawdzam czy w trakcie inicjalizacji utworzono obiekty odpowiednich klas
        self.assertIsInstance(self.game.window, window.Window)
        self.assertIsInstance(self.game.ball, ball.Ball)
        self.assertIsInstance(self.game.player, racket.Racket)
        self.assertIsInstance(self.game.judge, judge.Judge)
        self.assertIsInstance(self.game.level, level.Level)

    def test_run(self):
        """Test działania metody run()."""

        # sprawdzam czy metoda rzuca odpowiedni wyjątek
        self.assertRaises(SystemExit, lambda: self.game.run())  # wywołanie testowanej metody

    def test_handle_events(self):
        """Test działania metody handle_events()."""

        # sprawdzam czy zwracane wartości są poprawne w zależności od otrzymanych zdarzeń
        return_value = self.game.handle_events()  # wywołanie testowanej metody
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.assertTrue(return_value)
            else:
                self.assertFalse(return_value)

    def test_update(self):
        """Testy działania metody update()."""

        # sprawdzam czy dane zostały poprawnie zaaktualizowane
        self.game.update()  # wywołanie testowanej metody
        self.assertEqual(self.game.player.y_cord, self.game.window.height - 40)
        self.assertEqual(self.game.player.rect,
                         self.game.player.surface.get_rect(x=int(self.game.player.x_cord),
                                                           y=int(self.game.player.y_cord)))

    def test_reset(self):
        """Test działania metody reset()."""

        # sprawdzam czy wartości są odpowiednie po resecie gry
        self.game.reset()  # wywołanie testowanej metody
        self.assertEqual(self.game.ball.x_cord, self.game.ball.start_x_cord)
        self.assertEqual(self.game.ball.y_cord, self.game.ball.start_y_cord)
        self.assertEqual(self.game.ball.direction, 150)
        self.assertEqual(self.game.judge.lifes, 3)


if __name__ == '__main__':
    unittest.main()
