import sys, os

sep_str = "--------------------------------------------------------------------------------------"
out_line = sep_str
out_line += "\n                 Testing pbc moudle "
out_line +=  "\n"+sep_str

def main():

    print out_line

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



    command='pbc_i.return_basis()'
    tag='return_basis_2'
    rshift=len(tag)+len(command)
    try:
        basis_i = pbc_i.return_basis()
        f = open('%s.test'%(tag), 'w')
        for i in range(pbc_i.lat.d):
            for j in range(pbc_i.lat.d):
                f.write(" basis_i [%d][%d] = %g  \n"%(i,j,basis_i[i][j]))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.out"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.set_basis()'
    tag='set_basis_1'
    rshift=len(tag)+len(command)
    try:
        basis_i = pbc_i.return_basis()
        f = open('%s.test'%(tag), 'w')
        for i in range(pbc_i.lat.d):
            for j in range(pbc_i.lat.d):
                f.write(" basis_o [%d][%d] = %g  \n"%(i,j,basis_i[i][j]))
        basis_i[0,0]=150.0
        basis_i[1,1]=150.0
        basis_i[2,2]=150.0
        pbc_i.set_basis(basis_i)
        for i in range(pbc_i.lat.d):
            for j in range(pbc_i.lat.d):
                f.write(" basis_i [%d][%d] = %g  \n"%(i,j,basis_i[i][j]))
        f.write(" a  = %g  \n"%(pbc_i.lat.a))
        f.write(" b  = %g  \n"%(pbc_i.lat.b))
        f.write(" c  = %g  \n"%(pbc_i.lat.c))
        f.write(" alpha  = %g  \n"%(pbc_i.lat.alpha))
        f.write(" gamma  = %g  \n"%(pbc_i.lat.gamma))
        f.write(" beta  = %g  \n"%(pbc_i.lat.beta))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.out"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.find_Bravais()'
    tag='find_Bravais_1'
    rshift=len(tag)+len(command)
    try:
        Bravais_numb = pbc_i.find_Bravais()
        Bravais_type = pbc_i.return_Bravais()
        f = open('%s.test'%(tag), 'w')
        f.write(" Bravais  %s [%d]  \n"%(Bravais_type,Bravais_numb))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.out"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.delta_npos()'
    tag='delta_npos_1'
    rshift=len(tag)+len(command)
    try:

        npos_i = []
        npos_i.append(np.array([25.0,25.0,25.0], dtype='float64'))
        npos_i.append(np.array([-125.0,-125.0,-125.0], dtype='float64'))
        npos_i.append(np.array([-15.0,35.0,-5.0], dtype='float64'))
        npos_j = []
        npos_j.append(np.array([5.0,75.0,25.0], dtype='float64'))
        npos_j.append(np.array([-10.0,-15.0,0.0], dtype='float64'))
        npos_j.append(np.array([-25.0,-90.0,-45.0], dtype='float64'))
        npos_ij,nd_ij = pbc_i.delta_npos(npos_i,npos_j)

        print "len(npos_i)",len(npos_i)
        
        f = open('%s.test'%(tag), 'w')
        for n in range(len(npos_i)):
            pos_i = npos_i[n]
            f.write(" pos_i %d  [ %f %f %f ] \n"%(n+1,pos_i[0],pos_i[1],pos_i[2]))
        for n in range(len(npos_j)):
            pos_j = npos_j[n]
            f.write(" pos_j %d  [ %f %f %f ]  \n"%(n+1,pos_j[0],pos_j[1],pos_j[2]))
            
        for n in range(len(npos_ij)):
            pos_ij = npos_ij[n]
            f.write(" pos_ij %d  [ %f %f %f ] | %f | \n"%(n+1,pos_ij[0],pos_ij[1],pos_ij[2],nd_ij[n]))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.out"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    sys.exit(" test set 1")


    command='pbc_i.print_basis()'
    tag='print_basis_1'
    rshift=len(tag)+len(command)
    try:
        f = open('%s.test'%(tag), 'w')
        lat_string = pbc_i.print_basis()
        print "lat_string ",lat_string
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

if __name__=="__main__":
    main()

