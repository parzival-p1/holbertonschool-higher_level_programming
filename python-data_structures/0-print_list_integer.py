#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for elm in my_list:
        print_list_integer("{:d}".format(elm))
