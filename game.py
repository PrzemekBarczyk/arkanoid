"""Moduł łączący wszystkie elementy gry w całość"""

import pygame
from game_module import constants
from game_module import window
from game_module import racket
from game_module import ball
# from game_module import judge
from game_module import level


class Game:
    """Klasa nadzorująca pracę całego programu."""

    def __init__(self):
        """Konstruktor konfiguruje pracę programu, tworząc niezbęde obiekty"""

        self.fps_clock = pygame.time.Clock()  # zegar do kontrolowania szybkości rysowania kolejnych klatek gry
        self.window = window.Window()  # tworzy okienko
        self.ball = ball.Ball()  # tworzy piłkę
        self.player = racket.Racket()  # tworzy paletkę gracza
        self.level = level.Level()  # tworzy bloki w pewnej konfiguracji

    def run(self, game):
        """Główna pętla progamu:

        Na początku wywoływana jest funkcja main_menu() z modułu windows która odpowiada za wyświetlenie na ekranie
        głównego menu gry. Po wybraniu opcji 'start' funkcja kończy swoje działanie i program przechodzi do
        wykonywania nieskończonej głównej pętli programu, która odpowiada za kontrolowanie stanu gry i jego bieżącą
        aktualizację. Wyjście z głównej pętli jest możliwe w przypadku naciśnięcia przycisku 'exit' lub wyłączenia
        programu za pomocą krzyżyka w prawym górnym rogu ekranu."""

        self.window.main_menu(self.window)  # rysuje menu główne i czeka na wybór użytkownika
        while not self.handle_events(game):  # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.ball.move(self.player, self.level.blocks, self.window, game)  # wyznacza przemieszczenie piłki

            # rysowanie obiektów
            self.window.draw()  # rysuje okno
            self.ball.draw(self.window)  # rysuje piłkę
            self.player.draw(self.window)  # rysuje paletkę
            # self.judge.draw(self.window)  #
            self.level.draw(self.window)  # rysuje klocki

            pygame.display.update()  # nanoszenie zmian na ekran
            self.fps_clock.tick(constants.FPS_LIMIT)  # ogranicznik liczby klatek na sekundę

    def handle_events(self, game):
        """Funkcja obsługująca zdarzenia systemowe."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu ekranu
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                if event.key == pygame.K_ESCAPE or pygame.K_p:  # ESCAPE lub P
                    self.window.pause_menu(self.window, game)
            if event.type == pygame.MOUSEMOTION:  # poruszono myszą
                x_pos, y_pos = event.pos  # pobiera aktualne współrzędne kursora
                self.player.move(x_pos)

    def reset(self):
        """Resetuje stan gry:

        Zmienia ustawienia piłki i levelu do początkowych wartości."""

        self.ball.reset()
        self.level.reset()


def main():
    """Główna funkcja programu:

    Inicjalizuje biblioteki pygame, tworzy obiekt gry i uruchamia jego funkcje run(), która jest główną pętlą
    programu."""

    pygame.init()  # inicjalizuje biblioteki pygame
    pygame.font.init()  # incjalizuje czcionki

    game = Game()
    game.run(game)


if __name__ == "__main__":
    """Uruchamia funkcję main()"""

    main()
