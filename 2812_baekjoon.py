import sys

n, k = map(int, sys.stdin.readline().split())
value = list(map(int, sys.stdin.readline().rstrip()))
answer = []

for i in value:
    while answer and k > 0 and answer[-1] < i:
        answer.pop()
        k -= 1
    answer.append(i)

if k != 0:
    answer = answer[:-k]


print("".join(map(str, answer)))
# i = 1
# lim = n - k
# while lim > 0:
#     maxIndex = 0
#     if number[i] >= number[maxIndex]:
#         maxIndex = number[i]
#     answer.append(maxIndex)
#     i += 1
#     lim -= 1
# print(''.join(map(str, answer)))

# while k > 0:
#     maxIndex = 0
#     for i in range(1, len(number)):
#         if number[i] > number[maxIndex]:
#             maxIndex = i
#     answer.append(number[maxIndex])
#     number.remove(number[maxIndex])
#     k -= 1
# string = ''.join(map(str, answer))
# print(string)

#
# while k > 0:
#     for i in range(len(number)):
#         if i < 2:
#             answer.append(number[i])
#             counter += 1
#         elif i >= 2:
#             for j in range(len(answer)):
#                 if number[i] > answer[j]:
#                     answer.remove(answer[j])
#                     answer.append(number[i])
#                     k -= 1
#                     continue
#                 else:
#                     k -= 1
#                     continue
# string = ''.join(map(str, answer))
# print(string)

# for i in range(k):
#     largest_num = max(number)
#     answer.append(largest_num)
#     number.remove(largest_num)
# string = ''.join(map(str, answer))
# print(string)



#
# n, k = map(int, sys.stdin.readline().split())
# value = int(sys.stdin.readline())
# number = [int(ch) for ch in str(value)]
# sort_number = sorted(number, reverse = True)
# del sort_number[k:]
# string = ''.join(map(str, sort_number))
# print(string)
