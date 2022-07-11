import pygame
from constants import WIDTH, HEIGHT, WIN
from board import Board

FPS = 60
pygame.display.set_caption('Connect Four')


def get_row_col_from_mouse(pos):
    col,row = pos
    return row,col




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
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row,col)

        board.draw_board(WIN)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
