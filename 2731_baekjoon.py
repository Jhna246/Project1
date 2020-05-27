import sys


def findNum(num, mult):
    return num ** 3 % mult


for i in range(int(sys.stdin.readline())):
    t = int(sys.stdin.readline())

    digit = t % 10

    if digit == 3:
        number = 7
    elif digit == 7:
        number = 3
    else:
        number = digit

    if t == 3:
        print(7)
        continue
    elif t == 7:
        print(3)
        continue
    elif t == 9:
        print(9)
        continue
    elif t == 1:
        print(1)
        continue

    power = 10

    while True:
        step = power
        power *= 10

        numToFind = t % power

        while findNum(number, power) != numToFind:
            number += step

        if findNum(number, power) == t:
            print(number)
            break


# tc = int(input())
# for _ in range(tc):
#     r = input()
#     l = len(r)
#     r = int(r)
#     ans = 0
#     for ll in range(1, l+1):
#         r1 = int(str(r)[-ll:])
#         for j in range(10):
#             if (ans + j*(10**(ll-1)))**3 % (10**ll) == r1:
#                 ans += j*(10**(ll-1))
#                 break
#     print(ans)

# for tc in range(int(input())):
#     n=int(input())
#     i=1
#     t=0
#     while i<=n:
#         for j in range(10):
#             if (i*j+t)**3%(i*10)==n%(i*10):
#                 break
#         t+=i*j
#         i*=10
#     print(t)

# import sys
# n = int(sys.stdin.readline())
# for i in range(n):
#     t = int(sys.stdin.readline())
#     a_string = str(t)
#     length = len(a_string)
#     mod = 10 ** length
#     digit = t % 10
#     if digit == 3:
#         n = 7
#     elif digit == 7:
#         n = 3
#     elif digit == 9:
#         n = 9
#     else:
#         n = 1
#     number = n + 10
#     if t == 3:
#         print(7)
#     elif t == 7:
#         print(3)
#     mult = 1
#
#     while True:
#         numToFind = t % (10**(mult + 1))
#         if number ** 3 % (10 ** (mult + 1)) != numToFind and number ** 3 % mod != t:
#             number += 10 ** mult
#         elif number ** 3 % (10 ** (mult + 1)) == numToFind:
#             mult = mult + 1
#             continue
#         else:
#             print(number)
#             break