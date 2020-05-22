"""Wszystkie stałe występujące w programie"""

import pygame
pygame.init()  # konieczne dla fontów

# Window-----------------------------------------
WINDOW_WIDTH = 1240
WINDOW_HEIGHT = 700

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
BALL_WIDTH = 10
BALL_HEIGHT = 10
# Początkowe współrzędne piłki
BALL_START_X = 50
BALL_START_Y = 50

# Racket-----------------------------------------
RACKET_WIDTH = 80
RACKET_HEIGHT = 16
RACKET_X = WINDOW_WIDTH/2 - RACKET_WIDTH/2
RACKET_Y = WINDOW_HEIGHT-40

# Block------------------------------------------
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_X = 10
BLOCK_Y = 10

# Main menu--------------------------------------

# Options menu-----------------------------------

# Game over menu---------------------------------

# Button-----------------------------------------
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 80

# Judge------------------------------------------

# Time-------------------------------------------
FPS_LIMIT = 250
