"""
Q71. Given a 3x3 matrix, print only the main diagonal elements and replace
everything else with an asterisk (*).
# 1 2 3
# 4 5 6
# 7 8 9

# Expected Output:
# 1 * *
# * 5 *
# * * 9

"""


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

row = len(matrix)
column = len(matrix[0])

for i in range(0, row):
    for j in range(0, column):
        if i == j:
            print("*", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
