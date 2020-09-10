from board import Board
from player import Player
from bot_random import BotRandom

b = Board()
p1 = Player('x', b)
p2 = BotRandom('o', b)
player_time = True
while not b.get_winner():
    if player_time:
        print('-'*80)
        print(b)
        l, c = [int(n) for n in input('choose x y: ').split(' ')]
        p1.play(l, c)
        player_time = False
    else:
        p2.play()
        player_time = True
print('-'*20, 'final score', '-'*20)
print(b)
print('The winner is', b.get_winner())
