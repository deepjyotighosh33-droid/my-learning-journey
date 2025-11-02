/* Precedence 
1st - *, /, % (left to right)
2nd - +, -    (left to right)   
3rd - =
In case of same precedence, associativity will take care
Tip - always use parenthesis () 
*/ 

#include <stdio.h>

int main(){
    int a = 3;
    int b = 6;
    int c = 9;

    printf("The value is %d\n", a*b/c + 7);
    
// Advanced 
    printf("The value is %d\n", 3*b/2*c + 7*a);

    return 0;
}