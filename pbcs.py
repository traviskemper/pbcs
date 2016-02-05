from ctypes import cdll,c_int,c_double

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

    def dr_ij(self,r_i):
        ri_x = r_i[0]
        ri_y = r_i[1]
        ri_z = r_i[2]
        sum_i = lib.Lattice_dr_ij(self.obj,c_double(ri_x),c_double(ri_y),c_double(ri_z))
        print "in pbcs sum_i",sum_i
        return sum_i
