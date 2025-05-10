#include <iostream>


int main()
{
    bool b;
    int i;
    char c;
    float f;
    double d;

    std::cout << "Type a bollean: ";
    std::cin >> b;
    std::cout << "You typed: " << b << std::endl;

    std::cout << "Type a int: ";
    std::cin >> i;
    std::cout << "You typed: " << i << std::endl;

    std::cout << "Type a char: ";
    std::cin >> c;
    std::cout << "You typed: " << c << std::endl;

    std::cout << "Type a float: ";
    std::cin >> f;
    std::cout << "You typed: " << f << std::endl;

    std::cout << "Type a double: ";
    std::cin >> d;
    std::cout << "You typed: " << d << std::endl;

    return 0;
}
