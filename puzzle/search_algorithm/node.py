import numpy as np
from .constants import OBJ_GRID
from ..formulations import won_comp, available_moves, move_grid


def heuristic_manhattan(grid):
    distance = 0

    for x in range(1, 9):
        x0, y0 = np.where(grid == x)
        x0, y0 = x0[0], y0[0]
        
        x1, y1 = np.where(OBJ_GRID == x)
        x1, y1 = x1[0], y1[0]
        
        distance += abs(x1 - x0) + abs(y1 - y0)

    return distance


class Node:
    def __init__(self, state, cost, parent, action):
        self.state  = state
        self.cost   = cost
        self.parent = parent
        self.action = action
        self.f      = self.cost + heuristic_manhattan(self.state)

    def __str__(self):
        return '\n\n'.join(['  '.join(map(str, grid)) for grid in self.state[0:2]]) + \
               '  >>>  ' + str(self.cost) + '\n\n' + \
               '\n\n'.join(['  '.join(map(str, grid)) for grid in self.state[2:]])

    @classmethod
    def child(cls, problem, parent, action):
        state = problem.result(parent.state, action)

        return cls(state, parent.cost + 1, parent, action)

    @property
    def solution(self):
        solution = []

        node = self
        while node:
            solution.append(node)
            node = node.parent

        solution.reverse()

        return solution


class Problem:
    def __init__(self, initial):
        self.initial = Node(initial, 0, None, None)
        self.objective = won_comp
        self.actions = available_moves
        self.result = move_grid
