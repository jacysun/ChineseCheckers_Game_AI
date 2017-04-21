from board import *


def game_loop():
    selected_checker = None
    turn = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                mouse_pos = pygame.mouse.get_pos()
                if selected_checker is None:
                    for i in range(len(human.checkers)):
                        if math.sqrt(math.pow(mouse_pos[0] - human.checkers[i].pos[0], 2) + math.pow(mouse_pos[1] - human.checkers[i].pos[1], 2)) < 20:
                            human.checkers[i].selected()
                            selected_checker = human.checkers[i]
                            break
                else:
                    for i in range(len(board_list)):
                        if math.sqrt(math.pow(mouse_pos[0] - selected_checker.pos[0], 2) + math.pow(mouse_pos[1] - selected_checker.pos[1], 2)) < 20:
                            selected_checker.unselected()
                            selected_checker = None
                            break
                        if math.sqrt(math.pow(mouse_pos[0] - board_list[i][0], 2) + math.pow(mouse_pos[1] - board_list[i][1], 2)) < 20:
                            if board_list[i] in selected_checker.moves:
                                selected_checker.move(board_list[i])
                                selected_checker = None
                                turn = 1
                            break

            elif turn == 1:  # ai's turn to make a move
                #ai.make_move()
                print("ai has made a move")
                turn = 0
        pygame.display.update()


pygame.init()
draw_board()
init_checkers()
game_loop()
