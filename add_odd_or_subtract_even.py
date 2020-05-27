import sys

first = int(sys.stdin.readline())

for i in range(first):
    difference, sum, steps, temp = 0, 0, 0, 0

    a, b = map(int, sys.stdin.readline().split())
    # a is smaller than b
    if a < b:
        difference = b - a
        # if the difference between a and b is even
        if difference % 2 == 0:
            difference = difference - 1
            temp = temp + 1
            a = a + difference + temp
            steps += 2
            print(steps)
        # if the difference between a and b is odd
        else:
            a = a + difference
            steps += 1
            print(steps)
    # a is bigger than b
    elif a > b:
        difference = a - b
        # if the difference between a and b is even
        if difference % 2 == 0:
            a = a - difference
            steps += 1
            print(steps)
        else:
            difference = difference - 1
            temp = temp + 1
            a = a - difference - 1
            steps += 2
            print(steps)
    # a and b are the same numbers
    else:
        print(0)


# You are given two positive integers a and b.
#
# In one move, you can change a in the following way:
#
    # Choose any positive odd integer x (x>0) and replace a with a+x;
    # choose any positive even integer y (y>0) and replace a with a−y.
#
# You can perform as many such operations as you want.
# You can choose the same numbers x and y in different moves.
#
# Your task is to find the minimum number of moves required to obtain b from a.
# It is guaranteed that you can always obtain b from a.
#
# You have to answer t independent test cases.


