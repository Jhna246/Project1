import sys

n, k = map(int, sys.stdin.readline().split())
N = sys.stdin.readline().split()
for i in range(len(N)):
    N[i] = int(N[i])
N.sort()
print(N[k-1])