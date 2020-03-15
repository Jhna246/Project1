import sys


def maxSum(triangle, n):
    if n > 1:
        # row 1 + the elements of row 2
        triangle[1][1] = triangle[1][1] + triangle[0][0]
        triangle[1][0] = triangle[1][0] + triangle[0][0]
    # first and last elements of each row only have one number that is above
    for i in range(2, n):
        triangle[i][0] = triangle[i][0] + triangle[i-1][0]
        triangle[i][i] = triangle[i][i] + triangle[i-1][i-1]
        # add the columns
        for j in range(1, i):
            # check if left or right is bigger
            if triangle[i][j] + triangle[i-1][j-1] >= triangle[i][j] + triangle[i-1][j]:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
    print(max(triangle[n-1]))


first = int(sys.stdin.readline())
triangle = [list(map(int, input().split())) for _ in range(first)]

maxSum(triangle, first)


