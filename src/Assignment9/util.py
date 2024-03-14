# util.py :- This file will contain the function to get time difference in seconds
from datetime import datetime


def get_time_difference_in_seconds(time1, time2):
    format_str = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(time1, format_str)
    t2 = datetime.strptime(time2, format_str)
    difference = abs((t1 - t2).total_seconds())
    return int(difference)
