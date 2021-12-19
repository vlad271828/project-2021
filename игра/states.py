from enum import Enum

class State(Enum):
    MENU = 0,
    START = 1,
    QUIT = 2,
    RESTART = 3

class GameState:
    def __init__(self):
        self.state = State.MENU

    def change(self, state):
        self.state = state

    def check(self, state):
        if self.state == state:
            return True
        return False

