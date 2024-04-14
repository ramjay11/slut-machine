import unittest
from unittest.mock import patch
import main


class TestSlutMachine(unittest.TestCase):
    @patch('builtins.input', side_effect=['1000'])
    def test_deposit(self, mock_input):
        self.assertEqual(main.deposit(), 1000)

    @patch('builtins.input', side_effect=['2'])
    def test_get_number_of_lines(self, mock_input):
        self.assertEqual(main.get_number_of_lines(), 2)

    @patch('builtins.input', side_effect=['10'])
    def test_get_bet(self, mock_input):
        self.assertEqual(main.get_bet(), 10)

    def test_check_winnings_no_win(self):
        columns = [['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C']]
        lines = 2
        bet = 10
        values = {'A': 5, 'B': 4, 'C': 3, 'D': 2}
        winnings, winning_lines = main.check_winnings(columns, lines, bet, values)
        self.assertEqual(winnings, 0)
        self.assertEqual(winning_lines, [])
