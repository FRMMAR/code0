#include <iostream>  // ostream  C92 C99

// using namespace std;
// most basic

int addArray( int array[], int n );

int main()
{
      int data[] = {0, 1, 2, 3, 4, 5,6, 7, 8, 9};
      int size = sizeof(data) / sizeof(data[0]);
      std::cout << (sizeof(data)) << std::endl;

      std::cout << "和是: " << addArray(data, size) << std::endl;

      return 0;
}

int addArray( int array[], int n )
{
      int sum = 0;
      int i;

      std::cout << (sizeof(array)) << std::endl;

      for( i=0; i < n; i++ )
      {
            sum += array[i];
      }

      return sum;
}