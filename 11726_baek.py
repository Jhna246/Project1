# import sys
# 시간초과
#
# def p(x):
#     if x < 3:
#         return x
#     else:
#         array[x] = p(x-2) + p(x-1)
#         return array[x]
#
#
# n = int(sys.stdin.readline())
# array = [-1 for i in range(n+1)]
# array[0] = 0
# array[1] = 1
# array[2] = 2
#
# print(p(n) % 10007)

import sys

n = int(sys.stdin.readline())
array = [0, 1, 2]
for i in range(3, 1001):
    array.append(array[i-2] + array[i-1])
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
print(array[n] % 10007)
