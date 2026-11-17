
def minmax(n, turn):
    if n <= 0:
        return -1 if turn else 1

    if turn:
        return max(minmax(n-1, False), minmax(n-2, False))
    else:
        return min(minmax(n-1, True), minmax(n-2, True))

print(minmax(4, True))
