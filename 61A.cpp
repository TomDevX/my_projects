#include <iostream>

using namespace std;

int main(){
    string s1;
    string s2;
    cin >> s1 >> s2;

    for (int i = 0; i < s1.length(); i++){
        if (s1[i] == s2[i]){
            cout << 0;
        } else {
            cout << 1;
        }
    }
}