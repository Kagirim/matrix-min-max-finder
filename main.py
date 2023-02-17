def max_row_min_col(matrix):
    # Create empty sets to store the maximum in row and minimum in column, respectively
    max_in_row = set()  # O(1) space
    min_in_col = set()  # O(1) space

    # For each row in the matrix, find the maximum element in that row and add it to max_in_row set
    for row in matrix:  # O(m*n) time
        max_in_row.add(max(row))    # O(n) time

    # For each column in the matrix, find the minimum element in that column and add it to min_in_col set
    for col in range(len(matrix[0])):   # O(n) time
        # To find the minimum element in a column, we can iterate through all rows and take the minimum value
        # of the element in that column using a generator expression
        min_in_col.add(min(row[col] for row in matrix)) # O(m) time

    # Return the intersection of the two sets, which contains only the elements that are in both sets
    return max_in_row.intersection(min_in_col)  # O(min(m,n)) time, O(min(m,n)) space

# The function's time complexity is O(m*n) since it involves traversing through all the elements of the matrix twice. 
# Firstly, the maximum value in each row must be found and secondly, the minimum value in each column.

# The space complexity of the function is O(min(m, n)) since two sets are employed to store the maximum values of each row and 
# the minimum values of each column. 
# The size of each set is bounded by the smaller of the number of rows and the number of columns of the matrix.

# Tests
# Test case 1
matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
assert max_row_min_col(matrix) == {17}

# Test case 2
matrix = [[100, 60, 20, 50], [70, 80, 10, 90], [10, 50, 44, 30]]
assert max_row_min_col(matrix) == {50}

# Test case 3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert max_row_min_col(matrix) == {3}

# Test case 4
matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 20]]
assert max_row_min_col(matrix) == {16}
