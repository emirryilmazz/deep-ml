import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
   
    # Your code here
    det = matrix[0][0] * matrix[1][1] - matrix[1][0]*matrix[0][1]
    if det == 0:
        return None
    det_i = 1/det
    a = [[matrix[1][1] * det_i, matrix[0][1] * det_i * -1], [matrix[1][0] * det_i * -1, matrix[0][0] * det_i]]
    

    return a
    pass
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    arr = []
    n1 = len(a)
    m1 = len(a[0])
    n2 = len(b)
    m2 = len(b[0])
    if m1 != n2:
        return -1
    # yeni matrisin shape = (n1, m2)
    # 
    arr = []
    for i in range(n1): # row
        arr2 = []
        for j in range(m2): # col
            sum_val = 0
            for k in range(m1): #iteration count
                sum_val += a[i][k] * b[k][j]
            arr2.append(sum_val)
        arr.append(arr2)
    


    return arr

def check_invertible(arr):
    try:
        return np.linalg.det(arr)
    except:
        return 0

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    if check_invertible(T) == 0 or check_invertible(S) == 0:
        return -1
    t_i = np.linalg.inv(T)
    x = matrixmul(A,S)
    y = matrixmul(x, t_i)
    return y