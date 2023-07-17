// Constructor

#include<bits/stdc++.h>
using namespace std;

class A
{
    private:
    int x,y;

    public:
    // parameterized constructor
    A(int x1,int y1)
    {
        x=x1;
        y=y1;
    }
    int getx()
    {
        return x;
    }
    int gety()
    {
        return y;
    }
};

int main()
{
    A a(10,15);    //call the constructor
    // Access values assigned by constructor
    cout<<"a.x="<<a.getx()<<",a.y="<<a.gety();
}