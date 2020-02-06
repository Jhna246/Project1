import sys

count = 0

string = str(sys.stdin.readline())
for i in string:
    if i.isalpha():
        count += 1
    else:
        count = count
print(count)


