"""Wszystkie stałe występujące w programie, oraz klasa wczytująca czcionki."""
# pylint: disable=no-member

import pygame


class Fonts:  # pylint: disable=too-few-public-methods
    """Przechowuje czcionki."""

    FONT_HEADINGS = 0
    FONT_OPTIONS = 0

    @staticmethod
    def load():
        """Wczytuje czcionki z dysku."""

        pygame.init()  # biblioteki pygame
        pygame.font.init()  # czcionki

        Fonts.FONT_HEADINGS = pygame.font.SysFont(None, 60)  # czcionka nagłówków
        Fonts.FONT_OPTIONS = pygame.font.SysFont(None, 40)  # czcionka tekstów z menu'sów


# Okno i opcje---------------------------------------------------------------------------

# kolor tła okna
BACKGROUND_COLOR = (41, 39, 36)  # ciemny
# rozdzielczości okna
RESOLUTIONS = [(800, 600), (1200, 800)]
# tryb wyświetlania okna
FULLSCREEN = [0, pygame.FULLSCREEN]
# limity FPS'ów
FPS_LIMIT = [200, 300, 500]

# Piłka----------------------------------------------------------------------------------
BALL_SPEED = 3 # prędkość poruszania piłki
BALL_DIRECTION = 150  # początkowy kierunek poruszania piłki
# wymiary piłki
BALL_WIDTH = 15
BALL_HEIGHT = 15
# początkowe współrzędne piłki
BALL_START_X = 50
BALL_START_Y = 100
# kolor piłki
BALL_COLOR = (255, 15, 35)  # czerwony

# Racket-----------------------------------------
# wymiary paletki
RACKET_WIDTH = 80
RACKET_HEIGHT = 16
# kolor paletki
RACKET_COLOR = (70, 150, 60)  # ciemna zieleń

# Block------------------------------------------
# wymiary klocków
BLOCK_WIDTH = 96
BLOCK_HEIGHT = 25
# kolor klocków
BLOCK_COLOR = (34, 105, 125)  # niebieski

# Przyciski------------------------------------------------------------------------------

# wymiary przycisków
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 80

# kolor przycisków
BUTTON_COLOR = (62, 102, 138)  # niebiesko jakiś

# kolor napisów na przyciskach
BUTTON_TEXT_COLOR = (255, 255, 255)  # biały

# Menusy---------------------------------------------------------------------------------

GAME_ID = 0
# menu główne---
MAIN_MENU_ID = 1
MAIN_MENU_BUTTONS_NAMES = ["start", "options", "exit"]
MAIN_MENU_COLOR = (223, 240, 235) # białawo-błękitny
MAIN_MENU_HEADLINE = "main menu"
MAIN_MENU_HEADLINE_COLOR = (18, 49, 77)

# kody przycisków
MAIN_MENU_START = 1
MAIN_MENU_OPTIONS = 2
MAIN_MENU_EXIT = 3

# menu opcji---
SETTINGS_MENU_ID = 2
SETTINGS_MENU_HEADLINE = "settings"
SETTINGS_MENU_BUTTONS_NAMES = ["difficulty: easy", "resolution: 800x600", "fullscreen: off",
                               "main menu"]
# kody przycisków
SETTINGS_MENU_DIFFICULTY = 1
SETTINGS_MENU_RESOLUTIONS = 2
SETTINGS_MENU_FULLSCREEN = 3
SETTING_MENU_MAIN_MENU = 4

# kody poziomów trudności
SETTINGS_MENU_EASY = 0
SETTINGS_MENU_MEDIUM = 1
SETTINGS_MENU_HARD = 2

# kody rozdzielczości
SETTINGS_MENU_LOW_RES = 0
SETTINGS_MENU_HIGH_RES = 1

# kody opcji wyświetlania okna
SETTINGS_MENU_FULLSCREEN_OFF = 0
SETTINGS_MENU_FULLSCREEN_ON = 1

# menu porażki---
GAME_OVER_MENU_ID = 3
GAME_OVER_MENU_HEADLINE = 'game over'
GAME_OVER_MENU_BUTTONS_NAMES = ["try again", "main menu", "exit"]
GAME_OVER_MENU_COLOR = (219, 83, 100)  # czerwono jakiś
GAME_OVER_MENU_HEADLINE_COLOR = (0, 0, 0)

# kody przycisków
GAME_OVER_TRY_AGAIN = 1
GAME_OVER_MAIN_MENU = 2
GAME_OVER_EXIT = 3

# menu pauzy---
PAUSE_MENU_ID = 4
PAUSE_MENU_HEADLINE = 'pause'
PAUSE_MENU_BUTTONS_NAMES = ["continue", "main menu", "exit"]
PAUSE_MENU_COLOR = (0, 0, 0)
PAUSE_MENU_HEADLINE_COLOR = (0, 0, 0)

# kody przycisków
PAUSE_MENU_ESCAPE_P = 0
PAUSE_MENU_CONTINUE = 1
PAUSE_MENU_MAIN_MENU = 2
PAUSE_MENU_EXIT = 3

# menu zwycięstwa---
WIN_MENU_ID = 5
WIN_MENU_HEADLINE = 'You won!'
WIN_MENU_BUTTONS_NAMES = ["main menu", "exit"]
WIN_MENU_COLOR = (139, 191, 128)  # zielono jakiś
WIN_MENU_HEADLINE_COLOR = (0, 255, 0)

# kody przycisków
WIN_MENU_MAIN_MENU = 1
WIN_MENU_EXIT = 2

# Sędzia---------------------------------------------------------------------------------

# położenie napisu z pozostałymi życiami
LIVES_STATUS_X = 20
LIVES_STATUS_Y = 100

# początkowa ilość żyć
LIVES = 3

# kolor napisu wyświetlającego pozostałą liczbę żyć
LIVES_COLOR = (255, 255, 255)
