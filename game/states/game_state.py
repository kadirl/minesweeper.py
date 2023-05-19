from game.utils.state_manager import NullState
import pygame

class GameState(NullState):
    def __init__(self, config):
        super().__init__(config=config)
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def handle_events(self, events=None, state_manager=None):
        for event in events:
            if event.type == pygame.KEYDOWN:
                print('Key is pressed')

    def update(self):
        pass

    def render(self, screen):
            screen.fill((0, 0, 0))
            text = self.font.render("Hello, World!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.config.get('WIDTH') // 2, self.config.get('HEIGHT') // 2))
            screen.blit(text, text_rect)