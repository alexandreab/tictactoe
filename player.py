from board import Board

class Player:
    def __init__(self, symbol, board: Board):
        board.registry(symbol)
        self.__board = board
        self.__symbol = symbol

    def play(self, x, y):
        self.__board.set_value(self.__symbol, x, y)

    def get_positions(self):
        available_positions = []
        for i, line in enumerate(self.__board.get_board()):
            for j, cell in enumerate(line):
                if cell == ' ':
                    available_positions.append((i,j))
        return available_positions
