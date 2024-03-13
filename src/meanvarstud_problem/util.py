import numpy as np


def mean_var_stud(array):
    mean_result = np.mean(array, axis=1)
    var_result = np.var(array, axis=0)
    std_result = round(np.std(array, axis=None), 11)
    result_string = f"{mean_result}\n{var_result}\n{std_result}"
    return result_string
