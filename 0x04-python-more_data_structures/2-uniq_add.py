#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    sum = 0
    for idx in range(len(new_list)):
        sum += new_list[idx]
    return sum
