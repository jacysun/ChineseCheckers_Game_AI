import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption('Chinese Checkers')

a = 480
d = 40
board_list = []
black = (0, 0, 0)
white = (255, 255, 255)


def draw_board():
    for i in range(0, 4):
        for j in range(i+1):
            board_list.append((a - 22 * i + 44 * j, d * (i + 1)))
    for i in range(4, 9):
        for j in range(17-i):
            board_list.append((a - 22 * (16-i) + 44 * j, d * (i + 1)))
    for i in range(9, 13):
        for j in range(i+1):
            board_list.append((a - 22 * i + 44 * j, d * (i + 1)))
    for i in range(13, 17):
        for j in range(17-i):
            board_list.append((a - 22 * (16-i) + 44 * j, d * (i + 1)))

    screen.fill(white)
    for line in range(len(board_list)):
        pygame.draw.circle(screen, black, board_list[line], 20, 1)
    pygame.display.update()


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


draw_board()
game_loop()