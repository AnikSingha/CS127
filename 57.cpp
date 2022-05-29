//Name:Anik Singha
//Email:anik.singha68@myhunter.cuny.edu
//Date: September 16, 2021
//Print responses based on temperature from input

#include <iostream>
using namespace std;

int main() {
    int temp;
    cout << "Enter the temperature: ";
    cin >> temp;
    if (temp <= 32) {
        cout << "It's freezing!";
    }
    else if (temp < 68) {
        cout << "It's cold";
    }
    else if (temp < 73){
        cout << "It's warm";
    }
    else if (temp >= 73){
        cout << "It's hot";
    }
}