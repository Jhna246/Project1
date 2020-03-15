import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(int(sys.stdin.readline())):
    x = list(map(int, sys.stdin.readline().split()))
    s = 0
    y = []
    for p in range(x[0]):
        y.append(x[p+1])
    for j in range(x[0]):
        for k in range(x[0]):
            if (y[j], y[k]) == (y[k], y[j]):
                j += 1
                k += 1
            else:
                s += gcd(y[j], y[k])
    sys.stdout.write(str(s) + '\n')
