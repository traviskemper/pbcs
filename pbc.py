from ctypes import *
from numpy.ctypeslib import ndpointer

lib = cdll.LoadLibrary('./libpbc.so')


class Lattice(Structure):
    _fields_ = [("d", c_int),
                ("basis", (c_float * 3) * 3)]


class PBC():
    
    def __init__(self):
        '''
        '''
        # self.obj = lib.PBC_new()
        self.length = 1.0
        self.lat = Lattice()        
        self.lat.d = 3
        for i in range(self.lat.d):
            for j in range(self.lat.d):
                if( i == j ):
                    self.lat.basis[i][j] = self.length
                    
    def print_basis(self):
        
        lib.print_basis.argtypes = [POINTER(Lattice)]
        lib.print_basis.restype = None
        
        lib.print_basis(byref(self.lat))


    def set_diagbasis(self,l):
        '''
        Set diagonal elments of PBC basis vectors to value l
        
        agr: l (float)
        return: None
        '''
        self.length = l
        
        for i in range(self.lat.d):
            for j in range(self.lat.d):
                if( i == j ):
                    self.lat.basis[i][j] = self.length

        return None

 
    def print_basis(self):
        
        lib.print_basis.argtypes = [POINTER(Lattice)]
        lib.print_basis.restype = None
        
        lib.print_basis(byref(self.lat))

    def print_r(self,r_i):
        ri = (c_double * len(r_i))()
        for i in range(len(r_i)):
            ri[i] = r_i[i]


        lib.print_basis.argtypes = [ndpointer(dtype=c_double, shape=(len(r_i),))]
        lib.print_basis.restype = None
        
        lib.print_r(byref(ri))
            
        # lib.PBC_print_r.restype = ndpointer(dtype=ctypes.c_double, shape=(len(r_i),))
        # lib.PBC_print_r(self.obj,ri)
    

    def return_r(self,r_i):
        ri = (c_double * len(r_i))()
        for i in range(len(r_i)):
            ri[i] = r_i[i]
            
        lib.return_r.argtypes = [ndpointer(dtype=c_double, shape=(len(r_i),))]
        lib.return_r.restype = ndpointer(dtype=c_double, shape=(len(r_i),))
        return lib.return_r(r_i)


    def delta_r(self,r_i,r_j):
        lib.delta_r.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double, shape=(len(r_i),)),ndpointer(dtype=c_double, shape=(len(r_j),))]
        lib.delta_r.restype = ndpointer(dtype=c_double, shape=(len(r_i),))
        return lib.delta_r(byref(self.lat),r_i,r_j)
