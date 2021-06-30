from lib.sudoku import solve_sudoku

if __name__ == "__main__":
    grid = []
    file = open('sudoku_sample.txt', 'r')
    for line in file:
        line = line.strip('\n')
        a_list = line.split()
        map_object = map(int, a_list)
        list_ints = list(map_object)
        grid.append(list_ints)
    solution = solve_sudoku(grid)
    print(solution)




