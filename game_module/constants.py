"""Wszystkie stałe występujące w programie"""

import pygame
pygame.init()

# Fonts------------------------------------------
font_headings = pygame.font.SysFont(None, 60) # czcionka nagłówków
font_options = pygame.font.SysFont(None, 40) # czcionka tekstów z menu'sów

# Colors-----------------------------------------
COLOR_BACKGROUND = (0, 0, 0)  # czarny
COLOR_MENU = (223, 240, 235) # białawo-błękitny
COLOR_GAME_OVER_MENU = (0, 0, 0)  # czarny
COLOR_WIN_MENU = (0, 0, 0)  # czarny
COLOR_BUTTON = (255, 0, 0) # czerwony
COLOR_BALL = (255, 0, 0)  # czerwony
COLOR_RACKET = (0, 255, 0)  # zielony
COLOR_BLOCK = (0, 0, 255)  # niebieski

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
RACKET_HEIGHT = 15
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
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 80

# Judge------------------------------------------
FONT_SIZE = 32  # 64

# Time-------------------------------------------
FPS_LIMIT = 120
