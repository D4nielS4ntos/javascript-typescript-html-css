#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<string> vetor = {"AB", "CD", "EF", "GH"};

    vector<string>::iterator itP = vetor.begin();
    vector<string>::iterator itF = vetor.end()-1;
    string primeiro = *itP;
    string ultimo = *itF;
    cout << "primeiro: " << primeiro << endl << "ultimo: " << ultimo << endl;

    cout << "----------------------------------------------" << endl;
    
    cout << "primeiro: " << vetor.front() << endl << "ultimo: " << vetor.back() << endl;

    return 0;
}
