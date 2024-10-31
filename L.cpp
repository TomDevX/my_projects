#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int x, int y){
    while (x*y != 0){
        if (x > y){
            x = x - y;
        }
        else{
            y = y - x;
        }
    }
    return x + y;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a;
        vector<int> even;
        vector<int> odd;

        // divide into even and odd
        for (int i = 0; i < n; i++){
            int x;
            cin >> x;
            if (x % 2 == 0) {
                even.push_back(x);
            } else {
                odd.push_back(x);
            }
        }

        for (int i : even){
            a.push_back(i);
        }
        for(int i : odd){
            a.push_back(i);
        }
        
        // count
        int count = 0;
        for (int i = 0; i < a.size()-1; ++i) {
            for (int j = i + 1; j < a.size(); ++j) {
                if(gcd(a[i], a[j] * 2) > 1){
                    count++;
                }
            }
        }
        cout << count << endl;
    }
}

