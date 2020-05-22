"""Moduł zwierający klasę sędziego gry - w budowie"""

from game_module import constants


class Judge:
    """Klasa sędziego gry:

    Liczy ilość śmierci gracza oraz wyświetla informacje o pozostałych życiach"""

    def __init__(self):
        self.lifes = 3

    def remove_life(self, window, game, ball):
        """Usuwa jedno życie i sprawdza ile zostało"""
        self.lifes -= 1
        if self.lifes <= 0:
            window.game_over_menu(window, game)
        else:
            ball.reset()

    def reset(self):
        self.lifes = 3

    def draw(self, window):
        """Aktualizuje i rysuje wyniki"""
        text = "Lifes: " + str(self.lifes)
        text_obj = constants.FONT_OPTIONS.render(text, True, (0, 0, 0))
        text_rect = text_obj.get_rect()
        text_rect.topleft = (constants.LIFES_X, constants.LIFES_Y)
        window.surface.blit(text_obj, text_rect)
