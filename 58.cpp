//Name:Anik Singha
//Email:anik.singha68@myhunter.cuny.edu
//Date: September 16, 2021
//Print a trapezoid using a character

#include <iostream>
using namespace std;

int main(){
    int num;
    string character;
    string sent;
    cout << "Please enter a number: ";
    cin >> num;
    cout << "Please enter a character: ";
    cin >> character;
    for (int x = 0; x < num; x++){
            sent += character;
            cout << sent << '\n';
        }
    for (int x = 0; x < num; x++){
        cout << sent << '\n';
    }
}