from lib.sudoku import possible, solve_sudoku
import argparse
import sys
import os.path

if __name__ == "__main__":

    __version__ = '3.8.3'

    parser = argparse.ArgumentParser(description='Solve 9x9 sudoku puzzle')

    parser.add_argument('infile',
                        nargs='?',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='file that contains sudoku puzzle as grid')

    parser.add_argument('--version',
                        action='version',
                        version='<the version>')

    args = parser.parse_args()

    grid = []
    for f in args.file:
        a_list = parser.convert_arg_line_to_args(f)
        map_object = map(int, a_list)
        list_ints = list(map_object)
        grid.append(list_ints)
    solution = solve_sudoku(grid)
    print(solution)

    # grid = []
    # file = open('medium.txt', 'r')
    # for line in file:
    #     line = line.strip('\n')
    #     a_list = line.split()
    #     map_object = map(int, a_list)
    #     list_ints = list(map_object)
    #     grid.append(list_ints)
    # solution = solve_sudoku(grid)
    # print(solution)
