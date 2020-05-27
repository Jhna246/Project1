import sys

t = int(sys.stdin.readline())
all_visited = (1 << t) - 1  # all cities have been visited
mat = []
dp = [[0 for j in range(t)] for i in range(1 << t)]
for i in range(t):
    mat.append(list(map(int, sys.stdin.readline().split())))


def f(mask, path):
    # if all paths are visited
    # print(mask)
    if mask == all_visited:
        if not mat[path][0]:
            return 1e9
        else:
            return mat[path][0]
    if dp[mask][path]:
        return dp[mask][path]

    # visit all unvisited cities
    ans = 1e9
    for i in range(1, t):
        # print(mask & (1 << i), mat[path][i], 'test')
        # print(path, 'path')
        if not mask & (1 << i) and mat[path][i] != 0:
            # print(mat[path][i])
            # print(f(mask | (1 << i), i), 'test')
            ans = min(ans, mat[path][i] + f(mask | (1 << i), i))    # ex. 0001 or 0010 = 0011
            # print(ans)
    dp[mask][path] = ans
    # print(ans)
    return ans


print(f(1, 0))
# print(dp)