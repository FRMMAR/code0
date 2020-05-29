#include <iostream>
#include <string>

/*
其他的类想要访问类的protected或者时private方法和属性

*/


class Lovers
{
public:
    Lovers(std::string theName);
    void kiss(Lovers *lover);
    void ask(Lovers *lover, std::string something);

protected:
    std::string name;       //friend could be everywhere!!!
    friend class Others;    // evil third want to access the kiss behavior
};

class Boyfriend : public Lovers
{
public:
    Boyfriend(std::string theName);
};

class Girlfriend : public Lovers
{
public:
    Girlfriend(std::string theName);
};

class Others
{
public:
    Others(std::string theName);
    void kiss(Lovers *lover);

protected:
    std::string name;
};

Lovers::Lovers(std::string theName)
{
    name = theName;
}

void Lovers::kiss(Lovers *lover)
{
    std::cout << name << " lover's kissing " << lover->name << std::endl;
}

void Lovers::ask(Lovers *lover, std::string something)
{
    std::cout << "lover " << lover->name << " ask " << something << std::endl;
}

Boyfriend::Boyfriend(std::string theName) : Lovers(theName)
{
}

Girlfriend::Girlfriend(std::string theName) : Lovers(theName)
{
}

Others::Others(std::string theName)
{
    name = theName;
}

void Others::kiss(Lovers *lover)
{
    std::cout << name << " third one kissing " << lover->name << std::endl;
}

int main()
{
    Boyfriend boyfriend("zhanan");
    Girlfriend girlfriend("lvcha");

    Others others("luozhixiang");

    girlfriend.kiss(&boyfriend);
    girlfriend.ask(&boyfriend, " noodles");

    std::cout << "\n multi-people exercise \n";
    others.kiss(&girlfriend);
    //others.ask(&boyfriend, " noodles");

    return 0;
}
