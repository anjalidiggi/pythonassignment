# util.py :- This file will contain the function to determine the day given a date.

def calculate_average_marks(students):
    column_names = students[0]
    marks_index = column_names.index('MARKS')
    total_marks = sum(float(student[marks_index]) for student in students[1:])  # Sum up the marks
    total_students = len(students) - 1  # Exclude the header row
    return round(total_marks / total_students, 2)
