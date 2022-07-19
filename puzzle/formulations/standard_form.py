# Sets the default formulation of the puzzle problem:
# Initial state
# Actions
# Objective state


import numpy as np
from random import choice


ITER = 100


def objective_grid(n):
    return np.arange(n**2, dtype='int16').reshape((n, n))


def new_grid(n=3):  # returns a new grid
    grid = objective_grid(n)  # assigns the values

    grid = update_grid(grid)

    return grid


def update_grid(grid, iterations=ITER):
    for i in range(iterations):
        grid = random_move(grid)

    return grid


def move_grid(grid, movement):  # returns a new grid
    movement = movement.lower()

    if movement in available_moves(grid):
        x, y = is_empty(grid)
    
        grid = grid.copy()  # does not change the grid passed as a parameter

        if movement == 'l':
            grid[x][y], grid[x][y + 1] = grid[x][y + 1], grid[x][y]
        if movement == 'r':
            grid[x][y], grid[x][y - 1] = grid[x][y - 1], grid[x][y]
        if movement == 'u':
            grid[x][y], grid[x + 1][y] = grid[x + 1][y], grid[x][y]
        if movement == 'd':
            grid[x][y], grid[x - 1][y] = grid[x - 1][y], grid[x][y]

    return grid


def random_move(grid):
    grid = grid.copy()  # does not change the grid passed as a parameter

    movement = choice(['r', 'l', 'u', 'd'])  # choosing element at random

    return move_grid(grid, movement)


def won(grid):
    n = grid.shape[0]  # getting the grid dimension

    return np.array_equal(grid,
                          objective_grid(n))


def is_empty(grid):
    x, y = np.where(grid == 0)  # getting the zero position

    return x[0], y[0]  # unpacking the values
    

def available_moves(grid):
    x, y = is_empty(grid)

    moves = ''
    if y < (grid.shape[1] - 1):
        moves += 'l'
    if y > 0:
        moves += 'r'
    if x < (grid.shape[0] - 1):
        moves += 'u'
    if x > 0:
        moves += 'd'
        
    return moves
