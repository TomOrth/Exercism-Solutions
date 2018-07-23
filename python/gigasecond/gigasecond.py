import datetime
import math
def add_gigasecond(birth_date):
    if birth_date is None: raise ValueError('Invalid value')
    return birth_date + datetime.timedelta(0, math.pow(10, 9))
