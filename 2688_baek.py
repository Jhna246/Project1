import sys

row_count = 65
column_count = 10
mat = [[0 for j in range(column_count)] for i in range(row_count)]
first = int(sys.stdin.readline())

while first > 0:
    num = int(sys.stdin.readline())
    # creating two digits
    # d[1][0] = 0
    # d[1][1] = (0), 1
    # d[1][2] = (0, 1), 2
    for i in range(0, 10):
        mat[1][i] = i + 1
    # d[i-1][j] is the previous array's values
    # if we have d[1][2], we have (0, 1), 2.
    # right now, d[2][2] is at the value of 3 because we add from d[2][1], which has values 00, 01, 11
    # using the 2 from d[1][2], we can create 02, 12, 22 by distributing the 2
    # those are the values that we need to add to the current 00, 01, 11 from d[2][1],
    # making d[2][2] = 00, 01, 11, 02, 12, 22
    #
    # thus the algorithm is d[i][j] = d[i - 1][j] + d[i][j - 1]
    for i in range(2, num + 1):
        mat[i][0] = 1
        for j in range(1, 10):
            mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
    first -= 1
    print(mat[num][9])
    if first == 0:
        exit()
