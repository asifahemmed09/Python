"""
Given a 4x4 matrix, print only the border elements and replace the
inner elements with an asterisk (*).
"""

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 8],
    [1, 2, 3, 4],
]

row = len(matrix)
column = len(matrix[0])

for i in range(0, row):
    for j in range(0, column):
        if 0 < i < row - 1 and 0 < j < column - 1:
            print("*", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
