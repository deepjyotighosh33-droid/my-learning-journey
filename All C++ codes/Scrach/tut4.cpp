#include<iostream>
using namespace std;

int c = 45; //Global c

int main(){
    int a, b, c;
    cout<<"Enter value of a: "<<endl;
    cin>>a;
    cout<<"Enter value of b: "<<endl;
    cin>>b;

    c = a + b; //Local c

    cout<<"The sum is: "<< c<< endl;
    cout<<"The global c is: "<< ::c;

    return 0;
}