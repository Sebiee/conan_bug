from conans import ConanFile, CMake
import os

class conan_bug_recipe(ConanFile):
    name = "string_wrapper"
    version = "1.0.0"

    settings = "os", "compiler", "build_type", "arch"

    exports = "version.txt"

    generators = "cmake"

    scm = {
        "type": "git",
        "url": "git@github.com:Sebiee/conan_bug.git",
        "revision": "auto"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("**.hpp", dst="include", keep_path=True)
        self.copy("**.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libstring_wrapper.a"]
