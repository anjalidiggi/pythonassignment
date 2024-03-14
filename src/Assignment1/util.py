# Define a utility function for getting average score of each student
def calculate_average(scores_dict):
    """
    Calculate the average score for each student.

    Args:
        scores_dict (dict): Dictionary where keys are student names and values are lists of scores.

    Returns:
        dict: Dictionary where keys are student names and values are average scores.
    """
    average_scores = {}
    for student, scores in scores_dict.items():
        if not scores:
            average_scores[student] = 0
        else:
            average_scores[student] = sum(scores) / len(scores)
    return average_scores

