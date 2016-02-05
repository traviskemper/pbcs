from pbcs import *
from pbcs import Lattice

l = Lattice()
l.print_dim()
n=23
l.print_n(23)
print "x=", l.return_x(23)

ri_x=float(55.6)
r_i = [ float(55.6), float(35.6),float(66.7)]
sum_i =  l.dr_ij(r_i)
print "sum_i",sum_i