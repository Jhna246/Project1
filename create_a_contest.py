import sys

n, m = map(int, input().split())
exams = list(map(int, input().split()))
count = 0

d = {}

for i in range(n):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

while count <= m:
    if len(d.keys()) != n:
        print(0)
    elif len(d.keys()) == n:
        print(1)

        for i in d:
            if d[i] == 1:
                del d[i]
                print(d)
            else:
                d[i] -= 1


