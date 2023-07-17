// Read the n numbers and display maximum,minimum,average (only through iteration without array)

#include<stdio.h>

int main()
{
    int n;

    printf("Enter how much number u want to read:");
    scanf("%d",&n);

    int max=0;
    int min=99999999;
    int sum=0;
    float avg;

    for (int i=0;i<n;i++)
    {
        int a=0;
        printf("ENter number:");
        scanf("%d",&a);

        if (a>max)
        {
            max=a;
        }
        if(a<min)
        {
            min=a;
        }
        sum+=a;
    }
    avg=sum/n;

    printf("Maximum:%d \n Minimum:%d \n Sum:%d \n Average:%f",max,min,sum,avg);
}