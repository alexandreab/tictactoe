import unittest
from tictactoe.board import Board
from tictactoe.player import Player

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player = Board()
