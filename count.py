def multiply_matrices(matrix1, matrix2):
    # Check dimensions
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])


    result = [[0] * cols1 for _ in range(rows2)]

    # Perform element-wise multiplication
    for x in range (rows2):
        for y in range(cols1):
            print("calc ",x,y)
            
            for j in range(min(cols1,rows2)):
                result[x][y] += matrix1[x][j] * matrix2[j][y]

    return result

# Example matrices of different dimensions
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]

# Multiply matrices
try:
    result = multiply_matrices(matrix1, matrix2)
    print("Result of element-wise multiplication:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)
