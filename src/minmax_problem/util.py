import numpy as np


def min_max_axis_1(arr):
    max_length = max(len(sublist) for sublist in arr)
    arr_padded = [sublist + [0] * (max_length - len(sublist)) for sublist in arr]
    arr_np = np.array(arr_padded)
    min_along_axis_1 = np.min(arr_np, axis=1)
    max_of_min_axis_1 = np.max(min_along_axis_1)
    return max_of_min_axis_1
