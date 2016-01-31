from ctypes import cdll
lib = cdll.LoadLibrary('./libpbcs.so')

class Lattice(object):
    def __init__(self):
        self.obj = lib.Lattice_new()
    
    def print_dim(self):
        lib.Lattice_print_dim(self.obj)
