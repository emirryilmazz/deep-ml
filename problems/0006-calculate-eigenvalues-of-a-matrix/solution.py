import numpy as np

def traces(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total
   
def det(matrix):
  n = len(matrix)
  if n == 1:
    return matrix[0][0]
  t = 1
  total = 0
  for i in range(n):
    row_val = matrix[0][i] # i11, i12, i13
    matr = [x[:i] + x[i+1:] for x in matrix[1:]] # i11 iÃ§in -> i22, i23, i32, i3
    sum_arr = det(matr)
    val = row_val * t * sum_arr
    t *= -1
    total += val
  return total

def equation_solver(a, b, c):
    # (-b +- b^2-4ac) / 2a
    det_e = np.abs((b * b) - (4 * a * c))
    s1 = ((b) + np.sqrt(det_e)) / (2*a)
    s2 = ((b) - np.sqrt(det_e)) / (2*a)
    return (s1, s2)

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    det_m = det(matrix)
    tr = traces(matrix)
    l1, l2 = equation_solver(1, tr, det_m)
    return [l1, l2]