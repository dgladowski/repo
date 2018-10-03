#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#
# DANE WEJŚCIOWE liczba l2 dwucyfrowa podawana przez użytkownika
# DANE WYJŚCIOWE suma cyfr podanych przez użytkownika
# jupyter qtconsole


def main(args):

    suma = 0
    l2 = int(input("Podaj liczbę: "))

    while l2 < 10:
        l2 = int(input("Podaj liczbę: "))

    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
        print("Suma cyfr: ", suma)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


