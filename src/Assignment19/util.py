# util.py :- This file will contain the function for validating problem statement
def execute_commands(commands):
    result = []
    for command in commands:
        operation, *args = command.split()
        if operation == 'insert':
            i, e = map(int, args)
            result.insert(i, e)
        elif operation == 'print':
            print(result)
        elif operation == 'remove':
            e = int(args[0])
            result.remove(e)
        elif operation == 'append':
            e = int(args[0])
            result.append(e)
        elif operation == 'sort':
            result.sort()
        elif operation == 'pop':
            result.pop()
        elif operation == 'reverse':
            result.reverse()
    return result
