import numpy


def read_grid(file):
    """
    :param file: file containing sudoku puzzle to be solved
    :return: list of lists representing sudoku puzzle
    """
    grid = []
    file = open(file, 'r', encoding='utf-8')
    for line in file:
        grid.append([int(n) for n in line.split()])


def is_grid_valid(grid):
    """
    :param grid: list of lists representing sudoku puzzle
    :return: TRUE if grid is valid, FALSE otherwise
    """
    # 1. Check there are 9 rows
    if len(grid) != 9:
        return False

    # 2. Check all rows have 9 numbers
    for row in grid:
        if len(grid[row]) != 9:
            return False

    # 3. Check that grid contains only integers in range [0...9]
    for row in grid:
        for i in row:
            try:
                if not (0 <= i <= 9):
                    return False
            # if i is not an integer then a TypeError will arise, return False
            except TypeError:
                return False
    return True


def possible(grid, y, x, n):
    """
    function: determines whether inputting n in a particular cell (grid[y][x]) is possible according to sudoku rules
    :param grid: current state of sudoku puzzle
    :param y: row
    :param x: column
    :param n: number in cell
    :return: TRUE if possible for n to go in cell, FALSE otherwise
    """
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve_sudoku(grid):
    """
    function: iterates through each cell in the puzzle to determine which cells need to be solved
    :param grid: current state of sudoku puzzle
    """
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, y, x, n):
                        grid[y][x] = n
                        solve_sudoku(grid)
                        grid[y][x] = 0  # back-tracking (re-set cell if we reach dead-end)
                return
    return numpy.matrix(grid)
