"""
Problem Statement : -
Task

Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .

Your task is to help Dr. Wesley calculate the average marks of the students.


Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer , the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the , ,  and , under their respective column names.

Constraints


Output Format

Print the average marks of the list corrected to 2 decimal places.
"""
"""
Sample Output :-
     students1 = [['ID', 'MARKS', 'NAME', 'CLASS'],
                     ['1', '97', 'ANJALI', '9'],
                     ['2', '87', 'GAYTRI', '8']]
Total Number of Students :- 2
ID MARKS NAME CLASS
1 97 ANJALI 9
2 87 GAYTRI 8
92.00
"""
# driver.py :- This file will read input from the user, call the calculate_average_marks
# function from util.py, # and print the average marks.
# driver.py
from util import calculate_average_marks


def main():
    students = []
    num_students = int(input("Enter the total number of students: "))
    columns = input("Enter the column names separated by space: ").split()
    students.append(columns)
    for _ in range(num_students):
        student_data = input("Enter student data separated by space: ").split()
        students.append(student_data)

    average_marks = calculate_average_marks(students)
    print("Total Number of Students:", num_students)
    print(" ".join(columns))
    for student in students[1:]:
        print(" ".join(student))
    print(format(average_marks, ".2f"))


if __name__ == "__main__":
    main()
