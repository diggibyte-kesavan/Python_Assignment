# def percent_calc(student_marks, name):
#     n = len(student_marks[name])
#     total = 0
#     for i in range(n):
#         total = total + student_marks[name][i]
#     avg = format(total / n,'.2f')
#     return avg

def percent_calc(student_marks, name):
    n = len(student_marks[name])
    total = sum(student_marks[name])
    avg = format(total / n, '.2f')
    return avg
