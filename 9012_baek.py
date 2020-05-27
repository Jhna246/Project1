import sys

for i in range(int(sys.stdin.readline())):
    c = sys.stdin.readline()
    while '()' in c:
        c = c.replace('()', '')
    if len(c) == 1:
        print('YES')
    else:
        print('NO')

# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     a = list(sys.stdin.readline())
#     left_count = 0
#     right_count = 0
#     counter = 0
#
#     if a[len(a) - 2] == '(':
#         print('NO')
#         continue
#
#     if a[0] == ')':
#         print('NO')
#         continue
#
#     for i in range(len(a)):
#         if a[i] == '(':
#             left_count += 1
#             counter += 1
#         elif a[i] == ')':
#             right_count += 1
#             counter += 1
#         if counter == (len(a) - 1):
#             break
#         if left_count == right_count:
#             if a[i + 1] == ')':
#                 print('NO')
#                 right_count += 100
#                 break
#
#     if left_count != right_count and counter == (len(a) - 1):
#         print('NO')
#     else:
#         print('YES')