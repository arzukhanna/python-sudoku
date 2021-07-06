"""
Library program to solve Sudoku puzzles.
Author: Arzu Khanna
"""

import numpy


def read_grid(file):
    """
    :param file: File containing sudoku puzzle to be solved.
    :return: List of lists representing sudoku puzzle.
    """
    grid = []
    for line in file:
        grid.append([int(n) for n in line.split()])
    return grid


def is_dimension_valid(grid):
    """
    :return: TRUE if dimensions are valid, FALSE otherwise. To be valid,
    the grid has to be a 2 dimensional array with 9 rows and 9 columns.
    :param grid: List of lists representing sudoku puzzle.
    """
    if len(grid) != 9:
        return False
    for row in grid:
        if len(row) != 9:
            return False
    return True


def is_row_valid(grid):
    """
    :return: TRUE if row is valid, FALSE otherwise. To be valid, the
    row should not contain duplicates of integers other than 0.
    :param grid: List of lists representing sudoku puzzle.
    """
    for row in grid:
        numbers_in_row = []
        for i in row:
            if i != 0:
                numbers_in_row.append(i)
        if len(numbers_in_row) != len(set(numbers_in_row)):
            return False
    return True


def is_column_valid(grid):
    """
    :return: TRUE if column is valid, FALSE otherwise. To be valid,
    the column should not contain duplicates of integers other than 0.
    :param grid: List of lists representing sudoku puzzle.
    """
    grid = numpy.transpose(grid)
    return is_row_valid(grid)


def is_cell_valid(grid):
    """
    :return: TRUE if cell is valid, FALSE otherwise. To be valid, the
    cells should only be integers in the range [0...9] where 0 represents
    a cell that still needs to be solved (is empty), while the other cells
    have already been solved.
    :param grid: List of lists representing sudoku puzzle.
    """
    for row in grid:
        for i in row:
            if not isinstance(i, int):
                return False
            if not 0 <= i <= 9:
                return False
    return True


def is_grid_valid(grid):
    """
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if grid is valid, FALSE otherwise.
    """
    return all(
        [
            is_dimension_valid(grid),
            is_row_valid(grid),
            is_column_valid(grid),
            is_cell_valid(grid),
        ]
    )


def possible(grid, _y: int, _x: int, _n: int):
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
            return False

    # 2. Check if _n is already in column _x
    for i in range(9):
        if grid[i][_x] == _n:
            return False

    # 3. Check if _n is already in 3x3 block
    _x0 = (_x // 3) * 3
    _y0 = (_y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[_y0 + i][_x0 + j] == _n:
                return False

    # If _n is not in row _y, column _x, or 3x3 block where grid[_y][_x],
    # then the move is possible and return True.
    return True


def next_empty(grid):
    """
    Function: Iterates through the cells in the puzzle to find the
    next empty cell which needs to be solved.
    :param grid: current state of sudoku puzzle
    """
    for _y in range(9):
        for _x in range(9):
            if grid[_y][_x] == 0:
                return _y, _x
    return None, None


def solve_puzzle(grid):
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
