from src.noidea_problem.util import calculate_happiness_noidea

n, m = 4, 3
arr = [1, 2, 3, 4]
A = [1, 3]
B = [2]

happiness = calculate_happiness_noidea(n, m, arr, A, B)
print(happiness)