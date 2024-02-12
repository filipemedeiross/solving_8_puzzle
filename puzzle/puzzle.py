import pygame
from webbrowser import open
from .constants import *
from .logic_game import LogicGame
from .search_algorithm import ASGS


class Puzzle:
    def __init__(self):
        self.__puzzle = LogicGame(N)

        pygame.init()
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])

        # Creating the screen, clock and font objects
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('Puzzle Game')
        self.clock  = pygame.time.Clock()
        self.font   = pygame.font.SysFont(FONT_TYPE, size=FONT_SIZE, bold=True)

        # Loading images used in the game
        self.background = self.load_image(PATH_BG, SIZE)

        self.grid  = [self.load_image(path, (SIDE, SIDE)) for path in PATH_NUMBERS]
        self.rects = [pygame.Rect(GRID_LEFT + SIDE * j, GRID_TOP + SIDE * i, SIDE, SIDE)
                      for i in range(N)
                      for j in range(N)]

        self.button_play = self.load_image(PATH_PLAY, BUTTON_PLAY_SIZE)
        self.button_play_rect = self.button_play.get_rect(topleft=(BUTTON_LEFT, BUTTON_TOP))

        self.button_info = self.load_image(PATH_INFO, BUTTON_SIZE)
        self.button_info_rect = self.button_info.get_rect(topright=(WIDTH - GRID_LEFT, SPACING))

        self.button_return = self.load_image(PATH_RETURN, BUTTON_SIZE)
        self.button_return_rect = self.button_return.get_rect(topleft=(GRID_LEFT, SPACING))

        self.button_solve = self.load_image(PATH_SOLVE, BUTTON_SIZE)
        self.button_solve_rect = self.button_solve.get_rect(topright=(WIDTH - GRID_LEFT, SPACING))

        self.button_refresh = self.load_image(PATH_REFRESH, REFRESH_SIZE)
        self.button_refresh.set_alpha(180)
        self.button_refresh_rect = self.button_refresh.get_rect(topleft=self.rects[0].topleft)

        self.button_time = self.load_image(PATH_EMPTY, EMPTY_SIZE)
        self.button_time_rect = self.button_time.get_rect(topleft=(TMMV_LEFT, TMMV_TOP))

        self.button_moves = self.load_image(PATH_EMPTY, EMPTY_SIZE)
        self.button_moves_rect = self.button_moves.get_rect(topright=(WIDTH - TMMV_LEFT, TMMV_TOP))

    def init_game(self):
        while True:
            self.main_screen()
            self.play()

    def main_screen(self):
        self.display_main_screen()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play_rect.collidepoint(event.pos):
                        return
                    if self.button_info_rect.collidepoint(event.pos):
                        open('https://github.com/filipemedeiross', new=2)

            # Performing the presentation animation
            c0 = self.puzzle.is_empty
            self.puzzle.random_move()
            c1 = self.puzzle.is_empty

            if c0 != c1:
                self.update_puzzle(c0, c1)

            self.clock.tick(FRAMERATE_MS)

    def play(self):
        time = moves = 0

        self.display_play_screen()
        self.display_moves(moves)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_return_rect.collidepoint(event.pos):
                        self.puzzle.update()
                        return
                if self.puzzle.won:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button_refresh_rect.collidepoint(event.pos):
                            time = moves = 0
                            self.puzzle.update()

                            self.clock.tick()

                            self.display_play_screen()
                            self.display_moves(moves)
                elif event.type == pygame.KEYDOWN:
                    coord_0 = self.puzzle.is_empty
                    self.puzzle.move(MOVES[event.key])
                    coord_1 = self.puzzle.is_empty

                    if coord_0 != coord_1:
                        moves += 1

                        self.update_puzzle(coord_0, coord_1)
                        self.display_moves(moves)

                        if self.puzzle.won:
                            self.display_refresh()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_solve_rect.collidepoint(event.pos):
                        solution = ASGS(self.puzzle.grid)
                        solution.search()

                        for action in solution.actions:
                            coord_0 = self.puzzle.is_empty
                            self.puzzle.move(action)
                            coord_1 = self.puzzle.is_empty

                            self.clock.tick(FRAMERATE_MS)

                            self.update_puzzle(coord_0, coord_1)

                        self.display_refresh()

            if not self.puzzle.won:
                time += self.clock.tick(FRAMERATE_PS)

                self.display_time(time)

    def display_main_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_info, self.button_info_rect)

        self.display_puzzle()

        pygame.display.flip()

    def display_play_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.button_solve, self.button_solve_rect)
        self.screen.blit(self.button_return, self.button_return_rect)
        self.screen.blit(self.button_time, self.button_time_rect)
        self.screen.blit(self.button_moves, self.button_moves_rect)

        self.display_puzzle()

        pygame.display.flip()

    def display_moves(self, moves):
        moves_text = self.font.render(f'{moves}', True, FONT_COLOR)
        moves_rect = moves_text.get_rect(center=self.button_moves_rect.center)

        self.screen.blit(self.button_moves, self.button_moves_rect)
        self.screen.blit(moves_text, moves_rect)

        pygame.display.update(self.button_moves_rect)

    def display_time(self, t):
        time_text = self.font.render(f'{t // 1000 // 60}:{t // 1000 % 60}', True, FONT_COLOR)
        time_rect = time_text.get_rect(center=self.button_time_rect.center)

        self.screen.blit(self.button_time, self.button_time_rect)
        self.screen.blit(time_text, time_rect)

        pygame.display.update(self.button_time_rect)

    def display_refresh(self):
        self.screen.blit(self.button_refresh, self.button_refresh_rect)

        pygame.display.update(self.button_refresh_rect)

    def display_puzzle(self):
        self.screen.blit(self.background, self.rects[0], area=self.button_refresh_rect)

        for num, rect in zip(self.puzzle.grid.flatten(), self.rects):
            if num:
                self.screen.blit(self.grid[num - 1], rect)

    def update_puzzle(self, coord_0, coord_1):
        num = self.puzzle[coord_0] - 1
        index_0 = coord_0[0]*N + coord_0[1]
        index_1 = coord_1[0]*N + coord_1[1]

        # Drawing the moved element and cleaning up the white space
        self.screen.blit(self.grid[num], self.rects[index_0])
        self.screen.blit(self.background, self.rects[index_1], area=self.rects[index_1])

        pygame.display.update([self.rects[index_0], self.rects[index_1]])

    @staticmethod
    def load_image(path, size):
        return pygame.transform.scale(pygame.image.load(path), size)

    @property
    def puzzle(self):
        return self.__puzzle


if __name__ == '__main__':
    game = Puzzle()
    game.init_game()
