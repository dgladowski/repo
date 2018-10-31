#include <iostream>

using namespace std;

int liczby2() {
    int ile = 0; //deklaracja + inicjacja = definicja
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (i != j) {
            cout << i << j << " ";
            ile++;
            }
        }
    }
    return ile;
}

int liczby3() {
    int ile2 = 0;
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (i != j) {
            cout << i << j << " ";
            ile++;
            }
        }
    }
}

return



int main(int argc, char **argv)
{
    int ile = liczby2();
    cout << "\n\nIlość liczb dwucyfrowych: " << ile << endl;
    return 0;
}

