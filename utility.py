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
            distance += math.sqrt(math.pow(checkers[i].pos[0] - 480, 2) + math.pow(checkers[i].pos[1] - 120, 2))

    return distance


# y to the furthest end
def y_to_goal(player, checkers):
    distance = 0
    if player == "human":  # distance to 680
        for i in range(10):
            distance += abs(680 - checkers[i].pos[1])
    else: # distance to 40
        for i in range(10):
            distance += abs(checkers[i].pos[1] - 40)

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
    for i in range(len(self)):
        self_list.append(self[i].pos)
    for i in range(len(opponent)):
        opponent_list.append(opponent[i].pos)
    for i in range(10):
        self[i].moves = []
        self[i].possible_moves(self[i].pos, False, 0, self_list, opponent_list)
        advance += abs(self[i].best_vertical_move() - self[i].pos[1])

    return advance


def checker_looseness(checkers):
    distance = 0
    c_list = []

    for i in range(len(checkers)):
        g = checkers[i].pos
        c_list.append(g[1])
    average = sum(c_list)/len(c_list)
    for i in range(len(c_list)):
        distance += abs(c_list[i] - average)
    return distance


def eval_value(ai_checkers, human_checkers, ai_terminal, human_terminal):
    return 0.7 * (y_to_goal("human", human_checkers) - y_to_goal("ai", ai_checkers)) + 0.2 * (distance_to_midline(human_checkers) - distance_to_midline(ai_checkers)) + 0.3 * (vertical_advance(ai_checkers, human_checkers) - vertical_advance(human_checkers, ai_checkers)) + 0.2 * (checker_looseness(human_checkers) - checker_looseness(ai_checkers)) + 0.1 * (settled_count(ai_checkers, ai_terminal) - settled_count(human_checkers, human_terminal))


def list_to_set(list):
    s = set([])
    for i in range(len(list)):
        s.add(list[i])
    return s


def is_terminal(current, terminal):
    current_list = []
    terminal_list = []
    for i in range(10):
        current_list.append(current[i].pos)
        terminal_list.append(terminal[i].pos)
    return list_to_set(current_list) == list_to_set(terminal_list)


def settled_count(current, terminal):
    count = 0
    terminal_list = []
    for i in range(10):
        terminal_list.append(terminal[i].pos)
    for i in range(10):
        if current[i].pos in terminal_list:
            count += 1
    return count


