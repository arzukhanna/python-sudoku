# PYTHON SUDOKU

This program solves any problem to the sudoku puzzle.

## Inputs

Text file with a grid representing the sudoku puzzle to be solved.

### Input Grid requirements
(These requirements must be tested for using a helper function)

* Grid containing a total of 81 integers in a 9x9 format
* Integers must be in range `[0...9]` 
  * `0` - Empty cell that needs to be solved
  * `[1...9]` - Cells that are already solved and must not be changed
* Each row starts on a new line
* No duplicate integers in any row, column or 3x3 cell 

## Output

Solved sudoku puzzle with same dimensions as input with all 0's replaced with integers in range `[1...9]`.

## Sample sudoku problem

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## Virtual Environment

To specify the versions of the packages used, we set up a virtual environment for the project.
This allows the project to be replicated without any dependency conflicts.

### Setting Up Venv

| Command | Description |
| --------|-------------|
|`pip3 install -U virtualenv`| Install virtualenv |
|`python3 -m virtualenv venv`| Install virtualenv |   
|`virtual venv`              | Initialises a virtual environment (creates folder called venv)|
|`source venv/bin/activate`  | Start the virtual environment|
|`pip3 install -U -r requirements.txt`| From requirements.txt, installs all relevant dependencies to run program|
|`pip list` |Shows all packages installed in the environment|
|`deactivate` | Takes you out of the virtual environment and into the global environment|

### Updating Python version used in venv

Command:
```virtualenv --python=<path to python 3.9> <path/to/virtualenv/>```

To check versions being used:
```python3 --version```
```env/bin/python --version```

## Makefile

Makefiles are special format files that help build and manage projects automatically through use of `make`.
The makefile used specifies the virtual environment set-up process which can be accessed using `make help`.
The below tools are automatically run when the `make` command is run.

### Make Components

| Tool | Description |
| --------|-------------|
|`isort`| Sorts Inputs |
|`black `| Format the Code |   
|`flake8`| Style Checks|
|`pylint` | Static Code Checks|
|`pytest`| Unit Testing Framework|

## Requirements

[Package Versions Required](requirements.txt)

## References

* [Sudoku Code](https://www.youtube.com/watch?v=G_UYXzGuqvM)
* [How to create a Virtual Environment](https://www.youtube.com/watch?v=N5vscPTWKOk)
* [Pytest Fixtures](https://docs.pytest.org/en/6.2.x/fixture.html#fixtures-are-reusable)
* [Make Guidelines](https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make)
