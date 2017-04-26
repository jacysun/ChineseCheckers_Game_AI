import copy
from utility import *


class ANode:
    def __init__(self, checkers, g, h, path):
        self.checkers = checkers
        self.g = g
        self.h = h
        self.path = path

    def actions(self, ai, human):
        checker_states = []  # list of list, all 10 checkers states
        ai_list = []
        human_list = []
        for i in range(len(ai)):
            ai_list.append(ai[i].pos)
        for i in range(len(human)):
            human_list.append(human[i].pos)

        for i in range(10):
            self.checkers[i].moves = []
            self.checkers[i].possible_moves(self.checkers[i].pos, False, 0, ai_list, human_list)
            for j in range(len(self.checkers[i].moves)):
                checker_list = copy.deepcopy(self.checkers)
                checker_list[i].pos = self.checkers[i].moves[j]
                checker_states.append(checker_list)
        return checker_states


# if there is no interaction between human and ai, then ai just make best move to itself.
def a_star(initial, terminal, opponent):
    frontier = []
    explored = []
    explored_count = 0

    frontier.append(ANode(initial, 0, heuristic(initial, opponent, terminal), [initial]))
    while frontier:
        i = 0
        for j in range(1, len(frontier)):
            if (frontier[i].g + frontier[i].h) > (frontier[j].g + frontier[j].h):
                i = j
        current = frontier[i]
        #print("current g: ", current.g, "current h: ", current.h)
        path = current.path
        frontier.remove(frontier[i])
        if explored_count == 100 or is_terminal(current.checkers, terminal):
            break
        if current.checkers in explored:
            continue
        for state in current.actions(current.checkers, opponent):
            if state in explored:
                continue
            frontier.append(ANode(state, current.g + 1, heuristic(state, terminal, opponent), current.path + [state]))
        explored.append(current.checkers)
        explored_count += 1

    # print("path: ", len(path))
    # for l in range(len(path)):
    #     print(path[l][0].pos, path[l][1].pos, path[l][2].pos, path[l][3].pos, path[l][4].pos,
    #           path[l][5].pos, path[l][6].pos, path[l][7].pos, path[l][8].pos, path[l][9].pos)
    move = []
    for i in range(10):
        if path[0][i].pos != path[1][i].pos:
            move.append(path[0][i])
            move.append(path[1][i])
    return move


def heuristic(checkers, terminal, opponent):
    h = 0
    count = settled_count(checkers, terminal)
    # if count >= 7:
    #     h += 0.9 * (0.3 * y_to_goal("ai", checkers) / 40 + 0.15 * distance_to_midline(checkers) / 44 + 0.1 * checker_looseness(checkers) / 40 - 0.12 * vertical_advance(checkers, opponent) / 40 - 0.1 * count)
    # else:
    #     h += 0.9*(0.3 * y_to_goal("ai", checkers) / 40 + 0.15 * distance_to_midline(checkers) / 44 + 0.1 * checker_looseness(checkers) / 40 - 0.12 * vertical_advance(checkers, opponent) / 40 - 0.1 * count)
    #h += 0.9 * (0.3 * y_to_goal("ai", checkers) / 40 + 0.15 * distance_to_midline(checkers) / 44 + 0.15 * checker_looseness(checkers) / 40 - 0.1 * vertical_advance(checkers, opponent) / 40 - 0.25 * count)
    h += 0.9 * (0.3 * y_to_goal("ai", checkers) / 40 + 0.15 * distance_to_midline(checkers) / 44 + 0.1 * checker_looseness(checkers) / 40 - 0.12 * vertical_advance(checkers, opponent) / 40 - 0.1 * count)   # all ai 35 moves
    #h += 0.9 * (0.3 * y_to_goal("ai", checkers) / 40 + 0.15 * distance_to_midline(checkers) / 44 + 0.1 * checker_looseness(checkers) / 40 - 0.12 * vertical_advance(checkers, opponent) / 40)
    #print("h: ", h)
    return h






