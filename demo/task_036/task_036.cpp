#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    int limit = 2 * n;
    vector<bool> is_prime(limit + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i * i <= limit; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }

    int count = 0;
    for (int p = n + 1; p < 2 * n; p++) {
        if (is_prime[p]) {
            count++;
        }
    }

    cout << count;
    return 0;
}