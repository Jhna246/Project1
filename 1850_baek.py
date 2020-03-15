import sys


def gcd(a, b):
    if b == 0:
        for i in range(a):
            print("1", end='')
    else:
        return gcd(b, a % b)


a, b = map(int, sys.stdin.readline().split())

gcd(a, b)
