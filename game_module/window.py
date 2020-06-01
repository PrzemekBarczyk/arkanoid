"""Moduł zawierający klasę okna."""

import pygame

from game_module import constants


class Window:
    """Klasa okna:

    Odpowiada za okno programu i wyświetlanie odpowiedniego menu.
    Zmienna surface wymagana przy rysowaniu innych obiektów w okienku programu."""

    def __init__(self):
        """Konstruktor tworzy okienko programu."""

        self.width = constants.RESOLUTIONS[0][0]
        self.height = constants.RESOLUTIONS[0][1]

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Half-Life 3')

    def update(self, new_resolution, flags):
        """Zmienia rozmiar okna programu."""

        self.width = new_resolution[0]
        self.height = new_resolution[1]
        self.surface = pygame.display.set_mode((self.width, self.height), flags)

    def draw(self):
        """Wypełnia 'powierzchnie' kolorem."""

        self.surface.fill(constants.BACKGROUND_COLOR)
