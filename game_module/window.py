"""Klasa okna programu z metodami rysowania różnych menu"""

import pygame
from game_module import constants
from game_module import buttons


class Window:
    """Klasa odpowiadająca za okno programu i wyświetlanie na ekranie menu.
    Zmienna surface wymagana przy rysowaniu innych obiektów w okienku programu"""

    def __init__(self):
        """Tworzy okienko programu o podanych rozmiarach"""
        self.width = constants.WINDOW_WIDTH
        self.height = constants.WINDOW_HEIGHT

        self.surface = pygame.display.set_mode((self.width, self.height))  # tworzy 'powierzchnie'(okienko programu)
        pygame.display.set_caption('Half-Life 3')

    def draw(self):
        """Wypełnia 'powierzchnie' kolorem"""
        self.surface.fill(constants.COLOR_BACKGROUND)

    def main_menu(self, window):
        """Tworzy główne menu gry i pozwala wybrać przy użyciu myszy jedną z opcji: 'start', 'options', 'exit'.
        'Start' kończy działanie funkcji po czym program przechodzi do wykonywania funkcji znajdujących się w
        głównej pętli programu. 'Options' wywołuje funkcję odpowiedzialną za wyświetlenie menu z opcjami.
        'Exit' dezaktywuje bibliotekę pygame, po czym kończy pracę programu funkcją exit(0)"""
        x, y = 0, 0  # współrzędne kursora myszy
        headline_color = (18, 49, 77)  # kolor nagłówka menu
        text_color = (255, 255, 255)  # kolor napisów na przyciskach
        while True:
            print("main menu")
            self.surface.fill(constants.COLOR_MENU)  # koloruje tło menu
            window.print_headline("Main menu", headline_color)  # wypisuje nagłówek menu

            # tworzy obiekty będące przyciskami
            x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # współrzędna x lewej krawędzi przycisku
            start = buttons.Button("start", x_button, 100, text_color=text_color)
            options = buttons.Button("options", x_button, 200, text_color=text_color)
            close = buttons.Button("exit", x_button, 300, text_color=text_color)

            # rysuje przyciski na ekranie
            start.draw(window)
            options.draw(window)
            close.draw(window)

            pygame.display.update()  # nanosi zmiany na ekran

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu okna programu
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEMOTION:  # mysz się porusza
                    x, y = event.pos  # zapisuje aktualne współrzędne kursora
                if event.type == pygame.MOUSEBUTTONDOWN:  # klawisz myszy wciśnięty
                    if event.button == 1 and start.rect.collidepoint(x, y):  # LPM i kursor na przyciskiem start
                        return  # wraca do pętli głównej programu (odpala gre)
                    if event.button == 1 and options.rect.collidepoint(x, y):  # LPM i kursor nad przyciskiem opctions
                        window.options_menu(window)  # uruchamia menu opcji
                    if event.button == 1 and close.rect.collidepoint(x, y):  # LPM i kursor nad przyciskiem close
                        pygame.quit()
                        exit(0)

    def options_menu(self, window):
        """Tworzy menu z opcjami: 'difficulty' i 'background color'. Użytkownik może je zmieniać przy użyciu LPM.
        Pod opcjami znajduje się przycisk 'return' który kończy działanie tej funkcji i wraca do miejsca
        wywołania - funkcji main_menu(). Ten sam efekt powrotu do poprzedniego menu można uzyskać przy użyciu
        klawisza ESCAPE"""
        x, y = 0, 0  # współrzedne kursora myszy
        headline_color = (0, 0, 0)  # kolor nagłówka menu
        text_color = (255, 255, 255)  # kolor napisów na przyciskach
        self.surface.fill(constants.COLOR_MENU)  # koloruje tło menu
        window.print_headline("Settings", headline_color)  # wypisuje nagłówek menu

        # tworzy obiekty będące przyciskami
        x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # współrzędna x lewej krawędzi przycisku
        difficulty = buttons.Button("difficulty", x_button, 100, text_color=text_color)
        background_color = buttons.Button("background color", x_button, 200, text_color=text_color)
        return_main_menu = buttons.Button("return", x_button, 300, text_color=text_color)

        # rysuje przyciski na ekranie
        difficulty.draw(window)
        background_color.draw(window)
        return_main_menu.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

        while True:
            print("options")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu okna programu
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEMOTION:  # mysz się porusza
                    x, y = event.pos  # zapisuje aktualne współrzędne kursora
                if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                    if event.key == pygame.K_ESCAPE:  # ESCAPE
                        return  # wróć do menu głównego
                if event.type == pygame.MOUSEBUTTONDOWN:  # wciśnięto klawisz myszy
                    if event.button == 1 and difficulty.rect.collidepoint(x, y):  # LPM i kursor nad 'resolution'
                        pass
                        # TODO: rozbudować
                    if event.button == 1 and background_color.rect.collidepoint(x, y):  # LPM i kursor nad 'backgroud..'
                        pass
                        # TODO: rozbudować
                    if event.button == 1 and return_main_menu.rect.collidepoint(x, y):  # LPM i kursor nad 'return'
                        return  # wróć do menu głównego

    def game_over_menu(self, window, game):
        """Tworzy menu końca gry. Uruchamia się pod tym jak piłka wypadnie poza dół okienka programu i resetuje
        stan gry (lokalizację piłki, ilość zbitych klocków). Użytkownik może wybrać czy chce kontynuować gre
        'try again', wrócić do menu głównego 'main menu' czy zakończyć gre 'exit'. Wybranie 'try again' kończy
        działanie funkcji i wraca do głównej pętli programu która kontynuuje działanie ze zresetowanym stanem gry.
        Opcja 'main menu' uruchamia funkcje game.run(game), która uruchamia menu główne następnie główną petlę
        programu. 'Exit' kończy pracę programu. Opcje możliwe są do wyboru przy użyciu LPM, ponadto klawisz ESCAPE
        odpowiada za wybranie opcji 'exit'."""
        game.reset()  # resetuje stan gry
        x, y = 0, 0  # współrzedne kursora myszy
        headline_color = (0, 0, 0)  # kolor nagłówka menu
        text_color = (255, 255, 255)  # kolor napisów na przyciskach
        self.surface.fill(constants.COLOR_GAME_OVER_MENU)  # koloruje tło menu
        window.print_headline("GAME OVER", headline_color)  # wypisuje nagłówek menu

        # tworzy obiekty będące przyciskami
        x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # współrzędna x lewej krawędzi przycisku
        try_again = buttons.Button("try again", x_button, 100, text_color=text_color)
        main_menu = buttons.Button("main menu", x_button, 200, text_color=text_color)
        close = buttons.Button("exit", x_button, 300, text_color=text_color)

        # rysuje przyciski na ekranie
        try_again.draw(window)
        main_menu.draw(window)
        close.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

        while True:
            print("game over")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym górnym rogu ekranu
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEMOTION:  # mysz się porusza
                    x, y = event.pos  # zapisuje aktualne współrzędne kursora
                if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                    if event.key == pygame.K_ESCAPE:  # ESCAPE
                        pygame.quit()
                        exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:  # wciśnięto klawisz myszy
                    if event.button == 1 and try_again.rect.collidepoint(x, y):  # LPM i 'try again'
                        return
                    if event.button == 1 and main_menu.rect.collidepoint(x, y):  # LPM i 'main menu'
                        game.run(game)
                    if event.button == 1 and close.rect.collidepoint(x, y):  # LPM i 'exit'
                        pygame.quit()
                        exit(0)

    def pause_menu(self, window, game):
        """Tworzy menu pauzy które można wywołać klawiszem ESCAPE lub P w trakcie gry. Zatrzymuje ono rozgrywkę
        i wyświetla ekran menu z którego można wybrać: 'continue', 'main menu' i 'exit'. Opcja 'continue' pozwala
        kontynuować rozgrywkę z niezmienionym stanem rozgrywki (położenie piłki, liczba zbitych klocków). 'Main menu'
        uruchamia funkcję game.run(game), która odpowiada za wyświetlenie menu głownego i uruchomienie pętli głównej
        programu. 'Exit' kończy pracę programu. Powrót do rozgrywki możliwy jest również przy użyciu tych samych
        klawiszy które słuszą do wywołania menu."""
        x, y = 0, 0  # współrzedne kursora myszy
        headline_color = (0, 0, 0)  # kolor nagłówka menu
        text_color = (255, 255, 255)  # kolor napisów na przyciskach
        self.surface.fill(constants.COLOR_GAME_OVER_MENU)  # koloruje tło menu
        window.print_headline("pause", headline_color)  # wypisuje nagłówek menu

        # tworzy obiekty będące przyciskami
        x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # współrzędna x lewej krawędzi przycisku
        continue_button = buttons.Button("continue", x_button, 100, text_color=text_color)
        main_menu = buttons.Button("main menu", x_button, 200, text_color=text_color)
        close = buttons.Button("exit", x_button, 300, text_color=text_color)

        # rysuje przyciski na ekranie
        continue_button.draw(window)
        main_menu.draw(window)
        close.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran

        while True:
            print("pause")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu ekranu
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEMOTION:  # mysz się porusza
                    x, y = event.pos  # zapisuje aktualne współrzędne kursora
                if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:  # ESCAPE lub P
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:  # wciśnięto klawisz myszy
                    if event.button == 1 and continue_button.rect.collidepoint(x, y):  # LPM i 'continue'
                        return
                    if event.button == 1 and main_menu.rect.collidepoint(x, y):  # LPM i 'main menu'
                        game.run(game)
                    if event.button == 1 and close.rect.collidepoint(x, y):  # LPM i 'exit'
                        pygame.quit()
                        exit(0)

    def win_menu(self, window, game):
        """Wyświetla menu zwycięstwa po zbiciu wszystkich klocków z planszy. Składa się z przycisków: 'main menu',
        które przenosi do menu głównego poprzez wywołanie funkcji game.run(game), oraz 'exit' który kończy pracę
        programu."""
        x, y = 0, 0  # współrzędne kursora myszy
        headline_color = (0, 255, 0)  # kolor nagłówka menu (zielony)
        text_color = (255, 255, 255)  # kolor napisów na przyciskach (biały)
        while True:
            self.surface.fill(constants.COLOR_WIN_MENU)  # koloruje tło menu
            window.print_headline("You won!", headline_color)  # wypisuje nagłówek menu

            # tworzy obiekty będące przyciskami
            x_button = self.width / 2 - constants.BUTTON_WIDTH / 2  # współrzędna x lewej krawędzi przycisku
            main_menu = buttons.Button("main menu", x_button, 100, text_color=text_color)
            close = buttons.Button("exit", x_button, 200, text_color=text_color)

            # rysuje przyciski na ekranie
            main_menu.draw(window)
            close.draw(window)

            pygame.display.update()  # nanosi zmiany na ekran

            while True:
                print("win menu")

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu ekranu
                        pygame.quit()
                        exit(0)
                    if event.type == pygame.MOUSEMOTION:  # mysz się porusza
                        x, y = event.pos  # zapisuje aktualne współrzędne kursora
                    if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:  # ESCAPE lub P
                            return
                    if event.type == pygame.MOUSEBUTTONDOWN:  # wciśnięto klawisz myszy
                        if event.button == 1 and main_menu.rect.collidepoint(x, y):  # LPM i 'main menu'
                            game.run(game)
                        if event.button == 1 and close.rect.collidepoint(x, y):  # LPM i 'exit'
                            pygame.quit()
                            exit(0)

    def print_headline(self, text, color):
        """Funkcja pomocnicza do pisania nagłówku w menu"""
        headline_obj = constants.FONT_HEADINGS.render(text, True, color)
        headline_rect = headline_obj.get_rect()
        headline_rect.center = (self.width / 2, 30)
        self.surface.blit(headline_obj, headline_rect)
