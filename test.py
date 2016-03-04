from pbcs import *
from pbcs import Lattice

import numpy as np

l = Lattice()
l.print_dim()
n=23
l.print_n(23)
print "x=", l.return_x(23)

ri_x=float(55.6)
r_i = np.array([ float(55.6), float(35.6),float(66.7)])
print "ldr", l.sum_r(r_i)
#print "sum_i",sum_i

y = l.return_y(556)
print ' y in pyton ',y
print " pass ri \n"
print l.dr_ij(r_i)

