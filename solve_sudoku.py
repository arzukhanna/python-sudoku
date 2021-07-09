#!/usr/bin/env python
"""
Main Program to solve Sudoku Puzzles.
Author: Arzu Khanna
"""

import argparse
import logging
import sys

import numpy

from lib.sudoku import is_grid_valid, read_grid, solve_puzzle

if __name__ == "__main__":

    __version__ = "0.1.0"

    parser = argparse.ArgumentParser(
        description="Solve 9x9 sudoku puzzle",
        epilog="© 2021 Arzu Khanna mailto:arzukhanna@marlo.com",
    )

    parser.add_argument(
        "puzzle",
        type=argparse.FileType("r", encoding="utf-8"),
        help="file that contains sudoku puzzle as grid",
    )

    parser.add_argument("--version", action="version", version=__version__)

    parser.add_argument("-v", "--verbose", help="verbose", action="count")

    args = parser.parse_args()
    prog = parser.prog
    verbose = args.verbose

    grid = read_grid(args.puzzle)

    logging.basicConfig(
        filename="test.log",
        filemode="w",
        format="%(asctime)s:%(levelname)s:%(message)s",
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    if verbose:
        logger.setLevel(logging.DEBUG)

    logger.debug("prog ........................: %s", prog)
    logger.debug("verbose .....................: %s", verbose)
    logger.debug("version .....................: %s", __version__)

    if is_grid_valid(grid):
        if solve_puzzle(grid):
            print(numpy.matrix(grid))
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)
