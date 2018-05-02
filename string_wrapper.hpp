#include <iostream>
#include <string>

class string_wrapper
{
public:
  string_wrapper(std::string tmp): internal_string(tmp) {};
  ~string_wrapper() {};

  void print();

private:
  std::string internal_string;
};
