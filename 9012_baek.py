import sys

for _ in range(int(input())):
    a = input()
    b = 1
    c = []

    for i in a:
        if i == '(':
            c.append(1)
        else:
            if len(c) == 0:
                b = 0
                break
            else:
                c.pop()
    if b == 0:
        print('NO')
    elif len(c) != 0:
        print('NO')
    else:
        print('YES')