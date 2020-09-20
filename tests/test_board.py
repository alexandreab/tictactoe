import unittest

from tictactoe.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.registry('x')
        self.board.registry('o')

    def test_get_board(self):
        board_values = self.board.get_board()
        for line in board_values:
            for value in line:
                self.assertEqual(value, ' ')

    def test_set_valid_value(self):
        for i in range(3):
            for j in range(3):
                self.board.set_value('x' , i, j)
                values = self.board.get_board()
                self.assertEqual(values[i][j], 'x')

    def test_set_invalid_value(self):
        self.board.set_value('x' , 1, 1)
        with self.assertRaises(ValueError) as context:
            self.board.set_value('x' , 1, 1)
        exc = context.exception
        self.assertTrue('position already filled' in str(exc))

    def test_check_no_winner(self):
        self.assertEqual(self.board.get_winner(), None)

    def assert_line_winner(self, letter, line):
        self.board.set_value(letter , line, 0)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter , line, 1)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter , line, 2)
        self.assertEqual(self.board.get_winner(), letter,
                         f'Should return {letter} as winner')

    def assert_column_winner(self, letter, column):
        self.board.set_value(letter, 0, column)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter, 1, column)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter, 2, column)
        self.assertEqual(self.board.get_winner(), letter,
                         f'Should return {letter} as winner')

    def test_check_winner_first_line(self):
        letter = 'x'
        self.assert_line_winner(letter, 0)

    def test_check_winner_second_line(self):
        letter = 'o'
        self.assert_line_winner(letter, 1)

    def test_check_winner_third_line(self):
        letter = 'x'
        self.assert_line_winner(letter, 2)

    def test_check_winner_first_column(self):
        letter = 'x'
        self.assert_column_winner(letter, 0)

    def test_check_winner_second_column(self):
        letter = 'x'
        self.assert_column_winner(letter, 1)

    def test_check_winner_third_column(self):
        letter = 'x'
        self.assert_column_winner(letter, 2)

    def test_check_winner_main_diagonal(self):
        letter = 'x'
        self.board.set_value(letter, 0, 0)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter, 1, 1)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter, 2, 2)
        self.assertEqual(self.board.get_winner(), letter,
                         f'Should return {letter} as winner')

    def test_check_winner_secondary_diagonal(self):
        letter = 'x'
        self.board.set_value(letter, 0, 2)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter, 1, 1)
        self.assertEqual(self.board.get_winner(), None)
        self.board.set_value(letter, 2, 0)
        self.assertEqual(self.board.get_winner(), letter,
                         f'Should return {letter} as winner')

if __name__ == '__main__':
    unittest.main()
