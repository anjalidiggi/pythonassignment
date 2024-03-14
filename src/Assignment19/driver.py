"""
Assignment 1 Problem Statement :-
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

sample output
Enter the number of commands: 8
Enter command 1: insert 0 5
Enter command 2: print
Enter command 3: insert 1 3
Enter command 4: remove 5
Enter command 5: print
Enter command 6: append 6
Enter command 7: sort
Enter command 8: print
[5]
[3]
[3, 6]

Process finished with exit code 0

"""
# driver.py :This file will prompt the user to Enter the number of command
#  and Enter the command
# from util.py to validate python list command.
from util import execute_commands


def main():
    N = int(input("Enter the number of commands: "))
    commands = [input("Enter command {}: ".format(i + 1)) for i in range(N)]
    execute_commands(commands)


if __name__ == "__main__":
    main()
