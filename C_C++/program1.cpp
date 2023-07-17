// Identify the given year is leap year or not

#include<iostream>
using namespace std;

int main()
{
    int a;
    cout<<"Input the year:";
    cin>>a;

    // if (a%400==0)
    // {
    //     cout<<a <<" is leap year"<<endl;
    // }
    // else if (a%100==0)
    // {
    //     cout<<a <<" is not leap year"<<endl;
    // }
    // else if (a%4==0)
    // {
    //     cout<<a <<" is leap year"<<endl;
    // }
    // else
    // {
    //     cout<<a <<" is not leap year"<<endl;
    // }

    // Another way 

    if ((a%4==0) && ((a%400==0) || (a%100!=0)))
    {
       cout<<a <<" is leap year"<<endl; 
    }
    else
    {
        cout<<a <<" is not leap year"<<endl;
    }


}