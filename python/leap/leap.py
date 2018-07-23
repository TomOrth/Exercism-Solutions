def is_leap_year(year):
    is_leap = year % 4 == 0
    if not is_leap: return is_leap
    is_leap = year % 100 != 0
    if not is_leap:
        is_leap = year % 400 == 0
    return is_leap
