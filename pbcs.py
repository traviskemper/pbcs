from ctypes import cdll
lib = cdll.LoadLibrary('./libpbcs.so')

class Lattice(object):
    def __init__(self):
        self.obj = lib.Lattice_new()
    
    def print_dim(self):
        lib.Lattice_print_dim(self.obj)
    
    def dimensions(self):
        return lib.Lattice_dimensions(self.obj)

    def position(self,r):
        return lib.Lattice_position(self.obj)

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

    def print_dim(self):
        lib.Foo_print_dim(self.obj)
