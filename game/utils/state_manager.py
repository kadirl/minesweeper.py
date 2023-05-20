import logging
from game.utils.config import Config

class GameData:
    def __init__(self, *, score=0, player_name=None, field_size=(), difficulty=2, mine_count=None, minefield=[]):
        self.score = score
        self.player_name = player_name
        self.field_size = field_size
        self.mine_count = mine_count
        self.minefield = minefield
        self.difficulty = difficulty

    def set_difficulty(self, d):
        self.difficulty = d

class NullState:
    _null_state_exception = Exception("NullStateException: state isn't set")

    def __init__(self, config=None):
        if config is None:
            config = Config()
        self.config = config

    def set_state_manager(self, state_manager):
        self.state_manager = state_manager

    def handle_transition(self, d=0):
        raise self._null_state_exception

    def handle_events(self, events=None):
        raise self._null_state_exception

    def update(self):
        raise self._null_state_exception

    def render(self, screen):
        raise self._null_state_exception

class StateManager:
    def __init__(self, data=None):
        self.states = {}
        if data is None:
            self.data = GameData()
        self.data = data
        self.current_state = NullState()

    def register_state(self, state_name, state_instance):
        self.states[state_name] = state_instance
        state_instance.set_state_manager(self)

    def set_state(self, state_name, d=0):
        self.current_state = self.states[state_name]
        self.states[state_name].handle_transition(d)

    def handle_events(self, events):
        self.current_state.handle_events(events)

    def update(self):
        self.current_state.update()

    def render(self, screen):
        self.current_state.render(screen)