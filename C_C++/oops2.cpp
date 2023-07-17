// Comparison of two objects based on ages

#include<bits/stdc++.h>
using namespace std;

class geeks
{
    public:
    string geeksname;
    int age;

    void printname()
    {
        cout<<"Younger is:"<<geeksname;
    }
    geeks static returnYounger(geeks obj1,geeks obj2)
    {
        if (obj1.age<obj2.age)
        {
            return obj1;
        }
        else
        {
            return obj2;
        }
    }
};

int main()
{
    geeks obj1;
    obj1.geeksname='Ashvini'
    obj1.age=30
    geeks obj2;
    obj2.geeksname='Mummy'
    obj2.age=40
    geeks youngerobj;
    youngerobj=geeks::returnYounger(obj1,obj2)
    youngerobj.printname()
    return 0;
}