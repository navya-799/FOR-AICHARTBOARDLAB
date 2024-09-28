def add_matrices(A, B):
    """Add two matrices."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub_matrices(A, B):
    """Subtract matrix B from matrix A."""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mul_matrices(A, B):
    """Multiply two matrices."""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Incompatible dimensions for matrix multiplication.")
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
def trace_matrix(A):
    """Calculate the trace of a matrix."""
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to compute the trace.")    
    return sum(A[i][i] for i in range(len(A)))
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("Matrix A:")
    for row in A:
        print(row)
    print("\nMatrix B:")
    for row in B:
        print(row)
    print("\nAddition of A and B:")
    result_add = add_matrices(A, B)
    for row in result_add:
        print(row)
    print("\nSubtraction of B from A:")
    result_sub = sub_matrices(A, B)
    for row in result_sub:
        print(row)
    print("\nMultiplication of A and B:")
    result_mul = mul_matrices(A, B)
    for row in result_mul:
        print(row)
    print("\nTrace of matrix A:")
    print(trace_matrix(A))
