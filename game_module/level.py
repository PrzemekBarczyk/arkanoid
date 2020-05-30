"""Moduł zawierający klasę poziomu gry"""

from game_module import block
from game_module import constants


class Level:
    """Klasa poziomu gry:

    Rysuje na ekranie klocki w odpowiednim układzie."""

    def __init__(self):
        """Konstruktor tworzy listę obiektów klasy Block o odpowiednich wartościach"""

        self.blocks = []  # lista na bloki
        self.blocks = [block.Block(x_cord, y_cord) for x_cord in
                       range(1, constants.RESOLUTIONS[0][0], constants.BLOCK_WIDTH + 4)
                       for y_cord in
                       range(1, 3 * constants.BLOCK_HEIGHT, constants.BLOCK_HEIGHT + 4)]

    def reset(self, window):
        """Usuwa listę klocków i tworzy nową"""

        self.blocks.clear()
        self.blocks = [block.Block(x_cord, y_cord) for x_cord in
                       range(1, window.width, constants.BLOCK_WIDTH + 4) for y_cord in
                       range(1, 3 * constants.BLOCK_HEIGHT, constants.BLOCK_HEIGHT + 4)]

    def draw(self, window):
        """Rysuje klocki w oknie"""

        for single_block in self.blocks:
            single_block.draw(window)
