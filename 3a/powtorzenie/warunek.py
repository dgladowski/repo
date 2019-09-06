#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  



def main(args):
    a = int(input("Podaj 1-szą liczę: "))
    b = int(input("Podaj 2-gą liczę: "))
    c = int(input("Podaj 3-cią liczę: "))
    print(a)
    print(b)
    print(c)

    if a > b and a > c:
        print ("Największą liczbą jest: ", a)
    elif b > a and b > c:
        print ("Największą liczbą jest: ", b)
    else:
        print ("Największą liczbą jest: ", c)

    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
