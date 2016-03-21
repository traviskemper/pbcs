import numpy as np
import sys, os
from pbc import PBC


# Initialize periodic boundry condition object
pbc_i = PBC()

# Print lattice vectors 
pbc_i.print_basis()

# Get lattice vectors (basis) from defualt initializization
basis_i = pbc_i.return_basis()
print "basis_i",basis_i

# Set local basis to new values
basis_i[0,0]=120.0
basis_i[1,1]=110.0
basis_i[2,2]=130.0



# Set lattice vectors to new values 
print "basis_i",basis_i
pbc_i.set_basis(basis_i)

# Print lattice vectors
pbc_i.print_basis()

# Find Bravais lattice type 1-7 
Bravais_numb = pbc_i.find_Bravais()
print "Bravais_numb ",Bravais_numb
print "Bravais  ",pbc_i.return_Bravais()

# Create point and pass to PBC to test numpy passing and returning 
r_i = np.array([140.00002324213,54332.8,53543.7], dtype='float64')
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


