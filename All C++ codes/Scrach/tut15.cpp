#include<iostream>
using namespace std;

// structure
//using typedef 'ep' - not need to write 'struct eployee' we write 'ep employee' instead
typedef struct employee    
{
    /* data */
    int eID;
    char favChar;
    float salary;
}ep ;

// Union
// U can use only one of these 3 cause your memory is been shared
union money    
{
    /* data */
    int rice; 
    char car;
    float pounds;
};

int main(){ 
    
    // Structure
    ep DJ;                         // U can either use ep 
    struct employee Harry;         // or just type 'struct employee'
    struct employee Rohandas;      // can make as many employee u want
    DJ.eID = 1;
    DJ.favChar = 'C';
    DJ.salary = 12000000000;
    cout<<"The value is "<<DJ.eID<<endl;
    cout<<"The value is "<<DJ.favChar<<endl;
    cout<<"The value is "<<DJ.salary<<endl;

    // Union
    union money m1;
    m1.rice = 34;
    m1.car = 'c';
    cout<<m1.car<<endl;

    // Enum
    // all the values inside enum will be allocated as 0, 1, 2, 3.....
    enum Meal{breakfast, lunch, dinner}; // Meal is now a data type
    Meal k1 = lunch;
    cout<<(k1==1); //if true then returns 1, if false returns 0

    // cout<<breakfast<<endl;   //Also can be used like this
    // cout<<lunch<<endl;
    // cout<<dinner<<endl;

    return 0;
}