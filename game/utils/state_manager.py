import logging
from game.utils.config import Config

class NullState:
    _null_state_exception = Exception("NullStateException: state isn't set")

    def __init__(self, config=None):
        if config is None:
            config = Config()
        self.config = config

    def set_state_manager(self, state_manager):
        self.state_manager = state_manager

    def handle_events(self, events=None):
        raise self._null_state_exception

    def update(self):
        raise self._null_state_exception

    def render(self, screen):
        raise self._null_state_exception

class StateManager:
    def __init__(self):
        self.states = {}
        self.data = {}
        self.current_state = NullState()

    def register_state(self, state_name, state_instance):
        self.states[state_name] = state_instance
        state_instance.set_state_manager(self)

    def set_state(self, state_name):
        self.current_state = self.states[state_name]

    def handle_events(self, events):
        self.current_state.handle_events(events)

    def update(self):
        self.current_state.update()

    def render(self, screen):
        self.current_state.render(screen)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data