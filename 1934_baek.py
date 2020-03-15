import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    c = gcd(a, b)
    lcm = int((a * b) / c)
    print(lcm)

# import sys
#
# k = 1
# lcm = 0
#
# for i in range(int(sys.stdin.readline())):
#     a, b = map(int, sys.stdin.readline().split())
#
#     for i in range(45001):
#         if a == 1:
#             lcm = b
#             sys.stdout.write(str(lcm) + '\n')
#             break
#         elif (a * k) % b == 0:
#             lcm = a * k
#             sys.stdout.write(str(lcm) + '\n')
#             k = 1
#             break
#         else:
#             k += 1
#
