/*
 * gladowski_lpierwsza.cpp
 * 
 */


#include<iostream>

using namespace std;

bool pierwsza(int n)
{
    if(n<2)
        return false;   //kiedy liczba jest mniejsza niż 2 to nie jest liczba pierwszą

    for(int i=2;i*i<=n;i++)
        if(n%i==0)
            return false;   //gdy znajdziemy dzielnik tejliczby, to dana liczba nie jest liczbą pierwsza
	return true;
}

int main()
{
    int n;

    cout<<"Podaj liczbę: ";
    cin>>n;

    if(pierwsza(n))
        cout<<"Liczba "<<n<<" jest liczbą pierwsza"<<endl;
    else
        cout<<"Liczba "<<n<<" nie jest liczbą pierwsza"<<endl;
    
    return 0;
}
