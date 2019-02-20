/*
 * gladowski_zloznosc_alg1.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{   int a = 0;
    cout << "Podaj liczbę a: ";
    cin >> a;
    if (a <= 0 or a > 99) {
        cout << "Podaj liczbę a: ";
        cin >> a;
        }

    for (int i = 2; i < 101; i += 2) {
        if (a == i) {
            cout << "a jest liczbą parzystą";
            break;
            }
        if (i == 100) {
            cout << "a jest liczbą nieparzystą";
        }
    }

    return 0;
}

