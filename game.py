"""Moduł łączący wszystkie elementy gry w całość."""
# pylint: disable=too-many-instance-attributes
# pylint: disable=no-member

import pygame

from game_module import ball
from game_module import constants
from game_module import judge
from game_module import level
from game_module import menus
from game_module import racket
from game_module import window


class Game:
    """Klasa nadzorująca pracę całego programu."""

    def __init__(self):
        """Konstruktor konfiguruje pracę programu, tworząc niezbęde obiekty."""

        # tworzenie niezbędnych obiektów
        self.fps_clock = pygame.time.Clock()  # zegar do kontrolowania prędkości rysowania klatek
        self.fps = constants.FPS_LIMIT[0]  # limit FPS
        self.window = window.Window()  # okno programu
        self.ball = ball.Ball()  # tworzy piłkę
        self.player = racket.Racket()  # tworzy paletkę gracza
        self.judge = judge.Judge()  # tworzy sędziego gry
        self.level = level.Level()  # tworzy bloki w pewnej konfiguracji

        self.menu_id = constants.MAIN_MENU_ID  # określa które menu najpierw wyświetli

        # tworzenie menusów
        self.main_menu = menus.MainMenu()
        self.settings_menu = menus.SettingsMenu()
        self.game_over_menu = menus.GameOverMenu()
        self.pause_menu = menus.PauseMenu()
        self.win_menu = menus.WinMenu()

    def check_which_menu(self):
        """Uruchamia odpowienie menu na podstawie wartości zmiennej menu_id."""

        while self.menu_id > 0:  # póki nie zwrócono odpowiedniej wartości

            if self.menu_id == constants.MAIN_MENU_ID:
                self.main_menu.draw(self.window)
                self.menu_id = self.main_menu.run()

            elif self.menu_id == constants.SETTINGS_MENU_ID:
                self.settings_menu.draw(self.window)
                self.menu_id = self.settings_menu.run(self.window, self)

            elif self.menu_id == constants.GAME_OVER_MENU_ID:
                self.game_over_menu.draw(self.window)
                self.menu_id = self.game_over_menu.run(self)

            elif self.menu_id == constants.PAUSE_MENU_ID:
                self.pause_menu.draw(self.window)
                self.menu_id = self.pause_menu.run(self)

            elif self.menu_id == constants.WIN_MENU_ID:
                self.win_menu.draw(self.window)
                self.menu_id = self.win_menu.run(self)

    def run(self):
        """Główna pętla progamu:

        Uruchamiana jest główna pętla programu, która odpowiada za kontrolowanie stanu gry
        i jego bieżącą aktualizację. Wyjście z głównej pętli jest możliwe w przypadku
        wyłączenia programu za pomocą krzyżyka w prawym górnym rogu ekranu lub naciśnięcia
        przycisku 'exit' w którymś z menu. Klawisze 'ESCAPE' oraz 'P' uruchamiają pauze w
        grze."""

        while not self.handle_events():  # działa do momentu otrzymania sygnału wyjścia

            # sprawdzenie czy należy uruchomić któreś menu
            self.check_which_menu()

            # wyznaczenie przemieszczenia piłki
            self.ball.move(self.player, self.level.blocks, self.window, self, self.judge)

            # rysowanie obiektów
            self.window.draw()  # rysuje okno
            self.ball.draw(self.window)  # rysuje piłkę
            self.player.draw(self.window)  # rysuje paletkę
            self.judge.draw(self.window)  # wypisuję pozostałą liczbę żyć
            self.level.draw(self.window)  # rysuje klocki
            pygame.display.update()  # nanoszenie zmian na ekran

            # ogranicznik liczby klatek na sekundę
            self.fps_clock.tick(self.fps)

    def handle_events(self):
        """Funkcja obsługująca zdarzenia systemowe.

        Return:
            True jeśli użytkownik kliknął ikone krzyżyka w oknie programu.
            False jeśli nie został spełniony powyższy warunek."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu ekranu
                pygame.quit()
                return True
            if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                if event.key == pygame.K_ESCAPE or pygame.K_p:  # ESCAPE lub P
                    self.menu_id = constants.PAUSE_MENU_ID
            if event.type == pygame.MOUSEMOTION:  # poruszono myszą
                xy_cord = event.pos  # pobiera aktualne współrzędne kursora
                self.player.move(xy_cord[0], self.window)
            return False

    def update(self):
        """Dopasowuje położenie klocków i paletki do nowej rozdzielczości."""

        self.player.update(self.window)
        self.level.reset(self.window)

    def reset(self):
        """Resetuje stan gry:

        Zmienia ustawienia piłki i levelu do początkowych wartości."""

        self.ball.reset()
        self.level.reset(self.window)
        self.judge.reset()


def main():
    """Główna funkcja programu:

    Inicjalizuje biblioteki pygame, tworzy obiekt gry i uruchamia jego funkcje run(), która jest
    główną pętlą programu."""

    # inicjalizacja bibliotek zewnętrznych
    constants.Fonts.load()

    # tworzenie obiektów odpowiednich klas
    game = Game()

    # wywołanie metody wprawiającej obiekty w ruch
    try:
        game.run()

    except SystemExit:
        print("Nastąpiło pomyślne wyłączenie programu.")
    except:
        print("Nieznany wyjątek!")
        raise


# uruchamia funkcję main()
if __name__ == "__main__":
    main()
