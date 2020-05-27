from collections import deque

n, k = map(int, input().split())
r = [False]* 100001
q = deque()
q.append(n)
r[n] = -1
while q:
    new_n = q.popleft()
    if new_n == k:
        break
    for tmp in (new_n-1, new_n+1, new_n*2):
        if 0<= tmp<= 100000 and not r[tmp]:
            q.append(tmp)
            r[tmp] = new_n
path = deque([k])
while r[k]!= -1:
    k = r[k]
    path.appendleft(k)
print(len(path)-1)
print(*path)