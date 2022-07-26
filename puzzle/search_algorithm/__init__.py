# Documentation available at tests/informed_search.ipynb


from .priority_queue import PriorityQueue
from .node import Problem, Node


# Constants for current search status
SEARCH_NOT_STARTED = 0
SEARCH_STARTED = 1
SEARCH_FAIL = 2
SEARCH_SUCCESS = 3


# Class that will implement A* tree search
class ASTS:  # A* tree search
    def __init__(self, grid):
        self.problem = Problem(grid)
        self.frontier = PriorityQueue()
        self.situation = SEARCH_NOT_STARTED
        self.solution = []

    def step_search(self):
        # Root node initial check
        if self.situation == SEARCH_NOT_STARTED:  # only if the search did not fail or was successful
            self.frontier.add(self.problem.initial)
            self.situation = SEARCH_STARTED  # indicates that the search has started

        # Checking if the search process failed
        if self.situation == SEARCH_FAIL:
            return

        # Checking if the search was successful
        if self.situation == SEARCH_SUCCESS:
            return

        # Performing the search step
        node = self.frontier.remove_min()

        if not node:  # empty border ends the search
            self.situation = SEARCH_FAIL
            return

        if self.problem.objective(node.state):
            self.solution = node.solution
            self.situation = SEARCH_SUCCESS
            return

        for action in self.problem.actions(node.state):
            self.frontier.add(Node.child(self.problem, node, action))

    def search(self):
        # Loop that performs breadth-first search
        while self.situation != SEARCH_FAIL and self.situation != SEARCH_SUCCESS:
            self.step_search()

    @property
    def actions(self):
        for action in [step.action for step in self.solution[1:]]:
            yield action
