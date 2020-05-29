#include <iostream>
using namespace std;

/*
指针变量重写；
保存内存块的指针作用域；
new出来的在内存堆里，不在栈空间里边；
动态内存没有作用域，必须由程序员手动delete；
动态内存分配的内存块没有作用域，用来保存动态内存的指针变量是受作用域影响的；
*/

main()
{
	int * x;
	x = new int[1000];
	x = new int[2000]; 
	delete[] x;
	x = NULL;

}