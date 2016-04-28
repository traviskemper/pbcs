import numpy as np
import sys, os
from pbc import PBC

# Initialize periodic boundry condition object
pbc_i = PBC()

# Print lattice vectors 
pbc_i.print_basis()


npos_i = []
npos_i.append(np.array([25.0,25.0,25.0], dtype='float64'))
npos_i.append(np.array([5.0,75.0,25.0], dtype='float64'))
npos_j = []
npos_j.append(np.array([-10.0,-15.0,0.0], dtype='float64'))
npos_j.append(np.array([-25.0,-90.0,-45.0], dtype='float64'))
npos_ij,nd_ij = pbc_i.delta_npos(npos_i,npos_j)

for n in range(len(npos_i)):
    pos_i = npos_i[n]
    print " pos_i %d  [ %f %f %f ] \n"%(n+1,pos_i[0],pos_i[1],pos_i[2])
for n in range(len(npos_j)):
    pos_j = npos_j[n]
    print " pos_j %d  [ %f %f %f ]  \n"%(n+1,pos_j[0],pos_j[1],pos_j[2])

for n in range(len(npos_i)):
    for m in range(len(npos_j)):
        pos_ij = npos_ij[n][m]
        print " pos_ij %d %d [ %f %f %f ] | %f | \n"%(n+1,m+1,pos_ij[0],pos_ij[1],pos_ij[2],nd_ij[n][m])

print " Get basis and change it "
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


npos_i = []
npos_i.append(np.array([75.0,95.0,15.0], dtype='float64'))
npos_i.append(np.array([-85.0,75.0,25.0], dtype='float64'))
npos_i.append(np.array([-96.0,-68.0,33.0], dtype='float64'))
npos_i.append(np.array([-85.0,-38.0,-78.0], dtype='float64'))
npos_j = []
npos_j.append(np.array([-101.0,-152.0,-45.0], dtype='float64'))
npos_j.append(np.array([-64.0,-32.0,131.0], dtype='float64'))
npos_j.append(np.array([-48.0,377.0,77.0], dtype='float64'))
npos_j.append(np.array([12.0,152.0,45.0], dtype='float64'))
npos_ij,nd_ij = pbc_i.delta_npos(npos_i,npos_j)

for n in range(len(npos_i)):
    pos_i = npos_i[n]
    print " pos_i %d  [ %f %f %f ] \n"%(n+1,pos_i[0],pos_i[1],pos_i[2])
for n in range(len(npos_j)):
    pos_j = npos_j[n]
    print " pos_j %d  [ %f %f %f ]  \n"%(n+1,pos_j[0],pos_j[1],pos_j[2])

for n in range(len(npos_i)):
    for m in range(len(npos_j)):
        pos_ij = npos_ij[n][m]
        print " pos_ij %d %d [ %f %f %f ] | %f | \n"%(n+1,m+1,pos_ij[0],pos_ij[1],pos_ij[2],nd_ij[n][m])
