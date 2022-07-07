import numpy as np


# Class that implements the puzzle logic
class Puzzle:
    def __init__(self, n):
        self.__n = n
        self.__grid = np.arange(n**2, dtype='int16')  # assigns the values

        np.random.shuffle(self.__grid)  # shuffle the grid
        self.__grid.resize((n, n))  # resize the grid

    def move(self, movement):
        x, y = np.where(self.grid == 0)  # getting the zero position
        x, y = x[0], y[0]  # unpacking the values

        if movement in 'Ll' and y < (self.n-1):
            self.__grid[x][y], self.__grid[x][y+1] = self.__grid[x][y+1], self.__grid[x][y]
        if movement in 'Rr' and y > 0:
            self.__grid[x][y], self.__grid[x][y-1] = self.__grid[x][y-1], self.__grid[x][y]
        if movement in 'Uu' and x < (self.n-1):
            self.__grid[x][y], self.__grid[x+1][y] = self.__grid[x+1][y], self.__grid[x][y]
        if movement in 'Dd' and x > 0:
            self.__grid[x][y], self.__grid[x-1][y] = self.__grid[x-1][y], self.__grid[x][y]

    @property
    def won(self):
        return np.array_equal(self.grid,
                              np.roll(np.arange(self.n**2, dtype='int16').reshape((self.n, self.n)), -1))

    @property
    def n(self):
        return self.__n

    @property
    def grid(self):
        return self.__grid


# Testing the game
if __name__ == "__main__":
    N = 3

    puzzle = Puzzle(N)

    print(puzzle.grid)
    while not puzzle.won:
        inp = input('Insert a move [l,r,u,d]: ')
        puzzle.move(inp)

        print(puzzle.grid)

    print("You won!")
