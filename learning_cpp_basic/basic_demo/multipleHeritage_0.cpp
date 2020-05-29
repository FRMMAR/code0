#include <iostream>
#include <string>
/*
多继承的写法；
多继承子类实例化时的初始化；
继承了基类的多少个副本，推荐从没有任何属性且只有抽象方法的类开始继承，防止后代子类可能拥有好几个基类属性的问题；
这样的类又叫接口；
*/
class Person
{
public:
    Person(std::string theName);

    void introduce();

protected:
    std::string name;
};

class Teacher : public Person
{
public:
    Teacher(std::string theName, std::string theClass);

    void teach();
    void introduce();

protected:
    std::string classes;
};

class Student : public Person
{
public:
    Student(std::string theName, std::string theClass);

    void attendClass();
    void introduce();

protected:
    std::string classes;
};

class TeachingStudent : public Student, public Teacher
{
public:
    TeachingStudent(std::string theName, std::string classTeaching, std::string classAttending);

    void introduce();
};

Person::Person(std::string theName)
{
    name = theName;
}

void Person::introduce()
{
    std::cout << "Im a base person, My name is " << name << " over\n\n";
}

Teacher::Teacher(std::string theName, std::string theClass) : Person(theName)
{
    classes = theClass;
}

void Teacher::teach()
{
    std::cout << name << "Teacher's teach " << classes << ". Teacher's over\n\n";
}

void Teacher::introduce()
{
    std::cout << "My name is teacher " << name << ", I taught " << classes << ". over\n\n";
}

Student::Student(std::string theName, std::string theClass) : Person(theName)
{
    classes = theClass;
}

void Student::attendClass()
{
    std::cout << name << "student's attendent Class is " << classes << ". over\n\n";
}

void Student::introduce()
{
    std::cout << "im a student, my name is " << name << ", I attended class" << classes << ". over\n\n";
}

TeachingStudent::TeachingStudent(std::string theName,
                                 std::string classTeaching,
                                 std::string classAttending)
                                 : Teacher(theName, classTeaching), Student(theName, classAttending)
{
}

void TeachingStudent::introduce()
{
    std::cout << "I'm a teachingstudent. My name is " << Student::name << ". I teach" << Teacher::classes << ", ";
    std::cout << "I attend " << Student::classes << ". over\n\n";
}

int main()
{
    Teacher teacher("tiger", "classtop");
    Student student("rat", "classmedium");
    TeachingStudent teachingStudent("cat", "low", "high");

    teacher.introduce();
    teacher.teach();
    student.introduce();
    student.attendClass();
    teachingStudent.introduce();
    teachingStudent.teach();
    teachingStudent.attendClass();

    return 0;
}
