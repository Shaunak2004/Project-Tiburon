#include "calculator.h"
#include <iostream>

int main(){

    Calculator calc;
    double a, b;
    char ch; // provides you the choice to select which operations you have to do

    std::cout<< "Menu:\n";
    std::cout<< "1. Add\n";
    std::cout<< "2. Subtract\n";
    std::cout<< "3. Multiply\n";
    std::cout<< "4. Divide\n";
    std::cout<< "5. Modulo\n";
    std::cout<< "Enter your choice: ";
    std::cin>> ch;

    std::cout<< "Enter the first number: ";
    std::cin>> a;
    std::cout<< "Enter the second number: ";
    std::cin>> b;

    try{        
        double result;
        switch (ch){
            case '+':
            result = calc.add(a, b);
            break;

            case '-':
            result = calc.subtract(a, b);
            break;

            case '*':
            result = calc.multiply(a, b);
            break;

            case '/':
            result = calc.divide(a, b);
            break;

            case '%':
            result = calc.modulo(a, b);
            break;

            default:
            std::cerr << "Invalid operator chosen"<<std::endl;
            return 1;
        }
        std::cout << "Result: "<< result << std::endl;
    } catch (const std::invalid_argument& e){
        std::cerr << e.what() << std::endl;
    }
    return 0;
}