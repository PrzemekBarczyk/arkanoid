"""Moduł zawierający klasę menusów"""

import sys

import pygame

from game_module import buttons
from game_module import constants


class Menu:
    """Klasa menu:

    Odpowiada za utworzenie okna, narysowanie go i wybór odpowiedniej opcji."""

    def __init__(self, name, buttons_names, background_color, headline_color):
        """"""
        self.name = name  # nazwa menu
        self.buttons_names = buttons_names  # lista z nazwami przycisków
        self.background_color = background_color
        self.headline_color = headline_color

        self.buttons_objects = []  # lista na obiekty klasy Button
        for button in enumerate_with_step(buttons_names, 100, 100):  # tworzy obiekty będące przyciskami
            button_height, button_name = button
            self.buttons_objects.append(buttons.Button(button_name, y=button_height))

        print("created " + self.name)

    def draw(self, window):
        """Rysuje odpowiednie menu"""

        window.surface.fill(self.background_color)  # koloruje tło menu
        self.print_headline(window, self.name, self.headline_color)  # nagłówek menu

        for button in self.buttons_objects:  # rysuje przyciski
            button.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

    # def game_over_menu(self, window, game):
    #     """Tworzy menu końca gry.
    #
    #     Menu uruchamia się pod tym jak piłka wypadnie poza dół okienka programu i resetuje stan gry
    #     (lokalizację piłki, ilość zbitych klocków). Użytkownik może wybrać czy chce kontynuować gre
    #     'try again', wrócić do menu głównego 'main menu' czy zakończyć gre 'exit'.
    #     Wybranie 'try again' kończy działanie funkcji i wraca do głównej pętli programu która
    #     kontynuuje działanie ze zresetowanym stanem gry.
    #     Opcja 'main menu' uruchamia funkcje game.run(game), która uruchamia menu główne następnie
    #     główną petlę programu.
    #     'Exit' kończy pracę programu. Opcje możliwe są do wyboru przy użyciu lewego przycisku
    #     myszy, ponadto klawisz ESCAPE odpowiada za wybranie opcji 'exit'."""
    #
    # def pause_menu(self, window, game):
    #     """Tworzy menu pauzy:
    #
    #     Menu można wywołać klawiszem ESCAPE lub P w trakcie gry. Zatrzymuje ono rozgrywkę i
    #     wyświetla ekran menu z którego można wybrać: 'continue', 'main menu' i 'exit'.
    #     Opcja 'continue' pozwala kontynuować rozgrywkę z niezmienionym stanem rozgrywki
    #     (położenie piłki, liczba zbitych klocków).
    #     'Main menu' uruchamia funkcję game.run(game), która odpowiada za wyświetlenie menu
    #     głownego i uruchomienie pętli głównej programu.
    #     'Exit' kończy pracę programu. Powrót do rozgrywki możliwy jest również przy użyciu
    #     tych samych klawiszy które słuszą do wywołania menu."""
    #
    # def win_menu(self, window, game):
    #     """Wyświetla menu zwycięstwa
    #
    #     Pojawia się po zbiciu wszystkich klocków z planszy. Składa się z przycisków: 'main menu',
    #     które przenosi do menu głównego poprzez wywołanie funkcji game.run(game), oraz 'exit'
    #     który kończy pracę programu."""

    def print_headline(self, window, text, color):
        """Funkcja pomocnicza do pisania nagłówku w menu"""

        headline_obj = constants.FONT_HEADINGS.render(text, True, color)
        headline_rect = headline_obj.get_rect()
        headline_rect.center = (window.width // 2, 30)
        window.surface.blit(headline_obj, headline_rect)


class MainMenu(Menu):
    def __init__(self, name, buttons_names, background_color=constants.COLOR_MENU,
                 headline_color=constants.COLOR_MENU_HEADLINE):
        super().__init__(name, buttons_names, background_color, headline_color)

    def run(self, window, game, settings_menu):
        """Czeka na wybór opcji przez użytkownika."""

        while True:
            button_number = check_which_button(self.buttons_objects)
            if button_number == 1:  # przycisk 'start'
                game.run()  # uruchamia główną pętlę programu
            elif button_number == 2:  # przycisk 'options'
                settings_menu.draw(window)  # uruchamia menu opcji
                settings_menu.run(window)
            elif button_number == 3:  # przycisk 'close'
                pygame.quit()
                sys.exit(0)


class SettingsMenu(Menu):
    def __init__(self, name, buttons_names, background_color=constants.COLOR_MENU,
                 headline_color=constants.COLOR_MENU_HEADLINE):
        super().__init__(name, buttons_names, background_color, headline_color)

    def run(self, window):
        i = 0
        j = 0
        while True:
            print("settings menu")
            # zwraca nr naciśniętego przycisku
            button_number = check_which_button(self.buttons_objects)
            if button_number == 1:  # difficulty
                pass
                # TODO: rozbudować
            elif button_number == 2:  # resolution
                i -= 1
                window.update(constants.RESOLUTIONS[i], constants.FULLSCREEN[j])
                self.draw(window)
                break
                # TODO: rozbudować
            elif button_number == 3:  # fullscreen
                j -= 1
                window.update(constants.RESOLUTIONS[i], constants.FULLSCREEN[j])
                self.draw(window)
                break
                # TODO: włączony/wyłączony
            elif button_number == 4:  # lewy przycisk myszy i kursor nad 'return'
                return  # wróć do menu głównego


class GameOverMenu(Menu):
    def __init__(self, name, buttons_names, background_color, headline_color):
        super().__init__(name, buttons_names, background_color, headline_color)

    def run(self, game):
        game.reset()  # resetuje stan gry
        while True:
            print("game over")
            # zwraca nr naciśniętego przycisku
            button_number = check_which_button(self.buttons_objects)
            if button_number == 1:  # lewy przycisk myszy i 'try again'
                return
            elif button_number == 2:  # lewy przycisk myszy i 'main menu'
                game.run()
            elif button_number == 3:  # lewy przycisk myszy i 'exit'
                pygame.quit()
                exit(0)


class PauseMenu(Menu):
    def __init__(self, name, buttons_names, background_color, headline_color):
        super().__init__(name, buttons_names, background_color, headline_color)

    def run(self, game):
        while True:
            print("pause")

            # zwraca nr naciśniętego przycisku
            button_number = check_which_button(self.buttons_objects, (pygame.K_ESCAPE, pygame.K_p))
            # lewy przycisk myszy i 'continue' lub klawisz 'ESCAPE' lub 'p'
            if button_number == 1 or button_number == 0:
                return  # wraca do gry
            elif button_number == 2:  # lewy przycisk myszy i 'main menu'
                game.reset()  # resetuje stan gry
                game.menu()  # uruchamia grę od początku
            elif button_number == 3:  # lewy przycisk myszy i 'exit'
                pygame.quit()
                exit(0)


class WinMenu(Menu):
    def __init__(self, name, buttons_names, background_color, headline_color):
        super().__init__(name, buttons_names, background_color, headline_color)

    def run(self, game):
        print("win menu")
        while True:
            button_number = check_which_button(self.buttons_objects)  # zwraca nr naciśniętego przycisku
            if button_number == 1:  # lewy przycisk myszy i 'main menu'
                game.reset()
                game.menu()
            elif button_number == 2:  # lewy przycisk myszy i 'exit'
                pygame.quit()
                exit(0)


def enumerate_with_step(xs, start=0, step=1):
    for x in xs:
        yield start, x
        start += step


def check_which_button(buttons, keys=None):
    """Zwraca numer wybranego przez użytkownika przycisku z listy otrzymanych jako argumenty"""

    x, y = 0, 0  # współrzedne kursora myszy
    print("buttons check")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu okna programu
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEMOTION:  # mysz się porusza
                x, y = event.pos  # zapisuje aktualne współrzędne kursora
            if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                for key in keys:
                    if event.key == key:  # ESCAPE lub P
                        return 0  # zwraca 0 (wciśnięto żądany przycisk)
            if event.type == pygame.MOUSEBUTTONDOWN:  # klawisz myszy wciśnięty
                for button in enumerate(buttons):
                    # lewy przycisk myszy i kursor nad przyciskiem
                    if event.button == 1 and button[1].rect.collidepoint(x, y):
                        return button[0]+1  # zwraca numer przycisku
