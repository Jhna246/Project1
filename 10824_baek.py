import sys

a, b, c, d = sys.stdin.readline().split()
pt1 = sum([int(a), int(c)])
pt2 = sum([int(b), int(d)])
print(pt1, pt2, sep='')