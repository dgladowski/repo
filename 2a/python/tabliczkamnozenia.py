#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczkamnozenia.py
#  

def tabliczka(a, b):
    
    """
    Drukuje tabliczke mnożenia dla podanego zakresu 
    """
    
    for i in range(1, a + 1, 1): # pętla zewnętrzna
        for j in range(1, b + 1): # pętla wewnętrzna
            print("{:>3}".format(i * j), end='')
        print() # znak końca linii, przejscie do nastepnego wiersza
    
def main(args):
    a = int(input("Podaj zakres 1: "))
    b = int(input("Podaj zakres 2: "))
    tabliczka(a, b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
