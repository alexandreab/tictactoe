class Board:
    def __init__(self, x: int = 3, y: int = 3, c: int = 3):
        self.x = x
        self.y = y
        self.c = c
        self.reset_board()
        self.allowed_symbols = set()

    def reset_board(self):
        self.board = [[' ' for x in range(self.x)] for y in range(self.y)]

    def registry(self, value: str):
        if value in self.allowed_symbols:
            raise ValueError("Symbol already chosen")
        self.allowed_symbols.add(value)

    def get_board(self):
        return self.board

    def set_value(self, value: str, i: int, j: int):
        if value not in self.allowed_symbols:
            raise ValueError("Unregistered symbol")
        if self.board[i][j] != ' ':
            raise ValueError("Board position already filled")
        self.board[i][j] = value

    def get_winner(self):
        # check lines
        for i in range(self.y):
            for j in range(0, self.x, self.c):
                values = set(self.board[i][j:j+self.c])
                if len(values) == 1:
                    possible_winner = values.pop()
                    if possible_winner != ' ':
                        return possible_winner

        # check colums
        # TODO customize count of minimum quantity
        for j in range(self.x):
            values = set()
            for i in range(0, self.y):
                values.add(self.board[i][j])
            if len(values) == 1:
                possible_winner = values.pop()
                if possible_winner != ' ':
                    return possible_winner

        # check main diagonal
        values = set()
        for i in range(self.y):
            values.add(self.board[i][i])
        if len(values) == 1:
            possible_winner = values.pop()
            if possible_winner != ' ':
                return possible_winner

        # check secondary diagonal
        values = set()
        for i in range(self.y):
            values.add(self.board[i][self.x - 1 - i])
        if len(values) == 1:
            possible_winner = values.pop()
            if possible_winner != ' ':
                return possible_winner
        return None

    def __str__(self):
        data = [' | '.join(line) for line in self.board]
        return '\n'.join(data)

