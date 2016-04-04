//
//  main.cpp
//  pbc
//
//  Created by Kemper, Travis on 4/3/16.
//  Copyright (c) 2016 Kemper, Travis. All rights reserved.
//

#include "main.h"

#include <stdio.h>
#include <iostream>
#include <cmath>
#include "position.cpp"

using namespace std;

int main(int argc, const char * argv[])
{
    printf(" new system \n");
    Position *position = new Position() ;
    
    int i,j,n,m,o,ij  ;
    i = 4 ;
    j = 4 ;
    ij = i*j;
    double npos_i[i*3];
    double npos_j[i*3];
    double npos_ij[ij*3];
    
    for (n = 0; n < i*3; n=n+3) {
        npos_i[n] = 1.0 ;
        npos_i[n+1] = 10.0 ;
        npos_i[n+2] = 2.0 ;
        
    }
    for (m = 0; m < j*3; m=m+3) {
        npos_j[m] = 8.0 ;
        npos_j[m+1] = 9.0 ;
        npos_j[m+2] = 10.0 ;
        
    }
    position->delta_npos(npos_i,i,npos_j,j,npos_ij);
    
    for (m = 0; m < i*3; m=m+3) {
        printf("main npos_i (%d)  %f %f %f  \n", m , npos_i[m+0], npos_i[m+1], npos_i[m+2]);
    }
    for (o = 0; o < ij*3; o=o+3) {
        printf("mian npos_ij (%d)  %f %f %f  \n", o, npos_ij[o+0], npos_ij[o+1], npos_ij[o+2]);
    }
    printf("  \n");
    double d_r_ij[3];
    double pos_i[3];
    double pos_j[3];
    pos_i[0] = 1.75 ;
    pos_i[1] = 4.25 ;
    pos_i[2] = 2.25 ;
    pos_j[0] = -6.75 ;
    pos_j[1] = 23.5 ;
    pos_j[2] = -9.5 ;
    
    position->delta_pos(pos_i,pos_j,d_r_ij);
    printf("mian d_r  %f %f %f  \n", d_r_ij[0], d_r_ij[1], d_r_ij[2]);
    
    return 0;
}


