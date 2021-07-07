"""
Unit tests to check functioning of Sudoku solver.
"""

from lib import sudoku
import hypothesis.strategies as st

GOOD_GRID = [
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

INCORRECT_DIMENSIONS_GRID = [
    [2, 5, 4, 1, 9, 8, 3, 7, 6],
    [8, 1, 7, 4, 3, 6, 5, 2, 9],
    [9, 6, 3, 5, 2, 7, 8, 4, 1],
]

GOOD_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_WITH_DUPLICATES = [6, 5, 4, 1, 9, 8, 3, 7, 6]
LIST_WITH_LETTER = [[0, 1, 2, "a", 8, 9, 0, 0, 0, 0]]
LIST_WITH_INTEGER_OUTSIDE_RANGE = [[0, 1, 2, 10, 8, 9, 0, 0, 0, 0]]
VALID_CELL_VALUE = 0
INVALID_CELL_VALUE_STRING = "a"
INVALID_CELL_VALUE_OUTSIDE_RANGE = 10


def test_grid_dimension_is_valid():
    """Dimensions valid"""
    assert sudoku.is_dimension_valid(GOOD_GRID)


def test_grid_dimension_is_invalid():
    """Dimensions invalid"""
    assert not sudoku.is_dimension_valid(INCORRECT_DIMENSIONS_GRID)


def test_grid_list_valid():
    """Rows and columns valid"""
    assert sudoku.is_row_valid(GOOD_LIST)
    assert sudoku.is_column_valid(GOOD_LIST)


def test_grid_list_duplicates_invalid():
    """Row/Column has duplicates - invalid"""
    assert not sudoku.is_row_valid(LIST_WITH_DUPLICATES)
    assert not sudoku.is_column_valid(LIST_WITH_DUPLICATES)


def test_grid_list_cell_letter_invalid():
    """Row/Column has a letter - invalid"""
    assert not sudoku.is_row_valid(LIST_WITH_LETTER)
    assert not sudoku.is_column_valid(LIST_WITH_LETTER)


def test_grid_list_cell_outside_range_invalid():
    """Row/Column has a cell outside the range - invalid"""
    assert not sudoku.is_row_valid(LIST_WITH_INTEGER_OUTSIDE_RANGE)
    assert not sudoku.is_column_valid(LIST_WITH_INTEGER_OUTSIDE_RANGE)


def test_cell_is_valid():
    """Cell is valid"""
    assert sudoku.is_cell_valid(VALID_CELL_VALUE)


def test_cell_has_letter_invalid():
    """Cell has invalid letter"""
    assert not sudoku.is_cell_valid(INVALID_CELL_VALUE_STRING)


def test_cell_outside_range_invalid():
    """Cell has integer outside valid range"""
    assert not sudoku.is_cell_valid(INVALID_CELL_VALUE_OUTSIDE_RANGE)


def test_solved_puzzle_correctly():
    """Puzzle solved correctly."""
    assert sudoku.is_grid_valid(GOOD_GRID)
