# import sys
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     arr = list(map(int, sys.stdin.readline().split()))
#     for i in range(n):
#         temp = float("inf")
#         for j in range(i + 1, n):
#             s = abs(abs(arr[i]) - abs(arr[j]))
#             if s < temp:
#                 if j == i + 1:
#                     arr[i + 1] = arr[j]
#                     temp = s
#                 else:
#                     arr[i + 1], arr[j] = arr[j], arr[i + 1]
#                     temp = s
#             print(i, j)
#             print(temp)
#             print(arr)
#             print(s)
#     print(" ".join(map(str, arr)))

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    answer = []
    mid = len(arr) // 2

    if len(arr) % 2 == 0:
        k = mid - 1
        a = mid
        answer.append(arr[k])
        answer.append(arr[a])
        for i in range(0, mid - 1):
            k -= 1
            a += 1
            answer.append(arr[k])
            answer.append(arr[a])

        # answer.append(arr[0])
        # answer.append(arr[len(arr) - 1])

    else:
        k = mid - 1
        a = mid
        # print(arr)
        answer.append(arr[a])
        answer.append(arr[k])
        for i in range(0, mid - 1):
            k -= 1
            a += 1
            # print(k, a)
            answer.append(arr[a])
            answer.append(arr[k])
        answer.append(arr[len(arr) - 1])
        # print(answer)

    print(" ".join(map(str, answer)))
