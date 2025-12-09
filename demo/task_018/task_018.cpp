#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> digits(1, 1);

    for (int k = 2; k <= N; k++) {
        int carry = 0;
        for (int i = 0; i < digits.size(); i++) {
            int product = digits[i] * k + carry;
            digits[i] = product % 10;
            carry = product / 10;
        }

        while (carry) {
            digits.push_back(carry % 10);
            carry /= 10;
        }
    }

    for (int i = digits.size() - 1; i >= 0; i--) {
        cout << digits[i];
    }

    return 0;
}