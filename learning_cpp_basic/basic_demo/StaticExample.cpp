#include <iostream>
#include <string>

/*
对象是一种特殊的结构
对象的属性和方法（变量和函数）都是保存在内存中，都可以通过内存地址访问
this指针保存着对象本身的地址
调用一个方法时，this指针会随着提供的参数秘密地传递给那个方法
this指针和静态方法存放不在一块区域
*/
class Pet
{
public:
    Pet(std::string theName);
    ~Pet();

    static int getCount();  //static methos

protected:
    std::string name;

private:
    static int count;
};

class Dog : public Pet
{
public:
    Dog(std::string theName);
};

class Cat : public Pet
{
public:
    Cat(std::string theName);
};

int Pet::count = 0;         // 静态属性的初始化

Pet::Pet(std::string theName)
{
    name = theName;
    count++;

    std::cout << "pet's name is : " << name << "\n";
}

Pet::~Pet()
{
    count--;
    std::cout << name << " pet out\n";
}

int Pet::getCount()
{
    return count;
}

Dog::Dog(std::string theName) : Pet(theName)
{
    std::cout << "this dog :" << this << "\n";
}

Cat::Cat(std::string theName) : Pet(theName)
{
}

int main()
{
    Dog dog("Tom");
    Cat cat("Jerry");
    std::cout << "dog:" << &dog << "\n";
    std::cout << "\npet count1 " << Pet::getCount() << "over!\n\n";

    Dog dog_2("Tom_2");
    Cat cat_2("Jerry_2"); //在main函数的栈里，Jerry_2，位于栈顶，最先被析构

    std::cout << "\npet count2 " << Pet::getCount() << "over!\n\n";

    std::cout << "\npet count3 " << Pet::getCount() << " over!\n\n";

    return 0;
}
