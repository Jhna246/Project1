import sys

a, b = map(int, sys.stdin.readline().split())
biggest_value = 0
gcd = 0
gcf = 0
n, k = 1, 1

if a > b:
    biggest_value = a
elif b > a:
    biggest_value = b
else:
    biggest_value = a

for i in range(biggest_value):
    if a % n == 0:
        if b % n == 0:
            gcd = n
            n += 1
        else:
            n += 1
    else:
        n += 1

for i in range(10001):
    if (a * k) % b == 0:
        gcf = a * k
        break
    else:
        k += 1

print(gcd)
print(gcf)
