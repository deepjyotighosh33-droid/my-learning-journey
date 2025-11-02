#include <stdio.h>

int main(){
    int a = 9;
    int b = 2;
    float c = a/b;
    printf("Value a/b(int & int) is %f", c);
    // Output is 4.0 and not 4.5 cause int & int is int
    /* int and int - int
       int and float - float
       float and float - float
    */

// Correct syntax
    float d = 9.0;
    int e = 2;
    float f = d/e;
    printf("\nValue d/e(float & int) is %f", f);

    int k = 3.0/9;
    printf("\nK = %d", k);
    // 3.0 is float, but when typed as int, its type changes to int and becomes 3, therefore type demosion

    return 0;

}