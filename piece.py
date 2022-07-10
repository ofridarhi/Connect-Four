import pygame
from constants import RED, GREEN, RADIUS
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = RADIUS * self.col
        self.y = RADIUS * self.row

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), RADIUS)

    def __repr__(self):
        return  str(self.color)
