import os
import pygame


# Directories definition 

current_directory = os.getcwd()
assets_directory = os.path.join(current_directory, 'assets')
sprites_directory = os.path.join(assets_directory, 'sprites')
audio_directory = os.path.join(assets_directory, 'audio')
fonts_directory = os.path.join(assets_directory, 'fonts')


# Colors definition

NUMBER_COLOR = {
    1: pygame.Color('#0025F4'),
    2: pygame.Color('#29711E'),
    3: pygame.Color('#F02F1D'),
    4: pygame.Color('#001170'),
    5: pygame.Color('#6E160D'),
    6: pygame.Color('#277274'),
    7: pygame.Color('#000000'),
    8: pygame.Color('#757575'),
}

BACKGROUND = pygame.Color('#B8B8B8')


# Sprites definition

UNREVEALED_CELL = pygame.image.load(os.path.join(sprites_directory, "unrevealed_cell.png"))
REVEALED_CELL = pygame.image.load(os.path.join(sprites_directory, "revealed_cell.png"))
BOMB_CELL = pygame.image.load(os.path.join(sprites_directory, "revealed_cell_bomb.png"))
MINE = pygame.image.load(os.path.join(sprites_directory, "mine.png"))
CROSSED_MINE = pygame.image.load(os.path.join(sprites_directory, "crossed_mine.png"))
FLAG = pygame.image.load(os.path.join(sprites_directory, "flag.png"))

START_FACE = pygame.image.load(os.path.join(sprites_directory, "start.png"))
WIN_FACE = pygame.image.load(os.path.join(sprites_directory, "win.png"))
LOST_FACE = pygame.image.load(os.path.join(sprites_directory, "lost.png"))

EASY_BUTTON = pygame.image.load(os.path.join(sprites_directory, "easy_button.png"))
MEDIUM_BUTTON = pygame.image.load(os.path.join(sprites_directory, "medium_button.png"))
HARD_BUTTON = pygame.image.load(os.path.join(sprites_directory, "hard_button.png"))


# Fonts definition

FONT = os.path.join(fonts_directory, "PressStart2P-Regular.ttf")