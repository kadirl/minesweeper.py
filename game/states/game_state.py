from game.utils.state_manager import NullState
from game.minefield import Minefield
from assets import *
import pygame

continue_rect = CONTINUE_BUTTON.get_rect()
continue_rect.x = 313
continue_rect.y = 720

class GameState(NullState):
    def __init__(self, *, config):
        super().__init__(config=config)

    def handle_transition(self, d=0):
        print('game state d', d)
        data = self.state_manager.data
        cell_size = self.config.get('CELL_SIZE')

        field_width, field_height = 0, 0 # data.field_size
        mines_count = 0 # data.mine_count
        # difficulty = data.difficulty

        if d == 0:
            field_width = 10
            field_height = 10
            mines_count = 10
            cell_size = 60

        elif d == 1:
            field_width = 20
            field_height = 20
            mines_count = 45
            cell_size = 30

        elif d == 2:
            field_width = 30
            field_height = 30
            mines_count = 120
            cell_size = 20

        minefield = Minefield(field_height, field_width, mines_count, cell_size)
        minefield.generate_field()
        data.minefield = minefield

        self.clock = pygame.time.Clock()
        self.timer = 0

        print('time reset')

    def handle_events(self, events=None):
        screen_size = self.config.get('WIDTH'), self.config.get('HEIGHT')
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state_manager.set_state('GAME')
            if event.type == pygame.MOUSEBUTTONDOWN and not self.state_manager.data.minefield.lost and not self.state_manager.data.minefield.win:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    self.state_manager.data.minefield.reveal_cell(mouse_pos, screen_size)
                elif event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    self.state_manager.data.minefield.flag_cell(mouse_pos, screen_size)
            if event.type == pygame.MOUSEBUTTONDOWN and self.state_manager.data.minefield.lost:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if continue_rect.collidepoint(mouse_pos):
                        self.state_manager.set_state('LOST')
            if event.type == pygame.MOUSEBUTTONDOWN and self.state_manager.data.minefield.win:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if continue_rect.collidepoint(mouse_pos):
                        self.state_manager.set_state('WIN')


    def update(self):
        if self.state_manager.data.minefield.lost:
            print('GAME OVER')
            # self.state_manager.set_state('LOST')
        if self.state_manager.data.minefield.win:
            print('WIN')
            # self.state_manager.set_state('WIN')
        if not self.state_manager.data.minefield.lost and not self.state_manager.data.minefield.win:
            self.timer += self.clock.get_time() / 1000

    def render(self, screen):
        screen.fill(BACKGROUND)
        width, height = self.config.get('WIDTH'), self.config.get('HEIGHT')
        minefield, mines_left = self.state_manager.data.minefield.render()
        m_width, m_height = minefield.get_width(), minefield.get_height()
        x = width // 2 - m_width // 2
        y = height // 2 - m_height // 2
        screen.blit(minefield, (x, y))

        scaled_flag = pygame.transform.scale(FLAG, (50, 50))
        screen.blit(scaled_flag, (8, 8))

        font = pygame.font.Font(FONT, 20)
        text = font.render(str(mines_left), True, (0, 0, 0))
        screen.blit(text, (57, 23))

        font = pygame.font.Font(FONT, 20)
        text = font.render(f"{self.timer:.2f}", True, (0, 0, 0))
        rect_text = text.get_rect()
        screen.blit(text, (800-rect_text.width-20, 21))

        if self.state_manager.data.minefield.lost:
            screen.blit(CONTINUE_BUTTON, continue_rect)
            font = pygame.font.Font(FONT, 24)
            text = font.render("You Lost", True, (0, 0, 0))
            screen.blit(text, (304, 21))

        if self.state_manager.data.minefield.win:
            screen.blit(CONTINUE_BUTTON, continue_rect)
            font = pygame.font.Font(FONT, 24)
            text = font.render("You Win", True, (0, 0, 0))
            screen.blit(text, (304, 21))
        
        self.clock.tick(60)