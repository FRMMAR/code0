#include <iostream>

/*
析构器都是虚函数，基类函数的虚函数写成析构函数
当一个基类的指针删除一个派生类的对象时，派生类的析构函数可以被正确调用
抽象方法=纯虚函数，abstract method
*/
class ClxBase
{
public:
    ClxBase()
    {
    };

    virtual ~ClxBase() //不加virtual会造成子类的析构函数无法被调用
    {
    };

    virtual void doSomething()
    {
        std::cout << "Do something in class ClxBase!\n";
    }
};

class ClxDerived : public ClxBase
{
public:
    ClxDerived()
    {
    };

    ~ClxDerived()
    {
        std::cout << "Output from the destructor of class ClxDerived!\n";
    };

    void doSomething()
    {
        std::cout << "Do something in class ClxDerived!\n";
    };
};

int main()
{
    ClxBase *pTest = new ClxDerived;

    pTest -> doSomething();

    delete pTest;

    return 0;
}
