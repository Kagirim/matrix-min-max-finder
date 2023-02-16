# matrix-min-max-finder

Algorithm to find the maximum value in the row and minimum in the column of the given matrix

## Max in Row, Min in Column

A Python function to find all numbers that are the maximum value in its row but the minimum in its column in a given matrix.

### Usage

python
```
from max_in_row_min_in_col import max_in_row_min_in_col

matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
result = max_in_row_min_in_col(matrix)
print(result)   # {17}
```

The max_in_row_min_in_col function takes a matrix as input and returns a set of all numbers that are the maximum value in their respective row but the minimum in their respective column.

### Constraints

m == len(matrix)
n == len(matrix[0])
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5
All elements in the matrix are distinct.

## Algorithm

The function iterates through each row of the matrix and finds the maximum value in that row, and then iterates through each column of the matrix and finds the minimum value in that column. It then returns the intersection of the sets of maximum values and minimum values, which gives us the set of all numbers that satisfy the condition of being the maximum in their row and the minimum in their column.

The time complexity of the function is O(m*n) and the space complexity is O(min(m,n)), where m is the number of rows and n is the number of columns in the matrix.

### License

This project is licensed under the MIT License - see the LICENSE file for details.