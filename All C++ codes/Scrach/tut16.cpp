#include <iostream>
using namespace std;

void g();
int sum(int, int); // Can use this if the sum function is written after main
int sum(int a, int b){
    int c = a + b;
    return c;
}
int main() {
    int num1, num2;
    cout<<"Enter first no: "<<endl;
    cin>>num1;
    cout<<"Enter second no: "<<endl;
    cin>>num2;
    cout<<"The sum is: "<<sum(num1, num2); // Return value function key
    g();
    return 0;
}

// Greets when its called on main, can also right on top
void g(){
    cout<<"\nHello";
}

// So basically what we did - Created a function named sum gave it the plus sequence 
// and then triggered it with main function at last