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

    def main_screen(self):
        self.screen.fill(COLOR_BG)

        button1 = pygame.Rect(side_spacing, bottom_spacing,
                              width - (side_spacing * 2), height_buttom)
        button2 = pygame.Rect(side_spacing, button1.bottom + spacing,
                              width / 2 - side_spacing, height_buttom)
        button3 = pygame.Rect(button2.right, button1.bottom + spacing,
                              width / 2 - side_spacing, height_buttom)

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

        clock = pygame.time.Clock()  # create an object to help update the grid

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
                    if button3.collidepoint(event.pos) and self.puzzle.n != 4:
                        self.puzzle = LogicGame(4)
                        self.rects = self.init_rects()

            self.puzzle.random_move()
            self.display_puzzle()

            clock.tick(2)

            pygame.display.flip()

    def play(self):
        self.screen.fill(COLOR_BG)  # overriding home screen buttons
        self.display_puzzle()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.puzzle.move('u')
                    if event.key == pygame.K_DOWN:
                        self.puzzle.move('d')
                    if event.key == pygame.K_RIGHT:
                        self.puzzle.move('r')
                    if event.key == pygame.K_LEFT:
                        self.puzzle.move('l')

                    self.display_puzzle()

            pygame.display.flip()

    def display_puzzle(self):
        # Filling grid area
        rect = self.rects[0][0]
        self.screen.fill(COLOR_BG, rect=(rect.left, rect.top,
                                         rect.width * self.puzzle.n,
                                         rect.height * self.puzzle.n))

        for i in range(self.puzzle.n):
            for j in range(self.puzzle.n):
                rect = self.rects[i][j]

                if self.puzzle[i][j]:
                    pygame.draw.rect(self.screen, COLOR_RECT, rect, border_radius=5)

                    number = self.font.render(str(self.puzzle[i][j]), True, COLOR_FONT)

                    self.screen.blit(number, (rect.centerx - (number.get_width() / 2),
                                              rect.centery - (number.get_height() / 2)))

    def init_rects(self):
        side = (width - spacing_grid * 2) / self.puzzle.n

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

        if puzzle.init_game:
            puzzle.play()