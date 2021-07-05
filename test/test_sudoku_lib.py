"""
Unit tests to check functioning of Sudoku solver.
Created: 2.07.2021
Modified: 2.07.2021
"""
import unittest

from lib import sudoku


class MyTestCase(unittest.TestCase):
    """
    Test cases to determine whether all rows, columns and cells
    are valid, therefore creating a valid solution to the Sudoku puzzle.
    """

    def test_row_valid(self):
        """
        Test case in which all rows are valid.
        """
        grid = [[6, 5, 4, 1, 9, 8, 3, 7, 6], [8, 1, 7, 4, 3, 6, 5, 2, 9],
                [9, 6, 3, 5, 2, 7, 8, 4, 1], [6, 4, 2, 9, 5, 1, 7, 3, 8],
                [5, 8, 1, 2, 7, 3, 9, 6, 4], [7, 3, 9, 8, 6, 4, 2, 1, 5],
                [4, 7, 6, 3, 8, 5, 1, 9, 2], [1, 9, 8, 7, 4, 2, 6, 5, 3],
                [3, 2, 5, 6, 1, 9, 4, 8, 7]]
        result = sudoku.dim_valid(grid)
        self.assertEqual(True, result, "Dimensions are correct")

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
