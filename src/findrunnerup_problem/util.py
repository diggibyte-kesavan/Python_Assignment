def runner_up_score(scores):
    unique_sorted = sorted(set(scores), reverse=True)  # remove duplicates and sort descending order
    if len(unique_sorted) < 2:  # if two unique value is there at the time there is no runner-up score
        return None
    return unique_sorted[1]  # second runner-up score.
