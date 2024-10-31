#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int longestIncreasingSubsequenceLength(vector<int>& arr) {
    int n = arr.size();
    vector<int> dp(n, 1);

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    
    return *max_element(dp.begin(), dp.end());
}

int main() {
    int N;
    cin >> N; // Đọc số lượng phần tử trong dãy
    vector<int> A(N);
    
    // Đọc dãy số nguyên A
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    // Tìm độ dài của dãy con tăng đơn điệu dài nhất
    int result = longestIncreasingSubsequenceLength(A);
    
    // Xuất kết quả
    cout << result << endl;
    
    return 0;
}
