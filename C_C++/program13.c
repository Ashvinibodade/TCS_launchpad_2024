// find sum of even and odd digits

#include<stdio.h>

int main()
{
    int a;
    int rem;
    int even=0,odd=0;
    printf("Enter the number:");
    scanf("%d",&a);

    while(a!=0)
    {
        rem=a%10;
        if(rem%2==0)
        {
            even+=rem;
        }
        else
        {
            odd+=rem;
        }
        a=a/10;
    }
    printf("Even sum:%d \n Odd sum:%d",even,odd);
}