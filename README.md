# PYTHON SUDOKU

This program solves any problem to the sudoku puzzle.

## Inputs

Text file with a grid representing the sudoku puzzle to be solved.

### Input Grid requirements

(These requirements are tested using all functions ending in `_is_valid`).

* Grid containing a total of 81 integers in a 9x9 format
* Integers must be in range `[0...9]`
  * `0` - Empty cell that needs to be solved
  * `[1...9]` - Cells that are already solved and must not be changed
* Each row starts on a new line
* No duplicate integers in any row, column or 3x3 cell

#### Sample Input ([data/easy.txt](data/easy.txt))

```text
0 2 0 3 5 0 0 8 4
0 0 0 4 6 0 0 5 7
0 0 0 2 0 7 0 1 0
0 0 5 0 4 0 8 0 2
0 6 9 0 2 8 0 0 0
0 0 8 0 0 0 1 0 6
7 3 0 8 0 5 4 2 0
9 0 0 7 3 0 0 6 1
0 5 0 0 9 2 0 0 8
```

## Output

Solved sudoku puzzles with same dimensions as input with all 0's replaced with
integers in range `[1...9]`.

#### Sample Output

```bash
python3 solve_sudoku.py -p data/easy.txt

[[6 2 7 3 5 1 9 8 4]
 [8 1 3 4 6 9 2 5 7]
 [5 9 4 2 8 7 6 1 3]
 [1 7 5 9 4 6 8 3 2]
 [3 6 9 1 2 8 7 4 5]
 [2 4 8 5 7 3 1 9 6]
 [7 3 6 8 1 5 4 2 9]
 [9 8 2 7 3 4 5 6 1]
 [4 5 1 6 9 2 3 7 8]]
 ```



## Virtual Environment

To specify the versions of the packages used, we set up a virtual environment
for the project. This allows the project to be replicated without any dependency
  conflicts.

### Setting Up Virtual Environment

| Command | Description |
| --------|-------------|
|`pip3 install -U virtualenv`| Install virtualenv |
|`python3 -m virtualenv venv`| Install virtualenv |
|`virtual venv`              | Initialises a virtual environment (creates folder called venv)|
|`source venv/bin/activate`  | Start the virtual environment|
|`pip3 install -U -r requirements.txt`| From requirements.txt, installs all relevant dependencies to run program|
|`pip list` |Shows all packages installed in the environment|
|`deactivate` | Takes you out of the virtual environment and into the global environment|

### Updating Python version used in Virtual Environment

Command:

```bash
virtualenv --python=<path to python 3.9> <path/to/virtualenv/>
```

To check versions being used:

```bash
python3 --version
env/bin/python --version
```

## Makefile

Makefiles are special format files that help build and manage projects
automatically through use of `make`. The makefile used specifies the virtual
environment set-up process which can be accessed using `make help`. The below
tools are automatically run when the `make` command is run.

### Make Components

| Tool | Description |
| --------|-------------|
| [isort](https://pycqa.github.io/isort/) | Sorts Inputs |
| [black](https://pypi.org/project/black/) | Format the Code |
| [flake8](https://pypi.org/project/flake8/) | Style Checks |
| [pylint](https://pypi.org/project/pylint/) | Static Code Checks |
| [pytest](https://pypi.org/project/pylint/) | Unit Testing Framework |

## Requirements

* [Package Versions Required](requirements.txt)

## References

* [Sudoku Code](https://www.youtube.com/watch?v=G_UYXzGuqvM)
* [How to create a Virtual Environment](https://www.youtube.com/watch?v=N5vscPTWKOk)
* [Make Guidelines](https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make)
