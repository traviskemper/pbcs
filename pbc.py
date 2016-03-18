from ctypes import *

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
