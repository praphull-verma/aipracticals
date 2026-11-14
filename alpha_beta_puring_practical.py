
import math

# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Alpha-Beta Pruning function
def alphabeta(depth, nodeIndex, maxPlayer, values, alpha, beta):

    # Base case: Leaf node reached
    if depth == 3:
        return values[nodeIndex]

    # MAX player's turn
    if maxPlayer:
        best = -math.inf

        for i in range(2):
            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if alpha >= beta:
                print("Pruning at MAX node")
                break

        return best

    # MIN player's turn
    else:
        best = math.inf

        for i in range(2):
            val = alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if alpha >= beta:
                print("Pruning at MIN node")
                break

        return best


# Driver code
print("Leaf Node Values:", values)

result = alphabeta(
    depth=0,
    nodeIndex=0,
    maxPlayer=True,
    values=values,
    alpha=-math.inf,
    beta=math.inf
)

print("\nOptimal Value:", result)

print("\nLogic:")
print("Alpha stores the best value found by MAX.")
print("Beta stores the best value found by MIN.")
print("Whenever alpha >= beta, remaining branches are pruned.")
print("This reduces node evaluations without changing the")
print("optimal result.")

