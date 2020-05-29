#include <iostream>
#include <string>
using namespace std;

class animal
{
protected:       //成员变量，声明为protected或者public，这里选择protected
	int height;  //若声明为private，则不能被子类继承访问，会报错
	int weight;
public:
	animal(int height,int weight)   //带参的构造函数
	{
		this->height=height;
		this->weight=weight;
		cout<<"animal的带参构造函数被调用"<<endl;
	}
	virtual ~animal()
	{
		cout<<"animal的析构函数被调用"<<endl;
	}
};
//子类
class fish:public animal
{
public:
	fish():animal(height,weight) //显示调用父类的构造函数
	{
		cout<<"fish的构造函数被调用"<<endl;
	}
	virtual ~fish()
	{
		cout<<"fish的析构函数被调用"<<endl;
	}
};
