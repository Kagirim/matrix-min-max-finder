from main import max_row_min_col

# Test case 1
matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
result = max_row_min_col(matrix)
print(f"{matrix} : {result}")  # {17}

# Test case 2
matrix = [[100, 60, 20, 50], [70, 80, 10, 90], [10, 50, 44, 30]]
result = max_row_min_col(matrix)
print(f"{matrix} : {result}")   # {50}

# Test case 3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = max_row_min_col(matrix)
print(f"{matrix} : {result}")

# Test case 4
matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 20]]
result = max_row_min_col(matrix)
print(f"{matrix} : {result}")