#include<iostream>
#include<string>
using namespace std;

class teacher {
    // properties or attributes
    private:
    double salary;

    public:
    // non - parametarized
    teacher(){
        dept = "Computer Science";
    }

    string name;
    string dept;
    string subject;
    

    // methods or memberfunction
    void changeDept(string newDept){
        dept = newDept;
    }

    // setter
    void setSalary(double s){
        salary = s;
    }

    // getter
    double getSalary(){
        return salary;
    }
};


int main() { 
    teacher t1; //constructor call
    t1.name = "Shradha";
    t1.subject = "C++";
    t1.setSalary(25000);

    cout << "Teacher Name: " << t1.name << endl;
    cout << t1.getSalary() << endl;
    cout << t1.dept << endl;

   return 0;
}