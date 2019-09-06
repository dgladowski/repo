#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  


def main(args):
    imie = input('Podaj imię\n')
    nazwisko = input('Podaj nazwisko\n')
    print('Witaj ', imie, nazwisko, '!')

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
