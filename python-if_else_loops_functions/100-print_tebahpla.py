#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((c + (ord('A') - ord('a'))) if c % 2 else c), end='')
