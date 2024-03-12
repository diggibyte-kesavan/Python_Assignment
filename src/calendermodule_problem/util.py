import calendar


def find_day_of_date(date_string):
    month, day, year = map(int, date_string.split())
    day_of_week = calendar.day_name[calendar.weekday(year, month, day)]
    return day_of_week.upper()
