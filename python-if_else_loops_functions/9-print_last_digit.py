#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_ = number % -10
        print("{:d}".format(-(last_)), end='')
        return(-(last_))
    else:
        last_ = number % 10
        print("{:d}".format(last_), end='')
        return(last_)
