from itertools import combinations


def iterables_iterators(N, letters, K):
    com = list(combinations(letters, K))
    probability = sum(1 for j in com if 'a' in j) / len(com)
    return round(probability, 7)
