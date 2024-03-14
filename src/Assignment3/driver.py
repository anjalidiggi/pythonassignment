
"""
Write a Python program for below problem statement
Problem statement:

Task:-
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string 
Sample output :-
Enter the string: Anjali
Enter the position: 3
Enter the character: L
Mutated string By List : AnjLli
Mutated string By Slice method: AnjLli

Process finished with exit code 0

"""
# driver.py This file will call the mutate_string_with_list and mutate_string_with_slice function from util.py.
from util import mutate_string_with_list,mutate_string_with_slice

def main():
    # Input string
    string = input("Enter the string: ")

    # Input position
    position = int(input("Enter the position: "))

    # Input character
    character = input("Enter the character: ")

    # Mutate the string
    mutated_string_list = mutate_string_with_list(string, position, character)
    mutated_string_slice = mutate_string_with_slice(string, position, character)

    print("Mutated string By List :", mutated_string_list)
    print("Mutated string By Slice method:", mutated_string_slice)


if __name__ == "__main__":
    main()

