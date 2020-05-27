import sys
from itertools import permutations

t = int(sys.stdin.readline())
left_perm = []
right_perm = []

while t > 0:
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(0, len(a) - 1):
        left_perm.append(a[i])
    for i in range(1, len(a)):
        right_perm.append(a[i])

    counter = 0
    count = 1
    sort_list_l = sorted(left_perm)
    sort_list_r = sorted(right_perm)

    for i in range(1, len(left_perm)):
        temp = sort_list_l[i] - sort_list_l[i - 1]
        if temp == 1:
            count += 1
        if count == len(left_perm):
            print(a[0], max(left_perm))
            counter += 1
        # ignore if the numbers are the equal
        elif temp == 0:
            count += 1
            continue
        elif temp > 1:
            break

    count = 1

    for i in range(1, len(right_perm)):
        temp = sort_list_r[i] - sort_list_r[i - 1]
        if temp == 1:
            count += 1
        if count == len(right_perm):
            print(max(right_perm), min(right_perm))
            counter += 1
        # ignore if the numbers are the equal
        elif temp == 0:
            count += 1
            continue
        elif temp > 1:
            break
    print(counter)
    print()


# T=int(input())
# for t in range(T):
#     n=int(input())
#     a=list(map(int,input().split()))
#     c=0
#     cs=0
#     cnt=[0]*n
#     cnts=[0]*n
#     for i in range(n):
#         c+=a[i]
#         cs+=a[i]*a[i]*a[i]
#         cnt[i]=c
#         cnts[i]=cs
#     c=0
#     res=[]
#     for i in range(n-1):
#         N=i+1
#         k=n-N
#         if cnt[i]==(N)*(N+1)//2 and cnt[-1]-cnt[i]==k*(k+1)//2 and  cnts[i]==((N)*(N+1)//2)*((N)*(N+1)//2) and cnts[-1]-cnts[i]==(k*(k+1)//2)*(k*(k+1)//2):
#             #print('test')
#             c+=1
#             res.append([N,k])
#     print(c)
#     for i in res:
#         print(*i)
