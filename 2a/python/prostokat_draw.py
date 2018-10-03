#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat_draw.py
#  
#  DANE WEJŚCIOWE: boki a i b prostokata
#  DANE WYJŚCIOWE: prostokąt narysoowany w terminalu gwiazdkami o rozmiarach podanych przez użytkownika 
#
#  EXTRA: znak, który rysowany jest prostokąt, pobierz od uzytkownika
#


def main(args):
    a = int(input("Podaj długośc pierwszego boku: "))
    b = int(input("Podaj długośc drugiego boku: "))
    c = str(input("Podaj znak, którym ma być rysowany prostokąt: "))

    for a in range(1, a + 1, 1):
        print(b * c)
        for b in range(2, b + 2, 1):
            print(c, " ", c)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
