"""
Problem Statement : -
There is an array of  integers. There are also  disjoint sets,  A and B , each containing m  integers. You like all the integers in set  A and dislike all the integers in set B . Your initial happiness is 0 . For each i integer in the array, if i A , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers n  and  m separated by a space.
The second line contains  n integers, the elements of the array.
The third and fourth lines contain m  integers,  A and B , respectively.

Output Format

Output a single integer, your total happiness.

"""
"""
Sample Output :-
Enter n and m separated by a space: 3 2
Enter the elements of the array: 1 5 3
Enter the elements of set A: 3 1
Enter the elements of set B: 5 7
Total happiness: 1

"""
# driver.py :This file will prompt the user to Enter n and m separated by a space: and
#  and Enter the elements of the array and set A 's element and set B's element :
#  then call the function calculate_happiness
# from util.py to get value of Total happiness:"
from util import calculate_happiness


def main():
    n, m = map(int, input("Enter n and m separated by a space: ").split())
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    A = set(map(int, input("Enter the elements of set A: ").split()))
    B = set(map(int, input("Enter the elements of set B: ").split()))

    happiness = calculate_happiness(n, m, arr, A, B)
    print("Total happiness:", happiness)


if __name__ == "__main__":
    main()
