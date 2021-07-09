"""
Library program to solve Sudoku puzzles.
Author: Arzu Khanna
"""

# pylint: disable = R1729

import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def read_grid(file: str) -> list:
    """
    :param file: File containing sudoku puzzle to be solved.
    :return: List of lists representing sudoku puzzle.
    """
    grid = []
    for line in file:
        grid.append([int(n) for n in line.split()])
    return grid


def is_dimension_valid(grid: list) -> bool:
    """
    To have valid dimensions, the grid has to be a 2 dimensional array
    with 9 rows and 9 columns.
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if dimensions are valid, FALSE otherwise.
    """
    if len(grid) != 9:
        log.debug("Dimensions invalid, number of rows....:%s", len(grid))
        return False
    for row in grid:
        if len(row) != 9:
            log.debug("Dimensions invalid, number of columns....:%s", len(row))
            return False
    log.debug("Dimensions are valid, 9x9 grid")
    return True


def no_duplicates(row: list) -> bool:
    """Check row has no duplicates."""
    _row = [i for i in row if i != 0]
    duplicates = len(set(_row)) != len(_row)
    log.debug("No duplicates in row/column...%s", not duplicates)
    return not duplicates


def no_letters(row: list) -> bool:
    """Check does row have letter"""
    no_letter = all(isinstance(i, int) for i in row)
    log.debug("No letters in row/column...%s", no_letter)
    return no_letter


def no_wrong_integers(row: list) -> bool:
    """Check does cell have integer out of correct range"""
    no_wrong_integer = all(0 <= i <= 9 for i in row)
    log.debug("No wrong integers in row/column...%s", no_wrong_integer)
    return no_wrong_integer


def is_row_valid(row: list) -> bool:
    """
    For a row to be valid, it should not contain duplicates of integers
    other than 0 and all cell values should be valid (see is_cell_valid).
    :param row: Row in the sudoku puzzle.
    :return: TRUE if row is valid, FALSE otherwise.
    """
    valid = all([no_duplicates(row), no_letters(row), no_wrong_integers(row)])
    log.debug("Row/column is valid...%s", valid)
    return valid


def is_column_valid(column: list) -> bool:
    """
    For a column to be valid, it should not contain duplicates of integers
    other than 0 and all cell values should be valid (see is_cell_valid).
    :param column: Column in the sudoku puzzle.
    :return: TRUE if column is valid, FALSE otherwise.
    """
    return is_row_valid(column)


def is_grid_valid(grid: list) -> bool:
    """
    The grid is valid if it satisfies all other functions ending in _is_valid.
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if grid is valid, FALSE otherwise.
    """
    # 1. Check if dimensions of grid are valid
    if not is_dimension_valid(grid):
        return False

    # 2. Iterate through all rows to check if valid
    for row in grid:
        if not is_row_valid(row):
            return False

    # 3. Iterate through all columns to check if valid
    # Transpose grid so that columns can be treated as rows.
    transposed_grid = map(list, zip(*grid))
    for column in transposed_grid:
        if not is_column_valid(column):
            return False

    log.debug("Entire grid is valid!")
    return True


def possible(grid, _y: int, _x: int, _n: int) -> bool:
    """
    Function: Determines whether inputting n in a particular cell (grid[y][x])
    is possible according to sudoku rules.
    :param grid: The current state of sudoku puzzle.
    :param _y: Row
    :param _x: Column
    :param _n: Number in cell
    :return: TRUE if possible for n to go in cell, FALSE otherwise.
    """
    # 1. Check if _n is already in row _y
    for i in range(9):
        if grid[_y][i] == _n:
            log.debug("_n is already in current row - not a possible move")
            return False

    # 2. Check if _n is already in column _x
    for i in range(9):
        if grid[i][_x] == _n:
            log.debug("_n is already in current column - not a possible move")
            return False

    # 3. Check if _n is already in 3x3 block
    _x0 = (_x // 3) * 3
    _y0 = (_y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[_y0 + i][_x0 + j] == _n:
                log.debug("_n is already in current block - not possible move")
                return False

    # If _n is not in row _y, column _x, or 3x3 block where grid[_y][_x],
    # then the move is possible and return True.
    log.debug("Placing _n is a possible move!")
    return True


def next_empty(grid: list) -> (int, int):
    """
    Function: Iterates through the cells in the puzzle to find the
    next empty cell which needs to be solved.
    :param grid: current state of sudoku puzzle
    """
    for _y in range(9):
        for _x in range(9):
            if grid[_y][_x] == 0:
                log.debug("Next empty cell...%s", [_y][_x])
                return _y, _x
    log.debug("There are no more empty cells to fill!")
    return None, None


def solve_puzzle(grid: list) -> bool:
    """
    Function: Solve the sudoku puzzle
    :param grid: current state of sudoku puzzle
    """
    _y, _x = next_empty(grid)

    if _y is None:
        return True

    for _n in range(1, 10):
        if possible(grid, _y, _x, _n):
            grid[_y][_x] = _n
            if solve_puzzle(grid):
                return True

        grid[_y][_x] = 0

    return False
