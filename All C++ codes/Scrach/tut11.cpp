#include<iostream>
using namespace std;

int main(){

    for (int i = 0; i <= 40; i++)
    {
        if (i==2)
        {
            break; // Same for "continue"
        }
        
        cout<<i<<endl;
    }

    return 0;
    
}