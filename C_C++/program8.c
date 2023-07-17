// WOrd count in the sentence

#include<stdio.h>
#include<string.h>
#define MAX 1000

int main()
{
    char s[100];
    int i,totalwords;
    totalwords=0;
    i=0;

    printf("Enter the string :");
    fgets(s,MAX,stdin);

    while(s[i]!='\0')
    {
        if(s[i]==' ')
        {
            totalwords++;
        }
        i++;
    }
    printf("Total no of words in the string :%d",totalwords+1);
    return 0;
}