import numpy as np
import sys, os
from pbc import PBC


# Initialize periodic boundry condition object
pbc_i = PBC()

# Test call c++ 
print pbc_i.call_pbc()
# Test passing lattice
print pbc_i.pass_lat()


# Print lattice vectors 
pbc_i.print_basis()

# Get lattice vectors (basis) from defualt initializization
basis_i = pbc_i.return_basis()
print "  basis_i ",basis_i



# Set local basis to new values
basis_i[0,0]=120.0
basis_i[1,1]=110.0
basis_i[2,2]=130.0

# Set lattice vectors to new values 
print "basis_i",basis_i
pbc_i.set_basis(basis_i)

# Find Bravais lattice type 1-7 
Bravais_numb = pbc_i.find_Bravais()
print "Bravais_numb ",Bravais_numb
print "Bravais  ",pbc_i.return_Bravais()

# Print lattice vectors
pbc_i.print_basis()

# Test
npos_i = []
npos_i.append(np.array([25.0,25.0,25.0], dtype='float64'))
npos_i.append(np.array([-125.0,-125.0,-125.0], dtype='float64'))
npos_i.append(np.array([-15.0,35.0,-5.0], dtype='float64'))

pos_j = np.array([25.0,25.0,25.0], dtype='float64')

pbc_i.shift_npos(npos_i,pos_j)



npos_j = []
npos_j.append(np.array([5.0,75.0,25.0], dtype='float64'))
npos_j.append(np.array([-10.0,-15.0,0.0], dtype='float64'))
npos_j.append(np.array([-25.0,-90.0,-45.0], dtype='float64'))

npos_ij,nd_ij = pbc_i.delta_npos(npos_i,npos_j)

for n in range(len(npos_ij)):
    pos_i = npos_ij[n]
    print " pos_i %d  [ %f %f %f ] |%f| "%(n,pos_i[0],pos_i[1],pos_i[2],nd_ij[n])

sys.exit(" testing 1")


# Create point and pass to PBC to test numpy passing and returning
npos_i = []
r_i = np.array([140.00002324213,54332.8,53.7], dtype='float64')
npos_i.append( r_i )
r_i = np.array([3.13,9234.431,234.023084], dtype='float64')
npos_i.append( r_i )
r_i = np.array([234.234,324.431,974.023084], dtype='float64')
npos_i.append( r_i )
r_i = np.array([12.13,667.431,10.023084], dtype='float64')
npos_i.append( r_i )
npos_i = np.array(npos_i)
print "npos_i",npos_i
print "len(npos_i)",len(npos_i)
npos_j = pbc_i.pass_npos(npos_i)


# Create points  and pass to PBC to test numpy passing and returning 
r_i = np.array([25.0,25.0,25.0], dtype='float64')
r_j = np.array([-125.0,-125.0,-125.0], dtype='float64')
dr_ij = pbc_i.r_ij(r_i,r_j)


sys.exit('adf')

r_k = pbc_i.return_r(r_i)
print "r_k ",r_k
print "r_i ",r_i
# Note that r_k is not a pointer to r_i 
r_k[0] = 20.876
print "r_k ",r_k
print "r_i ",r_i

# Initialize numpy array of fractional coordinates 
frac_i = np.array([0.0,0.0,0.0], dtype='float64')
frac_i = pbc_i.calc_fractional(r_i,frac_i)
print "frac_i ",frac_i

# Find the difference between two positions
r_j = np.array([3.13,9234.431,234.023084], dtype='float64')
print "r_i ",r_i
print "r_j ",r_j
r_ij = pbc_i.r_ij(r_i,r_j)
print "r_ij ",r_ij


sys.exit()

r_j = np.array([99.03,77.8,66.7])
dr_ij = pbc_i.delta_r(r_i,r_j)
print "dr_ij",dr_ij



for i in range(pbc_i.lat.d):
    for j in range(pbc_i.lat.d):
        print "  ",i,j,pbc_i.lat.basis[i][j]



print "r_i",r_i
pbc_i.print_r(r_i)
print "r_j",r_j
r_k = pbc_i.return_r(r_j)
print "r_k",r_k


