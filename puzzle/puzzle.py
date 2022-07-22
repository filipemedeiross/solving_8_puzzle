import pygame
from webbrowser import open
from .logic_game import LogicGame
from .constants import *


class Puzzle:
    def __init__(self):
        pygame.init()  # initializing pygame

        self.__puzzle = LogicGame(N)  # 3x3 is the default

        # Creating a display Surface
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Puzzle Game")

        # Create a Font object
        self.font = pygame.font.SysFont('Arial', size=font_size, bold=True)

        # Create an object to help update the grid
        self.clock = pygame.time.Clock()

        # Loading images used in the game
        self.background = pygame.transform.scale(pygame.image.load('puzzle/media/background.jpg'), size)

        self.win = pygame.transform.scale(pygame.image.load('puzzle/media/check.png'),
                                          (side * self.puzzle.n, side * self.puzzle.n))
        self.win.set_alpha(10)

        self.grid = [pygame.transform.scale(pygame.image.load(f'puzzle/media/number_0{i}.png'), (side, side))
                     for i in range(1, 9)]
        self.rects = [(spacing_grid + side * j, top_spacing + side * i)
                      for i in range(self.puzzle.n)
                      for j in range(self.puzzle.n)]

        self.button_play = pygame.transform.scale(pygame.image.load('puzzle/media/play.png'),
                                                  (width - 2*side_spacing, height_button))
        self.button_play_rect = self.button_play.get_rect(topleft=(side_spacing, bottom_spacing))

        self.button_info = pygame.transform.scale(pygame.image.load('puzzle/media/info.png'),
                                                  (width_button, height_button))
        self.button_info_rect = self.button_info.get_rect(topleft=(width - (spacing_grid + width_button),
                                                                   top_spacing - (spacing + height_button)))

        self.button_return = pygame.transform.scale(pygame.image.load('puzzle/media/play_left.png'),
                                                    (font_size * 3 / 2, font_size * 3 / 2))
        self.button_return_rect = self.button_return.get_rect(topleft=(spacing_grid, spacing))

        self.button_time = pygame.transform.scale(pygame.image.load('puzzle/media/empty.png'),
                                                  (font_size * 4, font_size * 3 / 2))
        self.button_time_rect = self.button_time.get_rect(topleft=(spacing_grid + spacing,
                                                                   self.rects[-1][1] + side + 3 * spacing))

        self.button_moves = pygame.transform.scale(pygame.image.load('puzzle/media/empty.png'),
                                                   (font_size * 4, font_size * 3 / 2))
        self.button_moves_rect = self.button_moves.get_rect(topleft=(width - (spacing_grid + spacing + self.button_moves.get_width()),
                                                                     self.rects[-1][1] + side + 3 * spacing))

    def init_game(self):  # method that start the game
        while True:
            self.main_screen()
            self.play()

    def main_screen(self):
        self.puzzle.update()  # update the grid

        # Preparing the main screen
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_info, self.button_info_rect)

        self.display_puzzle()

        pygame.display.flip()  # displaying the screen

        while True:
            # Getting input from user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)  # leaving the game

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play_rect.collidepoint(event.pos):
                        return
                    if self.button_info_rect.collidepoint(event.pos):
                        open('https://github.com/filipemedeiross', new=2)

            # Performing the presentation animation
            coord_0 = self.puzzle.is_empty
            self.puzzle.random_move()
            coord_1 = self.puzzle.is_empty

            if coord_0 != coord_1:
                self.update_puzzle(coord_0, coord_1)

            # Updating clock and grid display
            self.clock.tick(2)

            pygame.display.update(self.rects[0], (side*self.puzzle.n, side*self.puzzle.n))

    def play(self):
        time = moves = 0  # auxiliary variables

        # Displaying fixed screen elements
        self.screen.blit(self.background, (0, 0))  # overriding home screen buttons

        self.screen.blit(self.button_return, self.button_return_rect)

        self.screen.blit(self.button_moves, self.button_moves_rect)

        moves_text = self.font.render(f'{moves}', True, COLOR_FONT)
        self.screen.blit(moves_text, (self.button_moves_rect.centerx - (moves_text.get_width() / 2),
                                      self.button_moves_rect.centery - (moves_text.get_height() / 2)))

        self.display_puzzle()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_return_rect.collidepoint(event.pos):
                        return

                if event.type == pygame.KEYDOWN and not self.puzzle.won:
                    coord_0 = self.puzzle.is_empty

                    if event.key == pygame.K_UP:
                        self.puzzle.move('u')
                    if event.key == pygame.K_DOWN:
                        self.puzzle.move('d')
                    if event.key == pygame.K_RIGHT:
                        self.puzzle.move('r')
                    if event.key == pygame.K_LEFT:
                        self.puzzle.move('l')

                    coord_1 = self.puzzle.is_empty

                    if coord_0 != coord_1:
                        self.update_puzzle(coord_0, coord_1)

                        moves += 1

                        self.screen.blit(self.button_moves, self.button_moves_rect)

                        moves_text = self.font.render(f'{moves}', True, COLOR_FONT)
                        self.screen.blit(moves_text, (self.button_moves_rect.centerx - (moves_text.get_width() / 2),
                                                      self.button_moves_rect.centery - (moves_text.get_height() / 2)))

            if self.puzzle.won:
                self.screen.blit(self.win, self.rects[0])
            else:
                # Game time
                time += self.clock.tick(10)

                self.screen.blit(self.button_time, self.button_time_rect)

                time_text = self.font.render(f'{time // 1000 // 60}:{time // 1000 % 60}', True, COLOR_FONT)
                self.screen.blit(time_text, (self.button_time_rect.centerx - (time_text.get_width() / 2),
                                             self.button_time_rect.centery - (time_text.get_height() / 2)))

            pygame.display.flip()

    def display_puzzle(self):
        self.screen.blit(self.background, self.rects[0],
                         area=(self.rects[0], (side * self.puzzle.n, side * self.puzzle.n)))

        # Displaying fixed screen elements
        for num, pos in zip(self.puzzle.grid.flatten(), self.rects):
            if num:
                self.screen.blit(self.grid[num - 1], pos)

    def update_puzzle(self, coord_0, coord_1):
        index_0 = coord_0[0]*N + coord_0[1]
        index_1 = coord_1[0]*N + coord_1[1]

        # Drawing the moved element
        self.screen.blit(self.grid[self.puzzle[coord_0] - 1], self.rects[index_0])

        # Cleaning up the white space
        self.screen.blit(self.background, self.rects[index_1],
                         area=(self.rects[index_1], (side, side)))

    @property
    def puzzle(self):
        return self.__puzzle


if __name__ == '__main__':
    puzzle = Puzzle()

    puzzle.init_game()
