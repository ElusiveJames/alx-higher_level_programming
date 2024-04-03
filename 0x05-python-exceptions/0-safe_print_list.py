#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for value in my_list[:x]:
            print(f"{value}", end="")
            count += 1
    except IndexError:
        print('IndexError')
    print('')
    return count
