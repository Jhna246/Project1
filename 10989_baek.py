import sys

a = [0] * 10001
for i in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    a[N] += 1

for i in range(len(a)):
    for j in range(a[i]):
        sys.stdout.write(str(i) + '\n')
