import pygame
from .logic_game import LogicGame
from .constants import *


class Puzzle:
    def __init__(self):
        pygame.init()  # initializing pygame

        self.__puzzle = LogicGame(3)  # 3x3 is the default
        self.__rects = self.init_rects()
        self.init_game = False

        # Creating a display Surface
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Puzzle Game")

        # Create a Font object
        self.font = pygame.font.SysFont('Arial', size=font_size, bold=True)

        # Create an object to help update the grid
        self.clock = pygame.time.Clock()

    def main_screen(self):
        self.screen.fill(COLOR_BG)

        button1 = pygame.Rect(side_spacing, bottom_spacing,
                              width - 2 * side_spacing, height_buttom)
        button2 = pygame.Rect(side_spacing, button1.bottom + spacing,
                              width / 2 - side_spacing - spacing, height_buttom)
        button3 = pygame.Rect(button2.right + 2 * spacing, button1.bottom + spacing,
                              width / 2 - side_spacing - spacing, height_buttom)

        text_button1 = self.font.render("Iniciar", True, COLOR_FONT)
        text_button2 = self.font.render("3", True, COLOR_FONT)
        text_button3 = self.font.render("4", True, COLOR_FONT)

        pygame.draw.rect(self.screen, COLOR_BUTTON, button1, border_radius=5)
        pygame.draw.rect(self.screen, COLOR_BUTTON, button2, border_radius=5)
        pygame.draw.rect(self.screen, COLOR_BUTTON, button3, border_radius=5)

        self.screen.blit(text_button1, (button1.centerx - (text_button1.get_width() / 2),
                                        button1.centery - (text_button1.get_height() / 2)))
        self.screen.blit(text_button2, (button2.centerx - (text_button2.get_width() / 2),
                                        button2.centery - (text_button2.get_height() / 2)))
        self.screen.blit(text_button3, (button3.centerx - (text_button3.get_width() / 2),
                                        button3.centery - (text_button3.get_height() / 2)))

        # Displaying the screen
        self.display_puzzle()
        pygame.display.flip()

        # Getting input from user
        while not self.init_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.collidepoint(event.pos):
                        self.init_game = True
                    if button2.collidepoint(event.pos) and self.puzzle.n != 3:
                        self.puzzle = LogicGame(3)
                        self.rects = self.init_rects()

                        self.display_puzzle()
                    if button3.collidepoint(event.pos) and self.puzzle.n != 4:
                        self.puzzle = LogicGame(4)
                        self.rects = self.init_rects()

                        self.display_puzzle()

            # Performing the presentation animation
            coord0 = self.puzzle.is_empty
            self.puzzle.random_move()
            coord1 = self.puzzle.is_empty

            if coord0 != coord1:
                self.update_display(coord0, coord1)

            self.clock.tick(2)

            pygame.display.update((self.rects[0][0].left,
                                   self.rects[0][0].top,
                                   self.rects[0][0].width * self.puzzle.n,
                                   self.rects[0][0].height * self.puzzle.n))

    def play(self):
        time = moves = 0

        # Displaying fixed screen elements
        self.screen.fill(COLOR_BG)  # overriding home screen buttons

        return_buttom = pygame.Rect(spacing_grid, spacing, font_size*3/2, font_size*3/2)
        time_buttom = pygame.Rect(spacing_grid + spacing,
                                  self.rects[-1][-1].bottom + 3 * spacing,
                                  font_size*4, font_size*3/2)
        moves_buttom = pygame.Rect(self.rects[-1][-1].right - spacing - font_size * 4,
                                   self.rects[-1][-1].bottom + 3 * spacing,
                                   font_size * 4, font_size * 3 / 2)

        return_text = self.font.render('<<', True, COLOR_FONT)
        moves_text = self.font.render(f'{moves}', True, COLOR_FONT)

        pygame.draw.rect(self.screen, COLOR_BUTTON, return_buttom, border_radius=5)
        pygame.draw.rect(self.screen, COLOR_BUTTON, moves_buttom, border_radius=5)

        self.screen.blit(return_text, (return_buttom.centerx - (return_text.get_width() / 2),
                                       return_buttom.centery - (return_text.get_height() / 2)))
        self.screen.blit(moves_text, (moves_buttom.centerx - (moves_text.get_width() / 2),
                                      moves_buttom.centery - (moves_text.get_height() / 2)))

        self.display_puzzle()

        while self.init_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_buttom.collidepoint(event.pos):
                        self.init_game = False

                if event.type == pygame.KEYDOWN:
                    coord0 = self.puzzle.is_empty

                    if event.key == pygame.K_UP:
                        self.puzzle.move('u')
                    if event.key == pygame.K_DOWN:
                        self.puzzle.move('d')
                    if event.key == pygame.K_RIGHT:
                        self.puzzle.move('r')
                    if event.key == pygame.K_LEFT:
                        self.puzzle.move('l')

                    coord1 = self.puzzle.is_empty

                    if coord0 != coord1:
                        self.update_display(coord0, coord1)

                        moves += 1

                        moves_text = self.font.render(f'{moves}', True, COLOR_FONT)

                        pygame.draw.rect(self.screen, COLOR_BUTTON, moves_buttom, border_radius=5)

                        self.screen.blit(moves_text, (moves_buttom.centerx - (moves_text.get_width() / 2),
                                                      moves_buttom.centery - (moves_text.get_height() / 2)))

            # Game time
            time += self.clock.tick(10)

            time_text = self.font.render(f'{time // 1000 // 60}:{time // 1000 % 60}', True, COLOR_FONT)

            self.screen.fill(COLOR_BG, time_buttom)

            pygame.draw.rect(self.screen, COLOR_BUTTON, time_buttom, border_radius=5)

            self.screen.blit(time_text, (time_buttom.centerx - (time_text.get_width() / 2),
                                         time_buttom.centery - (time_text.get_height() / 2)))

            pygame.display.flip()

    def display_puzzle(self):
        # Filling grid area
        self.screen.fill(COLOR_BG, rect=(self.rects[0][0].left,
                                         self.rects[0][0].top,
                                         self.rects[0][0].width * self.puzzle.n,
                                         self.rects[0][0].height * self.puzzle.n))

        for i in range(self.puzzle.n):
            for j in range(self.puzzle.n):
                rect = self.rects[i][j]

                if self.puzzle[i][j]:
                    pygame.draw.rect(self.screen, COLOR_RECT, rect, border_radius=5)

                    number = self.font.render(str(self.puzzle[i][j]), True, COLOR_FONT)
                    self.screen.blit(number, (rect.centerx - (number.get_width() / 2),
                                              rect.centery - (number.get_height() / 2)))

    def update_display(self, coord0, coord1):
        # Drawing the moved element
        pygame.draw.rect(self.screen, COLOR_RECT,
                         self.rects[coord0[0]][coord0[1]], border_radius=5)

        number = self.font.render(str(self.puzzle[coord0[0]][coord0[1]]),
                                  True, COLOR_FONT)

        self.screen.blit(number, (self.rects[coord0[0]][coord0[1]].centerx - (number.get_width() / 2),
                                  self.rects[coord0[0]][coord0[1]].centery - (number.get_height() / 2)))

        # Cleaning up the white space
        self.screen.fill(COLOR_BG, rect=self.rects[coord1[0]][coord1[1]])

    def init_rects(self):
        side = (width - 2 * spacing_grid) / self.puzzle.n

        return [[pygame.Rect(spacing_grid + side * j, top_spacing + side * i, side, side)
                 for j in range(self.puzzle.n)]
                for i in range(self.puzzle.n)]

    @property
    def puzzle(self):
        return self.__puzzle

    @puzzle.setter
    def puzzle(self, n_puzzle):
        self.__puzzle = n_puzzle

    @property
    def rects(self):
        return self.__rects

    @rects.setter
    def rects(self, n_rects):
        self.__rects = n_rects


if __name__ == '__main__':
    puzzle = Puzzle()

    while True:
        puzzle.main_screen()

        puzzle.play()
