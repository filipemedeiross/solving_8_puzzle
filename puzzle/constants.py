import pygame


# Game settings
N = 3

FRAMERATE_MS = 2
FRAMERATE_PS = 10

FONT_TYPE = 'Arial'
FONT_SIZE = 20
FONT_COLOR = 0, 0, 0

PATH_BG      = 'puzzle/media/background.jpg'
PATH_PLAY    = 'puzzle/media/play.png'
PATH_INFO    = 'puzzle/media/info.png'
PATH_RETURN  = 'puzzle/media/play_left.png'
PATH_SOLVE   = 'puzzle/media/forward.png'
PATH_REFRESH = 'puzzle/media/refresh.png'
PATH_EMPTY   = 'puzzle/media/empty.png'
PATH_NUMBERS = [f'puzzle/media/number_0{i}.png' for i in range(1, 9)]

MOVES = {pygame.K_UP    : 'u',
         pygame.K_DOWN  : 'd',
         pygame.K_RIGHT : 'r',
         pygame.K_LEFT  : 'l'}

# Dimensions
SIZE = WIDTH, HEIGHT = 240, 360

SPACING = 10
GRID_LEFT = 25
GRID_TOP  = 60
BUTTON_LEFT = 15
BUTTON_TOP  = HEIGHT * 3 / 4
TMMV_LEFT   = GRID_LEFT + SPACING
TMMV_TOP    = BUTTON_TOP + SPACING

SIDE = (WIDTH - 2 * GRID_LEFT) / N
REFRESH_SIZE = SIDE * N, SIDE * N
EMPTY_SIZE   = FONT_SIZE * 4, FONT_SIZE * 3 / 2
BUTTON_SIZE  = BUTTON_WIDTH, BUTTON_HEIGHT = FONT_SIZE * 3 / 2, FONT_SIZE * 3 / 2
BUTTON_PLAY_SIZE = WIDTH - 2 * BUTTON_LEFT, BUTTON_HEIGHT
