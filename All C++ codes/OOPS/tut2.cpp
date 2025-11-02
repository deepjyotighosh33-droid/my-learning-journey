#include<iostream>
#include<string>
using namespace std;

class teacher {
    // properties or attributes
    private:
    double salary;

    public:
    // parametarized
    teacher(string n, string d, string s, double sal){
        name = n;
        dept = d;
        subject = s;
        salary = sal;
    }

    string name;
    string dept;
    string subject;
    

    // methods or memberfunction
    void changeDept(string newDept){
        dept = newDept;
    }

    void getInfo(){
        cout << "name:" << name << endl;
        cout << "subject:" << subject << endl;
    }

   
};


int main() { 
    teacher t1("Shradha", "ComputerScience", "C++", 25000);
    t1.getInfo();

   return 0;
}