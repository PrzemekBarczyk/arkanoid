"""Moduł zawierający klasę piłki."""

import math

import pygame

from game_module import constants


class Ball:
    """Klasa piłki:

    Piłka sama kontroluje swoją prędkość i kierunek poruszania się, oraz wykrywa kolizje z paletką
    gracza i klockami"""

    # wyłącza warning pylinta o za dużej liczbie zmiennych w klasie
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        """Konstruktor inicjalizuje zmienne i tworzy powierzchnie piłki."""

        # wymiary piłki
        self.width = int(constants.BALL_WIDTH)
        self.height = int(constants.BALL_HEIGHT)

        # początkowe współrzędne piłki
        self.start_x_cord = int(constants.BALL_START_X)
        self.start_y_cord = int(constants.BALL_START_Y)

        # aktualne współrzędne piłki
        self.x_cord = int(self.start_x_cord)
        self.y_cord = int(self.start_y_cord)

        self.color = constants.BALL_COLOR
        self.speed = constants.BALL_SPEED  # prędkość poruszania piłki (piksele/tick procesora)
        self.direction = 150  # początkowy kąt poruszania się piłki w stopniach

        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        # ustawienie prostokąta zawierającego obiekt w początkowej pozycji
        self.rect = self.surface.get_rect(x=self.start_x_cord, y=self.start_y_cord)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])

    def reset(self):
        """Resetuje ustawienie i kierunek poruszania się piłki."""

        self.x_cord = self.start_x_cord
        self.y_cord = self.start_y_cord
        self.direction = 150

    def bounce(self, side):
        """Zmienia kierunek przemieszczania piłki po odbiciu od poziomej powierzchni."""

        # oblicza zmiane kierunku
        self.direction = (180 - self.direction) % 360
        # modyfikuje kierunek uwzględniając punkt paletki od którego odbiła się piłka
        self.direction += side

    def move(self, racket, bricks: list, window, game, judge):
        """Przesuwa piłkę i wykrywa kolizje.

        Piłka jest przesuwana o wartość wektora prędkości. W przypadku wykrycia kolizji zmieniany
        jest kierunek poruszania się piłki."""

        direction_radians = math.radians(self.direction)  # konwersja stopni na radiany

        # wyznacza nowe współrzędne piłki na podstawie prędkości i kierunku
        self.x_cord += self.speed * math.sin(direction_radians)
        self.y_cord -= self.speed * math.cos(direction_radians)

        # aktualizuje współrzędne obiektu piłki
        self.rect.x = round(self.x_cord)
        self.rect.y = round(self.y_cord)

        # piłka wykracza poza okno gry z lewej
        if self.rect.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x_cord = 1  # zabezpieczenie przed wypadnięciem piłki poza okno

        # piłka wykracza poza okno gry z prawej
        elif self.rect.x >= window.width - self.width:
            self.direction = (360 - self.direction) % 360
            # zabezpieczenie przed wypadnięciem piłki poza okno
            self.x_cord = window.width - self.width - 1

        # piłka wykracza poza okno gry z góry
        elif self.y_cord <= 0:
            self.bounce(0)
            self.y_cord = 1  # zabezpieczenie przed wypadnięciem piłki poza okno

        # piłka wykracza poza okno gry z dołu
        elif self.rect.y > window.height:
            judge.remove_life(game, self)

        # sprawdza czy nastąpiła kolizja między piłką a paletką
        elif self.rect.colliderect(racket.rect):
            # odległość środka piłki od środka paletki
            distance = (self.rect.x + self.width / 2) - (racket.rect.x + racket.width / 2)
            # zabezpieczenie przed wpadnięciem piłki w paletkę
            self.y_cord = racket.y_cord - self.height - 1
            self.bounce(distance)

        # sprawdza czy nastąpiła kolizja między piłką a klockiem
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)  # usuń klocek z listy
                if not bricks:  # wszystkie klocki zbite
                    game.reset()
                    game.menu_id = 5  # wyświetl odpowiednie menu
                    return
                if brick.rect.y <= self.rect.y <= brick.rect.y + brick.height - self.height: # bok
                    self.direction = (360 - self.direction) % 360
                else:  # dół lub góra klocka
                    self.bounce(0)
                break  # zabezpieczenie przed zbiciem kilku klocków na raz

    def draw(self, window):
        """Rysuje piłkę w oknie."""

        window.surface.blit(self.surface, self.rect)
