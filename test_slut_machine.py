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
