from ctypes import cdll,c_int

lib = cdll.LoadLibrary('./libpbcs.so')


class Lattice(object):
    def __init__(self):
        self.obj = lib.Lattice_new()
    
    def print_dim(self):
        lib.Lattice_print_dim(self.obj)
    
    def print_n(self,n):
        lib.Lattice_print_n(self.obj,c_int(n))
    
    def return_x(self,n):
        return lib.Lattice_return_x(self.obj,c_int(n))
