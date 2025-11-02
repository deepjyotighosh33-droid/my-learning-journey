// Pointers

#include<iostream>
using namespace std;

int main(){
    int a = 3;
    int* b = &a;
    // & ----> (Address of) operator
    cout<<"The address of a is: "<<&a<<endl; //} same output, shows the memory
    cout<<"The address of a is: "<<b<<endl;  //} same output, shows the memory
    
    // * ---> (Value at) Dereference operator
    cout<<"The value at address b is: "<<*b<<endl;
    
    // Pointer to pointer (A pointer which stores address of other pointers)
    int** c = &b;
    cout<<"The address of b is: "<<&b<<endl;  //} same output, shows the memory
    cout<<"The address of b is: "<<c<<endl;  //} same output, shows the memory
    cout<<"The value at address c is: "<<*c<<endl;
    cout<<"The value at address value_at(value_at(c)) is: "<<**c<<endl;


    return 0;
}