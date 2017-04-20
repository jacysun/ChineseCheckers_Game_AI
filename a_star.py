import copy


class ANode:
    def __init__(self, checkers, g, h):
        self.checkers = checkers
        self.g = g
        self.h = h

    def actions(self):
        # print("current checkers positions: ")
        # for i in range(10):
        #     print(self.checkers[i].pos)

        checker_states = []  # list of list, all 10 checkers states
        checker_list = copy.deepcopy(self.checkers)
        for i in range(10):
            self.checkers[i].possible_moves(self.checkers[i].pos, False, 0)
            # print("This checker is: ", i, "and position is: ", self.checkers[i].pos)
            # print("The possible moves number is: ", len(self.checkers[i].moves))
            # print("possible moves are: ")
            # if len(self.checkers[i].moves) > 0:
            #     print(self.checkers[i].moves)
            for j in range(len(self.checkers[i].moves)):
                checker_list[i].pos = self.checkers[i].moves[j]
                checker_states.append(checker_list)
        #         print("new added state")
        #         for k in range(10):
        #             print(checker_list[k].pos)
        #
        # print(len(checker_states))
        return checker_states

    def heuristic(self):
        h = 0
        for i in range(10):
            h += (self.checkers[i].pos[1] - 160) / 40
        return h


# if there is no interaction between human and ai, then ai just make best move to itself.
def a_star(initial, terminal):
    print("enter a star")
    moves = []
    frontier = []
    explored = []
    explored_count = 0

    frontier.append(ANode(initial, 0, 110.0))
    while frontier:
        i = 0
        print("frontier size: ", len(frontier))
        for j in range(1, len(frontier)):
            if (frontier[i].g + frontier[i].h) > (frontier[j].g + frontier[j].h):
                i = j
        current = frontier[i]
        frontier.remove(frontier[i])
        if current.checkers == terminal:
            break
        if current.checkers in explored:
            continue
        for state in current.actions():
            if state in explored:
                continue
            frontier.append(ANode(state, current.g + 1, current.heuristic()))
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





