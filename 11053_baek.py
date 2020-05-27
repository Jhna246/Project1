import sys

first = int(sys.stdin.readline())

dp = []

value = [int(i) for i in sys.stdin.readline().rstrip().split()]

# see if the value
for i in range(len(value)):
    temp_value = value[i]
    if value[i] not in dp:
        dp.append(temp_value)

print(len(dp))