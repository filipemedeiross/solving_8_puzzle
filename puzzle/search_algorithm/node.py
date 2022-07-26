import numpy as np
from .. import formulations  # formulation returns the default


# Defining the manhattan heuristic
def heuristic_manhattan(grid):
    objective_grid = formulations.objective_grid(3)

    distance = 0
    for x in range(1, 9):
        x0, y0 = np.where(grid == x)
        x0, y0 = x0[0], y0[0]

        x1, y1 = np.where(objective_grid == x)
        x1, y1 = x1[0], y1[0]

        distance += abs(x1 - x0) + abs(y1 - y0)

    return distance


# Class with a tree node
class Node:
    def __init__(self, state, cost, parent, action):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.action = action
        self.f = self.cost + heuristic_manhattan(self.state)

    def __str__(self):  # representing the node
        return '\n\n'.join(['  '.join(map(str, grid)) for grid in self.state[0:2]]) + \
               '  >>>  ' + str(self.cost) + '\n\n' + \
               '\n\n'.join(['  '.join(map(str, grid)) for grid in self.state[2:]])

    @classmethod
    def child(cls, problem, parent, action):
        state = problem.result(parent.state, action)

        return cls(state, parent.cost + 1, parent, action)  # returning the child

    @property
    def solution(self):
        node = self
        solution = []

        while node:
            solution.append(node)
            node = node.parent

        solution.reverse()

        return solution


# Class with a search problem
class Problem:
    def __init__(self, initial):
        self.initial = Node(initial, 0, None, None)
        self.objective = formulations.won
        self.actions = formulations.available_moves
        self.result = formulations.move_grid  # defines the transition model
