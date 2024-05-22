#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    int len = len(my_list) - 1
    if idx < 0:
        return my_list
    if idx > len:
        return my_list
    else:
        my_list[idx] = element
    return my_list
