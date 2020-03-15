import sys
import math

a = []
binary = str(sys.stdin.readline())
integer_val = int(binary, 2)

for i in range(len(str(integer_val))):
    a.append(integer_val % 8)
    integer_val = math.trunc(integer_val / 8)
b = list(reversed(a))

for i in b:
    print(i, end="")

