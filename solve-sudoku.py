from lib.sudoku import solve_sudoku, read_grid, is_grid_valid
import argparse
import sys

if __name__ == "__main__":

    __version__ = '0.1.0'

    parser = argparse.ArgumentParser(description='Solve 9x9 sudoku puzzle',
                                     epilog='© 2021 Arzu Khanna mailto:arzukhanna@marlo.com')

    parser.add_argument('-p', '--puzzle',
                        type=argparse.FileType('r', encoding='utf-8'),
                        help='file that contains sudoku puzzle as grid')

    parser.add_argument('--version',
                        action='version',
                        version=__version__)

    args = parser.parse_args()

    grid = read_grid(args.puzzle)

    if is_grid_valid(grid):
        print(solve_sudoku(grid))
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)
