import pygame
import math
from constants import WIDTH, HEIGHT, WHITE, RADIUS, GREEN, RED, COLORS
from board import Board, circles

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption('Connect Four')
board = Board()


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class TurnHandler:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b

        self.current_player = self.player_a

    def update_turn(self):
        if self.current_player == self.player_a:
            self.current_player = self.player_b
        else:
            self.current_player = self.player_a

    def get_current_player_color(self):
        return self.current_player.color

    def print_current_player(self):
        print(f'Player {self.current_player.name} is playing...')


def main():
    player_a = Player('1', RED)
    player_b = Player('2', GREEN)
    turn_handler = TurnHandler(player_a, player_b)

    run = True
    clock = pygame.time.Clock()
    board.create_board(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for circle in circles:
                    if circle.empty:
                        dis = math.sqrt((circle.x - m_x) ** 2 + (circle.y - m_y) ** 2)
                        if dis < RADIUS:
                            turn_handler.print_current_player()
                            # current_color = turn_handler.get_current_player_color()
                            # pygame.draw.circle(WIN, current_color, (circle.x, circle.y), RADIUS, 50)
                            valid = board.is_valid(circle, circles)
                            if valid:
                                current_color = turn_handler.get_current_player_color()
                                circle.fill(current_color)
                                pygame.draw.circle(WIN, circle.color, (circle.x, circle.y), RADIUS, 50)
                                turn_handler.update_turn()
                            board.is_winning(circle)
                            pygame.display.update()

                            # Board.change_turn(board,color)


if __name__ == '__main__':
    main()
    pygame.quit()
