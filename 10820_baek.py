import sys


while True:
    string = str(sys.stdin.readline())

    if len(string.strip()) is 0:
        exit()
    else:
        lower_count = 0
        upper_count = 0
        number_count = 0
        space_count = 0

        for i in string:
            if i.isupper():
                upper_count += 1
            elif i.islower():
                lower_count += 1
            elif i.isspace():
                space_count += 1
            else:
                number_count += 1
        print(upper_count, lower_count, number_count, space_count)

