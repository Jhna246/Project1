import sys

n = int(sys.stdin.readline())
lst = [0] * n
lst2 = []

for i in range(65, 0, -1):
    temp = n - i
    ans = temp
    lst2 = [int(j) for j in str(temp)]
    # print(lst2, 'list')
    for k in range(len(lst2)):
        ans += lst2[k]
    # print(ans, 'ans')
    if ans == n:
        print(temp)
        exit()