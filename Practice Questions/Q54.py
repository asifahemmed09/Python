"""
Given a 3x3 matrix as input, print its lower triangle.
Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*).

1  2  3
4  5  6
7  8  9

1  *  *
4  5  *
7  8  9
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

row = len(matrix)
column = len(matrix[0])

for i in range(0,row):
    for j in range(0,i + 1):
            print(matrix[i][j],end=" ")
    print()

print("\n")

for i in range(0,row):
    for j in range(0,column):
            if j - i > 0:
                  print("*",end=" ")
            else:
                print(matrix[i][j],end=" ")
    print()
