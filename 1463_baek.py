import sys

n = int(sys.stdin.readline())
array = [0 for i in range(n+1)]

array[0] = 0
array[1] = 0

for i in range(2, n + 1):
    if i % 3 == 0 and i % 2 == 0:
        array[i] = min(array[i // 3], array[i // 2]) + 1
    elif i % 3 == 0 and i % 2 != 0:
        # see if n - 1 is faster than n // 3
        array[i] = min(array[i // 3], array[i - 1]) + 1
    elif i % 3 != 0 and i % 2 == 0:
        # see if n - 1 result is faster than n // 2
        array[i] = min(array[i // 2], array[i - 1]) + 1

    else:
        array[i] = array[i - 1] + 1

print(array[n])