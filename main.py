import pygame
from constants import WIDTH, HEIGHT, WIN
from board import Board

FPS = 60
pygame.display.set_caption('Connect Four')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_board(WIN)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
