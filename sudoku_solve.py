
def get_constraints(board, r, c):

    used = set()

    for i in range(9):
        used.add(board[r][i])
        used.add(board[i][c])
    
    start_r, start_c = (r//3) * 3, (c//3)*3

    for i in range(3):
        for j in range(3):
            used.add(board[start_r + i][start_c+j])

    return {n for n in range(1,10)} - used

def solve_sudoku(board):
    min_choice = 10
    best_cell = None

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                choice = get_constraints(board,r,c)

                if len(choice) == 0:
                    return False

                if len(choice) < min_choice:
                    min_choice = len(choice)
                    best_cell = (r,c,choice)
        if not best_cell:
            return True

        r,c,choice = best_cell

        for val in choice:
            board[r][c] = val

            if solve_sudoku(board):
                return True
            board[r][c] = 0

if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Solved sudoku")

    if solve_sudoku(puzzle):
        for row in puzzle:
            print(row)
    else:
        print("No solution")

