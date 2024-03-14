# util.py :- This file will contain the function for validating problem statement

def can_stack_cubes(n, cubes):
    left_index = 0
    right_index = n - 1
    prev_cube = float('inf')

    while left_index <= right_index:
        if cubes[left_index] >= cubes[right_index]:
            if cubes[left_index] <= prev_cube:
                prev_cube = cubes[left_index]
                left_index += 1
            else:
                return False
        else:
            if cubes[right_index] <= prev_cube:
                prev_cube = cubes[right_index]
                right_index -= 1
            else:
                return False

    return True

