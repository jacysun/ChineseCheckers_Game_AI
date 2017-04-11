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

player = []
ai = []
player_pos = []
ai_pos = []
selected_checker = None

for i in range(len(player)):
    player_pos.append(player[i].pos)
for i in range(len(ai)):
    player_pos.append(ai[i].pos)



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

    def is_free(self, pos):
        if pos not in player_pos and pos not in ai_pos:
            return True
        else:
            return False

    # def possible_moves(self):
    #     moves = []



