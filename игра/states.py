from enum import Enum

class State(Enum):
    MENU = 0,
    START = 1,
    RESTART = 3,
    CHOOSE_THEME = 4,
    CHOOSE_LEVEL = 5,
    CHOOSE_MUSIC = 6,
    QUIT = 7

class GameState:
    def __init__(self):
        self.state = State.MENU

    def change(self, state):
        self.state = state

    def check(self, state):
        if self.state == state:
            return True
        return False

