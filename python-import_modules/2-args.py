#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv)
    print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
                                 "." if leng == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
