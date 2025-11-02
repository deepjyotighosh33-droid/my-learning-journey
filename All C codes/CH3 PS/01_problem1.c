#include <stdio.h>

int main(){
    int a = 10;
    if(a = 11){
        printf("I am 11");
    }
    else{
        printf("I am not 11");
    }
    return 0;
}

// returns "I am 11" cause = is a assignmet operator insteads use 
// a == 11 (Correct)