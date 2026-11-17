
visited = set()

def dfs(small, big):
    if (small, big) in visited:
        return False

    visited.add((small, big))
    print((small, big))

    if (small, big) == (0, 1):
        return True

    states = [
        (0, big), (small, 0), (3, big), (small, 5),
        (small-min(small, 5-big), big+min(small, 5-big)),
        (small+min(big, 3-small), big-min(big, 3-small))
    ]

    for x, y in states:
        if dfs(x, y):
            return True

    return False

dfs(0, 0)

