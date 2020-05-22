"""Moduł zawierający klasę okna i funkcję sprawdzającą który przycisk został wybrany
przez użytkownika"""

import pygame

from game_module import buttons
from game_module import constants


class Window:
    """Klasa okna:

    Odpowiada za okno programu i wyświetlanie odpowiedniego menu.
    Zmienna surface wymagana przy rysowaniu innych obiektów w okienku programu"""

    def __init__(self):
        """Konstruktor tworzy okienko programu o podanych rozmiarach"""
        self.width = constants.WINDOW_WIDTH
        self.height = constants.WINDOW_HEIGHT

        # inicjalizuje okno
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Half-Life 3')

    def draw(self):
        """Wypełnia 'powierzchnie' kolorem"""

        self.surface.fill(constants.COLOR_BACKGROUND)

    def main_menu(self, window):
        """Tworzy główne menu gry:

        Użytkownik może wybrać przy użyciu myszy jedną z opcji: 'start', 'options', 'exit'.
        'Start' kończy działanie funkcji po czym program przechodzi do wykonywania funkcji
        znajdujących się w głównej pętli programu.
        'Options' wywołuje funkcję odpowiedzialną za wyświetlenie menu z opcjami.
        'Exit' dezaktywuje bibliotekę pygame, po czym kończy pracę programu funkcją exit(0)"""

        while True:
            print("main menu")
            self.surface.fill(constants.COLOR_MENU)  # koloruje tło menu
            window.print_headline("Main menu", constants.COLOR_MENU_HEADLINE)  # nagłówek menu

            # tworzy obiekty będące przyciskami
            x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # lewa krawędź przycisku
            start = buttons.Button("start", x_button, 100, text_color=constants.COLOR_MENU_TEXT)
            options = buttons.Button("options", x_button, 200, text_color=constants.COLOR_MENU_TEXT)
            close = buttons.Button("exit", x_button, 300, text_color=constants.COLOR_MENU_TEXT)

            # rysuje przyciski na ekranie
            start.draw(window)
            options.draw(window)
            close.draw(window)

            pygame.display.update()  # nanosi zmiany na ekran

            # zwraca nr naciśniętego przycisku
            button_number = check_which_button((start, options, close))
            if button_number == 1:  # przycisk 'start'
                return  # wraca do pętli głównej programu (odpala gre)
            elif button_number == 2:  # przycisk 'options'
                window.options_menu(window)  # uruchamia menu opcji
            elif button_number == 3:  # przycisk 'close'
                pygame.quit()
                exit(0)

    def options_menu(self, window):
        """Tworzy menu z opcjami:

        Do wyboru są opcje: 'difficulty' i 'background color'. Użytkownik może zmieniać opcję przy
        użyciu lewego przycisku myszy. Pod opcjami znajduje się przycisk 'return' który kończy
        działanie tej funkcji i wraca do miejsca wywołania - funkcji main_menu(). Ten sam efekt
        powrotu do poprzedniego menu można uzyskać przy użyciu klawisza ESCAPE"""

        self.surface.fill(constants.COLOR_MENU)  # koloruje tło menu
        window.print_headline("Settings", constants.COLOR_MENU_HEADLINE)  # nagłówek menu

        # tworzy obiekty będące przyciskami
        x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # lewa krawędź przycisku
        difficulty = buttons.Button("difficulty", x_button, 100,
                                    text_color=constants.COLOR_MENU_TEXT)
        background_color = buttons.Button("background color", x_button, 200,
                                          text_color=constants.COLOR_MENU_TEXT)
        return_main_menu = buttons.Button("return", x_button, 300,
                                          text_color=constants.COLOR_MENU_TEXT)

        # rysuje przyciski na ekranie
        difficulty.draw(window)
        background_color.draw(window)
        return_main_menu.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

        while True:
            print("settings menu")
            # zwraca nr naciśniętego przycisku
            button_number = check_which_button((difficulty, background_color, return_main_menu))
            if button_number == 1:  # lewy przycisk myszy i kursor nad 'difficulty'
                pass
                # TODO: rozbudować
            elif button_number == 2:  # lewy przycisk myszy i kursor nad 'backgroud...'
                pass
                # TODO: rozbudować
            elif button_number == 3:  # lewy przycisk myszy i kursor nad 'return'
                button_number = 0
                return  # wróć do menu głównego

    def game_over_menu(self, window, game):
        """Tworzy menu końca gry.

        Menu uruchamia się pod tym jak piłka wypadnie poza dół okienka programu i resetuje stan gry
        (lokalizację piłki, ilość zbitych klocków). Użytkownik może wybrać czy chce kontynuować gre
        'try again', wrócić do menu głównego 'main menu' czy zakończyć gre 'exit'.
        Wybranie 'try again' kończy działanie funkcji i wraca do głównej pętli programu która
        kontynuuje działanie ze zresetowanym stanem gry.
        Opcja 'main menu' uruchamia funkcje game.run(game), która uruchamia menu główne następnie
        główną petlę programu.
        'Exit' kończy pracę programu. Opcje możliwe są do wyboru przy użyciu lewego przycisku
        myszy, ponadto klawisz ESCAPE odpowiada za wybranie opcji 'exit'."""

        game.reset()  # resetuje stan gry
        self.surface.fill(constants.COLOR_GAME_OVER_MENU)  # koloruje tło menu
        window.print_headline("GAME OVER", constants.COLOR_GAME_OVER_MENU_HEADLINE) # nagłówek menu

        # tworzy obiekty będące przyciskami
        x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # lewa krawędź przycisku
        try_again = buttons.Button("try again", x_button, 100,
                                   text_color=constants.COLOR_GAME_OVER_MENU_TEXT)
        main_menu = buttons.Button("main menu", x_button, 200,
                                   text_color=constants.COLOR_GAME_OVER_MENU_TEXT)
        close = buttons.Button("exit", x_button, 300,
                               text_color=constants.COLOR_GAME_OVER_MENU_TEXT)

        # rysuje przyciski na ekranie
        try_again.draw(window)
        main_menu.draw(window)
        close.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

        while True:
            print("game over")
            # zwraca nr naciśniętego przycisku
            button_number = check_which_button((try_again, main_menu, close))
            if button_number == 1:  # lewy przycisk myszy i 'try again'
                return
            elif button_number == 2:  # lewy przycisk myszy i 'main menu'
                game.run(game)
            elif button_number == 3:  # lewy przycisk myszy i 'exit'
                pygame.quit()
                exit(0)

    def pause_menu(self, window, game):
        """Tworzy menu pauzy:

        Menu można wywołać klawiszem ESCAPE lub P w trakcie gry. Zatrzymuje ono rozgrywkę i
        wyświetla ekran menu z którego można wybrać: 'continue', 'main menu' i 'exit'.
        Opcja 'continue' pozwala kontynuować rozgrywkę z niezmienionym stanem rozgrywki
        (położenie piłki, liczba zbitych klocków).
        'Main menu' uruchamia funkcję game.run(game), która odpowiada za wyświetlenie menu
        głownego i uruchomienie pętli głównej programu.
        'Exit' kończy pracę programu. Powrót do rozgrywki możliwy jest również przy użyciu
        tych samych klawiszy które słuszą do wywołania menu."""

        self.surface.fill(constants.COLOR_PAUSE_MENU)  # koloruje tło menu
        window.print_headline("pause", constants.COLOR_PAUSE_MENU_HEADLINE)  # nagłówek menu

        # tworzy obiekty będące przyciskami
        x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # lewa krawędź przycisku
        continue_button = buttons.Button("continue", x_button, 100,
                                         text_color=constants.COLOR_PAUSE_MENU_TEXT)
        main_menu = buttons.Button("main menu", x_button, 200,
                                   text_color=constants.COLOR_PAUSE_MENU_TEXT)
        close = buttons.Button("exit", x_button, 300,
                               text_color=constants.COLOR_PAUSE_MENU_TEXT)

        # rysuje przyciski na ekranie
        continue_button.draw(window)
        main_menu.draw(window)
        close.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

        while True:
            print("pause")

            # zwraca nr naciśniętego przycisku
            button_number = check_which_button((continue_button, main_menu, close),
                                               (pygame.K_ESCAPE, pygame.K_p))
            # lewy przycisk myszy i 'continue' lub klawisz 'ESCAPE' lub 'p'
            if button_number == 1 or button_number == 0:
                return  # wraca do gry
            elif button_number == 2:  # lewy przycisk myszy i 'main menu'
                game.reset()  # resetuje stan gry
                game.run(game)  # uruchamia grę od początku
            elif button_number == 3:  # lewy przycisk myszy i 'exit'
                pygame.quit()
                exit(0)

    def win_menu(self, window, game):
        """Wyświetla menu zwycięstwa

        Pojawia się po zbiciu wszystkich klocków z planszy. Składa się z przycisków: 'main menu',
        które przenosi do menu głównego poprzez wywołanie funkcji game.run(game), oraz 'exit'
        który kończy pracę programu."""

        x, y = 0, 0  # współrzędne kursora myszy
        while True:
            self.surface.fill(constants.COLOR_WIN_MENU)  # koloruje tło menu
            window.print_headline("You won!", constants.COLOR_WIN_MENU_HEADLINE)  # nagłówek menu

            # tworzy obiekty będące przyciskami
            x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # lewa krawędź przycisku
            main_menu = buttons.Button("main menu", x_button, 100,
                                       text_color=constants.COLOR_WIN_MENU_TEXT)
            close = buttons.Button("exit", x_button, 200,
                                   text_color=constants.COLOR_WIN_MENU_TEXT)

            # rysuje przyciski na ekranie
            main_menu.draw(window)
            close.draw(window)

            pygame.display.update()  # nanosi zmiany na ekran

            while True:
                print("win menu")

                # zwraca nr naciśniętego przycisku
                button_number = check_which_button((main_menu, close))
                if button_number == 1:  # lewy przycisk myszy i 'main menu'
                    game.run(game)
                elif button_number == 2:  # lewy przycisk myszy i 'exit'
                    pygame.quit()
                    exit(0)

    def print_headline(self, text, color):
        """Funkcja pomocnicza do pisania nagłówku w menu"""

        headline_obj = constants.FONT_HEADINGS.render(text, True, color)
        headline_rect = headline_obj.get_rect()
        headline_rect.center = (self.width / 2, 30)
        self.surface.blit(headline_obj, headline_rect)


def check_which_button(buttons, keys=None):
    """Zwraca numer wybranego przez użytkownika przycisku z listy otrzymanych jako argumenty"""

    x, y = 0, 0  # współrzedne kursora myszy
    while True:
        print("buttons check")
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
