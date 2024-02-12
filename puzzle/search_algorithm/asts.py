from .constants import *
from .priority_queue import PriorityQueue
from .node import Problem, Node


class ASTS:
    def __init__(self, grid):
        self.problem   = Problem(grid)
        self.frontier  = PriorityQueue()
        self.situation = SEARCH_NOT_STARTED
        self.solution  = None

    def step_search(self):
        node = self.frontier.remove_min()

        # Empty border ends the search
        if not node:
            self.situation = SEARCH_FAIL
            return
        
        if self.problem.objective(node.state, OBJ_GRID):
            self.solution = node.solution
            self.situation = SEARCH_SUCCESS
            return

        for action in self.problem.actions(node.state, node.action):
            self.frontier.add(Node.child(self.problem, node, action))

    def search(self):
        if self.situation == SEARCH_NOT_STARTED:
            self.frontier.add(self.problem.initial)
            self.situation = SEARCH_STARTED
        elif self.situation == SEARCH_FAIL:
            print('Search process failed!')
            return
        elif self.situation == SEARCH_SUCCESS:
            print('Solution already found!')
            return

        while self.situation == SEARCH_STARTED:
            self.step_search()

    @property
    def actions(self):
        for action in [step.action for step in self.solution[1:]]:
            yield action
