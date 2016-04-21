from ctypes import *
from numpy.ctypeslib import ndpointer
import numpy as np

lib = cdll.LoadLibrary('./libpbc.so')


class Lattice(Structure):
    _fields_ = [("d", c_int),("Bravais", c_int),
                ("a", c_float),("b", c_float),("c", c_float),
                ("alpha", c_float),("beta", c_float),("gamma", c_float),
                ("basis", (c_float * 3) * 3),("fractional", (c_float * 3) * 3)]


def getAngle(r_i,r_j):

    '''
    cos( \theta ) = ( a dot b ) / ( |a| |b| )

    Args:
        r_i (numpy[3] ) vector from particle i to particle k
        r_j (numpy[3] ) vector from particle i to particle j 
    Returns:
        ang_deg (float) angle_{kij}
    '''

    r_i_norm = r_i/np.linalg.norm(r_i)
    r_j_norm = r_j/np.linalg.norm(r_j) 
    dot_ij = np.dot(r_i_norm,r_j_norm)

    if( dot_ij >= 1.0 ):
        ang_deg = 0.0
    elif(  dot_ij <= -1.0 ):
        ang_deg = 180.0
    else:    
        cos_ang = np.arccos(dot_ij )
        ang_deg = np.rad2deg( cos_ang )

    return ang_deg
            
class PBC():
    
    def __init__(self):
        '''
        '''
        # self.obj = lib.PBC_new()
        
        self.lat = Lattice()
        
        self.lat.d = 3
        self.lat.Bravais = 1
        self.lat.a = 100.0 
        self.lat.b = 100.0 
        self.lat.c = 100.0 
        self.lat.alpha = 90.0 
        self.lat.beta  = 90.0 
        self.lat.gamma = 90.0 
        
        for i in range(self.lat.d):
            for j in range(self.lat.d):
                self.lat.basis[i][j] = 0.0
                
        self.lat.basis[0][0] = self.lat.a
        self.lat.basis[1][1] = self.lat.b
        self.lat.basis[2][2] = self.lat.c
                
    def find_Bravais(self):

        if(  self.lat.alpha == 90.0 and  self.lat.beta == 90.0 and self.lat.gamma == 90.0 ):
            if( self.lat.a == self.lat.b and self.lat.a == self.lat.c and self.lat.b == self.lat.c ):
                # Cubic
                self.lat.Bravais = 1
            elif( self.lat.a == self.lat.b or self.lat.a == self.lat.c ):
                # Tetragonal
                self.lat.Bravais = 2
            else:
                # Orthorhombic
                self.lat.Bravais = 3
        elif(  self.lat.alpha == 90.0 and  self.lat.beta == 90.0 and self.lat.gamma == 120.0 ):
            if( self.lat.a == self.lat.b or self.lat.a == self.lat.c ):
                # Hexagonal
                self.lat.Bravais = 4
        elif(  self.lat.alpha == 90.0 and  self.lat.beta == 90.0 and self.lat.gamma < 120.0 ):
            if( self.lat.a == self.lat.b and self.lat.a == self.lat.c ):
                # Trigonal
                self.lat.Bravais = 5
            
        elif(  self.lat.alpha == 90.0 and  self.lat.beta == 90.0 and self.lat.gamma != 90.0 ):
            if( self.lat.a != self.lat.b and self.lat.a != self.lat.c  and self.lat.b != self.lat.c ):
                # Monoclinic
                self.lat.Bravais = 6
        elif(  self.lat.alpha != 90.0 and  self.lat.beta != 90.0 and self.lat.gamma != 90.0 ):
            if( self.lat.a != self.lat.b and self.lat.a != self.lat.c  and self.lat.b != self.lat.c ):
                # Triclinic
                self.lat.Bravais = 7
                
        return self.lat.Bravais

    def return_Bravais(self):
        if( self.lat.Bravais == 1 ):
            return "cubic"
        elif( self.lat.Bravais == 2 ):
            return "Tetragonal"
        elif( self.lat.Bravais == 3 ):
            return "Orthorhombic"
        elif( self.lat.Bravais == 4 ):
            return "Hexagonal"
        elif( self.lat.Bravais == 5 ):
            return "Trigonal"
        elif( self.lat.Bravais == 6 ):
            return "Monoclinic"
        elif( self.lat.Bravais == 7 ):
            return "Triclinic"
        
    
    def set_basis(self,basis_i):
        '''
        
        (c) 
        |
        |  
        |________ (b)
         \
          \  
           \
            (a)

        a - gamma - b
        b - alpha - c
        a - beta  - c
        
        
        '''
        for i in range(self.lat.d):
            for j in range(self.lat.d):
                 self.lat.basis[i][j] = basis_i[i][j]

                 
        self.lat.a = np.linalg.norm(self.lat.basis[0])
        self.lat.b = np.linalg.norm(self.lat.basis[1])
        self.lat.c = np.linalg.norm(self.lat.basis[2])

        self.lat.gamma = getAngle(self.lat.basis[0],self.lat.basis[1])
        self.lat.alpha = getAngle(self.lat.basis[1],self.lat.basis[2])
        self.lat.beta  = getAngle(self.lat.basis[0],self.lat.basis[2])        

    def return_basis(self):
        return  np.array(self.lat.basis)

         
    def delta_npos(self,npos_i,npos_j):
        """
        Difference between two position in box 
        """

        npos_i_c = []
        for pos_i in npos_i:
            for r_i in pos_i:
                npos_i_c.append(r_i)
        npos_i_c = np.array(npos_i_c,dtype='float64')
                
        npos_j_c = []
        for pos_j in npos_j:
            for r_j in pos_j:
                npos_j_c.append(r_j)
        npos_j_c = np.array(npos_j_c,dtype='float64')

        print "npos_i_c",npos_i_c
        print "npos_j_c",npos_j_c

        n_i = len(npos_i)
        n_i_c = c_int(n_i)
        n_j = len(npos_j)
        n_j_c = c_int(n_j)

        n_ij = len(npos_i_c)*len(npos_j_c)
        n_ij_c = c_int(n_ij)

        npos_ij_c = np.empty(n_ij*3,dtype='float64')
        nd_ij_c = np.empty(n_ij,dtype='float64')
        
        lib.delta_npos.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double,shape=(n_i*3,)),c_int,ndpointer(dtype=c_double,shape=(n_j*3,)),c_int,ndpointer(dtype=c_double,shape=(n_ij*3,)),ndpointer(dtype=c_double,shape=(n_ij,))]
        lib.delta_npos.restype =  None #[ndpointer(dtype=c_double,shape=(ij_c,)),ndpointer(dtype=c_double,shape=(ij_c,))]
        lib.delta_npos(byref(self.lat),npos_i_c,n_i_c,npos_j_c,n_j_c,npos_ij_c,nd_ij_c)
        print " delta_npos finished "
        # print "npos_ij_c ",npos_ij_c 
        # Return 1D to 2D array of positions
        npos_ij  = [] 
        for n in range(0,n_ij*3,3):
            print " n ",n
            pos_ij = np.array([npos_ij_c[n],npos_ij_c[n+1],npos_ij_c[n+2]])
            print "pos_ij ",n,pos_ij
            npos_ij.append(pos_ij)
        print "n_ij ",n_ij 
        
        return  npos_ij,nd_ij_c


    def call_pbc(self):
        '''
        Test function 
        '''
        lib.call_pbc.argtypes = None
        lib.call_pbc.restypes = None 
        lib.call_pbc()
        

    def pass_lat(self):
        '''
        Test function 
        '''
        lib.pass_lat.argtypes = [POINTER(Lattice)]
        lib.pass_lat.restypes = None 
        lib.pass_lat(byref(self.lat))
        




    def shift_npos(self,npos_i,pos_j):
        """
        Shift set of positions npos_i by a vector pos_j 
        """
        npos_i_c = []
        for pos_i in npos_i:
            for r_i in pos_i:
                npos_i_c.append(r_i)
        npos_i_c = np.array(npos_i_c,dtype='float64')
        pos_j = np.array(pos_j,dtype='float64')

        n = c_int(len(npos_i))

        npos_j_c = np.zeros(len(npos_i_c))
        #lib.r_ij.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double, shape=(len(r_i),)), ndpointer(dtype=c_double, shape=(len(r_j),)),ndpointer(dtype=c_double, shape=(len(r_ij),))]
        #lib.r_ij.restype = ndpointer(dtype=c_double, shape=(len(r_ij),))
        lib.shift_npos.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double,shape=(len(npos_i_c),)),c_int]
        return  lib.shift_npos(byref(self.lat),npos_i_c,n)

    def r_ij(self,r_i,r_j):
        """
        Difference between two position in box 
        """
        r_ij = np.zeros(len(r_i))
        lib.r_ij.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double, shape=(len(r_i),)), ndpointer(dtype=c_double, shape=(len(r_j),)),ndpointer(dtype=c_double, shape=(len(r_ij),))]
        lib.r_ij.restype = ndpointer(dtype=c_double, shape=(len(r_ij),))
        return  lib.r_ij(byref(self.lat),r_i,r_j,r_ij)





    def pos_ij(self,pos_i,pos_j):

        i = c_int(len(pos_i))
        j = c_int(len(pos_j))

        npos_i = np.array(npos_i)
        pos_ij = np.zeros((i*j,3), dtype='float64')
        d_ij  = np.zeros((i*j*3), dtype='float64')
        
        lib.pos_ij.argtypes = [POINTER(Lattice), ndpointer( dtype=c_double,flags='C', shape=( 4,3 ) ),c_int ]
        lib.pos_ij.restype =  None # ndpointer( dtype=c_double, shape=( len(npos_i), len(npos_i[0])) )
        pos_ij,dpos_ij =  lib.pos_ij(byref(self.lat),npos_i,n)

        return  pos_ij,dpos_ij
        



    def calc_fractional(self,r_i,frac_i):
        lib.calc_fractional.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double, shape=(len(r_i),)),ndpointer(dtype=c_double, shape=(len(frac_i),))]
        lib.calc_fractional.restype = ndpointer(dtype=c_double, shape=(len(frac_i),))
        return  lib.calc_fractional(byref(self.lat),r_i,frac_i)
    
    def print_basis(self):
        
        lib.print_basis.argtypes = [POINTER(Lattice)]
        lib.print_basis.restype = None
        
        lib.print_basis(byref(self.lat))
  
    def delta_r(self,r_i,r_j):
        lib.delta_r.argtypes = [POINTER(Lattice),ndpointer(dtype=c_double, shape=(len(r_i),)),ndpointer(dtype=c_double, shape=(len(r_j),))]
        lib.delta_r.restype = ndpointer(dtype=c_double, shape=(len(r_i),))
        return lib.delta_r(byref(self.lat),r_i,r_j)

    def delta_rij_t(self,r_i,r_j):
        """
        Difference between two position in tetragonal box 
        """

        r_ij  = r_j - r_i    

        r_x = r_ij[0] - self.latvec[0][0] * round( r_ij[0]/  self.latvec[0][0] )
        r_y = r_ij[1] - self.latvec[1][1] * round( r_ij[1]/  self.latvec[1][1] )
        r_z = r_ij[2] - self.latvec[2][2] * round( r_ij[2]/  self.latvec[2][2] )

        return np.array( [r_x,r_y,r_z] )

    def delta_rij_r(self,r_i,r_j):
        """
        Difference between two position in tetragonal box 
        """

        r_ij  = r_j - r_i    

        r_x = r_ij[0] - self.latvec[0][0] * round( r_ij[0]/  self.latvec[0][0] )
        r_y = r_ij[1] - self.latvec[1][1] * round( r_ij[1]/  self.latvec[1][1] )
        r_z = r_ij[2] - self.latvec[2][2] * round( r_ij[2]/  self.latvec[2][2] )

        return np.array( [r_x,r_y,r_z] )
             
    def print_fractional(self):
        
        lib.print_basis.argtypes = [POINTER(Lattice)]
        lib.print_basis.restype = None
        
        lib.print_fractional(byref(self.lat))

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
        lib.return_r.argtypes = [ndpointer(dtype=c_double, shape=(len(r_i),))]
        lib.return_r.restype = ndpointer(dtype=c_double, shape=(len(r_i),))
        return lib.return_r(r_i)
    
