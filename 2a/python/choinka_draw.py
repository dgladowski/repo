#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  choinka_draw.py
#  


def main(args):
    a = int(input("Podaj wysokość: "))
    c = str(input("Podaj znak: "))

    for a in range(10, a + 1):
        print(a * c)
        
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
