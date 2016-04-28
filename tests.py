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
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
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
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
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
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.delta_npos()'
    tag='delta_npos_1'
    rshift=len(tag)+len(command)
    try:

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

        f = open('%s.test'%(tag), 'w')
        for n in range(len(npos_i)):
            pos_i = npos_i[n]
            f.write(" pos_i %d  [ %f %f %f ] \n"%(n+1,pos_i[0],pos_i[1],pos_i[2]))
        for n in range(len(npos_j)):
            pos_j = npos_j[n]
            f.write(" pos_j %d  [ %f %f %f ]  \n"%(n+1,pos_j[0],pos_j[1],pos_j[2]))

        for n in range(len(npos_i)):
            for m in range(len(npos_j)):
                pos_ij = npos_ij[n][m]
                f.write(" pos_ij %d %d [ %f %f %f ] | %f | \n"%(n+1,m+1,pos_ij[0],pos_ij[1],pos_ij[2],nd_ij[n][m]))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.set_basis()'
    tag='set_basis_2'
    rshift=len(tag)+len(command)
    try:

        basis_i = pbc_i.return_basis()
        f = open('%s.test'%(tag), 'w')
        for n in range(3):
            f.write(" Basis_o %d  [ %f %f %f ] \n"%(n+1,basis_i[n,0],basis_i[n,1],basis_i[n,2]))
        # Set local basis to new values
        basis_i[0,0]=120.0
        basis_i[1,1]=110.0
        basis_i[2,2]=130.0

        # Set lattice vectors to new values 
        pbc_i.set_basis(basis_i)
        for n in range(3):
            f.write(" Basis_i %d  [ %f %f %f ] \n"%(n+1,basis_i[n,0],basis_i[n,1],basis_i[n,2]))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.delta_npos()'
    tag='delta_npos_2'
    rshift=len(tag)+len(command)
    try:
        basis_i = pbc_i.return_basis()

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

        f = open('%s.test'%(tag), 'w')
        for n in range(3):
            f.write(" Basis_o %d  [ %f %f %f ] \n"%(n+1,basis_i[n,0],basis_i[n,1],basis_i[n,2]))        
        for n in range(len(npos_i)):
            pos_i = npos_i[n]
            f.write(" pos_i %d  [ %f %f %f ] \n"%(n+1,pos_i[0],pos_i[1],pos_i[2]))
        for n in range(len(npos_j)):
            pos_j = npos_j[n]
            f.write(" pos_j %d  [ %f %f %f ]  \n"%(n+1,pos_j[0],pos_j[1],pos_j[2]))

        for n in range(len(npos_i)):
            for m in range(len(npos_j)):
                pos_ij = npos_ij[n][m]
                f.write(" pos_ij %d %d [ %f %f %f ] | %f | \n"%(n+1,m+1,pos_ij[0],pos_ij[1],pos_ij[2],nd_ij[n][m]))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])


    command='pbc_i.delta_npos()'
    tag='delta_npos_3'
    rshift=len(tag)+len(command)
    try:
        basis_i = pbc_i.return_basis()

        npos_i = []
        npos_i.append(np.array([75.0,95.0,15.0], dtype='float64'))
        npos_i.append(np.array([-85.0,75.0,25.0], dtype='float64'))
        npos_i.append(np.array([-96.0,-68.0,33.0], dtype='float64'))
        npos_i.append(np.array([-85.0,-38.0,-78.0], dtype='float64'))
        npos_j = npos_i
        npos_ij,nd_ij = pbc_i.delta_npos(npos_i,npos_j)

        f = open('%s.test'%(tag), 'w')
        for n in range(3):
            f.write(" Basis_o %d  [ %f %f %f ] \n"%(n+1,basis_i[n,0],basis_i[n,1],basis_i[n,2]))        
        for n in range(len(npos_i)):
            pos_i = npos_i[n]
            f.write(" pos_i %d  [ %f %f %f ] \n"%(n+1,pos_i[0],pos_i[1],pos_i[2]))
        for n in range(len(npos_j)):
            pos_j = npos_j[n]
            f.write(" pos_j %d  [ %f %f %f ]  \n"%(n+1,pos_j[0],pos_j[1],pos_j[2]))

        for n in range(len(npos_i)):
            for m in range(len(npos_j)):
                pos_ij = npos_ij[n][m]
                f.write(" pos_ij %d %d [ %f %f %f ] | %f | \n"%(n+1,m+1,pos_ij[0],pos_ij[1],pos_ij[2],nd_ij[n][m]))
        f.close()
        status='[PASSED]'.rjust(term_width-rshift)
    except:
        status='[FAILED]'.rjust(term_width-rshift)
    if( os.system("diff %s.test %s.ref"%(tag,tag)) ):
        status='[FAILED]'.rjust(term_width-rshift) 
    print "%s %s %s"%(tag,command,status)
    test_list.append([tag,command,status.strip()])

    tests_status = '[PASSED]'
    for tag,command,status in test_list:
        if ( status == '[FAILED]' ):
            tests_status = '[FAILED]'

    print "\n          Testing of %s module  %s"%(mod_name,tests_status)

    update_ref = False  
    for tag,command,status in test_list:
        os.system("cp %s.test %s.ref"%(tag,tag))
        
    sys.exit(0)

if __name__=="__main__":
    main()

