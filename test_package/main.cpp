#include <iostream>
#include <string_wrapper.hpp>

int main()
{
  string_wrapper test("This is just a simple string.");
  test.print();
  std::cout << std::endl;
  return 0;
}
