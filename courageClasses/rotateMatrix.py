def rotate_matrix(mat, m, n):
    # Create a new matrix to store the rotated values
    result = [[0] * n for _ in range(m)]

    # Calculate the number of layers
    layers = min(m, n) // 2

    # Fill the result matrix with rotated values layer by layer
    for layer in range(layers):
        first_row = layer
        last_row = m - layer - 1
        first_col = layer
        last_col = n - layer - 1

        # Move elements from left to top
        for i in range(first_col, last_col + 1):
            result[first_row][i] = mat[last_row - (i - first_col)][first_col]

        # Move elements from bottom to left
        for i in range(first_row + 1, last_row + 1):
            result[i][first_col] = mat[last_row][last_col - (i - first_row)]

        # Move elements from right to bottom
        for i in range(last_col, first_col - 1, -1):
            result[last_row][i] = mat[i][last_col]

        # Move elements from top to right
        for i in range(last_row - 1, first_row, -1):
            result[i][last_col] = mat[first_row][i]

    # Handle any remaining center element for odd dimensions
    if min(m, n) % 2 != 0:
        if m > n:
            result[m // 2][n // 2] = mat[m // 2][n // 2]
        else:
            result[m // 2][n // 2] = mat[m // 2][n // 2]

    # Copy the result back to the original matrix
    for i in range(m):
        for j in range(n):
            mat[i][j] = result[i][j]


if __name__ == "__main__":
    import sys

    # Read input from stdin
    input_line_1 = sys.stdin.readline().strip()
    input_line_2 = sys.stdin.readline().strip()

    # Parse M and N from the first line
    dimensions = input_line_1.split(",")
    M = int(dimensions[0].split("=")[1].strip())
    N = int(dimensions[1].split("=")[1].strip())

    # Parse the matrix from the second line
    matrix_input = input_line_2.strip()
    matrix_input = matrix_input[matrix_input.index("[") + 1:matrix_input.rindex("]")]  # Remove [[ and ]]
    
    rows = matrix_input.split("],[")

    Mat = []
    for row in rows:
        cleaned_row = row.replace("[", "").replace("]", "").split(",")
        Mat.append([int(num.strip()) for num in cleaned_row])

    # Rotate the matrix
    rotate_matrix(Mat, M, N)

    # Print the rotated matrix
    for row in Mat:
        print(" ".join(map(str, row)))