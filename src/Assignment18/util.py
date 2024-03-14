# util.py :- This file will contain the function for validating problem statement
import re


def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def extract_valid_emails(N, emails):
    valid_emails = [email for email in emails if is_valid_email(email)]
    return sorted(valid_emails)
