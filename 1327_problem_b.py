import sys

for _ in range(int(input())):
    n = int(input())
    prince = set(range(1, n+1))
    princess = set(range(1, n+1))
    princess_list = [[] for _ in range(n+1)]
    # print(prince)
    # print(princess)
    for i in range(n):
        k = list(map(int, input().split()))[1:]
        princess_list[i+1] = k
        # print(princess_list)
        if k:
            for j in k:
                if j in prince:
                    prince.remove(j)
                    princess.remove(i+1)
                    break
    tmp = False
    for pr1 in princess:
        for pr2 in prince:
            if pr2 in princess_list[pr1]:
                continue
            else:
                print('IMPROVE')
                print(pr1, pr2)
                tmp = True
                break
        if tmp:
            break
    else:
        print('OPTIMAL')
