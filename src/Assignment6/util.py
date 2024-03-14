# util.py :- This file will contain the function to generate the HackerRank Logo.

def print_hackerrank_logo(thickness, character):
    """
    Print the HackerRank Logo of variable thickness.

    Args:
        thickness (int): The thickness value for the logo.
        character (str): The character to use in the logo.

    Returns:
        None. Prints the HackerRank Logo.
    """
    c = character

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
               (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
