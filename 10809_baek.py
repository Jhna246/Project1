alphabet_count = [-1] * 26
s = input()
list1 = list(s)

for alpha in list1:
    if alphabet_count[ord(alpha) - 97] is -1:
        alphabet_count[ord(alpha) - 97] = list1.index(alpha)
for i in alphabet_count:
    print(i, end = " ")

