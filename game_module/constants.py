"""Wszystkie stałe występujące w programie"""

import pygame
pygame.init()

# Fonts------------------------------------------
FONT_HEADINGS = pygame.font.SysFont(None, 60) # czcionka nagłówków
FONT_OPTIONS = pygame.font.SysFont(None, 40) # czcionka tekstów z menu'sów

# Colors-----------------------------------------
COLOR_BACKGROUND = (41, 39, 36)  # ciemny
COLOR_MENU = (223, 240, 235) # białawo-błękitny
COLOR_GAME_OVER_MENU = (219, 83, 100)  # czerwono jakiś
COLOR_WIN_MENU = (139, 191, 128)  # zielono jakiś
COLOR_BUTTON = (62, 102, 138) # niebiesko jakiś
COLOR_BALL = (255, 15, 35)  # czerwony
COLOR_RACKET = (70, 150, 60)  # ciemna zieleń
COLOR_BLOCK = (34, 105, 125)  # niebieski

# Ball-------------------------------------------
# Prędkość poruszania piłki
BALL_SPEED = 4
# Wymiary piłki
BALL_WIDTH = 10
BALL_HEIGHT = 10
# Początkowe współrzędne piłki
BALL_START_X = 50
BALL_START_Y = 50

# Racket-----------------------------------------
RACKET_WIDTH = 80
RACKET_HEIGHT = 16
RACKET_X = RACKET_WIDTH/2 - 40
RACKET_Y = RACKET_HEIGHT - 40

# Block------------------------------------------
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_X = 10
BLOCK_Y = 10

# Window-----------------------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Main menu--------------------------------------


# Options menu-----------------------------------

# Game over menu---------------------------------

# Button-----------------------------------------
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 80

# Judge------------------------------------------
FONT_SIZE = 32  # 64

# Time-------------------------------------------
FPS_LIMIT = 120
