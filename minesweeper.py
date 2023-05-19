import random

import pygame

import sys

from game.utils.config import Config
from game.utils.state_manager import StateManager
from game.states.game_state import GameState
import time

config = Config(
    WIDTH = 800,
    HEIGHT = 600,
    FPS = 60
)

# Initialize Pygame
pygame.init()

state_manager = StateManager()
state_manager.register_state('GAME', GameState(config=config))
state_manager.set_state('GAME')

screen = pygame.display.set_mode((config.get('WIDTH'), config.get('HEIGHT')))

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    state_manager.handle_events(events, state_manager)
    state_manager.update()
    state_manager.render(screen)

    pygame.display.flip()

    
