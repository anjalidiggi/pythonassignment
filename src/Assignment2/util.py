# util.py This file will contain the function to find the runner-up score.
# util.py

def find_runner_up(scores):
    """
    Find the runner-up score from a list of scores.

    Args:
        scores (list of int): List of scores.

    Returns:
        int: Runner-up score, or None if the input list is empty.
    """
    if not scores:
        return None
    unique_scores = set(scores)
    unique_scores.remove(max(unique_scores))
    return max(unique_scores) if unique_scores else 1
