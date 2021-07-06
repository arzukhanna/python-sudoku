"""
Unit tests to check functioning of Sudoku solver.
"""

from lib import sudoku

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

ROW_WITH_DUPLICATES_GRID = [[6, 5, 4, 1, 9, 8, 3, 7, 6]]

COLUMN_WITH_DUPLICATES_GRID = [
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

CELL_HAS_LETTER_GRID = [[0, 1, 2, "a", 8, 9, 0, 0, 0, 0]]

CELL_OUTSIDE_RANGE_GRID = [[0, 1, 2, 10, 8, 9, 0, 0, 0, 0]]


def test_grid_dimension_is_valid():
    """Test case in which all rows are valid."""
    assert sudoku.is_dimension_valid(GOOD_GRID)


def test_grid_dimension_is_invalid():
    """Test case in which all rows are valid."""
    assert not sudoku.is_dimension_valid(INCORRECT_DIMENSIONS_GRID)


def test_grid_rows_valid():
    """Test case in which at least one row is invalid."""
    assert sudoku.is_row_valid(GOOD_GRID)


def test_grid_rows_duplicates_invalid():
    """Test case in which at least one row is invalid."""
    assert not sudoku.is_row_valid(ROW_WITH_DUPLICATES_GRID)


def test_column_valid():
    """Test case in which all columns are valid."""
    assert sudoku.is_column_valid(GOOD_GRID)


def test_grid_cols_duplicates_invalid():
    """Test case in which all columns are valid."""
    assert not sudoku.is_column_valid(COLUMN_WITH_DUPLICATES_GRID)


def test_cell_is_valid():
    """Test case in which all cells are valid."""
    assert sudoku.is_cell_valid(GOOD_GRID)


def test_cell_has_letter_invalid():
    """Test case in which letter appears in grid."""
    assert not sudoku.is_cell_valid(CELL_HAS_LETTER_GRID)


def test_cell_outside_range_invalid():
    """Test case in which integer outside correct range appears in grid."""
    assert not sudoku.is_cell_valid(CELL_OUTSIDE_RANGE_GRID)


def test_solved_puzzle_correctly():
    """Test case in which puzzle has been solved correctly."""
    assert sudoku.is_grid_valid(GOOD_GRID)
