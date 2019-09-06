#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cw3.py
#  
#  Copyright 2019  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    # losowanie liczb
    liczby = []  # lista wylosowanych liczb
    i = 0  # lista wylosowanych liczb
    # print("Wylosowano:", liczba)
    # pobranie typu użytkownika
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba + 1)  # losowanie liczby <1; 10>
        if liczby.count(liczba) == 0:  # sprawdzenie czy wartość jest w liście
            liczby.append(liczba)
            i += 1  # powiększ i o jeden
    print(liczby)

    typy = set()  # deklaracja pustego zbioru na typy użytkownika
    i = 0
    while i < ileliczb:
            typ = input("Podaj liczbę {}:".format(i + 1))
            if typ not in typy:  # jeżeli podanego typu nie ma w zbiorze
                typy.add(typ)
                i += 1
    print(typy)

    # odp = input("Podaj liczbę od 1 do 10: ")
    # print("Podana liczba: ", odp)
    # if liczba == odp:  # porównywanie z wylosowaną liczbą
    #     print("Zgadłeś!")
    #     break  # przerwanie działania pętli
    # else:
    #     print("Spróbuj ponownie")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
