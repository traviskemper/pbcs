from ctypes import cdll
lib = cdll.LoadLibrary('./libpbcs.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

    def print_dim(self):
        lib.Foo_print_dim(self.obj)
