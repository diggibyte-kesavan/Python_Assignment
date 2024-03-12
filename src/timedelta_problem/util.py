from datetime import datetime


def time_difference(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)
    difference = time2 - time1
    return abs(difference.total_seconds())
