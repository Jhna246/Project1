from collections import deque
n, k = map(int, input().split())
r = [1500000] * 200001
q = deque()
q.append((n, 0))
total = 0
max_ = 1500000
while q:
    new_n, val = q.popleft()
    if r[new_n] < val:
        continue
    else:
        r[new_n] = val
    if val > max_:
        print(max_)
        print(total)
        exit()
    if new_n == k:
        total += 1
        max_ = val
    for tmp in (new_n*2, new_n-1, new_n+1):
        if 0<= tmp<= 100000:
            q.append((tmp, val+1))
else:
    print (max_)
    print (total)