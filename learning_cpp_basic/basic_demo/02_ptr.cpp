#include <iostream>

/*


*/

int main()		
{				
	int i = 5;
	int *p1 = &i;
	std::cout << "i is " << i << " the addres is " << &i << std::endl;
	std::cout << "p1 is " << p1 << " the addres is " << &p1 << std::endl;
	int **p2 = &p1;		//p2 是指向p1指针的指针
	int *&p3 = p1;		//p3是p1指针的引用，离变量名最近的符号说明变量的类型
	std::cout << "p3 is " << p3 << " the addres is " << &p3 << std::endl;

	double d =3.66;
	const int &dd = d;//const int temp = d; const int dd = temp;
	std::cout << d << &d << std::endl;
	std::cout << dd << &i << std::endl;

	return 0;
}