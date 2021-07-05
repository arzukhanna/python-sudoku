"""
Unit tests to check functioning of Sudoku solver.
Created: 2.07.2021
Modified: 2.07.2021
"""
import unittest

import pytest

from lib import sudoku


@pytest.fixture
def correct_grid():
    """
    Initialising a correct grid for testing purposes
    """
    return [
        [2, 5, 4, 1, 9, 8, 3, 7, 6],
        [8, 1, 7, 4, 3, 6, 5, 2, 9],
        [9, 6, 3, 5, 2, 7, 8, 4, 1],
        [6, 4, 2, 9, 5, 1, 7, 3, 8],
        [5, 8, 1, 2, 7, 3, 9, 6, 4],
        [7, 3, 9, 8, 6, 4, 2, 1, 5],
        [4, 7, 6, 3, 8, 5, 1, 9, 2],
        [1, 9, 8, 7, 4, 2, 6, 5, 3],
        [3, 2, 5, 6, 1, 9, 4, 8, 7],
    ]


@pytest.fixture
def incorrect_dim_grid():
    """
    Initialising grid with incorrect dimensions for testing purposes.
    """
    return [
        [2, 5, 4, 1, 9, 8, 3, 7, 6],
        [8, 1, 7, 4, 3, 6, 5, 2, 9],
        [9, 6, 3, 5, 2, 7, 8, 4, 1],
    ]


@pytest.fixture
def row_dup_grid():
    """
    Initialising grid with duplicates in row.
    """
    return [[6, 5, 4, 1, 9, 8, 3, 7, 6]]


@pytest.fixture
def col_dup_grid():
    """
    Initialising grid with duplicates in column.
    """
    return [
        [2, 5, 4, 1, 9, 8, 3, 7, 6],
        [8, 1, 7, 4, 3, 6, 5, 2, 9],
        [9, 6, 3, 5, 2, 7, 8, 4, 1],
        [6, 4, 2, 9, 5, 1, 7, 3, 8],
        [5, 8, 1, 2, 7, 3, 9, 6, 4],
        [7, 3, 9, 5, 6, 4, 2, 1, 0],
        [4, 7, 6, 3, 8, 5, 1, 9, 2],
        [2, 9, 8, 7, 4, 0, 6, 5, 3],
        [3, 2, 5, 6, 1, 9, 4, 8, 7],
    ]


@pytest.fixture
def cell_incorrect_grid1():
    """
    Initialising grid with duplicates in column.
    """
    return [[0, 1, 2, "a", 8, 9, 0, 0, 0, 0]]


@pytest.fixture
def cell_incorrect_grid2():
    """
    Initialising grid with duplicates in column.
    """
    return [[0, 1, 2, 10, 8, 9, 0, 0, 0, 0]]


class MyTestCase(unittest.TestCase):
    """
    Test cases to determine whether all rows, columns and cells
    are valid, therefore creating a valid solution to the Sudoku puzzle.
    """

    def test_dim_valid(self):
        """
        Test case in which all rows are valid.
        """
        result = sudoku.dim_val(correct_grid)
        self.assertEqual(True, result, "Dimensions are correct")

    def test_dim_invalid(self):
        """
        Test case in which all rows are valid.
        """
        result = sudoku.dim_val(incorrect_dim_grid)
        self.assertEqual(False, result, "Dimensions are incorrect")

    def test_row_valid(self):
        """
        Test case in which at least one row is invalid.
        """
        result = sudoku.row_val(correct_grid)
        self.assertEqual(True, result, "Rows are correct")

    def test_row_invalid(self):
        """
        Test case in which at least one row is invalid.
        """
        result = sudoku.row_val(row_dup_grid)
        self.assertEqual(False, result, "Row has duplicate numbers")

    def test_column_valid(self):
        """
        Test case in which all columns are valid.
        """
        result = sudoku.col_val(correct_grid)
        self.assertEqual(True, result, "Columns are correct")

    def test_column_invalid(self):
        """
        Test case in which at least one row is invalid.
        """
        result = sudoku.col_val(col_dup_grid)
        self.assertEqual(False, result, "Column has duplicate numbers")

    def test_cell_valid(self):
        """
        Test case in which all cells are valid.
        """
        result = sudoku.cell_val(correct_grid)
        self.assertEqual(True, result, "All cells are valid")

    def test_cell_invalid(self):
        """
        Test case in which at least one row is invalid.
        """
        result1 = sudoku.cell_val(cell_incorrect_grid1)
        result2 = sudoku.cell_val(cell_incorrect_grid2)
        self.assertEqual(False, result1, "Invalid as string is included")
        self.assertEqual(False, result2, "Invalid as integer not in [0...9]")

    def test_solved_puzzle(self):
        """
        Test case in which puzzle has been solved correctly.
        """
        result = sudoku.is_grid_valid(correct_grid)
        self.assertEqual(False, result, "Solution is correct")


if __name__ == "__main__":
    unittest.main()
