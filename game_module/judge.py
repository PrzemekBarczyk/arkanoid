"""Klasa sędziego gry - w budowie"""

# import pygame
# from game_module import constants
#
#
# class Judge:
#     """Sędzia gry - liczy ilość śmierci gracza oraz wyświetla informacje w oknie"""
#
#     def __init__(self, Window, Ball, Racket):
#         self.ball = Ball
#         self.window = Window
#         self.racket = Racket
#         self.score = 0
#
#         # Przed pisaniem tekstów, musimy zainicjować mechanizmy wyboru fontów PyGame
#         pygame.font.init()
#         font_path = pygame.font.match_font('arial')
#         self.font = pygame.font.Font(font_path, constants.FONT_SIZE)
#
#     def update_score(self, board_height):
#         """Przydziela punkty i ustawia piłeczkę w poczatkowym położeniu"""
#         if self.ball.rect.y == board_height:
#             self.score += 1
#             self.ball.reset()
#
#     def draw_text(self, surface, text, x_cord, y_cord):
#         """Rysuje podany tekst we wskazanym miejscu"""
#         text = self.font.render(text, True, (150, 150, 150))
#         rect = text.get_rect()
#         rect.center = x_cord, y_cord
#         surface.blit(text, rect)
#
#     def draw(self, Window):
#         """Aktualizuje i rysuje wyniki"""
#         height = self.window.surface.get_height()
#         self.update_score(height)
#
#         width = self.window.surface.get_width()
#         self.draw_text(Window.board, "counter: {}".format(self.score), width/2, height * 0.3)
