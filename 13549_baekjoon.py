from collections import deque
n, k = map(int, input().split())
r = [False]* 100001
q = deque()
q.append((n, 0))
while q:
    new_n, val = q.popleft()
    if r[new_n]:
        continue
    else:
        r[new_n]= True
    if new_n == k:
        print(val)
        exit()
    for tmp in (new_n-1, new_n+1):
        if 0<= tmp<= 100000:
            q.append((tmp, val+1))
    if 0<= new_n *2 <=100000:
        q.appendleft((new_n *2, val))