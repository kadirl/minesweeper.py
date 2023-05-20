from game.utils.state_manager import NullState
from game.minefield import Minefield
from assets import *
import pygame

class GameState(NullState):
    def __init__(self, *, config):
        super().__init__(config=config)

    def handle_transition(self):
        data = self.state_manager.data
        cell_size = self.config.get('CELL_SIZE')
        field_width, field_height = data.field_size
        mines_count = data.mine_count
        minefield = Minefield(field_height, field_width, mines_count, cell_size)
        minefield.generate_field()
        data.minefield = minefield


    def handle_events(self, events=None):
        screen_size = self.config.get('WIDTH'), self.config.get('HEIGHT')
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    self.state_manager.data.minefield.reveal_cell(mouse_pos, screen_size)
                elif event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    self.state_manager.data.minefield.flag_cell(mouse_pos, screen_size)

    def update(self):
        if self.state_manager.data.minefield.lost:
            print('GAME OVER')

    def render(self, screen):
        screen.fill(BACKGROUND)
        width, height = self.config.get('WIDTH'), self.config.get('HEIGHT')
        minefield = self.state_manager.data.minefield.render()
        m_width, m_height = minefield.get_width(), minefield.get_height()
        x = width // 2 - m_width // 2
        y = height // 2 - m_height // 2
        screen.blit(minefield, (x, y))