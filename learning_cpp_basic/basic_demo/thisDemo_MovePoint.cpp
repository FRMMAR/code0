#include<iostream>

/*
栈底是return
自由存储区，malloc，free
this指针是类的一个自动生成、自动隐藏的私有成员，它存在于类的非静态成员函数中，指向被调用函数所在的对象的地址



*/
class Point
{
private:
	int x, y;
public:
	Point(int a, int b)
	{ 
		x = a;
		y = b;
	}
	void MovePoint( int a, int b)
	{ 
		x = a; 
		y = b;
	}
	void print()
	{ 
		std::cout << "x=" << x << "   y=" << y << std::endl;
	}
};

int main()
{
	Point point1(10, 10);
	point1.MovePoint(2, 2);
	point1.print();

	return 0;
}
//point1调用MovePoint方法时，其实是将point1对象的地址传递给this指针；
//void MovePoint( Point *this, int a, int b)