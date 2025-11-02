#include<iostream>
using namespace std;

// Selection control structure: If-else ladder
int main(){
    int age;
    cout<<"Tell me your age"<<endl;
    cin>>age;
    if((age<18) && (age>0)){
        cout<<"No Party"<<endl;
    }
    else if(age == 18){
        cout<<"Partially allowed"<<endl;
    }
    else if(age<1){
        cout<<"Not yet born"<<endl;
    }
    else{
        cout<<"You are allowed"<<endl;
    }

    return 0;
}