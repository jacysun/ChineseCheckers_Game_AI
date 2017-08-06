import copy
from utility import *

class Node:
    def __init__(self, checkers, path):
        self.checkers = checkers
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

maxDepth = 2

def alpha_beta(state, terminal, human_terminal, opponent):
    infinity = float('inf')
    best_val = -infinity
    alpha = -infinity
    beta = infinity
    new_pos = None
    best_move = []

    node = Node(state, [state])
    successors = node.actions(state, opponent)

    for child in successors:
    	value = min_value(child, alpha, beta, terminal, human_terminal, opponent, 1)
    	if value > best_val:
    		best_val = value
    		new_pos = child
    print("AlphaBeta:  Utility Value of Root Node: = " + str(best_val))
    for i in range(10):
    	if new_pos[i].pos != state[i].pos:
            best_move.append(state[i])
            best_move.append(new_pos[i])

    return best_move

def max_value(state, alpha, beta, terminal, human_terminal, opponent, depth):
    # print(depth)
    global maxDepth
    if terminal_test(state, terminal) or terminal_test(opponent, human_terminal) or depth >= maxDepth:
        d = eval_value(state, opponent, terminal, human_terminal)
        return d
    infinity = float('inf')
    value = -infinity
    node = Node(state, [state])
    successors = node.actions(state, opponent)

    for child in successors:
    	value = max(value, min_value(child, alpha, beta, terminal, human_terminal, opponent, depth+1))
    	if value >= beta:
    		return value
    	alpha = max(alpha, value)

    return value

def min_value(state, alpha, beta, terminal, human_terminal, opponent, depth):
    # print(depth)
    global maxDepth
    if terminal_test(state, terminal) or terminal_test(opponent, human_terminal) or depth >= maxDepth:
        d = eval_value(state, opponent, terminal, human_terminal)
        return d
    infinity = float('inf')
    value = infinity
    node = Node(opponent, [opponent])
    successors = node.actions(opponent, state)

    for child in successors:
    	# print('minnim', len(successors))
    	value = min(value, max_value(state, alpha, beta, terminal, human_terminal, child, depth+1))
    	if value <= alpha:
    		return value
    	beta = min(beta, value)

    return value

def terminal_test(state, terminal):
    s = list_to_set(state)
    t = list_to_set(terminal)
    return s == t
