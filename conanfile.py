from conans import ConanFile, CMake
import os

class conan_bug_recipe(ConanFile):
    name = "string_wrapper"
    version = "1.0.0"

    settings = "os", "compiler", "build_type", "arch"

    generators = "cmake"

    def configure(self):
        if self.settings.compiler != "Visual Studio":
            self.settings.compiler.libcxx="libstdc++11"

    def source(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("**.hpp", dst="include", keep_path=True)
        self.copy("**.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [
             os.path.join(self.package_folder,"lib","libstring_wrapper.a")
        ]
        del self.cpp_info.lib_paths[:]
