import sys

first = int(sys.stdin.readline())

while first > 0:
    flag = 0
    a, b = map(int, sys.stdin.readline().split())
    alist = list(map(int, sys.stdin.readline().split()))
    plist = list(map(int, sys.stdin.readline().split()))

    sorted(plist)
    for i in range(a):
        for j in range(b):
            if alist[plist[j]] < alist[plist[j] - 1]:
                alist[plist[j]], alist[plist[j] - 1] = alist[plist[j] - 1], alist[plist[j]]
    if alist == sorted(alist):
        flag = 1
    if flag:
        print('YES')
        first -= 1
    else:
        print('NO')
        first -= 1