"""
Problem Statement : -
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T , the number of testcases.
Each testcase contains  2 lines, representing time t1  and time t2 .

Constraints

Input contains only valid timestamps
.
Output Format

Print the absolute difference(t1-t2)  in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200
"""
"""
Sample Output :-
Enter the number of testcases: 2
Enter timestamp 1: Sun 10 May 2015 13:54:36 -0700
Enter timestamp 2: Sun 10 May 2015 13:54:36 -0000
Absolute difference in seconds: 25200
Enter timestamp 1: Sun 02 May 2015 19:54:36 +0530
Enter timestamp 2: Sat 01 May 2015 13:54:36 -0000
Absolute difference in seconds: 88200

Process finished with exit code 0
"""
# driver.py :This file will prompt the user to enter a two different time stamp and
# # then call the def get_time_difference_in_seconds(time1, time2): function
# from util.py to get difference of date in seconds.

from util import get_time_difference_in_seconds


def main():
    # Input
    num_testcases = int(input("Enter the number of testcases: "))
    for _ in range(num_testcases):
        t1 = input("Enter timestamp 1: ")
        t2 = input("Enter timestamp 2: ")

        # Output
        difference = get_time_difference_in_seconds(t1, t2)
        print("Absolute difference in seconds:", difference)


if __name__ == "__main__":
    main()
