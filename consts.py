import pygame as pg
from funcs import Point

# constants
DARKRED = (250, 250, 243)
RED = (255, 0, 0)
BLUE = (67, 89, 249)
LIGHTBLUE = (51, 153, 255)
GREEN = (93, 237, 76)
LIGHTGREEN = (153, 255, 51)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (84, 84, 69)
ORANGE = (255, 128, 0)
ESPECIAL = (222, 104, 104)
EPS = 0.0000000001
FPS = 30
MAX_BOARD_SIZE = 20
MIN_BOARD_SIZE = 5

"""
DARKRED = (155, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (51, 153, 255)
GREEN = (0, 255, 0)
LIGHTGREEN = (153, 255, 51)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (255, 255, 51)
ORANGE = (255, 128, 0)
EPS = 0.0000000001
FPS = 30
MAX_BOARD_SIZE = 20
MIN_BOARD_SIZE = 5
"""

# setup()
TILE_IMG = 'tile.png'
BG_IMG = 'bg.jpg'
PAUSE_IMG = 'pause.png'
BACK_IMG = 'back.png'
UP_IMG = 'up-arrow.png'
DOWN_IMG = 'down-arrow.png'
RULES = 'rules.txt'
INFO = 'info.txt'
BACKGROUND_MUSIC = 'bg-music.wav'
CLICK_SOUND = 'click.wav'
# size of the window
W = 800
H = 600
# size of the grid
SIZE = 5
moves = [Point(1, 0), Point(1, -1), Point(0, 1), Point(0, -1), Point(-1, 1), Point(-1, 0)]


#Tamaño caja preguntas
WIDTH_QUESTIONS = 850
HEIGHT_QUESTIONS = 300
TITULO = 'Preguntas'
