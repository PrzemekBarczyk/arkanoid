"""Moduł zwierający klasę sędziego gry."""
# pylint: disable=no-member

from game_module import constants


class Judge:
    """Klasa sędziego gry:

    Liczy ilość śmierci gracza oraz wyświetla informacje o pozostałych życiach."""

    def __init__(self):
        self.lives = constants.LIVES  # 3

    def remove_life(self, game, ball):
        """Usuwa jedno życie i sprawdza ile zostało."""

        self.lives -= 1
        if self.lives <= 0:
            game.reset()
            game.menu_id = constants.GAME_OVER_MENU_ID
        else:
            ball.reset()

    def reset(self):
        """Resetuje liczbę żyć gracza."""

        self.lives = constants.LIVES  # 3

    def draw(self, window):
        """Aktualizuje i rysuje wyniki."""

        text = 'Lives: {}'.format(str(self.lives))
        text_obj = constants.Fonts.FONT_OPTIONS.render(text, True, constants.LIVES_COLOR)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (constants.LIVES_STATUS_X, constants.LIVES_STATUS_Y)
        window.surface.blit(text_obj, text_rect)
