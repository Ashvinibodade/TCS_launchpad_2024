// Print even position substring

#include<stdio.h>
#include<string.h>
#define MAX 1000

int main()
{
    char s[100];
    char news[100];
    int i,j;
    i=0;
    j=0;

    printf("Enter the string :");
    fgets(s,MAX,stdin);

    for (i=1;s[i]!='\0';i+=2)
    {
        printf("%c",s[i]);
    }
    return 0;
}