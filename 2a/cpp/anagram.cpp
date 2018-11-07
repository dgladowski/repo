/*
 * anagram.cpp
 */


#include <iostream>

using namespace std;
 // anagram() funkcja odwraca znaki w danym wyrazie
 //wyrazy funkcja odwraca znaki w wyrazach

int zlicz(char tb[]) {
    int i = 0;
    while(tb[i] != '\0') i++;
    return i;
}

void wyswietl(char tekst[], int rozmiar) {
    for(int i = 0; i < rozmiar; i++) {
        cout << tekst[i];
    }
}

void anagram(char tekst[], int rozmiar) {
// for zaczyna od ostatmniego znaku
    for (int i = rozmiar; i >= 0; i--) {
        cout << tekst[i];
    }
}

int main(int argc, char **argv)
{
    const int rozmiar = 30;
    char tekst[rozmiar];
    cout << "Podaj słowa: ";
    cin.getline(tekst, rozmiar);
    wyswietl(tekst, zlicz(tekst));
    cout << "\nSłowa zapisane od tyłu: ";
    anagram(tekst, zlicz(tekst));
   
    return 0;
}

