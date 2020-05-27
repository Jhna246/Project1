def repeated_digit(n):
    a = []

    # Traversing through each digit
    while n != 0:
        d = n % 10

        # if the digit is present
        # more than once in the
        # number
        if d in a:
            # return 0 if the number
            # has repeated digit
            return 0
        a.append(d)
        n = n // 10

    # return 1 if the number has no
    # repeated digit
    return 1


# Function to find total number
# in the given range which has
# no repeated digit
def calculate(L, R):
    answer = 0

    # Traversing through the range
    for i in range(L, R + 1):
        # Add 1 to the answer if i has
        # no repeated digit else 0
        answer = answer + repeated_digit(i)

        # return answer
    return answer


# Driver's Code
L = 1
R = 2147483647

# Calling the calculate
print(calculate(L, R))