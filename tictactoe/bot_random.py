import random
from tictactoe.player import Player

class BotRandom(Player):
    def play(self):
        pos = random.choice(self.get_positions())
        super().play(*pos)

