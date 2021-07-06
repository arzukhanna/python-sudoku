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
    Grid with incorrect dimensions
    """
    return [
        [2, 5, 4, 1, 9, 8, 3, 7, 6],
        [8, 1, 7, 4, 3, 6, 5, 2, 9],
        [9, 6, 3, 5, 2, 7, 8, 4, 1],
    ]


@pytest.fixture
def row_dup_grid():
    """
    Grid with duplicates in row
    """
    return [[6, 5, 4, 1, 9, 8, 3, 7, 6]]


@pytest.fixture
def col_dup_grid():
    """
    Grid with duplicates in column
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
def cell_has_letter_grid():
    """
    Grid with string
    """
    return [[0, 1, 2, "a", 8, 9, 0, 0, 0, 0]]


@pytest.fixture
def cell_outside_range_grid():
    """
    Grid with integer outside of range
    """
    return [[0, 1, 2, 10, 8, 9, 0, 0, 0, 0]]


def test_grid_dimension_is_valid():
    """
    Test case in which all rows are valid.
    """
    assert sudoku.dimension_is_valid(correct_grid)


def test_grid_dimension_is_invalid():
    """
    Test case in which all rows are valid.
    """
    assert sudoku.dimension_is_valid(incorrect_dim_grid)


def test_grid_rows_valid():
    """
    Test case in which at least one row is invalid.
    """
    assert sudoku.row_is_valid(correct_grid)


def test_grid_rows_duplicates_invalid():
    """
    Test case in which at least one row is invalid.
    """
    assert not sudoku.row_is_valid(row_dup_grid)


def test_column_valid():
    """
    Test case in which all columns are valid.
    """
    assert sudoku.col_is_valid(correct_grid)


def test_grid_cols_duplicates_invalid():
    """
    Test case in which all columns are valid.
    """
    assert not sudoku.col_is_valid(col_dup_grid)


def test_cell_is_valid():
    """
    Test case in which all cells are valid.
    """
    assert sudoku.cell_is_valid(correct_grid)


def test_cell_has_letter_invalid():
    """
    Test case in which letter appears in grid.
    """
    assert not sudoku.cell_is_valid(cell_has_letter_grid)


def test_cell_outside_range_invalid():
    """
    Test case in which integer outside correct range appears in grid.
    """
    assert not sudoku.cell_is_valid(cell_outside_range_grid)


def test_solved_puzzle_correctly():
    """
    Test case in which puzzle has been solved correctly.
    """
    assert sudoku.is_grid_valid(correct_grid)


if __name__ == "__main__":
    unittest.main()
