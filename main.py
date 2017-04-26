from board import *
import time


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()


def game_end(winner):
    if winner is human:
        message_display('You win!', 800, 100, 50)
    else:
        message_display('You lose!', 800, 100, 50)


def button(text, x, y, w, h, light_color, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, light_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "Start":
                game_loop()
            elif action == "Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(TextSurf, TextRect)


def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Chinese Checkers", largeText)
        TextRect.center = (960/2, 200)
        screen.blit(TextSurf, TextRect)

        button("Start", 250, 350, 100, 50, light_red, red, "Start")
        button("Quit", 650, 350, 100, 50, light_blue, blue, "Quit")

        pygame.display.update()


def game_loop():
    draw_board()
    init_checkers()
    selected_checker = None
    turn = 0
    ai_count = 0
    human_count = 0
    ai_time = 0

    while True:
        move_string = "move count: " + str(human_count)
        screen.fill(white, (30, 140, 150, 40))
        message_display(move_string, 100, 150, 20)
        if ai_time == 0:
            time_string = "AI took:"
        else:
            time_string = "AI took: " + str(ai_time) + "s"
        screen.fill(white, (20, 180, 170, 40))
        message_display(time_string, 100, 200, 20)
        button("Replay", 50, 50, 100, 50, light_red, red)
        button("Quit", 180, 50, 100, 50, light_blue, blue)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] < 300 and mouse_pos[1] < 100:
                    button("Replay", 50, 50, 100, 50, light_red, red, "Start")
                    button("Quit", 180, 50, 100, 50, light_blue, blue, "Quit")

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
                                human_count += 1
                                if is_terminal(human.checkers, human_terminal):
                                    game_end(human)
                                else:
                                    selected_checker = None
                                    turn = 1
                            break

            elif turn == 1:  # ai's turn to make a move
                t0 = time.time()
                ai.make_move()
                ai_time = round(time.time() - t0, 2)
                print(ai_time)
                turn = 0
                #ai_count += 1
                if is_terminal(ai.checkers, ai_terminal):
                    game_end(ai)
        pygame.display.update()


pygame.init()
init_board()
game_intro()
game_loop()
pygame.quit()
quit()
