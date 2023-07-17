// Reverse of the string

#include<stdio.h>

int main()
{
    int a,c,rem;

    printf("Enter number:");
    scanf("%d",&a);

    c=a;
    rem=0;
    printf("Before reverse:%d",c);
    while(a!=0)
    {
        rem=(rem*10)+(a%10);
        a=a/10;
    }
    printf("\nAfter reverse:%d",rem);


}