import sys


def bellman(field):
    dist[0] = 0
    asdf = False
    for i in range(field):
        asdf = False
        for j in range(field):
            for a, b in value[j]:
                if dist[j] + b < dist[a]:
                    asdf = True
                    dist[a] = dist[j] + b
        if not asdf:
            break
    print(dist)
    if asdf:
        print('YES')
        return
    print('NO')
    return


f = int(sys.stdin.readline())
for _ in range(f):
    # N fields, M paths, and W wormholes
    n, m, w = map(int, sys.stdin.readline().split())
    value = [[] for _ in range(n + 1)]
    dist = [1e9] * n
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        value[s - 1].append((e - 1, t))
        value[e - 1].append((s - 1, t))
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        value[s - 1].append((e - 1, -t))
    bellman(n)
