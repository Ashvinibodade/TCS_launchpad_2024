// Count each vowel separatly and return the count for each vowel

#include<stdio.h>

int main()
{
    char s[100];
    int i=0,counta=0,counte=0,counti=0,counto=0,countu=0;

    printf("Enter the string:");
    scanf("%s",s);

    while(s[i]!='\0')
    {
        if((s[i]=='a') || (s[i]=='A'))
        {
            counta++;
        }
        if((s[i]=='e') || (s[i]=='E'))
        {
            counte++;
        }
        if((s[i]=='i') || (s[i]=='I'))
        {
            counti++;
        }
        if((s[i]=='o') || (s[i]=='O'))
        {
            counto++;
        }
        if((s[i]=='u') || (s[i]=='U'))
        {
            countu++;
        }
        i++;
    }

    printf("Number of a vowel in the string:%d\n",counta);
    printf("Number of e vowel in the string:%d\n",counte);
    printf("Number of i vowel in the string:%d\n",counti);
    printf("Number of o vowel in the string:%d\n",counto);
    printf("Number of u vowel in the string:%d\n",countu);
}