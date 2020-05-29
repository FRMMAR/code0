#include <iostream>
#include <string>

class Animal
{
	public:
		Animal(std::string Aname, float height);
		std::string name;
		void run();
		float weight();
	private:
		float w;

};

class Dog: public Animal
{
public:
	std::string hair;
	void run();
};

Animal::Animal(std::string Aname, float weight)
{
	name = Aname;
	w = weight;
}


void Dog::run()
{
	std::cout << "this dog is running" << std::endl;
}

void Animal::run()
{
	std::cout << "this animal is running" << std::endl;
}

float Animal::weight()
{
	return Animal::w;
}

int main()
{
	Animal A("creature", 1.1);
	A.run();
	std::cout << "hahh " << A.weight();
	// Dog d("wangcai", "yellow");
	// d.run();
	// std::cout << "wangwangwang" << d.name << d.hair << std::endl;
}