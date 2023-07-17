// WAP to find second largest number in the integer array

#include<stdio.h>

int main()
{
    int arr[10]={3,90,65,4,23,56,87,5,78,34};
    int max=0;
    int sec_max=0;

    for(int i=0;i<10;i++)
    {
        if(i==0)
        {
            max=arr[i];
        }
        else if(max<arr[i])
        {
            max=arr[i];
        }
        else if (arr[i]>sec_max && arr[i]<max)
        {
            sec_max=arr[i];
        }
    }
    printf("Second largest :%d",sec_max);
}