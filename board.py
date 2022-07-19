import pygame
from constants import startx, starty, GAP, RADIUS, WHITE, BLACK, RED, GREEN, COLORS

circles = []
empty = True
init_color = BLACK
dis_between_circles = (RADIUS * 2 + GAP)

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
            x = startx + GAP * 2 + (dis_between_circles * (i % 7))
            y = starty + (((i // 7)) * dis_between_circles)
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


    def is_winning(self, circle):
        if circle.color == RED:
            for neighbor_circle in circles:
                #vertical line
                if neighbor_circle.color == circle.color and neighbor_circle.x == circle.x and neighbor_circle.y == circle.y + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.x == neighbor_circle.x and sec_neighbor_circle.y == neighbor_circle.y + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.x == sec_neighbor_circle.x and third_neighbor_circle.y == sec_neighbor_circle.y + dis_between_circles:
                                    print("red wins")
                #horizontal line
                elif neighbor_circle.color == circle.color and neighbor_circle.y == circle.y and neighbor_circle.x == circle.x + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.y == neighbor_circle.y and sec_neighbor_circle.x == neighbor_circle.x + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.y == sec_neighbor_circle.y and third_neighbor_circle.x == sec_neighbor_circle.x + dis_between_circles:
                                    print("red wins")
                #diaginal to the left
                elif neighbor_circle.color == circle.color and neighbor_circle.x == circle.x + dis_between_circles and neighbor_circle.y == circle.y + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.x == neighbor_circle.x + dis_between_circles and sec_neighbor_circle.y == neighbor_circle.y + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.x == sec_neighbor_circle.x +dis_between_circles and third_neighbor_circle.y == sec_neighbor_circle.y + dis_between_circles:
                                    print("red wins")

                # diaginal to the right
                elif neighbor_circle.color == circle.color and neighbor_circle.x == circle.x - dis_between_circles and neighbor_circle.y == circle.y + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.x == neighbor_circle.x - dis_between_circles and sec_neighbor_circle.y == neighbor_circle.y + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.x == sec_neighbor_circle.x - dis_between_circles and third_neighbor_circle.y == sec_neighbor_circle.y + dis_between_circles:
                                    print("red wins")



        if circle.color == GREEN:
            for neighbor_circle in circles:
                # vertical line
                if neighbor_circle.color == circle.color and neighbor_circle.x == circle.x and neighbor_circle.y == circle.y + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.x == neighbor_circle.x and sec_neighbor_circle.y == neighbor_circle.y + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.x == sec_neighbor_circle.x and third_neighbor_circle.y == sec_neighbor_circle.y + dis_between_circles:
                                    print("GREEN WINS")

                # horizontal line
                elif neighbor_circle.color == circle.color and neighbor_circle.y == circle.y and neighbor_circle.x == circle.x + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.y == neighbor_circle.y and sec_neighbor_circle.x == neighbor_circle.x + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.y == sec_neighbor_circle.y and third_neighbor_circle.x == sec_neighbor_circle.x + dis_between_circles:
                                    print("green wins")

                #diaginal to the left
                elif neighbor_circle.color == circle.color and neighbor_circle.x == circle.x + dis_between_circles and neighbor_circle.y == circle.y + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.x == neighbor_circle.x + dis_between_circles and sec_neighbor_circle.y == neighbor_circle.y + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.x == sec_neighbor_circle.x +dis_between_circles and third_neighbor_circle.y == sec_neighbor_circle.y + dis_between_circles:
                                    print("green wins")

                # diaginal to the right
                elif neighbor_circle.color == circle.color and neighbor_circle.x == circle.x - dis_between_circles and neighbor_circle.y == circle.y + dis_between_circles:
                    for sec_neighbor_circle in circles:
                        if sec_neighbor_circle.color == neighbor_circle.color and sec_neighbor_circle.x == neighbor_circle.x - dis_between_circles and sec_neighbor_circle.y == neighbor_circle.y + dis_between_circles:
                            for third_neighbor_circle in circles:
                                if third_neighbor_circle.color == sec_neighbor_circle.color and third_neighbor_circle.x == sec_neighbor_circle.x - dis_between_circles and third_neighbor_circle.y == sec_neighbor_circle.y + dis_between_circles:
                                    print("green wins")