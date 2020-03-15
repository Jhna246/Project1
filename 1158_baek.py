import sys

n, a = map(int, sys.stdin.readline().split())

lst = []
new_lst = []
index = 0

for i in range(n):
    lst.append(i+1)

while len(lst) > 0:
    index = ((a - 1) + index) % len(lst)
    new_lst.append(lst.pop(index))

result = map(str, new_lst)
result = ', '.join(result)
print("<", end = '')
print(result, end = '')
print(">")
