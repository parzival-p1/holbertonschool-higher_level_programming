#!/usr/bin/python3
def print_diagonal(n):
    if (n > 0):
        for i in range(n):
            for j in range(i):
                print(" ", end = "")
            print("\\")
    print("")
