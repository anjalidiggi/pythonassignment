# util.py :- This file will contain the function to print the formatted values.

def print_formatted(n):
    """
    Print the values for each integer from 1 to n: Decimal, Octal, Hexadecimal (capitalized), Binary.

    Args:
        n (int): The maximum value to print.

    Returns:
        None. Prints the formatted values.
    """
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{dec.rjust(width)} {octal.rjust(width)} {hexa.rjust(width)} {binary.rjust(width)}")
