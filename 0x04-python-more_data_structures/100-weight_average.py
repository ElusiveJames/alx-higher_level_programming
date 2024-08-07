#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    total_weight = 0
    total_score = 0
    for score, weight in my_list:
        total_weight += weight
        total_score += score * weight
    return total_score / total_weight
