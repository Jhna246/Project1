import sys

first = int(sys.stdin.readline())
count = {}

for i in range(first):
    n = int(sys.stdin.readline())
    if n in count:
        count[n] += 1
    else:
        count[n] = 1




