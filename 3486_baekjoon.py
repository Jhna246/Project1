import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, k = list(map(str, sys.stdin.readline().split()))
    rev_n = n[::-1]
    rev_k = k[::-1]
    sum = str(int(rev_n) + int(rev_k))
    print(int(sum[::-1]))