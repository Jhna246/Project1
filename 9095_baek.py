import sys

array = [-1] * 12
array[0] = 0
array[1] = 1
array[2] = 2
array[3] = 4


def p(x):
    if array[x] > 0:
        return array[x]
    array[x] = p(x-1) + p(x-2) + p(x-3)
    return array[x]


first = int(sys.stdin.readline())
for i in range(first):
    n = int(sys.stdin.readline())
    print(p(n))
