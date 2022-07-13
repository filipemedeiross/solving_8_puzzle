# Sets the default formulation of the puzzle problem:
# Initial state
# Actions
# Objective state


import numpy as np


def new_grid(n=3):  # returns a new grid
    grid = np.arange(n**2, dtype='int16')  # assigns the values

    np.random.shuffle(grid)  # shuffle the grid
    grid.resize((n, n))  # resize the grid

    return grid


def move_grid(grid, movement):  # returns a new grid
    x, y = np.where(grid == 0)  # getting the zero position
    x, y = x[0], y[0]  # unpacking the values

    grid = grid.copy()  # does not change the grid passed as a parameter

    if movement in 'Ll' and y < (grid.shape[1] - 1):
        grid[x][y], grid[x][y + 1] = grid[x][y + 1], grid[x][y]
    if movement in 'Rr' and y > 0:
        grid[x][y], grid[x][y - 1] = grid[x][y - 1], grid[x][y]
    if movement in 'Uu' and x < (grid.shape[0] - 1):
        grid[x][y], grid[x + 1][y] = grid[x + 1][y], grid[x][y]
    if movement in 'Dd' and x > 0:
        grid[x][y], grid[x - 1][y] = grid[x - 1][y], grid[x][y]

    return grid


def won(grid):
    n = grid.shape[0]  # getting the grid dimension

    return np.array_equal(grid,
                          np.roll(np.arange(n**2, dtype='int16').reshape((n, n)), -1))
