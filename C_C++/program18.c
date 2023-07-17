// Sort the array (use any basis algorithum)

#include<stdio.h>

int main()
{
    int arr[10]={3,90,65,4,23,56,87,5,78,34};

    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }

    for(int i=0;i<10;i++)
    {
        printf("%d ",arr[i]);
    }
}