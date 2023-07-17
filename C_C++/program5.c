// Reading date as ddmmyyyy and displaying day,month,year

#include<stdio.h>
#include<string.h>

int main()
{
    char s[100];
    int i=0;
    
    printf("Enter the string:");
    scanf("%s",&s);

    printf("\nDay is:%c%c",s[0],s[1]);
    printf("\nMonth is:%c%c",s[2],s[3]);
    printf("\nYear is:%c%c%c%c",s[4],s[5],s[6],s[7]);

    printf("\n-----------Another Way------------------");

    printf("\nDay :");
    for(i=0;i<2;i++)
    {
        printf("%c",s[i]);
    }
    printf("\nMonth :");
    for(i=2;i<4;i++)
    {
        printf("%c",s[i]);
    }
    printf("\nYear :");
    for(i=4;i<strlen(s);i++)
    {
        printf("%c",s[i]);
    }
}