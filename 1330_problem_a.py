import sys

t = int(sys.stdin.readline())
a = [0] * 101

for i in range(t):
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    sort_a = sorted(a)
    count = 1
    length = x + 1
    i = 1
    while i < length:
        # if number is not in the list
        if i not in sort_a:
            sort_a.append(i)
            i += 1
        # if it is, increase length and i
        elif i in sort_a:
            length += 1
            i += 1
        # if i == length
        else:
            break
    new_sort = sorted(sort_a)
    # if temp == 1, then they are consecutive
    for i in range(1, len(new_sort)):
        temp = new_sort[i] - new_sort[i - 1]
        if temp == 1:
            count += 1
        # ignore if the numbers are the equal
        elif temp == 0:
            continue
        else:
            break

    print(count)
