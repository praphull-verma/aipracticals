import math

def check_game_over(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Tie'
    return None

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    result = check_game_over(board)
    
    if result == 'X': return 10 - depth
    if result == 'O': return depth - 10
    if result == 'Tie': return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                
                if beta <= alpha:
                    break 
        return max_eval

    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                
                if beta <= alpha:
                    break 
        return min_eval
