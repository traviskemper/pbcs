
sep_str = "--------------------------------------------------------------------------------------"
out_line = sep_str
out_line += "\n                 Testing pbc moudle "
out_line +=  "\n"+sep_str

print out_line
import sys, os

mod_name = "pbc"
term_width=80
orig_stdout = sys.stdout

test_list = []


command='import numpy as np'
tag='importnumpy'
rshift=len(tag)+len(command)
try:
    import numpy as np
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])

command='from pbc import PBC'
tag='importPBC'
rshift=len(tag)+len(command)
try:
    from pbc import PBC
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])

command='pbc_i = PBC'
tag='intializePBC'
rshift=len(tag)+len(command)
try:
    pbc_i = PBC()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])

command='pbc_i.print_basis()'
tag='print_basis_1'
rshift=len(tag)+len(command)
try:
    f = open('%s.test'%(tag), 'w')
    print >> pbc_i.print_basis()
    f.close()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])



command='pbc_i.set_diagbasis(55.0)'
tag='set_diagbasis_1'
rshift=len(tag)+len(command)
try:
    f = open('%s.test'%(tag), 'w')
    print >> pbc_i.set_diagbasis(55.0)
    f.close()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])

command='pbc_i.print_basis()'
tag='print_basis_2'
rshift=len(tag)+len(command)
try:
    f = open('%s.test'%(tag), 'w')
    print >> pbc_i.print_basis()
    f.close()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])


command='pbc_i.print_r()'
tag='print_r_1'
rshift=len(tag)+len(command)
try:
    r_i = np.array([99.03,77.8,66.7])
    f = open('%s.test'%(tag), 'w')
    print >> pbc_i.print_r(r_i)
    f.close()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])


command='pbc_i.return_r(r_i)'
tag='return_r_1'
rshift=len(tag)+len(command)
try:
    r_i = np.array([0.00002324213,324554332.8,53543.7])
    r_j = pbc_i.return_r(r_i)
    print "r_j",r_j
    f = open('%s.test'%(tag), 'w')
    f.write(" r_i %g %g %g  "%(r_i[0],r_i[1],r_i[2]))
    f.write("\n r_j %g %g %g  "%(r_j[0],r_j[1],r_j[2]))
    f.close()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])


command='pbc_i.delta_r(r_i,r_j)'
tag='delta_r_1'
rshift=len(tag)+len(command)
try:
    r_i = np.array([0.00002324213,324554332.8,53543.7])
    r_j = np.array([99.03,77.8,66.7])
    dr_ij = pbc_i.delta_r(r_i,r_j)
    print "dr_ij",dr_ij
    f = open('%s.test'%(tag), 'w')
    f.write("\n r_i %g %g %g  "%(r_i[0],r_i[1],r_i[2]))
    f.write("\n r_j %g %g %g  "%(r_j[0],r_j[1],r_j[2]))
    f.write("\n dr_ij %g %g %g  "%(dr_ij[0],dr_ij[1],dr_ij[2]))
    f.write("\n")
    f.close()
    status='[PASSED]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
print "diff %s.test %s.out"%(tag,tag)
diff_out = os.system("diff %s.test %s.out"%(tag,tag))
print "diff_out",diff_out
if( diff_out ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status.strip()])


tests_status = '[PASSED]'
for tag,command,status in test_list:
    if ( status == '[FAILED]' ):
        tests_status = '[FAILED]'

print "\n          Testing of %s module  %s"%(mod_name,tests_status)
    
sys.exit(0)
