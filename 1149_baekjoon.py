import sys

t = int(sys.stdin.readline())
arr = []
for i in range(t):
    arr.append(list(map(int, sys.stdin.readline().split())))
# [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
for i in range(1, len(arr)):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

print(min(min(arr[len(arr) - 1][0], arr[len(arr) - 1][1]), arr[len(arr) - 1][2]))