// WAp to reverse the string without using any library function and pointer

#include<stdio.h>
#include<string.h>

int main()
{
    char str1[150] ;
    int i,j;

    printf("Enter the string :");
    scanf("%s",str1);

    j=strlen(str1)-1;

    for(i=j;i>=0;i--)
    {
        printf("%c",str1[i]);
    }
}