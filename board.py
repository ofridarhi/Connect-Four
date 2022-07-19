import pygame
from constants import startx, starty, GAP, RADIUS, WHITE, BLACK, RED, GREEN, COLORS

circles = []
empty = True
init_color = BLACK


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.empty = True
        self.color = BLACK

    def fill(self, color):
        """
        Fill new circle with Player color and set not empty
        :param color: Player color
        """
        self.color = color
        self.empty = False


class Board:

    def create_board(self, win):
        win.fill(WHITE)
        for i in range(42):
            x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 7))
            y = starty + (((i // 7)) * (GAP + RADIUS * 2))
            circle = Circle(x, y)
            pygame.draw.circle(win, circle.color, (circle.x, circle.y), RADIUS, 3)
            circles.append(circle)
            pygame.display.update()

    def is_valid(self, circle,circles):
        max_y = 625
        if circle.y == max_y and circle.empty:
            print("ok 1")
            return True

        # if circle is not in the lowest row
        if circle.y < max_y and circle.empty:
            for neighbor_circle in circles:
                # if there is a circle below him
                if neighbor_circle.y == circle.y + (
                        RADIUS * 2 + GAP) and neighbor_circle.x == circle.x and not neighbor_circle.empty:
                    print('ok 2')
                    return True

        return False


    def is_winning(self, color):
        for circle in circles:
            x, y, empty = circle
