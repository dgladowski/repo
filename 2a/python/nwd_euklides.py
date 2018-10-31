#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd_euklides.py
#

def nwd(a, b):

    while a != b:
        if a > b:
            a = a - b
        if a < b:
            b = b - a

    return a


def main(args):
    b = int(input("Podaj drugą liczbę: "))
    a = int(input("Podaj pierwszą liczbę: "))
    print("Największy wspólny dzielnik {} i {} to {}" .format(a, b, nwd(a, b)))

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
