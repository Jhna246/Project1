n = int(sys.stdin.readline())
height = list(map(int, input().split()))

pre = [0 for _ in range(n)]
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
l[0] = height[0]
for i in range(1, n):
    p = i-1
    while height[p] > height[i]:
        p = pre[p]
    l[i] = l[p] + (i-p) * height[i]
    pre[i] = p