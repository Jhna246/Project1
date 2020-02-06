import sys

S = str(input())
lst = []

for i in S:
    lst.append(S)
    S = S[1:]

str1 = "\n".join(sorted(lst))
print(str1)
