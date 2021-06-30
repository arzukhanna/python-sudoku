import numpy


def possible(grid, y, x, n):
    """
    :param y: row
    :param x: column
    :param n: number in cell
    :return: TRUE if possible for nn to go in cell, FALSE otherwise
    """
    # global grid
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
    #global grid
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
