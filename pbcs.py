import ctypes
from ctypes import cdll,c_int,c_double,POINTER
from numpy.ctypeslib import ndpointer

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
    
    def return_y(self,n):
        return lib.Lattice_return_y(self.obj,c_int(n))


    def sum_r(self,r_i):
        ri_x = r_i[0]
        ri_y = r_i[1]
        ri_z = r_i[2]
        lib.Lattice_sum_r.restype = c_double
        return lib.Lattice_sum_r(self.obj,c_double(ri_x),c_double(ri_y),c_double(ri_z))

#
    def dr_ij(self,r_i):
        ri = (ctypes.c_double * len(r_i))()
        for i in range(len(r_i)):
            ri[i] = r_i[i]
        lib.Lattice_dr_ij.restype = ndpointer(dtype=ctypes.c_double, shape=(len(r_i),))
        return lib.Lattice_dr_ij(self.obj,ri)
