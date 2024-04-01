#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    new_list = list(a_dictionary)
    for key in new_list:
        count += 1
    return count
