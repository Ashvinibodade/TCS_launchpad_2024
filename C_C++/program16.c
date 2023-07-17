// Create a subarray of all odd numbers in array
// Subarray:
// A subarray ia a continuous part of array.An array that is inside another array .For example ,consider the 
// array [1,2,3,4] ,There are 10 non-empty sub-arrays.The subarrays are (1),(2),(3),(4),(1,2),(2,3),(3,4),(1,2,3),
// (2,3,4),(1,2,3,4) 

#include<stdio.h>

int main()
{
    int arr[100];
    int res[100];
    int n,j=0;

    printf("Enter the number of elements (1 to 100):");
    scanf("%d",&n);

    printf("Enter elements in array:");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }

    // Find the odd numbers in array
    for (int i=0;i<n;i++)
    {
        if(arr[i]%2==1)
        {
            res[j]=arr[i];
            j++;
        }
    }
    for(int i=0;i<j;i++)
    {
        printf("\n%d",res[i]);
    }

}