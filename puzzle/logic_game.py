from .search_algorithm.constants import OBJ_GRID
from .formulations.standard_form import new_grid, update_grid_ip, move_grid_ip, \
                                        random_move_ip, won_comp, is_empty


class LogicGame:
    def __init__(self, n):
        self.grid = new_grid(n)

    def __getitem__(self, args):
        return self.grid[args]

    def __str__(self):
        return '\n\n'.join(['  '.join(map(str, row))
                            for row in self.grid])

    def move(self, movement):
        move_grid_ip(self.grid, movement)

    def random_move(self):
        random_move_ip(self.grid)

    def update(self):
        update_grid_ip(self.grid)

    @property
    def won(self):
        return won_comp(self.grid, OBJ_GRID)

    @property
    def is_empty(self):
        return is_empty(self.grid)

    @property
    def n(self):
        return self.grid.shape[0]


# Testing the game
if __name__ == "__main__":
    import sys

    N = int(sys.argv[1])
    puzzle = LogicGame(N)

    print(puzzle)
    while not puzzle.won:
        inp = input('Insert a move [l,r,u,d]: ')
        puzzle.move(inp)

        print(puzzle)

    print("You won!")
