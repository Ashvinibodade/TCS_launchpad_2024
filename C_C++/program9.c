// Print odd position substring

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

    while(s[i]!='\0')
    {
        if(i%2==0)
        {
            news[j]=s[i];
            j++;
        }
        i++;
    }
    printf("The odd position substring:%s",news);

    printf("\n");

    // another simpler version to solve this

    for (i=0;s[i]!='\0';i+=2)
    {
        printf("%c",s[i]);
    }
    return 0;
}