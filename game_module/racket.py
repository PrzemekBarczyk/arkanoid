"""Moduł zawierający klase rakietki"""

import pygame
from game_module import constants


class Racket:
    """Klasa rakietki gracza:

    Porusza się w osi X sterowana przez gracza za pomocą myszy."""

    def __init__(self):
        """Konstruktor inicjalizuje zmienne i tworzy powierzchnie piłki"""

        self.width = constants.RACKET_WIDTH
        self.height = constants.RACKET_HEIGHT
        self.x_cord = constants.WINDOW_WIDTH/2 - constants.RACKET_WIDTH/2
        self.y_cord = constants.WINDOW_HEIGHT-40
        self.color = constants.COLOR_RACKET

        # konfiguruje kształt rakietki
        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        self.surface.fill(self.color)  # pokolorowanie powierzchni
        # ustawienie prostokąta zawierającego obiekt w początkowej pozycji
        self.rect = self.surface.get_rect(x=self.x_cord, y=self.y_cord)

    def move(self, x_cord):
        """Przesuwa rakietkę o wyznaczone miejsce"""

        # wyznacza przesunięcie paletki gracza
        x_cord_new = x_cord - (self.width / 2)  # wyznacza nowe współrzędne paletki

        # paletka wykracza poza okno gry w prawo
        if x_cord_new > constants.WINDOW_WIDTH - self.width:
            x_cord_new = constants.WINDOW_WIDTH - self.width
        # paletka wykracza poza okno gry w lewo
        elif x_cord_new < 0:
            x_cord_new = 0

        # aktualizuje położenie paletki w poziomie
        self.rect.x = x_cord_new

    def draw(self, window):
        """Rysuje piłkę w oknie"""

        window.surface.blit(self.surface, self.rect)
