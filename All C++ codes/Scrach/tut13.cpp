// Arrays

#include<iostream>
using namespace std;

int main(){
    int marks[] = {23, 45, 56, 89};
    cout<<"These are marks"<<endl;
    // cout<<marks[0]<<endl;
    // cout<<marks[1]<<endl;
    // cout<<marks[2]<<endl;
    // cout<<marks[3]<<endl;
    
    
    // using for loop to print array
    for (int i = 0; i < 4; i++)
    {
        cout<<"The value of marks "<<i <<"is: "<<marks[i]<<endl;
    }

    // Using while loop
    // int index = 0; 
    // while (index < 4) { 
    //     cout << marks[index] << endl; 
    //     index++; 
    // }
    
    // Using do-while loop
    // int index = 0;
    // do {
    //     cout << marks[index] << endl; 
    //     index++; 
    // } while (index < 4); 
    
    int mathmarks[4];
    mathmarks[0] = 53; 
    mathmarks[1] = 84;
    mathmarks[2] = 21;
    mathmarks[3] = 90;

    cout<<"These are mathmarks"<<endl;
    mathmarks[1] = 455;       // Way to change the value in array
    cout<<mathmarks[0]<<endl;
    cout<<mathmarks[1]<<endl;
    cout<<mathmarks[2]<<endl;
    cout<<mathmarks[3]<<endl;

    
    return 0;
}