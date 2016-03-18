import numpy as np
import sys, os
from pbc import PBC

pbc_i = PBC()

r_i = np.array([0.00002324213,324554332.8,53543.7])
r_j = np.array([99.03,77.8,66.7])

print "r_i",r_i
pbc_i.print_r(r_i)
print "r_j",r_j
r_k = pbc_i.return_r(r_j)
print "r_k",r_k

dr_ij = pbc_i.delta_r(r_i,r_j)
print "dr_ij",dr_ij

