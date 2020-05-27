import sys
n = int(sys.stdin.readline())
height = list(map(int, input().split()))
reverse_height = height[::-1]
count = 1

temp = [[0 for i in range(len(height))] for j in range(len(height))]
reverse_temp = [[0 for i in range(len(height))] for j in range(len(height))]
l = [[0 for i in range(len(height))] for j in range(len(height))]
r = [[0 for i in range(len(height))] for j in range(len(height))]
r_reverse = r[::-1]

maxlist = [0 for i in range(len(height))]
sum_list = []

for i in range(len(height)):
    for j in range(count):
        if count == 1:
            temp[i][j] = height[j]
            reverse_temp[i][j] = reverse_height[j]
        if count > 1:
            temp[i][j] = height[j]
            reverse_temp[i][j] = reverse_height[j]
    count += 1

# for left
count = 1
for i in range(len(height)):
    l[0][0] = temp[0][0]
    for j in range(count - 1):
        if count > 1:
            if temp[i][j] < temp[i][j+1]:
                l[i][j] = temp[i][j]
                l[i][j+1] = temp[i][j+1]
            elif temp[i][j] > temp[i][j+1]:
                l[i][j] = temp[i][j + 1]
                l[i][j+1] = temp[i][j+1]
                for k in range(len(height)):
                    if l[i][j-k] > l[i][j]:
                        l[i][j-k] = l[i][j]
            elif temp[i][j] == temp[i][j+1]:
                l[i][j] = temp[i][j]
                l[i][j + 1] = temp[i][j + 1]
    count += 1

# for right
count = 1
for i in range(len(height)):
    r[0][0] = reverse_temp[0][0]
    for j in range(count - 1):
        if count > 1:
            if reverse_temp[i][j] < reverse_temp[i][j+1]:
                r[i][j] = reverse_temp[i][j]
                r[i][j+1] = reverse_temp[i][j+1]
            elif reverse_temp[i][j] > reverse_temp[i][j+1]:
                r[i][j] = reverse_temp[i][j + 1]
                r[i][j+1] = reverse_temp[i][j+1]
                for k in range(len(height)):
                    if r[i][j-k] > r[i][j]:
                        r[i][j-k] = r[i][j]
            elif reverse_temp[i][j] == reverse_temp[i][j+1]:
                r[i][j] = reverse_temp[i][j]
                r[i][j + 1] = reverse_temp[i][j + 1]
    count += 1

sum_rows_l = [sum(x) for x in l]
sum_rows_r = [sum(x) for x in r_reverse]
sum_total = [x + y - z for x, y, z in zip(sum_rows_l, sum_rows_r, height)]

maxpos = sum_total.index(max(sum_total))
maxlist[maxpos] = height[maxpos]

for i in range(maxpos, len(height) - 1):
    if sum_total[i + 1] < sum_total[i]:
        maxlist[i + 1] = height[i + 1]
    else:
        maxlist[i + 1] = height[i]

for i in range(0, maxpos):
    if sum_total[i] < sum_total[i+1]:
        maxlist[i] = height[i]
    else:
        maxlist[i] = height[i + 1]

abc = ' '.join(map(str, maxlist))
print(abc)

print(sum_rows_l)