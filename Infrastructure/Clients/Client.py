class Client:

    COLOR_BLACK = 'Black'
    COLOR_WHITE = 'White'
    PROMPT_FROM = 'From (row col):'
    PROMPT_TO = 'To (row col):'

    game = None

    def __init__(self, game):
        self.game = game

    def get_game(self):
        return self.game

    def show_game_state(self):
        pass
