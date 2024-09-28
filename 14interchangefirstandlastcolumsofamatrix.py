def swap_first_last_columns(matrix):
    if not matrix or not matrix[0]:
        return matrix  
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for row in matrix:
        row[0], row[-1] = row[-1], row[0]
    return matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
swapped_matrix = swap_first_last_columns(matrix)
for row in swapped_matrix:
    print(row)
