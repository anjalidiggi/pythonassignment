# util.py :- This file will contain the function to merge the tools.
def merge_the_tools(s, k):
    """
    Merge the tools to split string s into n/k substrings and print each subsequence without any repeated characters.

    Args:
        s (str): The string to analyze.
        k (int): The size of substrings to analyze.

    Returns:
        None. Prints each subsequence on a new line.
    """
    n = len(s)
    for i in range(0, n, k):
        substr = s[i:i+k]
        unique_chars = []
        for char in substr:
            if char not in unique_chars:
                unique_chars.append(char)
        print(''.join(unique_chars))
