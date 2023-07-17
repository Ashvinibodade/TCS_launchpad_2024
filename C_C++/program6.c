// Count the number of vowel present in the string

#include<stdio.h>

int main()
{
    char s[100];
    int i=0,count=0;

    printf("Enter the string:");
    scanf("%s",s);

    while(s[i]!='\0')
    {
        if((s[i]=='a') || (s[i]=='A') || (s[i]=='e') || (s[i]=='E') || (s[i]=='i') || (s[i]=='I') || (s[i]=='o') || (s[i]=='O') || (s[i]=='u') || (s[i]=='U'))
        {
            count++;
        }
        i++;
    }
    printf("Number of vowel present in the string:%d",count);
    return 0;
}