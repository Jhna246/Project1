import sys

t = int(sys.stdin.readline())
matrix = ([list(map(int, sys.stdin.readline().split())) for i in range(t)])

matrix.sort(key=lambda x: (x[1], x[0]))

answer, end = 0, 0
for m in matrix:
    if end <= m[0]:
        end = m[1]
        answer += 1

print(answer)