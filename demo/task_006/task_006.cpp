#include <iostream>
#include <string>
using namespace std;

int main()
{
    string move;
    getline(cin, move);

    if (move.length() != 5) {
        cout << "ERROR";
        return 0;
    }

    if (move[0] < 'A' || move[0] > 'H' ||
        move[1] < '1' || move[1] > '8' ||
        move[2] != '-' ||
        move[3] < 'A' || move[3] > 'H' ||
        move[4] < '1' || move[4] > '8') {
        cout << "ERROR";
        return 0;
    }

    int dx = abs(move[3] - move[0]);
    int dy = abs(move[4] - move[1]);

    if ((dx == 1 && dy == 2) || (dx == 2 && dy == 1)) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}