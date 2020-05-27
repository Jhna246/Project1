import sys
n = int(sys.stdin.readline())
t = list(map(str, sys.stdin.readline()))
lst = []

for i in range(len(t) - 1):
    lst.append(t[i])
sorted_list = sorted(lst)
string = ''.join(map(str, sorted_list))
print(string)