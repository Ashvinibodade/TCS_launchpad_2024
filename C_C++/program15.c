// WAP to print array holding the sum of elements at respective indices of two same sized array
// Get elements from user for a[5] and b[5]  and hold the result in c[5]
// Print array element of result in separate lines with indices stating values of two arrays

#include<stdio.h>

int main()
{
    int n=5;
    int a[n] ,b[n] ,c[n];

    printf("Enter data for array a:");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    printf("Enter data for array b:");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&b[i]);
    }

    printf("Final resultant array:");
    for(int i=0;i<n;i++)
    {
        c[i]=a[i]+b[i];
    }
    for(int i=0;i<n;i++)
    {
        printf("%d ",c[i]);
    }
}