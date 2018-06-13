from conans import ConanFile, CMake, tools
import os


class conan_bug_test_package(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()

    def test(self):
        os.chdir("bin")
        self.run("./conan_bug_test_package")
