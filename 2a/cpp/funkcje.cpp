/*
 * szkielet.cpp
 *
 */


#include <iostream>
/* io input/output czyli biblioteka wejścia/wyjścia w pythonie nie trzeba tego importować
 * zawsze musi być main bo to nazwa funkcji*/

using namespace std;

void suma(int a, int b) {
    int wynik = a + b;
    cout << wynik;
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
   
    cout << "Podaj liczbę 1: ";
    cin >> a;
    cout << a;

    cout << endl << "Podaj liczbę 2: ";
    cin >> b;
    ,
    cout << b;
   
    cout << endl << "Suma: " << a + b << endl;
    cout << endl << "Różnica: " << a - b << endl;
    cout << endl << "Iloczyn: " << a * b << endl;
    cout << endl << "Iloraz: " << a / b << endl;
    return 0;
}

//DRY dont repeat yourself

