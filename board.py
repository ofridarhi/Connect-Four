import pygame
import math
from constants import RED, WIN, BLACK,WHITE, ROWS, COLS, RADIUS, WIDTH, HEIGHT


class Board:
    def __init__(self):
        self.board = []

    def draw_board(self, win):
        win.fill(BLACK)
        padding = RADIUS * 3
        rows_jump = math.ceil(HEIGHT / ROWS)
        cols_jump = math.ceil(WIDTH / COLS)
        for row in range(padding, HEIGHT + padding, rows_jump):
            for col in range(padding, WIDTH + padding, cols_jump):
                # surface,color,center,radius,width,draw_top_right,draw_top_left,draw_bottom_left,draw_bottom_right
                pygame.draw.circle(win, WHITE, (row, col), RADIUS)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

