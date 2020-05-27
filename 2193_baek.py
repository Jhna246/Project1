import sys

# N = 1-> 1
# N = 2 -> 10
# N = 3 -> 100, 101
# N = 4 -> 1000, 1001, 1010
# N = 5 -> 10000, 10001, 10010, 10100, 10101,
# so from this, I can assume that list[N] = list[N-1] + list[N-2]

n = int(sys.stdin.readline())
bin_list = [0, 1, 1]
# N(1 <= N <= 90)
for i in range(3, 91):
    bin_list.append(bin_list[i-1] + bin_list[i-2])

print(bin_list[n])

