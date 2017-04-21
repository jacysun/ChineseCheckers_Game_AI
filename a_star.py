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
            #print("possible moves from this checker: ", self.checkers[i].moves)
            for j in range(len(self.checkers[i].moves)):
                checker_list = copy.deepcopy(self.checkers)
                checker_list[i].pos = self.checkers[i].moves[j]
                checker_states.append(checker_list)
        #print(len(checker_states))
        return checker_states


# if there is no interaction between human and ai, then ai just make best move to itself.
def a_star(initial, terminal, opponent):
    print("enter a star")
    frontier = []
    explored = []
    explored_count = 0

    frontier.append(ANode(initial, 0, heuristic(initial, opponent), [initial]))
    while frontier:
        i = 0
        print("frontier size: ", len(frontier))
        for j in range(1, len(frontier)):
            if (frontier[i].g + frontier[i].h) > (frontier[j].g + frontier[j].h):
                i = j
        current = frontier[i]
        path = current.path
        # print("current chosen node: ")
        # for p in range(10):
        #     print(current.checkers[p].pos)
        frontier.remove(frontier[i])
        if len(terminal) == 0:
            if explored_count == 5:
                break
        else:
            if list_to_set(current.checkers) == list_to_set(terminal):
                break
        if current.checkers in explored:
            continue
        for state in current.actions(current.checkers, opponent):
            if state in explored:
                continue
            frontier.append(ANode(state, current.g + 1, heuristic(state, opponent), current.path + [state]))
        explored.append(current.checkers)
        explored_count += 1

    # print out all explored states as output sequence
    print("explored: ", len(explored))
    # for l in range(len(explored)):
    #     print(explored[l])

    print("path: ", len(path))
    for l in range(len(path)):
        print(path[l][0].pos, path[l][1].pos, path[l][2].pos, path[l][3].pos, path[l][4].pos,
              path[l][5].pos, path[l][6].pos, path[l][7].pos, path[l][8].pos, path[l][9].pos)
    return path


def heuristic(checkers, opponent):
    h = 0
    self_list = []
    opponent_list = []
    for i in range(len(checkers)):
        self_list.append(checkers[i].pos)
    for i in range(len(opponent)):
        opponent_list.append(opponent[i].pos)
    for i in range(10):
        checkers[i].moves = []
        checkers[i].possible_moves(checkers[i].pos, False, 0, self_list, opponent_list)
        h += 1.1*(checkers[i].pos[1] - 160) / 40 + 0.1*abs(checkers[i].pos[0] - 480) / 44 - 1.2 * abs(checkers[i].best_vertical_move() - checkers[i].pos[1]) / 40
        #h += (checkers[i].pos[1] - 160) / 40
    #print("h: ", h)
    return h






