import numpy as np


def calculate_determinant(arr):
    arr_np = np.array(arr)
    determinant = np.linalg.det(arr_np)
    return round(determinant, 1)
