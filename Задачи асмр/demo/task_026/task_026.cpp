#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x1, y1, r1, x2, y2, r2;
    cin >> x1 >> y1 >> r1;
    cin >> x2 >> y2 >> r2;

    int dx = x1 - x2;
    int dy = y1 - y2;
    int distance_sq = dx * dx + dy * dy;
    int sum_r = r1 + r2;
    int diff_r = abs(r1 - r2);

    if (distance_sq <= sum_r * sum_r && distance_sq >= diff_r * diff_r) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}