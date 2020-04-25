"""Łączy wszystkie elementy gry w całość
TODO game:
- rozbudować menu do gry
- dodać inne level'e
"""

import pygame
from game_module import constants
from game_module import window
from game_module import racket
from game_module import ball
# from game_module import judge
# from game_module import block
from game_module import level


class Game:
    """Klasa nadzorująca pracę całego programu"""

    # Konfiguracja programu
    def __init__(self):
        pygame.init()  # inicjalizuje biblioteki pygame
        self.fps_clock = pygame.time.Clock()  # zegar do kontrolowania szybkości rysowania kolejnych klatek gry
        self.window = window.Window()  # tworzy okienko
        self.ball = ball.Ball()  # tworzy piłkę
        self.player = racket.Racket()  # tworzy paletkę gracza
        self.level = level.Level()  # tworzy bloki w pewnej konfiguracji

    def run(self, game):
        """Główna pętla progamu"""
        self.window.main_menu(self.window)  # rysuje menu główne i czeka na wybór użytkownika
        while not self.handle_events():  # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.ball.move(self.player, self.level.blocks, self.window, game)  # wyznacza przemieszczenie piłki
            # rysowanie obiektów
            self.window.draw()  # rysuje okno
            self.ball.draw(self.window)  # rysuje piłkę
            self.player.draw(self.window)  # rysuje paletkę
            # self.judge.draw(self.window)  #
            self.level.draw(self.window)  # rysuje klocki
            pygame.display.update()  # nanoszenie zmian na ekran
            self.fps_clock.tick(constants.FPS_LIMIT)  # ogranicznik FPS

    def handle_events(self):
        """Funkcja obsługująca zdarzenia systemowe"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu ekranu
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                if event.key == pygame.K_ESCAPE or pygame.K_p:  # ESCAPE lub P
                    self.window.pause_menu(self.window, game)
            if event.type == pygame.MOUSEMOTION:  # poruszono myszą
                # myszka steruje ruchem gracza
                x_pos, y_pos = event.pos
                self.player.move(x_pos)

    def reset(self):
        """Resetuje stan gry (zmienia ustawienia obiektów należących do klasy do początkowych wartości)."""
        self.ball.reset_configuration()
        self.level.reset_configuration()


if __name__ == "__main__":
    """Tworzy obiekt klasy gry i uruchamia jej metodę run() (główną pętlę programu)"""
    game = Game()  # tworzy obiekt Game
    game.run(game)  # uruchamia główną pętle programu
