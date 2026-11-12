import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    for i, arr in enumerate(matrix):
        for j, val in enumerate(arr):
            matrix[i][j] = matrix[i][j] * scalar
    return matrix
    
def det(matrix):
  n = len(matrix)
  if n == 1:
    return matrix[0][0]
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

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n = len(a)
    m = len(a[0])
    new_arr = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
          new_arr[j][i] = a[i][j]
    return new_arr

def adj_matrix(a):
  a_t = transpose_matrix(a)
  adj = []
  for i, arr in enumerate(a_t):
    adj_list = []
    for j in range(len(arr)):
      minor = [x[:j] + x[j+1:] for x in a_t[:i] + a_t[i+1:]]
      det_m = det(minor)
      if (i+j) % 2 == 1:
        det_m *= -1
      adj_list.append(det_m)
    adj.append(adj_list)
  return adj

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    det_val = det(matrix)
    if det_val == 0:
        return None
    adj_m = adj_matrix(matrix)
    det_i = 1/det_val
    return scalar_multiply(adj_m, det_i)
