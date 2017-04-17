import pygame
import math


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

visited = []


class Player:
    def __init__(self, color):
        self.color = color
        self.checkers = []
        self.checker_pos = []

    # distance to the furthest end
    def distance_to_goal(self):
        distance = 0
        if self is human: # distance to (480, 680)
            for i in range(10):
                distance += math.sqrt(math.pow(self.checkers[i].pos[0] - 480, 2) + math.pow(self.checkers[i].pos[1] - 680, 2))
        else: # distance to (480, 40)
            for i in range(10):
                distance += math.sqrt(math.pow(self.checkers[i].pos[0] - 480, 2) + math.pow(self.checkers[i].pos[1] - 40, 2))

        return distance

    # y to the furthest end
    def y_to_goal(self):
        distance = 0
        if self is human:  # distance to 680
            for i in range(10):
                distance += math.pow(680 - self.checkers[i].pos[1], 2)
        else:  # distance to 40
            for i in range(10):
                distance += math.pow(self.checkers[i].pos[1] - 40, 2)

        return distance

    # horizontal distance to middle line
    def distance_to_midline(self):
        distance = 0
        for i in range(10):
            distance += abs(self.checkers[i].pos[0] - 480)

        return distance

    # vertical advance towards goal
    def vertical_advance(self):
        advance = 0
        for i in range(10):
            self.checkers[i].moves = []
            self.checkers[i].possible_moves(self.checkers[i].pos, False)
            advance += abs(self.checkers[i].best_vertical_move() - self.checkers[i].pos[1])

        return advance

    # ai make a move
    def make_move(self):
        # call minimax function and return two things: the target checker object that will be moved (target), and the new_pos
        # target =
        # new_pos =
        # pygame.draw.circle(screen, white, target.pos, 20, 0)
        # pygame.draw.circle(screen, black, target.pos, 20, 1)
        # pygame.draw.circle(screen, blue, new_pos, 20, 0)
        # target.pos = new_pos
        print("ai has just made a move")


human = Player(red)
ai = Player(blue)


class Checker:

    def __init__(self, pos):
        self.pos = pos
        self.moves = []

    def render(self, color):
        pygame.draw.circle(screen, color, self.pos, 20, 0)

    def selected(self):
        pygame.draw.circle(screen, light_red, self.pos, 20, 0)
        # show possible moves
        global visited
        human.checker_pos = []
        ai.checker_pos = []
        visited = []
        for i in range(len(human.checkers)):
            human.checker_pos.append(human.checkers[i].pos)
        for i in range(len(ai.checkers)):
            ai.checker_pos.append(ai.checkers[i].pos)

        if len(self.moves) == 0:
            self.possible_moves(self.pos, False)

        for i in range(len(self.moves)):
            pygame.draw.circle(screen, pink, self.moves[i], 20, 0)
            pygame.draw.circle(screen, black, self.moves[i], 20, 1)

    def unselected(self):
        pygame.draw.circle(screen, red, self.pos, 20, 0)
        # clear possible moves
        for i in range(len(self.moves)):
            pygame.draw.circle(screen, white, self.moves[i], 20, 0)
            pygame.draw.circle(screen, black, self.moves[i], 20, 1)
        self.moves = []

    def move(self, new_pos):
        pygame.draw.circle(screen, white, self.pos, 20, 0)
        pygame.draw.circle(screen, black, self.pos, 20, 1)
        pygame.draw.circle(screen, red, new_pos, 20, 0)
        self.pos = new_pos
        # clear possible moves except the new_pos
        for i in range(len(self.moves)):
            if self.moves[i] != new_pos:
                pygame.draw.circle(screen, white, self.moves[i], 20, 0)
                pygame.draw.circle(screen, black, self.moves[i], 20, 1)
        self.moves = []

    def possible_moves(self, pos, hop):
        global visited

        x = pos[0]
        y = pos[1]

        # check top_left
        if is_free((x - 22, y - 40)) and hop is False:
            self.moves.append((x - 22, y - 40))
        elif ((x - 22, y - 40) in human.checker_pos or (x - 22, y - 40) in ai.checker_pos) and (
            x - 22, y - 40) not in visited:
            visited.append((x - 22, y - 40))
            if is_free((x - 22 * 2, y - 40 * 2)):
                self.moves.append((x - 22 * 2, y - 40 * 2))
                self.possible_moves((x - 22 * 2, y - 40 * 2), True)

        # check top_right
        if is_free((x + 22, y - 40)) and hop is False:
            self.moves.append((x + 22, y - 40))
        elif ((x + 22, y - 40) in human.checker_pos or (x + 22, y - 40) in ai.checker_pos) and (
            x + 22, y - 40) not in visited:
            visited.append((x + 22, y - 40))
            if is_free((x + 22 * 2, y - 40 * 2)):
                self.moves.append((x + 22 * 2, y - 40 * 2))
                self.possible_moves((x + 22 * 2, y - 40 * 2), True)

        # check left
        if is_free((x - 44, y)) and hop is False:
            self.moves.append((x - 44, y))
        elif ((x - 44, y) in human.checker_pos or (x - 44, y) in ai.checker_pos) and (x - 44, y) not in visited:
            visited.append((x - 44, y))
            if is_free((x - 44 * 2, y)):
                self.moves.append((x - 44 * 2, y))
                self.possible_moves((x - 44 * 2, y), True)

        # check right
        if is_free((x + 44, y)) and hop is False:
            self.moves.append((x + 44, y))
        elif ((x + 44, y) in human.checker_pos or (x + 44, y) in ai.checker_pos) and (x + 44, y) not in visited:
            visited.append((x + 44, y))
            if is_free((x + 44 * 2, y)):
                self.moves.append((x + 44 * 2, y))
                self.possible_moves((x + 44 * 2, y), True)

        # check down_left
        if is_free((x - 22, y + 40)) and hop is False:
            self.moves.append((x - 22, y + 40))
        elif ((x - 22, y + 40) in human.checker_pos or (x - 22, y + 40) in ai.checker_pos) and (
            x - 22, y + 40) not in visited:
            visited.append((x - 22, y + 40))
            if is_free((x - 22 * 2, y + 40 * 2)):
                self.moves.append((x - 22 * 2, y + 40 * 2))
                self.possible_moves((x - 22 * 2, y + 40 * 2), True)

        # check down_right
        if is_free((x + 22, y + 40)) and hop is False:
            self.moves.append((x + 22, y + 40))
        elif ((x + 22, y + 40) in human.checker_pos or (x + 22, y + 40) in ai.checker_pos) and (
            x + 22, y + 40) not in visited:
            visited.append((x + 22, y + 40))
            if is_free((x + 22 * 2, y + 40 * 2)):
                self.moves.append((x + 22 * 2, y + 40 * 2))
                self.possible_moves((x + 22 * 2, y + 40 * 2), True)

    def get_moves(self):
        return self.moves

    def best_vertical_move(self):
        if self is human: # find the largest y
            ymax = 0
            for i in range(len(self.moves)):
                if self.moves[i] > ymax:
                    ymax = self.moves[i]
            return ymax
        else: # find the smallest y
            ymin = 700
            for i in range(len(self.moves)):
                if self.moves[i] < ymin:
                    ymin = self.moves[i]
            return ymin


# static methods
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
        piece = Checker(board_list[i])
        piece.render(human.color)
        human.checkers.append(piece)
        human.checker_pos.append(board_list[i])
    for i in reversed(range(len(board_list)-10, len(board_list))):
        piece = Checker(board_list[i])
        piece.render(ai.color)
        ai.checkers.append(piece)
        ai.checker_pos.append(board_list[i])


def is_free(pos):
    if pos in board_list and pos not in human.checker_pos and pos not in ai.checker_pos:
        return True
    else:
        return False


def eval_value():
    return 0.3 * (human.y_to_goal() - ai.y_to_goal()) + 0.3 * (human.distance_to_midline() - ai.distance_to_midline()) + 0.4 * (ai.vertical_advance() - human.vertical_advance())


