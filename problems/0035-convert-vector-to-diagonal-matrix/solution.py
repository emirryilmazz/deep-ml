import numpy as np

def make_diagonal(x):
    n = len(x)
    final = []
    for i, val in enumerate(x):
        arr = [0 for j in range(n)]
        arr[i] = val
        final.append(arr)
    return final