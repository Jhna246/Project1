import sys

n = int(sys.stdin.readline())
array = [0, 1, 2]
for i in range(3, 1001):
    array.append(array[i-2] + array[i-1])
print(array[n] % 10007)
print(array)
