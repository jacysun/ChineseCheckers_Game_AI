import pygame


screen = pygame.display.set_mode((960, 720))
pygame.display.set_caption('Chinese Checkers')

a = 480
d = 40
board_list = []
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
red = (200, 0, 0)
light_red = (255, 0, 0)
light_blue = (0, 0, 255)
pink = (255, 200, 200)

player = []
ai = []
player_pos = []
ai_pos = []
selected_checker = None
selected_moves = []


def is_free(pos):
    if pos in board_list and pos not in player_pos and pos not in ai_pos:
        return True
    else:
        return False


class Checker:

    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def render(self):
        pygame.draw.circle(screen, self.color, self.pos, 20, 0)

    def selected(self, new_color):
        pygame.draw.circle(screen, new_color, self.pos, 20, 0)

    def move(self, new_pos):
        pygame.draw.circle(screen, white, self.pos, 20, 0)
        pygame.draw.circle(screen, black, self.pos, 20, 1)
        pygame.draw.circle(screen, self.color, new_pos, 20, 0)
        self.pos = new_pos

        global selected_moves
        for i in range(len(selected_moves)):
            if selected_moves[i] != new_pos:
                pygame.draw.circle(screen, white, selected_moves[i], 20, 0)
                pygame.draw.circle(screen, black, selected_moves[i], 20, 1)

    def show_possible_moves(self):
        global selected_moves
        selected_moves = self.possible_moves()
        for i in range(len(selected_moves)):
            pygame.draw.circle(screen, pink, selected_moves[i], 20, 0)
            pygame.draw.circle(screen, black, selected_moves[i], 20, 1)

    def hide_possible_moves(self):
        global selected_moves
        for i in range(len(selected_moves)):
            pygame.draw.circle(screen, white, selected_moves[i], 20, 0)
            pygame.draw.circle(screen, black, selected_moves[i], 20, 1)

    def possible_moves(self):
        global player_pos, ai_pos
        player_pos = []
        ai_pos = []
        for i in range(len(player)):
            player_pos.append(player[i].pos)
        for i in range(len(ai)):
            ai_pos.append(ai[i].pos)

        x = self.pos[0]
        y = self.pos[1]
        moves = []

        if is_free((x-22, y-40)):
            moves.append((x-22, y-40))
        elif (x-22, y-40) in board_list:
            end = False
            i = 2
            while not end:
                if is_free((x - 22*i, y - 40*i)):
                    moves.append((x - 22*i, y - 40*i))
                    i += 1
                    if is_free((x-22*i, y-40*i)):
                        end = True
                    elif (x-22*i, y-40*i) in board_list:
                        i += 1
                else:
                    end = True

        if is_free((x+22, y-40)):
            moves.append((x+22, y-40))
        elif (x+22, y-40) in board_list:
            end = False
            i = 2
            while not end:
                if is_free((x + 22*i, y - 40*i)):
                    moves.append((x + 22*i, y - 40*i))
                    i += 1
                    if is_free((x+22*i, y-40*i)):
                        end = True
                    elif (x+22*i, y-40*i) in board_list:
                        i += 1
                else:
                    end = True

        if is_free((x-44, y)):
            moves.append((x-44, y))
        elif (x-44, y) in board_list:
            end = False
            i = 2
            while not end:
                if is_free((x - 44 * i, y)):
                    moves.append((x - 44 * i, y))
                    i += 1
                    if is_free((x-44*i, y)):
                        end = True
                    elif (x-44*i, y) in board_list:
                        i += 1
                else:
                    end = True

        if is_free((x+44, y)):
            moves.append((x + 44, y))
        elif (x+44, y) in board_list:
            end = False
            i = 2
            while not end:
                if is_free((x + 44 * i, y)):
                    moves.append((x + 44 * i, y))
                    i += 1
                    if is_free((x+44*i, y)):
                        end = True
                    elif (x+44*i, y) in board_list:
                        i += 1
                else:
                    end = True

        if is_free((x - 22, y+40)):
            moves.append((x - 22, y+40))
        elif (x-22, y+40) in board_list:
            end = False
            i = 2
            while not end:
                if is_free((x - 22 * i, y+40*i)):
                    moves.append((x - 22 * i, y+40*i))
                    i += 1
                    if is_free((x-22*i, y+40*i)):
                        end = True
                    elif (x-22*i, y+40*i) in board_list:
                        i += 1
                else:
                    end = True

        if is_free((x + 22, y+40)):
            moves.append((x + 22, y+40))
        elif (x+22, y+40) in board_list:
            end = False
            i = 2
            while not end:
                if is_free((x + 22 * i, y + 40 * i)):
                    moves.append((x + 22 * i, y + 40 * i))
                    i += 1
                    if is_free((x+22*i, y+40*i)):
                        end = True
                    elif (x+22*i, y+40*i) in board_list:
                        i += 1
                else:
                    end = True

        return moves







