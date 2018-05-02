project(conan_bug_test_package)

cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(conan_bug_test_package
  main.cpp
)

target_link_libraries(conan_bug_test_package ${CONAN_LIBS})
