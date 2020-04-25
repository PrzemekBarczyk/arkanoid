"""Klasa reprezenetująca piłkę"""

import math
import pygame
from game_module import constants


class Ball:
    """Piłka - sama kontroluje prędkość i kierunek poruszania się, oraz kolizje z paletką i
    klockami"""

    # wyłącza warning pylinta o za dużej liczbie zmiennych w klasie
    # pylint: disable=too-many-instance-attributes
    def __init__(self): # inicjalizuje zmienne
        self.width = constants.BALL_WIDTH  # szerokość piłki
        self.height = constants.BALL_HEIGHT  # wysokość piłki
        self.start_x_cord = constants.BALL_START_X  # początkowe współrzędne piłki
        self.start_y_cord = constants.BALL_START_Y
        self.x_cord = self.start_x_cord  # aktualne współrzędne piłki
        self.y_cord = self.start_y_cord
        self.color = constants.COLOR_BALL
        self.speed = constants.BALL_SPEED  # prędkość przemieszczania piłki w pikselach na tick procesora
        self.direction = 150  # kąt poruszania się piłki w stopniach

        # konfiguruje kształt piłki
        self.surface = pygame.Surface([self.width, self.height])  # utworzenie pow. obiektu
        self.rect = self.surface.get_rect(x=self.start_x_cord, y=self.start_y_cord)  # ustawienie prostokąta ...
        # zawierającego obiekt w początkowej pozycji
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])

    def reset_configuration(self):
        self.x_cord = self.start_x_cord
        self.y_cord = self.start_y_cord
        self.direction = 150

    def bounce(self, side):
        """Zmienia kierunek przemieszczania piłki po odbiciu od poziomej powierzchni"""
        self.direction = (180 - self.direction) % 360  # oblicza zmiane kierunku
        self.direction += side  # modyfikuje kierunek uwzględniając punkt paletki od którego odbiła się piłka
        # self.rect.y = constants.RACKET_Y - self.width - 1 # chyba nic nie daje

    def reset(self):
        """Resetuje położenie piłki - ustawia ją w położeniu początkowym"""
        self.x_cord = self.start_x_cord
        self.y_cord = self.start_y_cord
        # self.bounce(0)

    def move(self, racket, bricks: list, window, game):
        """Przesuwa piłkę o wektro prędkości"""
        direction_radians = math.radians(self.direction)  # konwersja stopni na radiany

        # wyznacza nowe współrzędne piłki na podstawie prędkości i kierunku
        self.x_cord += self.speed * math.sin(direction_radians)
        self.y_cord -= self.speed * math.cos(direction_radians)
        # aktualizuje współrzędne obiektu piłki
        self.rect.x = self.x_cord
        self.rect.y = self.y_cord

        # jeśli wykraczamy poza okno gry w lewo
        if self.rect.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x_cord = 1  # zabezpieczenie przed wypadnięciem

        # jeżeli wykraczamy poza okno gry w prawo
        if self.rect.x >= constants.WINDOW_WIDTH - self.width:
            self.direction = (360 - self.direction) % 360
            self.x_cord = constants.WINDOW_WIDTH - self.width - 1

        # jeżeli wykraczamy poza okno gry w górę
        if self.y_cord <= 0:
            self.bounce(0)
            self.y_cord = 1  # zabezpieczenie przed wypadnięciem

        # jeżeli wykraczamy poza okno gry w dół
        if self.rect.y > constants.WINDOW_HEIGHT:
            window.game_over_menu(window, game)

        # sprawdza czy nastąpiła kolizja między piłką a paletką
        if self.rect.colliderect(racket.rect):
            side = (self.rect.x + self.width / 2) - (racket.rect.x + racket.width / 2)  # odległość piłki od rakiety
            self.bounce(side)

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
