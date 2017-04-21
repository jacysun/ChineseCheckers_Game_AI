import math


# distance to the furthest end
def distance_to_goal(player, checkers):
    distance = 0
    if player == "human":  # distance to (480, 680)
        for i in range(10):
            distance += math.sqrt(
                math.pow(checkers[i].pos[0] - 480, 2) + math.pow(checkers[i].pos[1] - 680, 2))
    else: # distance to (480, 40)
        for i in range(10):
            distance += math.sqrt(math.pow(checkers[i].pos[0] - 480, 2) + math.pow(checkers[i].pos[1] - 40, 2))

    return distance


# y to the furthest end
def y_to_goal(player, checkers):
    distance = 0
    if player == "human":  # distance to 680
        for i in range(10):
            distance += math.pow(680 - checkers[i].pos[1], 2)
    else: # distance to 40
        for i in range(10):
            distance += math.pow(checkers[i].pos[1] - 40, 2)

    return distance


# horizontal distance to middle line
def distance_to_midline(checkers):
    distance = 0
    for i in range(10):
        distance += abs(checkers[i].pos[0] - 480)

    return distance


# vertical advance towards goal
def vertical_advance(self, opponent):
    advance = 0
    self_list = []
    opponent_list = []
    for i in range(len(self.checkers)):
        self_list.append(self.checkers[i].pos)
    for i in range(len(opponent)):
        opponent_list.append(opponent[i].pos)
    for i in range(10):
        self.checkers[i].moves = []
        self.checkers[i].possible_moves(self.checkers[i].pos, False, 0, self_list, opponent_list)
        advance += abs(self.checkers[i].best_vertical_move() - self.checkers[i].pos[1])

    return advance


def eval_value(ai_checkers, human_checkers):
    return 0.3 * (y_to_goal("human", human_checkers) - y_to_goal("ai", ai_checkers)) + 0.3 * (distance_to_midline(human_checkers) - distance_to_midline(ai_checkers)) + 0.4 * (vertical_advance(ai_checkers, human_checkers) - vertical_advance(human_checkers, ai_checkers))


def list_to_set(list):
    s = set([])
    for i in range(len(list)):
        s.add(list[i])
    return s