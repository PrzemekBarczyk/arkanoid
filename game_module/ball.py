"""Moduł zawierający klasę piłki"""

import pygame
import math
from game_module import constants


class Ball:
    """Klasa piłki:

    Piłka sama kontroluje swoją prędkość i kierunek poruszania się, oraz wykrywa kolizje z paletką gracza i
    klockami"""

    # wyłącza warning pylinta o za dużej liczbie zmiennych w klasie
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        """Konstruktor inicjalizuje zmienne i tworzy powierzchnie piłki"""

        # wymiary piłki
        self.width = constants.BALL_WIDTH
        self.height = constants.BALL_HEIGHT

        # początkowe współrzędne piłki
        self.start_x_cord = constants.BALL_START_X
        self.start_y_cord = constants.BALL_START_Y

        # aktualne współrzędne piłki
        self.x_cord = self.start_x_cord
        self.y_cord = self.start_y_cord

        self.color = constants.COLOR_BALL
        self.speed = constants.BALL_SPEED  # prędkość przemieszczania piłki w pikselach na tick procesora
        self.direction = 150  # początkowy kąt poruszania się piłki w stopniach

        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        # ustawienie prostokąta zawierającego obiekt w początkowej pozycji
        self.rect = self.surface.get_rect(x=self.start_x_cord, y=self.start_y_cord)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])

    def reset(self):
        """Resetuje ustawienie i kierunek poruszania się piłki"""

        self.x_cord = self.start_x_cord
        self.y_cord = self.start_y_cord
        self.direction = 150

    def bounce(self, side):
        """Zmienia kierunek przemieszczania piłki po odbiciu od poziomej powierzchni"""

        self.direction = (180 - self.direction) % 360  # oblicza zmiane kierunku
        self.direction += side  # modyfikuje kierunek uwzględniając punkt paletki od którego odbiła się piłka
        # self.rect.y = constants.RACKET_Y - self.width - 1 # chyba nic nie daje

    def move(self, racket, bricks: list, window, game):
        """Przesuwa piłkę i wykrywa kolizje

        Piłka jest przesuwana o wartość wektora prędkości. W przypadku wykrycia kolizji zmieniany jest kierunek
        poruszania się piłki."""

        direction_radians = math.radians(self.direction)  # konwersja stopni na radiany

        # wyznacza nowe współrzędne piłki na podstawie prędkości i kierunku
        self.x_cord += self.speed * math.sin(direction_radians)
        self.y_cord -= self.speed * math.cos(direction_radians)

        # aktualizuje współrzędne obiektu piłki
        self.rect.x = self.x_cord
        self.rect.y = self.y_cord

        # piłka wykracza poza okno gry z lewej
        if self.rect.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x_cord = 1  # zabezpieczenie przed wypadnięciem piłki poza okno

        # piłka wykracza poza okno gry z prawej
        elif self.rect.x >= constants.WINDOW_WIDTH - self.width:
            self.direction = (360 - self.direction) % 360
            self.x_cord = constants.WINDOW_WIDTH - self.width - 1 # zabezpieczenie przed wypadnięciem piłki poza okno

        # piłka wykracza poza okno gry z góry
        elif self.y_cord <= 0:
            self.bounce(0)
            self.y_cord = 1  # zabezpieczenie przed wypadnięciem piłki poza okno

        # piłka wykracza poza okno gry z dołu
        elif self.rect.y > constants.WINDOW_HEIGHT:
            window.game_over_menu(window, game)

        # sprawdza czy nastąpiła kolizja między piłką a paletką
        elif self.rect.colliderect(racket.rect):
            # odległość środka piłki od środka paletki
            distance = (self.rect.x + self.width / 2) - (racket.rect.x + racket.width / 2)
            self.bounce(distance)

        # sprawdza czy nastąpiła kolizja między piłką a klockiem
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)  # usuń klocek z listy
                if len(bricks) == 0:  # wszystkie klocki zbite
                    window.win_menu(window, game)  # wyświetl odpowiednie menu
                self.bounce(0)

    def draw(self, window):
        """Rysuje piłkę w oknie"""

        window.surface.blit(self.surface, self.rect)
