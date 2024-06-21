#include "calculator.h"
#include <stdexcept>

double Calculator::add(double a, double b){
    return a+b;
}

double Calculator::subtract(double a, double b){
    return a-b;
}
double Calculator::multiply(double a, double b){
    return a*b;
}

double Calculator::divide(double a, double b){
    if(b == 0){
        throw std::runtime_error("If divided by zero");
        
    }
    else{
        return a/b;
    }
}

double Calculator::modulo(double a, double b){
    return static_cast<int>(a) % static_cast<int>(b);
}