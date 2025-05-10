#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;


int main() {
    vector<string> vetor = {"AB", "CD", "EF", "GH"};

    for (auto i: vetor) cout << i << " ";
    cout << endl;
    reverse(vetor.begin(), vetor.end());
    for (auto i: vetor) cout << i << " ";
    cout << endl;

    vector<string> v;
    for (auto i: vetor) {
        v.push_back(i);
    }
    for (auto i: v) cout << i << " ";

    return 0;
}
