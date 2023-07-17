// FInd the maximum value before and after digit-
// E.g.for input 4452.4567 ,max is 4567 and min is 4452

#include<stdio.h>

int main()
{
    char str[50];
    gets(str);
    int val=0;
    int a=0;

    for(int i=0;str[i]!='\0';i++)
    {
        if(str[i]=='.')
        {
            val=a;
            a=0;
        }
        else
        {
            a=a*10+(str[i]-'0');
        }
    }
    printf("Maximum :");
    (val>a)?printf("%d",val):printf("%d",a);
}