#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gladowski_zaleznosc_alg2.py
#  


def main(args):
    a = int(input("Podaj a: "))
    if (a <= 0 or a > 100):
        a = int(input("Podaj a: "))

    for i in range(2, a + 2, 2):
        if (a == i):
            print("a jest liczbą parzystą")
            break
        if (i > a):
            print("a jest liczbą nieparzystą")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
