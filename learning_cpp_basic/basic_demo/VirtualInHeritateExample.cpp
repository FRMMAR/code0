#include <iostream>
#include <string>
/*
防止多继承时子类的实例拥有其基类的多个属性
使用virtual的类继承方式使其只有一个基类属性的实现
*/
class Person
{
public:
    Person(std::string theName);

    void introduce();

protected:
    std::string name;
};

class Teacher : virtual public Person
{
public:
    Teacher(std::string theName, std::string theClass);

    void teach();
    void introduce();

protected:
    std::string classes;
};

class Student : virtual public Person
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
    std::cout << "person name is " << name << " introduce over\n\n";
}

Teacher::Teacher(std::string theName, std::string theClass) : Person(theName)
{
    classes = theClass;
}

void Teacher::teach()
{
    std::cout << name << " teacher teach " << classes << " teach over\n\n";
}

void Teacher::introduce()
{
    std::cout << "Teacher's name is " << name << " , teach " << classes << " introduce over\n\n";
}

Student::Student(std::string theName, std::string theClass) : Person(theName)
{
    classes = theClass;
}

void Student::attendClass()
{
    std::cout << name << " attend " << classes << " attend over\n\n";
}

void Student::introduce()
{
    std::cout << "student " << name << ", attend " << classes << " introduce over\n\n";
}

TeachingStudent::TeachingStudent(std::string theName,
                                 std::string classTeaching,
                                 std::string classAttending)
                                 :
                                 Teacher(theName, classTeaching),
                                 Student(theName, classAttending),
                                 Person(theName)
{
}

void TeachingStudent::introduce()
{
    std::cout << "TeachingStudent" << name << " teach " << Teacher::classes << ", ";
    std::cout << "TeachingStudent attend " << Student::classes << " intro over\n\n";
}

int main()
{
    Teacher teacher("Tiger", "Kill");
    Student student("Cat", "Sleep");
    TeachingStudent teachingStudent("Elephant", "Drink", "Eat");

    teacher.introduce();
    teacher.teach();
    student.introduce();
    student.attendClass();
    teachingStudent.introduce();
    teachingStudent.teach();
    teachingStudent.attendClass();

    return 0;
}
