"""Klasa sędziego gry"""

import pygame
from game_module import constants
from game_module import block


class Level:
    """Klasa zajmuje się narysowaniem na ekranie klocków w odpowiednim układzie"""
    def __init__(self):
        self.blocks = []  # tworzy listę na bloki
        # tworzy bloki o współrzędnych x i y
        for y_cord in range(0, 2 * constants.BLOCK_HEIGHT + 4, constants.BLOCK_HEIGHT + 2):
            for x_cord in range(0, constants.WINDOW_WIDTH, constants.BLOCK_WIDTH + 2):
                self.blocks.append(block.Block(x_cord, y_cord))  # dodaje do listy bloki

    def reset_configuration(self):
        self.blocks.clear()
        for y_cord in range(0, 2 * constants.BLOCK_HEIGHT + 4, constants.BLOCK_HEIGHT + 2):
            for x_cord in range(0, constants.WINDOW_WIDTH, constants.BLOCK_WIDTH + 2):
                self.blocks.append(block.Block(x_cord, y_cord))

    def draw(self, window):
        for single_block in self.blocks:
            single_block.draw(window)  # rysuje klocki
