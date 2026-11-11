import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    tr = matrix[0][0] + matrix[1][1]
    det_x = np.abs(tr*tr - 4 * det)
    l1 = (tr + np.sqrt(det_x)) / 2
    l2 = (tr - np.sqrt(det_x)) / 2
    return [l1, l2]