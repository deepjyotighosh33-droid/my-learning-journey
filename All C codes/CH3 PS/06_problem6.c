#include <stdio.h>

int main(){
    int a, b, c ,d ;
    printf("Enter 1st numbers\n");
    scanf("%d", &a);
    printf("Enter 2nd numbers\n");
    scanf("%d", &b);
    printf("Enter 3rd numbers\n");
    scanf("%d", &c);
    printf("Enter 4th numbers\n");
    scanf("%d", &d);
    if(a>b && a>c && a>d){
        printf("The greatest of all is %d", a);
    }
    else if(b>a && b>c && b>d){
        printf("The greatest of all is %d", b);
    }
    else if(c>a && c>b && c>d){
        printf("The greatest of all is %d", c);
    }
    else if(d>a && d>c && d>b){
        printf("The greatest of all is %d", d);
    }
    return 0;
}