# python-sudoku

What you need to learn about GitLab Markdown.

* headings (levels)
* links to code
* embed images
* lists
* format inline code

---

## Aim: 

To create a solution to the sudoku puzzle.

## Inputs:

Text file with a grid representing the sudoku puzzle to be solved.

**Input Grid requirements:**
(These requirements must be tested for using a helper function)

* Grid containing a total of 81 integers in a 9x9 format
* Integers must be in range [0...9] 
* Integers on each row separated by spaces
* Each row starts on a new line

## Output:

Solved sudoku puzzle in a grid format (same as imput) with all 0's replaced with integers in range [1...9].

## Sample sudoku problem:

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

## Requirements / Dependencies 

### How to create:

`virtualenv`

`source venv/bin/activate`

`pip freeze --local > requirements.txt`

`pip list` shows all packages installed in the environment.

`deactivate` takes you out of virtual environment into global environment.

### Dependencies:

[Link to dependencies](requirements.txt)

## References

* sudoku code: https://www.youtube.com/watch?v=G_UYXzGuqvM
* virtualenv: https://www.youtube.com/watch?v=N5vscPTWKOk


