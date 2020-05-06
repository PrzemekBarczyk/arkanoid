"""Moduł zawierający klase klocków"""

import pygame
from game_module import constants


class Block:
    """Klasa klocka:

    Klocek posiada swoje współrzędne, wymiary i kolor. Jeden obiekt = jeden klocek"""

    def __init__(self, x, y):
        """Konstruktor inicjalizuje zminne i tworzy powierzchnie klocka"""
        self.width = constants.BLOCK_WIDTH
        self.height = constants.BLOCK_HEIGHT
        self.color = constants.COLOR_BLOCK

        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        self.surface.fill(constants.COLOR_BLOCK) # pokolorowanie powierzchni
        self.rect = self.surface.get_rect(x=x, y=y)  # ustawienie prostokąta zawierającego obiekt w początkowej pozycji

    def draw(self, window):
        """Rysuje pojedyńczy klocek w oknie"""

        window.surface.blit(self.surface, self.rect)
