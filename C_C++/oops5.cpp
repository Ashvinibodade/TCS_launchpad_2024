#include<bits/stdc++.h>
using namespace std;

class Human
{
    private:   // Encapsulation
    int anger;
    int sadness;

    public:
    string hair;
    string eyes;

    //Default constructor
    // Human()
    // {
    //     cout<<"Constructor called"<<endl;
    // }

    // parameterized constructor
    Human(string a,string b,int c, int d)
    {
        hair=a;
        eyes=b;
        anger=c;
        sadness=d;
    }

    void setAnger(int a)
    {
        anger=a;
    }

    void setSadness(int a)
    {
        Sadness=a;
    }

    void setHair(string a)
    {
        Hair=a;
    }

    void setEyes(string a)
    {
        Eyes=a;
    }

    void display()
    {
        cout<<"\nHair:"<<hair<<"\nEyes:"<<eyes<<"\nAnger:"<<anger<<"\nSadness:"<<sadness<<endl;
    }

    void printSomething()
    {
        cout<<"You are in print something method."<<endl;
    }
    // Method declaration
    void displayAlldata();
};

// Define method outside the class
void Human::displayAlldata()
{
    cout<<"\nHair:"<<hair<<"\nEyes:"<<eyes<<"\nAnger:"<<anger<<"\nSadness:"<<sadness<<endl;
}

// Inheritance
class Men:public Human
{
    // Polymorphism
    public:
    void printSomething(int a)
    {
        cout<<"Welcome to men class which is inherited from human class."<<a<<endl;
    }
};

int main()
{
    // object of human class get created
    Human jack('Long','Blue',5,5);
    // jack.hair='long';
    // jack.eyes='blue';
    // jack.anger=7;
    // jack.sadness=4;

    // jack.display();

    jack.displayAlldata();

    // object of second class
    Men Aashutosh;
    Aashutosh.hair="black";
    cout<<Aashutosh.hair<<endl;
    // Aashutosh.anger=5;

    // Polymorphism
    jack.printSomething();
    Aashutosh.printSomething(2020);
    // Aashutosh.printSomething();

    return 0;

}