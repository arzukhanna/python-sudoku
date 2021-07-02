"""
Unit tests to check functioning of Sudoku solver.
Created: 2.07.2021
Modified: 2.07.2021
"""
import unittest


class MyTestCase(unittest.TestCase):
    """
    Test cases to determine whether all rows, columns and cells
    are valid, therefore creating a valid solution to the Sudoku puzzle.
    """

    def test_row_valid(self):
        """
        Test case in which all rows are valid.
        """
        self.assertEqual(True, False)

    def test_row_invalid(self):
        """
        Test case in which at least one row is invalid.
        """
        self.assertEqual(True, False)

    def test_column_valid(self):
        """
        Test case in which all columns are valid.
        """
        self.assertEqual(True, False)

    def test_column_invalid(self):
        """
        Test case in which at least one row is invalid.
        """
        self.assertEqual(True, False)

    def test_cell_valid(self):
        """
        Test case in which all cells are valid.
        """
        self.assertEqual(True, False)

    def test_cell_invalid(self):
        """
        Test case in which at least one row is invalid.
        """
        self.assertEqual(True, False)

    def test_solved_puzzle(self):
        """
        Test case in which puzzle has been solved correctly.
        """
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
