def word_order(n, words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words = list(word_count.keys())
    occurrences = list(word_count.values())

    return len(distinct_words), occurrences
