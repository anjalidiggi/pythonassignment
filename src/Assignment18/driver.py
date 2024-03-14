"""
Problem Statement : -
You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

"""
"""
Sample Output :-
input:- 
Enter the number of email addresses: 3
Enter email 1: anjali@diggibyte.com
Enter email 2: gaytri@diggibyte.com
Enter email 3: laxmi@diggibyte.com
output
Valid email addresses: ['anjali@diggibyte.com', 'gaytri@diggibyte.com', 'laxmi@diggibyte.com']

Process finished with exit code 0
"""
# driver.py :This file will prompt the user to
# Enter the number of email addresses: and enter email id
# and then call extract_valid_emails  from util.py to valid email address.
from util import extract_valid_emails


def main():
    N = int(input("Enter the number of email addresses: "))
    emails = [input(f"Enter email {i + 1}: ") for i in range(N)]
    valid_emails = extract_valid_emails(N, emails)
    print("Valid email addresses:", valid_emails)


if __name__ == "__main__":
    main()
