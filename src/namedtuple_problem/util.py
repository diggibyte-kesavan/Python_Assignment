from collections import namedtuple


def calculate_average_mark(students_data):
    N = int(students_data[0])
    columns = students_data[1].split()
    Student = namedtuple('Student', columns)
    total_marks = sum(int(Student(*student.split()).MARKS) for student in students_data[2:])
    average_mark = total_marks / N
    formatted_average_mark = format(average_mark, '.2f')
    return formatted_average_mark
