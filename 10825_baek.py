import sys
import functools

i = 0
c = []
order = 0

first = int(sys.stdin.readline())

# name, korean, english, math
def compare(item1, item2):
    if item1[1] == item2[1]:
        if item1[2] == item2[2]:
            if item1[3] == item2[3]:
                if item1[0] < item2[0]:
                    return -1
                else:
                    return 1
            else:
                return item2[3] - item1[3]
        else:
            return item1[2] - item2[2]
    else:
        return item2[1] - item1[1]


for i in range(first):
    x, y, z, a = sys.stdin.readline().split()

    b = [str(x), int(y), int(z), int(a)]
    c.append(b)

for i in sorted(c, key = functools.cmp_to_key(compare)):
    print(i[0])