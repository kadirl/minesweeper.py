import logging
from game.utils.config import Config

class NullState:
    _placeholder_warning_message = 'Placeholder state is used'

    def __init__(self, config=None):
        if config is None:
            config = Config()
        self.config = config

    def handle_events(self, events=None, state_manager=None):
        logging.debug(self._placeholder_warning_message)
        pass

    def update(self):
        logging.debug(self._placeholder_warning_message)
        pass

    def render(self, screen):
        logging.debug(self._placeholder_warning_message)
        pass

class StateManager:
    def __init__(self):
        self.states = {}
        self.current_state = NullState()

    def register_state(self, state_name, state_instance):
        self.states[state_name] = state_instance

    def set_state(self, state_name):
        self.current_state = self.states[state_name]

    def handle_events(self, events, state_manager):
        self.current_state.handle_events(events, state_manager)

    def update(self):
        self.current_state.update()

    def render(self, screen):
        self.current_state.render(screen)