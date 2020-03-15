alphabet_count = [0] * 26

s = input()
list1 = list(s)

for i in list1:
    alphabet_count[ord(i) - 97] += 1

for i in alphabet_count:
    print(i, end = " ")
