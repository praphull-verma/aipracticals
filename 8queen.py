
n = 8

board = [-1] * n

def solve(r):

    if r == n:

        return True

    for c in range(n):
        if all(board[i] != c and abs(board[i] - c) != r - i for i in range(r)):
            board[r] = c
            if solve(r+1):
                return True

        
    return False

solve(0)

for r in range(n):
    for c in range(n):

        if board[r] == c:
            print("Q", end=' ')
        else:
            print(".", end=' ')
    print()

