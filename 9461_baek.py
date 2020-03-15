import sys
array = [-1] * 100
array[0] = array[1] = array[2] = 1


def p(x):
    if x < 3:
        return 1
    else:
        if array[x] > 0:
            return array[x]
        array[x] = p(x - 2) + p(x - 3)
        return array[x]


for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(p(n-1))
