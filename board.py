import pygame
from constants import RED, WIN, BLACK, ROWS, COLS, RADIUS


class Board:
    def __init__(self):
        self.board = []

    def draw_board(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                # surface,color,center,radius,width,draw_top_right,draw_top_left,draw_bottom_left,draw_bottom_right
                pygame.draw.circle(win, RED, (row * RADIUS * 5, col * RADIUS * 5), RADIUS)
