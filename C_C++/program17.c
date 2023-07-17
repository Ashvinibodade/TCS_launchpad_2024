// Swap the list from middle

#include<stdio.h>

int main()
{
    int arr[100];
    int swaparr[100];
    int n,j=0;
    int z0,z1;

    printf("Enter the number of elements (1 to 100):");
    scanf("%d",&n);

    printf("Enter elements in array:");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }

    for(int i=0;i<n;i++)
    {
        if(n%2==0)
        {
            z0=n/2;
            for(int i=z0,j=0;i<n,j<z0;i++,j++)
            {
                swaparr[i]=arr[j];
                swaparr[j]=arr[i];
            }
        }
        else
        {
            z0=(n-1)/2;
            swaparr[z0]=arr[z0];
            z1=(n+1)/2;
            for(int i=z1,j=0;i<n,j<z0;i++,j++)
            {
                swaparr[i]=arr[j];
                swaparr[j]=arr[i];
            }
        }
    }
    printf("Swaped array:");
    for(int i=0;i<n;i++)
    {
        printf("%d +",swaparr[i]);
    }

}