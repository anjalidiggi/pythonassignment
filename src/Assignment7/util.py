# util.py :- This file will contain the function to determine the day given a date.

from datetime import datetime


def find_day(month, day, year):
    # Create a datetime object for the given date
    date_object = datetime(year, month, day)
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = date_object.weekday()

    # Map the day of the week to its corresponding name
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    # Return the day in capital letters
    return days[day_of_week]
