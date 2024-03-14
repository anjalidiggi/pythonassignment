# Define a common program for getting average score of any student
"""
Problem Statement :-
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Sample Output :-
Enter student name (or type 'done' to finish): Anjali
Enter scores for Anjali separated by commas: 98,87,65,78,90,45
Enter student name (or type 'done' to finish): Moti
Enter scores for Moti separated by commas: 45,6,98,65,78
Enter student name (or type 'done' to finish): done
Anjali: Average score: 77.17
Moti: Average score: 58.40
"""
from util import calculate_average


def get_student_scores():
    """
    Description:- the user to input student names and their scores.

    Returns:
        dict: Dictionary where keys are student names and values are lists of scores.
    """
    student_scores = {}
    while True:
        student_name = input("Enter student name (or type 'done' to finish): ")
        if student_name.lower() == "done":
            break
        scores_str = input(f"Enter scores for {student_name} separated by commas: ")
        scores = [float(score.strip()) for score in scores_str.split(",")]
        student_scores[student_name] = scores
    return student_scores


def main():
    # Get student scores from user input
    student_scores = get_student_scores()

    # Calculate the average score for each student
    average_scores = calculate_average(student_scores)

    # Print the average scores for each student
    for student, average_score in average_scores.items():
        print(f"{student}: Average score: {format(average_score, ".2f")}")


if __name__ == "__main__":
    main()
