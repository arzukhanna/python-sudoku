# PYTHON SUDOKU

This program solves any problem to the [Sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku).

## Input

A text file with a grid representing the sudoku puzzle to be solved.

### Grid

A valid grid is one that:

* Contains a total of 81 integers in a 9x9 grid format
* Integers represent a cell and must be in range `0` to `9`
    * `0` - represents an empty cell that needs to be solved
    * `1` to `9` - are cells that have been solved and must not change
* Each row of the grid starts on a new line
* There are no duplicate integers in any row, column or 3x3 cell

#### Example Easy Puzzle

Source: [data/easy.txt](data/easy.txt)

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

Solved sudoku puzzles with same dimensions as input with all `0`'s replaced with integers in range from `1` to `9`.

#### Example Solved Puzzle

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

To specify the versions of the packages used, we set up a virtual environment for the project. This allows the project
to be replicated without any dependency conflicts.

### Setup

| Command | Description |
| --------|-------------|
|`pip3 install -U virtualenv`| Install virtualenv |
|`python3 -m virtualenv venv`| Install virtualenv |
|`virtual venv`              | Initialises a virtual environment (creates folder called venv)|
|`source venv/bin/activate`  | Start the virtual environment|
|`pip3 install -U -r requirements.txt`| From requirements.txt, installs all relevant dependencies to run program|
|`pip list` |Shows all packages installed in the environment|
|`deactivate` | Takes you out of the virtual environment and into the global environment|

### Set Version of Python

Command:

```bash
virtualenv --python=<path to python 3.9> <path/to/virtualenv/>
```

To check versions being used:

```bash
python3 --version
env/bin/python --version
```

#### IDE should be set with correct venv

Must ensure that the IDE is set with the appropriate venv, otherwise 
false positives may occur where the IDE cannot run correctly - but 
running `make` in the command line does. 

Check the IDE venv by looking at the `python interpreter`.

## Makefile

Makefiles are special format files that help build and manage projects automatically through use of `make`. The makefile
used specifies the virtual environment set-up process which can be accessed using `make help`. The tools below are
automatically run when the `make` command is run.

Source: [Make Guidelines](https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make)

### Make Components

| Tool | Description |
| --------|-------------|
| [isort](https://pycqa.github.io/isort/) | Sorts Inputs |
| [black](https://pypi.org/project/black/) | Format the Code |
| [flake8](https://pypi.org/project/flake8/) | Style Checks |
| [pylint](https://pypi.org/project/pylint/) | Static Code Checks |
| [pytest](https://pypi.org/project/pylint/) | Unit Testing Framework |

## Unit Testing

- [ ] TODO What tools are we using
- [ ] TODO Example run

## Pipelines

### GitLab Pipelines

A pipeline is declared using a YAML file, [.gitlab-ci.yml](.gitlab-ci.yml).

A pipeline is comprised of:

* Jobs: Define what and how to run.
* Stages: Define when to run the jobs.

To configuring a pipeline:

* Add a YAML file called [.gitlab-ci.yml](.gitlab-ci.yml) to the project.
* The YAML file will dictate the structure, and order of execution of the pipeline.
* When a `push` is made to the `origin` and GitLab finds a `.gitlab-ci.yml` file inside the repository root a Pipeline
  starts building automatically.

### Job Keywords used

| Keyword | Description |
| --------|-------------|
| [before_script](https://docs.gitlab.com/ee/ci/yaml/#before_script) | Override a set of commands that are executed before job |
| [cache](https://docs.gitlab.com/ee/ci/yaml/#cache) | List of files that should be cached between subsequent runs |
| [image](https://docs.gitlab.com/ee/ci/yaml/#image) | Use Docker images |
| [stage](https://docs.gitlab.com/ee/ci/yaml/#stage) | Defines a job stage (E.g., build) |
| [variables](https://docs.gitlab.com/ee/ci/yaml/#variables) | Define job variables on a job level |

### GitHub Pipelines

- [ ] TODO

## Requirements

* [Package Versions Required](requirements.txt)

## References

* [Sudoku Code](https://www.youtube.com/watch?v=G_UYXzGuqvM)
* [How to create a Virtual Environment](https://www.youtube.com/watch?v=N5vscPTWKOk)
* [Make Guidelines](https://interrupt.memfault.com/blog/gnu-make-guidelines#when-to-choose-make)
* [GitLab Pipelines](https://docs.gitlab.com/ee/ci/yaml/)
