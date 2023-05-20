from game.utils.state_manager import NullState
from assets import *
import pygame

easy_rect = EASY_BUTTON.get_rect()
easy_rect.x = 242
easy_rect.y = 382

medium_rect = MEDIUM_BUTTON.get_rect()
medium_rect.x = 242
medium_rect.y = 502

hard_rect = HARD_BUTTON.get_rect()
hard_rect.x = 242
hard_rect.y = 622

class StartState(NullState):
    def __init__(self, *, config):
        super().__init__(config=config)

    def handle_transition(self, d=0):
        print('start state d', d)


    def handle_events(self, events=None):
        screen_size = self.config.get('WIDTH'), self.config.get('HEIGHT')
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    print(self.state_manager)
                    print(self.state_manager.data)

                    if easy_rect.collidepoint(mouse_pos):
                        self.state_manager.set_state('GAME', d=0)
                        # self.state_manager.data.set_difficulty(0)

                    if medium_rect.collidepoint(mouse_pos):
                        self.state_manager.set_state('GAME', d=1)
                        # self.state_manager.data.set_difficulty(1)

                    if hard_rect.collidepoint(mouse_pos):
                        self.state_manager.set_state('GAME', d=2)
                        # self.state_manager.data.set_difficulty(2)


                    
    def update(self):
        pass

    def render(self, screen):
        screen.fill(BACKGROUND)

        screen.blit(START_FACE, (336, 83))

        font = pygame.font.Font(FONT, 40)
        text = font.render("Minesweeper", True, (0, 0, 0))
        screen.blit(text, (180, 245))

        font = pygame.font.Font(FONT, 16)
        text = font.render("by Kadir", True, (0, 0, 0))
        screen.blit(text, (336, 300))

        screen.blit(EASY_BUTTON, easy_rect)
        screen.blit(MEDIUM_BUTTON, medium_rect)
        screen.blit(HARD_BUTTON, hard_rect)