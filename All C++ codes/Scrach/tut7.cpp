#include<iostream>
using namespace std;

// Selection control structure: switch case statement

int main(){
    int age;
    cout<<"Tell me your age"<<endl;
    cin>>age;

    switch (age)
    {
    case 18:
        cout<<"You are 18";
        break;
    case 22:
        cout<<"You are 22";
        break;
    case 2:
        cout<<"You are 2";
        break;
    
    default:
    cout<<"No special cases"<< endl;
        break;
    }

    return 0;
}