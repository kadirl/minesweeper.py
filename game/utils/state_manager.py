import logging
from game.utils.config import Config

class GameData:
    def __init__(self, *, score=0, player_name=None, field_size=(), mine_count=None, minefield=[]):
        self._score = score
        self._player_name = player_name
        self._field_size = field_size
        self._mine_count = mine_count
        self._minefield = minefield

    @staticmethod
    def _create_property(attribute_name):
        def getter(self):
            return getattr(self, f"_{attribute_name}")

        def setter(self, value):
            setattr(self, f"_{attribute_name}", value)

        return property(getter, setter)
    
    score = _create_property("score")
    player_name = _create_property("player_name")
    field_size = _create_property("field_size")
    mine_count = _create_property("mine_count")
    minefield = _create_property("minefield")

class NullState:
    _null_state_exception = Exception("NullStateException: state isn't set")

    def __init__(self, config=None):
        if config is None:
            config = Config()
        self.config = config

    def set_state_manager(self, state_manager):
        self.state_manager = state_manager

    def handle_transition(self):
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
        state_instance.handle_transition()

    def set_state(self, state_name):
        self.current_state = self.states[state_name]
        self.states[state_name].handle_transition()

    def handle_events(self, events):
        self.current_state.handle_events(events)

    def update(self):
        self.current_state.update()

    def render(self, screen):
        self.current_state.render(screen)