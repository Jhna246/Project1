import sys

a, b, c = map(int, sys.stdin.readline().split())
largest = 0
diff = 0

if a > b and a > c:
    largest = a
    if b + c <= largest:
        diff = largest - (b + c) + 1
        print(diff)
    else:
        print(0)
elif b > a and b > c:
    largest = b
    if a + c <= largest:
        diff = largest - (a + c) + 1
        print(diff)
    else:
        print(0)
else:
    largest = c
    if a + b <= largest:
        diff = largest - (a + b) + 1
        print(diff)
    else:
        print(0)

