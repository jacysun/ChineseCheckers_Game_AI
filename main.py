from board import *
import math

pygame.init()


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
                    print("enter none selected")
                    for i in range(len(player)):
                        if math.sqrt(math.pow(mouse_pos[0] - player[i].pos[0], 2) + math.pow(mouse_pos[1] - player[i].pos[1], 2)) < 20:
                            player[i].selected()
                            selected_checker = player[i]
                            break
                else:
                    for i in range(len(board_list)):
                        if math.sqrt(math.pow(mouse_pos[0] - selected_checker.pos[0], 2) + math.pow(mouse_pos[1] - selected_checker.pos[1], 2)) < 20:
                            selected_checker.unselected()
                            selected_checker = None
                            break
                        if math.sqrt(math.pow(mouse_pos[0] - board_list[i][0], 2) + math.pow(mouse_pos[1] - board_list[i][1], 2)) < 20:
                            moves = get_moves()
                            if board_list[i] in moves:
                                selected_checker.move(board_list[i])
                                selected_checker = None
                            break
        pygame.display.update()


draw_board()
init_checkers()
game_loop()
