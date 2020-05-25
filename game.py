"""Moduł łączący wszystkie elementy gry w całość"""

import pygame

from game_module import ball
from game_module import constants
from game_module import judge
from game_module import level
from game_module import menus
from game_module import window
from game_module import racket


class Game:
    """Klasa nadzorująca pracę całego programu."""

    def __init__(self):
        """Konstruktor konfiguruje pracę programu, tworząc niezbęde obiekty"""

        # tworzenie niezbędnych obiektów
        self.fps_clock = pygame.time.Clock()  # zegar do kontrolowania prędkości rysowania klatek
        self.window = window.Window()  # okno programu
        self.ball = ball.Ball()  # tworzy piłkę
        self.player = racket.Racket()  # tworzy paletkę gracza
        self.judge = judge.Judge()  # tworzy sędziego gry
        self.level = level.Level()  # tworzy bloki w pewnej konfiguracji

        # tworzenie menusów
        self.main_menu = menus.MainMenu("main menu", constants.MAIN_MENU_BUTTONS_NAMES)
        self.settings_menu = menus.SettingsMenu("setting menu", constants.SETTINGS_MENU_BUTTONS_NAMES)
        self.game_over_menu = menus.GameOverMenu("game over menu", constants.GAME_OVER_MENU_BUTTONS_NAMES,
                                                 constants.COLOR_GAME_OVER_MENU,
                                                 constants.COLOR_GAME_OVER_MENU_HEADLINE)
        self.pause_menu = menus.PauseMenu("pause menu", constants.PAUSE_MENU_BUTTONS_NAMES,
                                          constants.COLOR_PAUSE_MENU, constants.COLOR_PAUSE_MENU_HEADLINE)
        self.win_menu = menus.WinMenu("win menu", constants.WIN_MENU_BUTTONS_NAMES, constants.COLOR_WIN_MENU,
                                      constants.COLOR_WIN_MENU_HEADLINE)

    def menu(self):
        """Główne menu:

        Wyświetla główne menu gry z którego użytkownik może przejść do głównej
        pętli programu, menu opcji lub zakończyć program."""

        self.main_menu.draw(self.window)  # rysuje menu główne
        self.main_menu.run(self.window, self, self.settings_menu)  # czeka na wybór opcji

    def run(self):
        """Główna pętla progamu:

        Na początku wywoływana jest funkcja main_menu() (moduł windows) która odpowiada za
        wyświetlenie na ekranie głównego menu gry. Po wybraniu opcji 'start' funkcja kończy
        swoje działanie i program przechodzi do wykonywania nieskończonej głównej pętli programu,
        która odpowiada za kontrolowanie stanu gry i jego bieżącą aktualizację. Wyjście z
        głównej pętli jest możliwe w przypadku naciśnięcia przycisku 'exit' lub wyłączenia
        programu za pomocą krzyżyka w prawym górnym rogu ekranu."""

        while not self.handle_events():  # działa do momentu otrzymania sygnału wyjścia
            # wyznaczenie przemieszczenia piłki
            self.ball.move(self.player, self.level.blocks, self.window, self, self.judge, self.game_over_menu,
                           self.win_menu)

            # rysowanie obiektów
            self.window.draw()  # rysuje okno
            self.ball.draw(self.window)  # rysuje piłkę
            self.player.draw(self.window)  # rysuje paletkę
            self.judge.draw(self.window)  # wypisuję pozostałą liczbę żyć
            self.level.draw(self.window)  # rysuje klocki
            pygame.display.update()  # nanoszenie zmian na ekran

            # ogranicznik liczby klatek na sekundę
            self.fps_clock.tick(constants.FPS_LIMIT)

    def handle_events(self):
        """Funkcja obsługująca zdarzenia systemowe."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu ekranu
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                if event.key == pygame.K_ESCAPE or pygame.K_p:  # ESCAPE lub P
                    self.pause_menu.draw(self.window)
                    self.pause_menu.run(self)
            if event.type == pygame.MOUSEMOTION:  # poruszono myszą
                xy_cord = event.pos  # pobiera aktualne współrzędne kursora
                self.player.move(xy_cord[0])
            return False

    def reset(self):
        """Resetuje stan gry:

        Zmienia ustawienia piłki i levelu do początkowych wartości."""

        self.ball.reset()
        self.level.reset()
        self.judge.reset()


def main():
    """Główna funkcja programu:

    Inicjalizuje biblioteki pygame, tworzy obiekt gry i uruchamia jego funkcje run(), która jest
    główną pętlą programu."""

    # inicjalizacja bibliotek zewnętrznych
    pygame.init()  # biblioteki pygame
    pygame.font.init()  # czcionki

    # tworzenie obiektów odpowiednich klas
    game = Game()

    # wywołanie metody wprawiającej obiekty w ruch
    try:
        game.menu()

    except SystemExit:
        print("Złapano SystemExit")


if __name__ == "__main__":
    """Uruchamia funkcję main()"""

    main()
