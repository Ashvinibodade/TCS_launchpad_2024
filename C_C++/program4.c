// Reverse the string as a whole and printing the reversed string

#include<stdio.h>
#include<string.h>

int main()
{
    char s[100] ;
    char temp;
    int i=0,j=0;

    printf("Enter the string:");
    scanf("%s",&s);

    j=strlen(s)-1;

    while(i<j)
    {
        temp=s[j];
        s[j]=s[i];
        s[i]=temp;

        i++;
        j--;
    }

    printf("Reversed string :%s",s);
}