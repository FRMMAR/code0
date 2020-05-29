#include <iostream>
#include <string>

class Pet
{
public:
	Pet(std::string theName);

	void eat();
	void sleep();
	virtual void play();

protected:
	std::string name;
};

class Cat : public Pet
{
public:
	Cat(std::string theName);

	void climb();
	void play();
};

class Dog : public Pet
{
public:
	Dog(std::string theName);

	void bark();
	void play();
};

Pet::Pet(std::string theName)
{
	name = theName;
}

void Pet::eat()
{
	std::cout << name << "pet eat!\n";
}

void Pet::sleep()
{
	std::cout << name << "pet sleep!\n";
}

void Pet::play()
{
	std::cout << name << "pet play!\n";
}

Cat::Cat(std::string theName) : Pet(theName)
{
}

void Cat::climb()
{
	std::cout << name << "cat climb!\n";
}

void Cat::play()
{
	Pet::play();
	std::cout << name << "cat play!\n";
}

Dog::Dog(std::string theName) : Pet(theName)
{
}

void Dog::bark()
{
	std::cout << name << "dog bark\n";
}

void Dog::play()
{
	Pet::play();
	std::cout << name << "dog play!\n";
}

int main()
{
	Pet *cat = new Cat("mao");
	Pet *dog = new Dog("gou");

	cat -> sleep();
	cat -> eat();
	cat -> play();

	dog -> sleep();
	dog -> eat();
	dog -> play();

	delete cat;
	delete dog;

	return 0;
}