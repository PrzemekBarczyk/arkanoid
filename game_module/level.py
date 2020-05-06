"""Moduł zawierający klasę poziomu gry"""

from game_module import constants
from game_module import block


class Level:
    """Klasa poziomu gry:

    Rysuje na ekranie klocki w odpowiednim układzie"""

    def __init__(self):
        """Konstruktor tworzy listę obiektów klasy Block o odpowiednich wartościach"""

        self.blocks = []  # tworzy listę na bloki
        # tworzy bloki o współrzędnych x i y
        for y_cord in range(0, 2 * constants.BLOCK_HEIGHT + 4, constants.BLOCK_HEIGHT + 2):
            for x_cord in range(0, constants.WINDOW_WIDTH, constants.BLOCK_WIDTH + 2):
                self.blocks.append(block.Block(x_cord, y_cord))  # dodaje do listy bloki

    def reset(self):
        """Usuwa listę klocków i tworzy nową"""

        self.blocks.clear()
        for y_cord in range(0, 2 * constants.BLOCK_HEIGHT + 4, constants.BLOCK_HEIGHT + 2):
            for x_cord in range(0, constants.WINDOW_WIDTH, constants.BLOCK_WIDTH + 2):
                self.blocks.append(block.Block(x_cord, y_cord))

    def draw(self, window):
        """Rysuje klocki w oknie"""

        for single_block in self.blocks:
            single_block.draw(window)  # rysuje klocki
