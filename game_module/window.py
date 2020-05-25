"""Moduł zawierający klasę okna i funkcję sprawdzającą który przycisk został wybrany
przez użytkownika"""


import sys

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

    def update(self, new_resolution, flags):
        """Zmienia rozmiar okna programu"""
        self.surface = pygame.display.set_mode(new_resolution, flags)
        self.width = new_resolution[0]
        self.height = new_resolution[1]

    def draw(self):
        """Wypełnia 'powierzchnie' kolorem"""
        self.surface.fill(constants.COLOR_BACKGROUND)

########################################################
    #
    # def draw_main_menu(self, window):
    #     """Tworzy główne menu gry:
    #
    #     Użytkownik może wybrać przy użyciu myszy jedną z opcji: 'start', 'options', 'exit'.
    #     'Start' kończy działanie funkcji po czym program przechodzi do wykonywania funkcji
    #     znajdujących się w głównej pętli programu.
    #     'Options' wywołuje funkcję odpowiedzialną za wyświetlenie menu z opcjami.
    #     'Exit' dezaktywuje bibliotekę pygame, po czym kończy pracę programu funkcją exit(0)"""
    #
    #
    # def draw_options_menu(self, window):
    #     """Tworzy menu z opcjami:
    #
    #     Do wyboru są opcje: 'difficulty' i 'background color'. Użytkownik może zmieniać opcję przy
    #     użyciu lewego przycisku myszy. Pod opcjami znajduje się przycisk 'return' który kończy
    #     działanie tej funkcji i wraca do miejsca wywołania - funkcji main_menu(). Ten sam efekt
    #     powrotu do poprzedniego menu można uzyskać przy użyciu klawisza ESCAPE"""
    #
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
    #
    # def win_menu(self, window, game):
    #     """Wyświetla menu zwycięstwa
    #
    #     Pojawia się po zbiciu wszystkich klocków z planszy. Składa się z przycisków: 'main menu',
    #     które przenosi do menu głównego poprzez wywołanie funkcji game.run(game), oraz 'exit'
    #     który kończy pracę programu."""

