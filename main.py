from board import *
import math

pygame.init()


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
    for i in range(len(board_list)):
        pygame.draw.circle(screen, black, board_list[i], 20, 1)


def init_checkers():
    for i in range(0, 10):
        piece = Checker(board_list[i], red)
        piece.render()
        player.append(piece)
    for i in reversed(range(len(board_list)-10, len(board_list))):
        piece = Checker(board_list[i], blue)
        piece.render()
        ai.append(piece)


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                global selected_checker
                if selected_checker is None:
                    for i in range(len(player)):
                        if math.sqrt(math.pow(mouse_pos[0] - player[i].pos[0], 2) + math.pow(mouse_pos[1] - player[i].pos[1], 2)) < 20:
                            player[i].selected(light_red)
                            player[i].show_possible_moves()
                            selected_checker = player[i]
                            break
                    for i in range(len(player)):
                        if math.sqrt(math.pow(mouse_pos[0] - ai[i].pos[0], 2) + math.pow(mouse_pos[1] - ai[i].pos[1], 2)) < 20:
                            ai[i].selected(light_blue)
                            selected_checker = ai[i]
                            break
                else:
                    for i in range(len(board_list)):
                        if math.sqrt(math.pow(mouse_pos[0] - selected_checker.pos[0], 2) + math.pow(mouse_pos[1] - selected_checker.pos[1], 2)) < 20:
                            if selected_checker.color == red:
                                selected_checker.selected(red)
                                selected_checker.hide_possible_moves()
                            else:
                                selected_checker.selected(blue)
                            selected_checker = None
                            break
                        if math.sqrt(math.pow(mouse_pos[0] - board_list[i][0], 2) + math.pow(mouse_pos[1] - board_list[i][1], 2)) < 20:
                            selected_checker.move(board_list[i])
                            selected_checker = None
                            break
        pygame.display.update()


draw_board()
init_checkers()
game_loop()
