
import sys, os

term_width=80
orig_stdout = sys.stdout

test_list = []

command='from pbc import PBC'
tag='importPBC'
rshift=len(tag)+len(command)
try:
    from pbc import PBC
    status='[OK]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status])

command='pbc_i = PBC'
tag='intializePBC'
rshift=len(tag)+len(command)
try:
    pbc_i = PBC()
    status='[OK]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status])

command='pbc_i.print_basis()'
tag='print_basis_1'
rshift=len(tag)+len(command)
try:
    f = open('%s.test'%(tag), 'w')
    print >> pbc_i.print_basis()
    f.close()
    status='[OK]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status])



command='pbc_i.set_diagbasis(55.0)'
tag='set_diagbasis_1'
rshift=len(tag)+len(command)
try:
    f = open('%s.test'%(tag), 'w')
    print >> pbc_i.set_diagbasis(55.0)
    f.close()
    status='[OK]'.rjust(term_width-rshift)
except:
    status='[FAILED]'.rjust(term_width-rshift)
if( os.system("diff %s.test %s.out"%(tag,tag)) ):
    status='[FAILED]'.rjust(term_width-rshift) 
print "%s %s %s"%(tag,command,status)
test_list.append([tag,command,status])

for tag,command,status in test_list:
    if ( status == '[FAILED]' ):
        tests_status = '[FAILED]'
        sys.exit(tag)
    
sys.exit(0)
