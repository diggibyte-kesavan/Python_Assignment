def piling_up(t, tests):
    results = []
    for test in tests:
        n = len(test)
        b = []
        while len(test) > 0:
            if test[-1] > test[0]:
                b.append(test.pop(-1))
            else:
                b.append(test.pop(0))
        c = b.copy()
        b.sort(reverse=True)
        if b == c:
            results.append('Yes')
        else:
            results.append('No')
    return ' '.join(results)
