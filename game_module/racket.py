"""Klasa rakietki"""

import pygame
from game_module import constants


class Racket:
    """Rakietka, porusza się w osi X z ograniczeniem prędkości"""

    def __init__(self):
        self.width = constants.RACKET_WIDTH
        self.height = constants.RACKET_HEIGHT
        self.x_cord = constants.WINDOW_WIDTH/2 - constants.RACKET_WIDTH/2
        self.y_cord = constants.WINDOW_HEIGHT-40
        self.color = constants.COLOR_RACKET

        # konfiguruje kształt rakietki
        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        self.surface.fill(self.color)  # pokolorowanie powierzchni
        self.rect = self.surface.get_rect(x=self.x_cord, y=self.y_cord)  # ustawienie prostokąta ...
        # zawierającego obiekt w początkowej pozycji

    def move(self, x_cord):
        """Przesuwa rakietkę o wyznaczone miejsce"""
        # oblicz przesunięcie paletki gracza
        x_cord_new = x_cord - (self.width / 2)  # wyznacza nowe współrzędne paletki

        # jeżeli wykraczamy poza okno gry w prawo
        if x_cord_new > constants.WINDOW_WIDTH - self.width:
            x_cord_new = constants.WINDOW_WIDTH - self.width
        # jeżeli wykraczamy poza okno gry w lewo
        if x_cord_new < 0:
            x_cord_new = 0
        # zaktualizuj położenie paletki w poziomie
        self.rect.x = x_cord_new

    def draw(self, window):
        """Rysuje piłkę w oknie"""
        window.surface.blit(self.surface, self.rect)
