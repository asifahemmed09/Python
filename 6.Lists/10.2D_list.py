matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [5, 4, 3, 2],
    [1, 2, 3, 4],
]

row = len(matrix2)
column = len(matrix2[0])

for i in range(0,row):
    for j in range(0,column):
        print(matrix2[i][j],end="")
    print()

