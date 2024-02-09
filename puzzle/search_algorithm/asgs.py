import numpy as np
from collections import deque
from .constants import *
from .priority_queue import PriorityQueue
from .node import Problem, Node


class ASGS:
    def __init__(self, grid):
        self.problem   = Problem(grid)
        self.explored  = deque([])
        self.frontier  = PriorityQueue()
        self.situation = SEARCH_NOT_STARTED
        self.solution  = None

    def step_search(self):
        # Checking three initial conditions:
        # Root node initial check
        # Checking if the search process failed
        # Checking if the search was successful
        if self.situation == SEARCH_NOT_STARTED:
            self.frontier.add(self.problem.initial)
            self.situation = SEARCH_STARTED
        elif self.situation == SEARCH_FAIL:
            print('Search process failed!')
            return
        elif self.situation == SEARCH_SUCCESS:
            print('Solution already found!')
            return

        # Performing the search step
        node = self.frontier.remove_min()

        # Empty border ends the search
        if not node:
            self.situation = SEARCH_FAIL
            return
        
        if self.problem.objective(node.state, OBJ_GRID):
            self.solution = node.solution
            self.situation = SEARCH_SUCCESS
            return

        self.explored.append(node.state)

        for action in self.problem.actions(node.state):
            child = Node.child(self.problem, node, action)
            idx_frontier = self.frontier.index(child)

            if idx_frontier:
                if child.f < self.frontier[idx_frontier].f:
                    self.frontier.remove_idx(idx_frontier)
                    self.frontier.add(child)
            elif not self.explored_node(child.state):                
                self.frontier.add(child)

    def search(self):
        while self.situation == SEARCH_STARTED or self.situation == SEARCH_NOT_STARTED:
            self.step_search()

    def explored_node(self, state):
        for state_explored in self.explored:
            if np.array_equal(state, state_explored):
                return True

        return False

    @property
    def show_solution(self):
        if self.situation == SEARCH_SUCCESS:
            return '\n\n'.join([node.__str__() for node in self.solution]) + \
                  f'\nCost: {self.solution[-1].cost}'
    
        return 'Solution still not found!'

    @property
    def show_frontier(self):
        return '#'*15 + '\n' + \
               '\n'.join([node.__str__() for node in self.frontier]) + \
               '\n' + '#'*15

    @property
    def actions(self):
        for action in [step.action for step in self.solution[1:]]:
            yield action
