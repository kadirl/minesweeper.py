import pygame
import sys
from game.utils.config import Config
from game.utils.state_manager import StateManager, GameData
from game.states.game_state import GameState
from game.states.start_state import StartState
from game.states.lost_state import LostState
from game.states.win_state import WinState

import time

config = Config(
    WIDTH = 800,
    HEIGHT = 800,
    FPS = 60,
    CELL_SIZE = 30
)

# Initialize Pygame
pygame.init()

game_data = GameData(score=0, player_name="John Doe")
state_manager = StateManager(data=game_data)
state_manager.register_state('START', StartState(config=config))
state_manager.register_state('GAME', GameState(config=config))
state_manager.register_state('LOST', LostState(config=config))
state_manager.register_state('WIN', WinState(config=config))

state_manager.set_state('START')

screen = pygame.display.set_mode((config.get('WIDTH'), config.get('HEIGHT')))

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    state_manager.handle_events(events)
    state_manager.update()
    state_manager.render(screen)

    pygame.display.flip() 