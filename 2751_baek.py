import sys

i = 0
a = []

first = int(sys.stdin.readline())

for i in range(first):
    N = sys.stdin.readline()
    a.append(int(N))

sort_numbers = sorted(a)

for i in sort_numbers:
    sys.stdout.write(str(i) +'\n')