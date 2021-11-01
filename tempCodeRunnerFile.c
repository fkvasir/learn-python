#include <stdio.h>

int main(){
    int num1,num2,mod;

    printf("Enter 3 digit number:\n");
    scanf("%d",&num1);
    printf("Enter 2 digit number:\n");
    scanf("%d",&num2);
    printf("    %d\n x   %d\n-------\n",num1,num2);
    mod = (num2%10);
    printf("    %d\n + %d \n-------\n   %d\n",num1*mod,num1*((num2-mod)/10),num1*num2);

    return 0;
}
