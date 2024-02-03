import numpy as np
from .constants import *


def objective_grid(n=3):
    return np.arange(n**2, dtype='int8').reshape((n, n))

def new_grid(n=3):
    grid = objective_grid(n)

    update_grid_ip(grid)

    return grid

def update_grid(grid, iterations=ITER):
    grid = grid.copy()

    update_grid_ip(grid, iterations)

    return grid

def update_grid_ip(grid, iterations=ITER):
    for _ in range(iterations):
        random_move_ip(grid)

def move_grid(grid, movement):
    grid = grid.copy()
    movement = movement.lower()

    move_grid_ip(grid, movement)

    return grid

def move_grid_ip(grid, movement):
    movement = movement.lower()

    if available_move(grid, movement):
        x, y = is_empty(grid)

        if movement == 'l':
            grid[x][y], grid[x][y + 1] = grid[x][y + 1], grid[x][y]
        if movement == 'r':
            grid[x][y], grid[x][y - 1] = grid[x][y - 1], grid[x][y]
        if movement == 'u':
            grid[x][y], grid[x + 1][y] = grid[x + 1][y], grid[x][y]
        if movement == 'd':
            grid[x][y], grid[x - 1][y] = grid[x - 1][y], grid[x][y]

def random_move(grid):
    return move_grid(grid, np.random.choice(MOVES))

def random_move_ip(grid):
    move_grid_ip(grid, np.random.choice(MOVES))

def is_empty(grid):
    x, y = np.where(grid == 0)

    return x[0], y[0]

def available_move(grid, move):
    x, y = is_empty(grid)
    rows, cols = grid.shape

    if move == 'd':
        if x > 0:
            return True
    elif move == 'r':
        if y > 0:
            return True
    elif move == 'u':
        if x < rows - 1:
            return True
    elif move == 'l':
        if y < cols - 1:
            return True

    return False

def available_moves(grid):
    x, y = is_empty(grid)
    rows, cols = grid.shape

    moves = []
    if x > 0:
        moves.append('d')
    if y > 0:
        moves.append('r')
    if x < rows - 1:
        moves.append('u')
    if y < cols - 1:
        moves.append('l')

    return moves

def won(grid):
    n = grid.shape[0]

    return np.array_equal(grid, objective_grid(n))

def won_comp(grid, obj_grid):
    return np.array_equal(grid, obj_grid)
