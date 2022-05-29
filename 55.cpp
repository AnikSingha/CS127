//Name:Anik Singha
//Email:anik.singha68@myhunter.cuny.edu
//Date: September 16, 2021
//Cryptocurrency converter

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    float amount;
    cout << "Enter amount in cryptocurrency: ";
    cin >> amount;
    cout << fixed << setprecision(2);
    cout << amount << " BTC in USD: $" << amount * 31901.19 << '\n';
    cout << amount << " ETH in USD: $" << amount * 1901.54 << '\n';
    cout << amount << " DOGE in USD: $" << amount * 0.179733;
}