"""Klasa przycisków"""

import pygame
from game_module import constants
from game_module import window


class Button:
    """Klasa zawierające przyciski z menu, które gracz może wybrać przy użyciu kursora myszki
    zaznaczając ich pole i klikając LPM"""

    def __init__(self, name, x, y, width=constants.BUTTON_WIDTH, height=constants.BUTTON_HEIGHT,
                 button_color=constants.COLOR_BUTTON, text_color=(255, 255, 255)):
        """Kontruktor"""
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_color = button_color
        self.text_color = text_color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        """Rysuje przycisk"""
        pygame.draw.rect(window.surface, self.button_color, self.rect) # rysuje tło przycisku

        text_obj = constants.FONT_OPTIONS.render(self.name, True, self.text_color)
        text_rect = text_obj.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        window.surface.blit(text_obj, text_rect)
