"""Moduł zawierający klasę poziomu gry"""

from game_module import block
from game_module import constants


class Level:
    """Klasa poziomu gry:

    Rysuje na ekranie klocki w odpowiednim układzie"""

    def __init__(self):
        """Konstruktor tworzy listę obiektów klasy Block o odpowiednich wartościach"""

        self.blocks = []  # tworzy listę na bloki
        # tworzy bloki o współrzędnych x i y
        self.blocks = [block.Block(x_cord, y_cord) for x_cord in
                       range(0, constants.WINDOW_WIDTH, constants.BLOCK_WIDTH + 2) for y_cord in
                       range(0, 2 * constants.BLOCK_HEIGHT + 4, constants.BLOCK_HEIGHT + 2)]

    def reset(self):
        """Usuwa listę klocków i tworzy nową"""

        self.blocks.clear()
        self.blocks = [block.Block(x_cord, y_cord) for x_cord in
                       range(0, constants.WINDOW_WIDTH, constants.BLOCK_WIDTH + 2) for y_cord in
                       range(0, 2 * constants.BLOCK_HEIGHT + 4, constants.BLOCK_HEIGHT + 2)]

    def draw(self, window):
        """Rysuje klocki w oknie"""

        for single_block in self.blocks:
            single_block.draw(window)  # rysuje klocki
