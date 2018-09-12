#!/usr/bin/env python
# -*- coding: utf-8 -*-
#duck typing
#wszystko co pobierane jest z domyślnego wejścia z terminala jest znakiem
# zasięŋ zmiennych: zasięg lokalny (ograniczony np. funkcją)

def suma(a, b):
    return a + b
    
    
def różnica(a, b):
    return a - b
    
    
def iloczyn(a, b):
    return a * b    


def iloraz(a, b):
    return a / b
    
    
def main(args):
    a = int(input("Podaj liczbę 1: "))
    b = int(input("Podaj liczbę 2: "))
    print(a)
    print(b)
    
    print("Suma: ", suma(a, b))
    print("Różnica: ", różnica(a, b))
    print("Iloczyn: ", iloczyn(a, b))
    print("Iloraz: ", iloraz(a, b))

    
    return 0    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
