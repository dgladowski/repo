#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  

def potega_it(a, n):
    
    # a^n = a1 * a2 * ... * an
    # a^1 = a
    
    iloczyn = 1
    for i in range (n):
        iloczyn = iloczyn * a
    return iloczyn

def main(args):
    a = int(input("Podaj podstawę potęgi"))
    n = int(input("Podaj wykładnik potęgi"))
    print("{} do poręgi {} wynosi {}".format(a, n, potega_it(a, n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
