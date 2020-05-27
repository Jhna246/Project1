import sys


def decimalToBinary(n):
    return bin(n).replace("0b", "")


count = 0
lst = []
n = 1

for i in range(int(sys.stdin.readline())):
    a = decimalToBinary(i)
    if i == 1 or i == 2 or i == 3 or i == 4 or i == 6 or i == 12:
        # print(a)
        lst.append(i)
        count += 1
    if "000" in a or "111" in a:
        count += 1

print(count)