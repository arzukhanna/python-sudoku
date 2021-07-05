"""
Library program to solve Sudoku puzzles.
Author: Arzu Khanna
Created: 30.06.2021
Modified: 2.07.2021
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


def dim_val(grid):
    """
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if dimensions are valid, FALSE otherwise.
    """
    if len(grid) != 9:
        return False
    for row in grid:
        if len(row) != 9:
            return False
    return True


def row_val(grid):
    """
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if row is valid, FALSE otherwise.
    """
    for row in grid:
        if len(row) == len(set(row)):
            return False
    return True


def col_val(grid):
    """
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if column is valid, FALSE otherwise.
    """
    grid = numpy.transpose(grid)
    return row_val(grid)


def cell_val(grid):
    """
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if cell is valid, FALSE otherwise.
    """
    for row in grid:
        for i in row:
            try:
                if not 0 <= i <= 9:
                    return False
            # if i is not an integer then a TypeError will arise, return False
            except TypeError:
                return False
    return True


def is_grid_valid(grid):
    """
    :param grid: List of lists representing sudoku puzzle.
    :return: TRUE if grid is valid, FALSE otherwise.
    """
    return all([dim_val(grid), row_val(grid), col_val(grid), cell_val(grid)])


def possible(grid, _y, _x, _n):
    """
    Function: Determines whether inputting n in a particular cell (grid[y][x])
    is possible according to sudoku rules.
    :param grid: The current state of sudoku puzzle.
    :param _y: Row
    :param _x: Column
    :param _n: Number in cell
    :return: TRUE if possible for n to go in cell, FALSE otherwise.
    """
    for i in range(9):
        if grid[_y][i] == _n:
            return False
    for i in range(9):
        if grid[i][_x] == _n:
            return False
    _x0 = (_x // 3) * 3
    _y0 = (_y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[_y0 + i][_x0 + j] == _n:
                return False
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
