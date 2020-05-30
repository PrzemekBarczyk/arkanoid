"""Moduł zawierający klasę bazową menusów, klasy pochodne oddzielne dla
każdego typu menu, oraz funkcje pomocnicze modułu

Klasa bazowa łączy elementy wspólne dla wszystkich menu (parametry i funkcję draw()).
Klasy pochodne zwracają kod na podstawie którego w pętli głównej programu podejmowana
jest odpowiednia akcja np. uruchomienie konkretnego menu lub uruchomienie fragmentu kodu
odpowiedzialnego za rozgrywkę."""
# pylint: disable=too-few-public-methods
# pylint: disable=no-member

import sys

import pygame

from game_module import buttons
from game_module import constants


class Menu:
    """Klasa bazowa dla wszystkich menusów:

    Zawiera niezbędne parametry charakteryzujące każde menu, oraz metodę draw() do
    rysowania menu na ekranie wspólną dla każdego typu menu.

    Attributes:
        name: String oznaczający nazwę menu która będzie wypisana na jego górze.
        buttons_names: Lista stringów z nazwami przycisków do utworzenia.
        background_color: Krotka integerów określających kolor tła.
        headline_color: Krotka integerów określających kolor nagłówka menu."""

    def __init__(self, name, buttons_names, background_color, headline_color):
        """Kontruktor zapisuje parametry określające menu, oraz tworzy obiekty
        przycisków o podanych nazwach"""

        self.name = name  # nazwa menu
        self.buttons_names = buttons_names  # lista z nazwami przycisków
        self.background_color = background_color
        self.headline_color = headline_color
        self.buttons_objects = []  # lista na obiekty klasy Button

        # tworzy obiekty przycisków
        for button in enumerate_with_step(buttons_names, start=100, step=100):
            button_y, button_name = button
            self.buttons_objects.append(buttons.Button(button_name, y=button_y))

        print("created " + self.name)

    def draw(self, window):
        """Rysuje odpowiednie menu"""

        window.surface.fill(self.background_color)  # koloruje tło menu
        print_headline(window, self.name, self.headline_color)  # nagłówek menu

        for button in self.buttons_objects:  # rysuje przyciski
            button.draw(window)

        pygame.display.update()  # nanosi zmiany na ekran


class MainMenu(Menu):
    """Klasa menu głównego dziedzicząca z klasy bazowej Menu:

    Rozszerza klasę bazową o funkcję run(). Uruchamiana jest w pierwszej iteracji głównej
    pętli programu lub gdy w innym miejscu programu zostanie zwrócony odpowiedni kod."""

    def __init__(self, name, buttons_names):
        """Wywołuje konstruktor klasy bazowej przekazując mu swoje argumenty wywołania"""

        super().__init__(name, buttons_names, constants.COLOR_MENU, constants.COLOR_MENU_HEADLINE)

    def run(self):
        """Pozwala wybrać użytkownikowi spośród opcji charakterystycznych dla menu głównego

        Użytkownik może wybrać przy użyciu myszy jedną z opcji: 'start', 'options', 'exit'.
        'Start' uruchamia rozgrywkę.
        'Options' otwiera menu opcji.
        'Exit' kończy pracę programu.

        Returns:
            Kod 0 po naciśnięciu przycisku 'start', który odpowiada za uruchomienie rozgrywki
            Kod 2 po naciśnięciu przycisku 'options', który odpowiada za uruchomienie menu z
            opcjami.

        Raises:
             SystemExit(0): naciśnięto klawisz 'exit' odpowiadający za zakończenie rozgrywki."""

        print("entered main menu")
        while True:
            # sprawdzenie który przycisk został naciśnięty
            button_number = check_which_button(self.buttons_objects)
            if button_number == 1:  # wybrano 'start'
                return 0  # uruchamia rozgrywkę
            if button_number == 2:  # wybrano 'options'
                return 2  # uruchomia menu opcji
            if button_number == 3:  # wybrano 'close'
                pygame.quit()
                sys.exit(0)


class SettingsMenu(Menu):
    """Klasa menu opcji dziedzicząca z klasy bazowej Menu:

    Rozszerza klasę bazową o funkcję run(). Menu możliwe jest do uruchomienia z poziomu
    menu głownego.

    Attributes:
        difficulty_nr: Integer służący do kontroli aktualnie wybranej opcji trudności.
        resolution_nr: Integer służący do kontroli aktulanie wybranej opcji rozdzielczości.
        fullscreen_nr: Integer służący do kontroli aktulanie wybranej opcji typu wyświetlania
        okna."""

    def __init__(self, name, buttons_names):
        """Wywołuje konstruktor klasy bazowej przekazując mu swoje argumenty wywołania"""

        super().__init__(name, buttons_names, constants.COLOR_MENU, constants.COLOR_MENU_HEADLINE)
        self.difficulty_nr, self.resolution_nr, self.fullscreen_nr = 0, 0, 0

    def run(self, window, game):
        """Pozwala wybrać użytkownikowi opcje charakterystyczne dla menu opcji

        Do wyboru są opcje: 'difficulty', 'resolution', 'fullscreen' i 'main menu
        'Difficulty' pozwala na wybór jednego z 3 poziomów trugności (łatwy, średni,
        trudny). Zmiana poziomów możliwa jest przez pojedyńcze kliknięcie na przycisk.
        Domyślnie ustawiony jest poziom trudności łatwy. Wraz ze zmianą poziomu
        zmienia się prędkość poruszania piłki.
        'Resolution' odpowiada za zmianę rozdzielczości okna. Dostępne są dwie
        rozdzielczości: 800x600, 1200x800. Zasada zmiany rozdzielczości jest analogiczna
        do zmiany poziomu trudności. Domyśla rozdzielczość to 800x600.
        'Fullscreen' zaznaczenie tej opcji zmienia tryb wyświetlania programu na
        pełnoekranowy lub okienkowy. Domyślnie aplikacja wyświetlana jest w oknie.
        'Main menu' pozwala na powrót do menu głównego.

        Returns:
            Kod 1 po naciśnięciu przycisku 'main menu', który odpowiada za uruchomienie menu
            głównego."""

        while True:
            print("entered settings menu")
            # sprawdzenie który przycisk został naciśnięty
            button_number = check_which_button(self.buttons_objects)

            # podjęcie odpowiednich działań w zależności od przyciśniętego przycisku
            if button_number == 1:  # wybrano 'difficulty'
                self.difficulty_nr += 1  # zmienia poziom trudności na następny
                game.fps = constants.FPS_LIMIT[self.difficulty_nr % 3]  # zmiana limitu FPS
                if self.difficulty_nr % 3 == 0:  # easy
                    self.buttons_objects[0].name = "difficulty: easy"
                elif self.difficulty_nr % 3 == 1:  # medium
                    self.buttons_objects[0].name = "difficulty: medium"
                elif self.difficulty_nr % 3 == 2:  # hard
                    self.buttons_objects[0].name = "difficulty: hard"
                self.draw(window)  # nanosi zmiany na ekran

            elif button_number == 2:  # wybrano 'resolution'
                self.resolution_nr += 1  # zmienia rozdzielczość na następną

                # aktualizacja bieżącej rozdzielczości
                window.update(constants.RESOLUTIONS[self.resolution_nr % 2],
                              constants.FULLSCREEN[self.fullscreen_nr % 2])

                # aktualizacja napisu na przycisku
                if self.resolution_nr % 2 == 0:  # 800x600
                    self.buttons_objects[1].name = "resolution: 800x600"
                elif self.resolution_nr % 2 == 1:  # 1200x900
                    self.buttons_objects[1].name = "resolution: 1200x900"

                # dopasowuje elementy do nowej rozdzielczości i nanosi zmiany na ekran
                game.update()
                self.draw(window)

            elif button_number == 3:  # wybrano 'fullscreen'
                self.fullscreen_nr += 1  # zmienia tryb okna na następny
                # zmiana trybu wyświetlania okna i aktualizacja zmian
                window.update(constants.RESOLUTIONS[self.resolution_nr % 2],  # zmiana trybu okna
                              constants.FULLSCREEN[self.fullscreen_nr % 2])
                if self.fullscreen_nr % 2 == 0:  # on
                    self.buttons_objects[2].name = "fullscreen: off"
                elif self.fullscreen_nr % 2 == 1:  # off
                    self.buttons_objects[2].name = "fullscreen: on"
                self.draw(window)  # nanosi zmiany na ekran

            elif button_number == 4:  # wybrano 'main menu'
                return 1  # uruchom menu główne


class GameOverMenu(Menu):
    """Klasa menu porażki dziedzicząca z klasy bazowej Menu:

    Rozszerza klasę bazową o funkcję run(). Uruchamia się po tym jak piłka wypadnie poza dół
    okienka programu i resetuje stan gry (lokalizację piłki, ilość zbitych klocków)."""

    def __init__(self, name, buttons_names):
        """Wywołuje konstruktor klasy bazowej przekazując mu swoje argumenty wywołania"""

        super().__init__(name, buttons_names, constants.COLOR_GAME_OVER_MENU,
                         constants.COLOR_GAME_OVER_MENU_HEADLINE)

    def run(self, game):
        """Pozwala wybrać użytkownikowi opcje charakterystyczne dla menu porażki

        Użytkownik może wybrać jedną z 3 opcji: 'try again', 'main menu', 'exit'.
        'Try again' uruchamia rozgrywkę jeszcze raz.
        'Main menu' otwiera menu główne.

        Attributes:
            Kod 0 po naciśnięciu przycisku 'try again', który odpowiada za ponowne uruchomienie
            rozgrywki ze zresetowanym stanem gry.
            Kod 1 po naciśnięciu przycisku 'main menu', który odpowiada za uruchomienie menu
            głównego.

        Raises:
            SystemExit(0): naciśnięto klawisz 'exit' odpowiadający za zakończenie rozgrywki."""

        print("entered game over menu")
        game.reset()
        while True:
            # sprawdzenie który przycisk został naciśnięty
            button_number = check_which_button(self.buttons_objects)

            if button_number == 1:  # wybrano 'try again'
                return 0  # uruchamia rozgrywkę
            if button_number == 2:  # wybrano 'main menu'
                return 1  # uruchamia menu główne
            if button_number == 3:  # wybrano 'exit'
                pygame.quit()
                sys.exit(0)


class PauseMenu(Menu):
    """Klasa menu pauzy dziedzicząca z klasy bazowej Menu:

    Rozszerza klasę bazową o funkcję run(). Menu można wywołać klawiszem ESCAPE lub P w
    trakcie gry."""

    def __init__(self, name, buttons_names):
        """Wywołuje konstruktor klasy bazowej przekazując mu swoje argumenty wywołania"""

        super().__init__(name, buttons_names, constants.COLOR_PAUSE_MENU,
                         constants.COLOR_PAUSE_MENU_HEADLINE)

    def run(self, game):
        """Pozwala wybrać użytkownikowi opcje charakterystyczne dla menu pauzy

        Zatrzymuj rozgrywkę i wyświetla ekran menu z którego można wybrać:
        'continue', 'main menu' i 'exit'.
        'Continue' pozwala kontynuować rozgrywkę z niezmienionym stanem rozgrywki
        (położenie piłki, liczba zbitych klocków).
        'Main menu' uruchamia menu główne.
        'Exit' kończy pracę programu. Powrót do rozgrywki możliwy jest również przy użyciu
        tych samych klawiszy które słuszą do wywołania menu.

        Attributes:
            Kod 0 po naciśnięciu przycisku 'continue', który odpowiada za kontynuowanie
            rozgrywki.
            Kod 1 po naciśnięciu przycisku 'main menu', który odpowiada za otwarcie
            menu głównego.

        Raises:
            SystemExit(0): naciśnięto klawisz 'exit' odpowiadający za zakończenie rozgrywki."""

        print("entered pause menu")
        while True:
            # sprawdzenie który przycisk został naciśnięty
            button_number = check_which_button(self.buttons_objects, (pygame.K_ESCAPE, pygame.K_p))

            if button_number == 1 or button_number == 0:  # wybrano 'continue', 'ESCAPE' lub 'P'
                return 0  # wraca do gry
            if button_number == 2:  # wybrano 'main menu'
                game.reset()  # resetuje stan gry (piłke, level, sędziego)
                return 1  # uruchamia menu główne
            if button_number == 3:  # wybrano 'exit'
                pygame.quit()
                sys.exit(0)


class WinMenu(Menu):
    """Klasa menu pauzy dziedzicząca z klasy bazowej Menu:

    Rozszerza klasę bazową o funkcję run(). Pojawia się po zbiciu wszystkich klocków z
    planszy.

    Attributes:
        Takie same jak w klasie bazowej Menu."""

    def __init__(self, name, buttons_names):
        """Wywołuje konstruktor klasy bazowej przekazując mu swoje argumenty wywołania"""

        super().__init__(name, buttons_names, constants.COLOR_WIN_MENU,
                         constants.COLOR_WIN_MENU_HEADLINE)

    def run(self, game):
        """Pozwala wybrać użytkownikowi opcje charakterystyczne dla menu zwycięstwa

        Składa się z przycisków: 'main menu', który przenosi do menu głównego poprzez zwrócenie
        kodu 1, oraz 'exit' który kończy pracę programu.

        Returns:
            Kod 1 po naciśnięciu przycisku 'main menu', który uruchamia menu główne.

        Raises:
            SystemExit(0): naciśnięto klawisz 'exit' odpowiadający za zakończenie rozgrywki."""

        print("entered win menu")
        game.reset()  # resetuje stan gry (piłke, level, sędziego)
        while True:
            # sprawdzenie który przycisk został naciśnięty
            button_number = check_which_button(self.buttons_objects)
            if button_number == 1:  # wybrano 'main menu'
                game.reset()
                return 1  # uruchamia menu główne
            if button_number == 2:  # wybrano 'exit'
                pygame.quit()
                sys.exit(0)


def enumerate_with_step(xs, start=0, step=100):
    """Funkcja działająca jak enumerate, pozwalająca dodatkowo wyznaczyć krok o jaki
    zwiększane są wartości"""

    for x in xs:
        yield start, x
        start += step


def print_headline(window, text, color):
    """Funkcja pomocnicza do pisania nagłówków w menu"""

    headline_obj = constants.FONT_HEADINGS.render(text, True, color)
    headline_rect = headline_obj.get_rect()
    headline_rect.center = (window.width // 2, 30)
    window.surface.blit(headline_obj, headline_rect)


def check_which_button(buttons_list, keys=None):
    """Zwraca numer wybranego przez użytkownika przycisku z listy otrzymanych jako argumenty,
    oraz 0 jeśli naciśnięto klawisz 'ESCAPE' lub 'P'"""

    print("entered buttons check")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # wciśnięto krzyżyk w prawym-górnym rogu okna programu
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:  # wciśnięto klawisz na klawiaturze
                for key in keys:
                    if event.key == key:  # ESCAPE lub P
                        return 0  # zwraca 0
            if event.type == pygame.MOUSEBUTTONDOWN:  # klawisz myszy wciśnięty
                x_cord, y_cord = event.pos  # zapisuje aktualne współrzędne kursora
                for button in enumerate(buttons_list, start=1):
                    # lewy przycisk myszy i kursor nad przyciskiem
                    if event.button == 1 and button[1].rect.collidepoint(x_cord, y_cord):
                        return button[0]  # zwraca numer przycisku
