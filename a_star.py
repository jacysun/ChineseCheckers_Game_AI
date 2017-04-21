import copy


class ANode:
    def __init__(self, checkers, g, h):
        self.checkers = checkers
        self.g = g
        self.h = h

    def actions(self):
        checker_states = []  # list of list, all 10 checkers states
        for i in range(10):
            self.checkers[i].moves = []
            self.checkers[i].possible_moves(self.checkers[i].pos, False, 0)
            #print("possible moves from this checker: ", self.checkers[i].moves)
            for j in range(len(self.checkers[i].moves)):
                checker_list = copy.deepcopy(self.checkers)
                checker_list[i].pos = self.checkers[i].moves[j]
                checker_states.append(checker_list)
        #print(len(checker_states))
        return checker_states


# if there is no interaction between human and ai, then ai just make best move to itself.
def a_star(initial, terminal):
    print("enter a star")
    moves = []
    frontier = []
    explored = []
    explored_count = 0

    frontier.append(ANode(initial, 0, heuristic(initial)))
    while frontier:
        i = 0
        print("frontier size: ", len(frontier))
        for j in range(1, len(frontier)):
            if (frontier[i].g + frontier[i].h) > (frontier[j].g + frontier[j].h):
                i = j
        current = frontier[i]
        # print("current chosen node: ")
        # for p in range(10):
        #     print(current.checkers[p].pos)
        frontier.remove(frontier[i])
        if list_to_set(current.checkers) == list_to_set(terminal):
            break
        if current.checkers in explored:
            continue
        for state in current.actions():
            if state in explored:
                # print("state in explored")
                continue
            frontier.append(ANode(state, current.g + 1, heuristic(state)))
        explored.append(current.checkers)
        explored_count += 1
    print("a star has explored states: ", len(explored))

    for k in range(len(explored) - 1):
        for p in range(10):
            if explored[k].checkers[p] is not explored[k+1].checkers[p]:
                target = explored[k].checkers[p]
                new = explored[k+1].checkers[p]
                moves.append((target, new))

    print("end a star moves")
    return moves


def heuristic(checkers):
    h = 0
    for i in range(10):
        checkers[i].moves = []
        checkers[i].possible_moves(checkers[i].pos, False, 0)
        h += 0.3 * (checkers[i].pos[1] - 160) / 40 + 0.3 * abs(checkers[i].pos[0] - 480) / 44 + 0.4 * abs(checkers[i].best_vertical_move() - checkers[i].pos[1])
        #h += (checkers[i].pos[1] - 160) / 40
    #print("h: ", h)
    return h


def list_to_set(list):
    s = set([])
    for i in range(len(list)):
        s.add(list[i])
    return s





