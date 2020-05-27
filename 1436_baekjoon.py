from itertools import product

d = {i: str(i) for i in range(10)}
d[10] = '666'
k = sorted(set([int(d[i] + d[j] + d[k] + d[l]+ d[m])
                for i, j, k, l, m in product(range(11), repeat = 5) if 10 in (i, j, k, l, m)]))
print(k[int(input()) -1])