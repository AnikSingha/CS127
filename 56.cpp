//Name:Anik Singha
//Email:anik.singha68@myhunter.cuny.edu
//Date: September 16, 2021
//Count down

#include <iostream>
using namespace std;

int main(){
    int num;
    string word;
    cout << "Please enter a number: ";
    cin >> num;
    cout << "Please type a word: ";
    cin >> word;
    while (num > 0){
        cout << num << ',' << '\n';
        num--;
    }
    cout << "Time for " << word << '!';
}