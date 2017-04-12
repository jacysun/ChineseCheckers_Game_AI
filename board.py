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
moves = []
visited = []


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


def is_free(pos):
    if pos in board_list and pos not in player_pos and pos not in ai_pos:
        return True
    else:
        return False


def possible_moves(pos, hop):
    global player_pos, ai_pos, visited

    x = pos[0]
    y = pos[1]

    # check top_left
    if is_free((x-22, y-40)) and hop is False:
        moves.append((x-22, y-40))
    elif ((x-22, y-40) in player_pos or (x-22, y-40) in ai_pos) and (x-22, y-40) not in visited:
        visited.append((x-22, y-40))
        if is_free((x - 22 * 2, y - 40 * 2)):
            moves.append((x - 22 * 2, y - 40 * 2))
            possible_moves((x-22*2, y-40*2), True)

    # check top_right
    if is_free((x + 22, y - 40)) and hop is False:
        moves.append((x + 22, y - 40))
    elif ((x + 22, y - 40) in player_pos or (x+22, y-40) in ai_pos) and (x + 22, y - 40) not in visited:
        visited.append((x + 22, y - 40))
        if is_free((x + 22 * 2, y - 40 * 2)):
            moves.append((x + 22 * 2, y - 40 * 2))
            possible_moves((x + 22 * 2, y - 40 * 2), True)

    # check left
    if is_free((x - 44, y)) and hop is False:
        moves.append((x -44, y))
    elif ((x -44, y) in player_pos or (x-44, y) in ai_pos) and (x -44, y) not in visited:
        visited.append((x -44, y))
        if is_free((x -44 * 2, y)):
            moves.append((x -44 * 2, y))
            possible_moves((x -44 * 2, y), True)

    # check right
    if is_free((x + 44, y)) and hop is False:
        moves.append((x + 44, y))
    elif ((x + 44, y) in player_pos or (x+44, y) in ai_pos) and (x + 44, y) not in visited:
        visited.append((x + 44, y))
        if is_free((x + 44 * 2, y)):
            moves.append((x + 44 * 2, y))
            possible_moves((x + 44 * 2, y), True)

    # check down_left
    if is_free((x - 22, y + 40)) and hop is False:
        moves.append((x - 22, y + 40))
    elif ((x - 22, y + 40) in player_pos or (x-22, y+40) in ai_pos) and (x - 22, y + 40) not in visited:
        visited.append((x - 22, y + 40))
        if is_free((x - 22 * 2, y + 40 * 2)):
            moves.append((x - 22 * 2, y + 40 * 2))
            possible_moves((x - 22 * 2, y + 40 * 2), True)

    # check down_right
    if is_free((x + 22, y + 40)) and hop is False:
        moves.append((x + 22, y + 40))
    elif ((x + 22, y + 40) in player_pos or (x+22, y+40) in ai_pos) and (x + 22, y + 40) not in visited:
        visited.append((x + 22, y + 40))
        if is_free((x + 22 * 2, y + 40 * 2)):
            moves.append((x + 22 * 2, y + 40 * 2))
            possible_moves((x + 22 * 2, y + 40 * 2), True)

def get_moves():
    return moves

class Checker:

    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def render(self):
        pygame.draw.circle(screen, self.color, self.pos, 20, 0)

    def selected(self):
        pygame.draw.circle(screen, light_red, self.pos, 20, 0)
        # show possible moves
        global moves, player_pos, ai_pos, visited
        moves = []
        player_pos = []
        ai_pos = []
        visited = []
        for i in range(len(player)):
            player_pos.append(player[i].pos)
        for i in range(len(ai)):
            ai_pos.append(ai[i].pos)

        possible_moves(self.pos, False)

        for i in range(len(moves)):
            pygame.draw.circle(screen, pink, moves[i], 20, 0)
            pygame.draw.circle(screen, black, moves[i], 20, 1)
        print("in board")
        print(moves)

    def unselected(self):
        pygame.draw.circle(screen, red, self.pos, 20, 0)
        # clear possible moves
        global moves
        for i in range(len(moves)):
            pygame.draw.circle(screen, white, moves[i], 20, 0)
            pygame.draw.circle(screen, black, moves[i], 20, 1)

    def move(self, new_pos):
        pygame.draw.circle(screen, white, self.pos, 20, 0)
        pygame.draw.circle(screen, black, self.pos, 20, 1)
        pygame.draw.circle(screen, self.color, new_pos, 20, 0)
        self.pos = new_pos
        # clear possible moves except the new_pos
        global moves
        for i in range(len(moves)):
            if moves[i] != new_pos:
                pygame.draw.circle(screen, white, moves[i], 20, 0)
                pygame.draw.circle(screen, black, moves[i], 20, 1)










