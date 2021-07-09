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

GOOD_LIST = [0, 2, 3, 4, 5, 6, 7, 8, 9]
LIST_WITH_DUPLICATES = [6, 5, 4, 1, 9, 8, 3, 7, 6]
LIST_WITH_LETTER = [0, 1, 2, "a", 8, 9, 0, 0, 0, 0]
LIST_WITH_INTEGER_OUTSIDE_RANGE = [0, 1, 2, 10, 8, 9, 0, 0, 0, 0]


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
    assert not sudoku.no_duplicates(LIST_WITH_DUPLICATES)


def test_grid_list_cell_letter_invalid():
    """Row/Column has a letter - invalid"""
    assert not sudoku.no_letters(LIST_WITH_LETTER)


def test_grid_list_cell_outside_range_invalid():
    """Row/Column has a cell outside the range - invalid"""
    assert not sudoku.no_wrong_integers(LIST_WITH_INTEGER_OUTSIDE_RANGE)


def test_is_grid_valid():
    """Entire grid is valid"""
    assert sudoku.is_grid_valid(GOOD_GRID)


def test_possible_in_row():
    """n is a possible move in the row"""
    assert sudoku.possible_in_row(GOOD_LIST, 1)


def test_not_possible_in_row():
    """n is not a possible move in the row"""
    assert not sudoku.possible_in_row(GOOD_LIST, 2)


def test_possible_in_column():
    """n is a possible move in the column"""
    assert sudoku.possible_in_row(GOOD_LIST, 1)


def test_not_possible_in_column():
    """n is not a possible move in the column"""
    assert not sudoku.possible_in_row(GOOD_LIST, 2)


def test_possible_in_block():
    """n is a possible move in the block"""
    assert sudoku.possible_in_block(GOOD_LIST, 1)


def test_not_possible_in_block():
    """n is not a possible move in the block"""
    assert not sudoku.possible_in_block(GOOD_LIST, 2)
