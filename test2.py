import sys
import functools

i = 0
a = []

first = int(sys.stdin.readline())


def compare(item1, item2):
    if item1[0] == item2[0]:
        return item1[1] - item2[1]
    else:
        return item1[0] - item2[0]


for i in range(first):
    x, y = sys.stdin.readline().split()
    b = [int(x), int(y)]
    a.append(b)

for i in sorted(a, key = functools.cmp_to_key(compare)):
    print(i[0],i[1])