# util.py :- This file will contain the function to mutate the string.
# util.py

def mutate_string_with_list(string, position, character):
    """
    Mutate the given string by replacing the character at the specified position with the given character.
    This implementation uses a list to manipulate the string.

    Args:
        string (str): The original string.
        position (int): The index to insert the character at.
        character (str): The character to insert.

    Returns:
        str: The altered string.
    """
    if position < 0 or position >= len(string):
        return string
    # Convert the string to a list of characters
    char_list = list(string)
    # Replace the character at the specified position
    char_list[position] = character
    # Convert the list of characters back to a string
    return ''.join(char_list)


def mutate_string_with_slice(string, position, character):
    """
    Mutate the given string by replacing the character at the specified position with the given character.
    This implementation uses slicing to manipulate the string.

    Args:
        string (str): The original string.
        position (int): The index to insert the character at.
        character (str): The character to insert.

    Returns:
        str: The altered string.
    """
    if position < 0 or position >= len(string):
        return string
    # Slice the string and join it back with the mutated character
    return string[:position] + character + string[position + 1:]
