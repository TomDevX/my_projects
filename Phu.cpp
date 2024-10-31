// Đề bài: Cho người dùng nhập vào số n, in ra số nguyên tố từ 1-n. DO ITTTT
#include <iostream>
 
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i = 2;i <= n;i++){
        for(int j = 2;i <= n;i++){
            if(i%i != 0){
                cout << i << "\n";
            }
        }
        }
}