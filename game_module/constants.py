"""Wszystkie stałe występujące w programie"""
# pylint: disable=no-member

import pygame
pygame.init()  # konieczne dla fontów

# Fonts------------------------------------------
FONT_HEADINGS = pygame.font.SysFont(None, 60) # czcionka nagłówków
FONT_OPTIONS = pygame.font.SysFont(None, 40) # czcionka tekstów z menu'sów

# Colors-----------------------------------------
# MENUS
COLOR_BACKGROUND = (41, 39, 36)  # ciemny
COLOR_MENU = (223, 240, 235) # białawo-błękitny
COLOR_MENU_HEADLINE = (18, 49, 77)
COLOR_MENU_TEXT = (255, 255, 255)
COLOR_GAME_OVER_MENU = (219, 83, 100)  # czerwono jakiś
COLOR_GAME_OVER_MENU_HEADLINE = (0, 0, 0)
COLOR_GAME_OVER_MENU_TEXT = (255, 255, 255)
COLOR_PAUSE_MENU = (0, 0, 0)
COLOR_PAUSE_MENU_HEADLINE = (0, 0, 0)
COLOR_PAUSE_MENU_TEXT = (255, 255, 255)
COLOR_WIN_MENU = (139, 191, 128)  # zielono jakiś
COLOR_WIN_MENU_HEADLINE = (0, 255, 0)
COLOR_WIN_MENU_TEXT = (255, 255, 255)
# OTHERS
COLOR_BUTTON = (62, 102, 138) # niebiesko jakiś
COLOR_BUTTON_TEXT = (255, 255, 255)
COLOR_BALL = (255, 15, 35)  # czerwony
COLOR_RACKET = (70, 150, 60)  # ciemna zieleń
COLOR_BLOCK = (34, 105, 125)  # niebieski

# Ball-------------------------------------------
# Prędkość poruszania piłki
BALL_SPEED = 3
# Wymiary piłki
BALL_WIDTH = 15
BALL_HEIGHT = 15
# Początkowe współrzędne piłki
BALL_START_X = 50
BALL_START_Y = 100

# Racket-----------------------------------------
# wymiary paletki
RACKET_WIDTH = 80
RACKET_HEIGHT = 16
# początkowe ustawienie paletki
# RACKET_X = WINDOW_WIDTH/2 - RACKET_WIDTH/2
# RACKET_Y = WINDOW_HEIGHT-40

# Block------------------------------------------
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 25

# Button-----------------------------------------
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 80

# Menus
RESOLUTIONS = [(800, 600), (1200, 800)]
FULLSCREEN = [0, pygame.FULLSCREEN]
FPS_LIMIT = [200, 300, 500]

MAIN_MENU_BUTTONS_NAMES = ["start", "options", "exit"]
SETTINGS_MENU_BUTTONS_NAMES = ["difficulty: easy", "resolution: 800x600", "fullscreen: off",
                               "main menu"]
GAME_OVER_MENU_BUTTONS_NAMES = ["try again", "main menu", "exit"]
PAUSE_MENU_BUTTONS_NAMES = ["continue", "main menu", "exit"]
WIN_MENU_BUTTONS_NAMES = ["main menu", "exit"]

# Judge------------------------------------------
LIFES_X = 20
LIFES_Y = 65
