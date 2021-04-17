#!/usr/bin/python3





def find_duplicate_number(numbers):

    stack = list()
    number = None
    for x in numbers:
        number = x
        if x not in stack:
            stack.append(x)
        else:
            break

    
    return number


print(find_duplicate_number([3,1,3,4,2]))