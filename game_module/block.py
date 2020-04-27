"""Klasa klocków"""

import pygame
from game_module import constants


class Block:
    """Klasa zawierające klocki, które gracz może zbijać przy użyciu piłki
    Jeden obiekt = jeden klocke"""

    def __init__(self, x, y):
        self.width = constants.BLOCK_WIDTH
        self.height = constants.BLOCK_HEIGHT
        self.color = constants.COLOR_BLOCK

        # utworzenie powierzchni obiektu
        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        self.surface.fill(constants.COLOR_BLOCK) # pokolorowanie powierzchni
        self.rect = self.surface.get_rect(x=x, y=y)  # ustawienie prostokąta zawierającego obiekt w początkowej pozycji

    def draw(self, window):
        """Rysuje bloki w oknie"""
        window.surface.blit(self.surface, self.rect)
