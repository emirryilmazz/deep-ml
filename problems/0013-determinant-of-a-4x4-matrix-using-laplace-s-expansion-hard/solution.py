def det(matrix):
    n = len(matrix)
    if n == 1:
      return matrix[0][0]
    m = len(matrix[0])
    t = 1
    total = 0
    for i in range(n):
      row_val = matrix[0][i] # i11, i12, i13
      matr = [x[:i] + x[i+1:] for x in matrix[1:]] # i11 için -> i22, i23, i32, i3
      sum_arr = det(matr)
      val = row_val * t * sum_arr
      t *= -1
      total += val
    return total
def determinant_4x4(matrix: list[list[int|float]]) -> float:
    # Your recursive implementation here
    return det(matrix)