#include <math.h>       /* sqrt */
#include <cmath>

#include <stdio.h>
#include <iostream>

using namespace std;


typedef struct Lattice {
    int     d;
    int     Bravais;
    double     a;
    double     b;
    double     c;
    double     alpha;
    double     beta;
    double     gamma;
    double   basis[3][3];
} Lattice;

class Position{
    
public:
    
    Position(){
        
    }
    
    void delta_pos_c(Lattice* lat,double* pos_i,double* pos_j,double* d_pos){
        
        d_pos[0] = pos_j[0] - pos_i[0];
        d_pos[1] = pos_j[1] - pos_i[1];
        d_pos[2] = pos_j[2] - pos_i[2];
        
        d_pos[0] = d_pos[0] - lat->basis[0][0] * round( d_pos[0]/lat->basis[0][0] );
        d_pos[1] = d_pos[1] - lat->basis[1][1] * round( d_pos[1]/lat->basis[1][1] );
        d_pos[2] = d_pos[2] - lat->basis[2][2] * round( d_pos[2]/lat->basis[2][2] );
        
    }
    
    void delta_pos(Lattice* lat,double* pos_i,double* pos_j,double* d_pos){
        
        // Set lattice vectors
        double frac_i[3];
        double frac_j[3];
        double frac_ij[3];
        
        double AA;
        double AB;
        double AC;
        double BA;
        double BB;
        double BC;
        double CA;
        double CB;
        double CC;
        double X;
        double Y;
        double Z;
        
        AA = lat->basis[0][0];
        AB = lat->basis[0][1];
        AC = lat->basis[0][2];
        BA = lat->basis[1][0];
        BB = lat->basis[1][1];
        BC = lat->basis[1][2];
        CA = lat->basis[2][0];
        CB = lat->basis[2][1];
        CC = lat->basis[2][2];
        
        X = pos_i[0];
        Y = pos_i[1];
        Z = pos_i[2];
        frac_i[0] = -((-BC*CB*X+BB*CC*X+BC*CA*Y-BA*CC*Y-BB*CA*Z+BA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        frac_i[1] = -((AC*CB*X-AB*CC*X-AC*CA*Y+AA*CC*Y+AB*CA*Z-AA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        frac_i[2] = -((-AC*BB*X+AB*BC*X+AC*BA*Y-AA*BC*Y-AB*BA*Z+AA*BB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        X = pos_j[0];
        Y = pos_j[1];
        Z = pos_j[2];
        frac_j[0] = -((-BC*CB*X+BB*CC*X+BC*CA*Y-BA*CC*Y-BB*CA*Z+BA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        frac_j[1] = -((AC*CB*X-AB*CC*X-AC*CA*Y+AA*CC*Y+AB*CA*Z-AA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        frac_j[2] = -((-AC*BB*X+AB*BC*X+AC*BA*Y-AA*BC*Y-AB*BA*Z+AA*BB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        
        frac_ij[0] = frac_j[0] - frac_i[0];
        frac_ij[1] = frac_j[1] - frac_i[1];
        frac_ij[2] = frac_j[2] - frac_i[2];
        
        frac_ij[0] = frac_ij[0] - round(frac_ij[0]);
        frac_ij[1] = frac_ij[1] - round(frac_ij[1]);
        frac_ij[2] = frac_ij[2] - round(frac_ij[2]);
                
        d_pos[0] = AA*frac_ij[0] + BA*frac_ij[1] + CA*frac_ij[2];
        d_pos[1] = AB*frac_ij[0] + BB*frac_ij[1] + CB*frac_ij[2];
        d_pos[2] = AC*frac_ij[0] + BC*frac_ij[1] + CC*frac_ij[2];
        
        // return r_ij;
    }
    
    double mag_pos(Lattice* lat, double* pos_i, double d_ij){
        d_ij = sqrt(pos_i[0]*pos_i[0] + pos_i[1]*pos_i[1] + pos_i[2]*pos_i[2]);
        return d_ij;
    }
    
    void delta_npos(Lattice* lat,double* npos_i,int i,double* npos_j,int j,double* npos_ij,double* nd_ij){
        int n,m,o,p;
        double pos_i[3];
        double pos_j[3];
        double d_r_ij[3];
        
        o = 0;
        p = 0;
        for (m = 0; m < i*3; m=m+3) {
            //printf("print_npos npos_i (%d)  %f %f %f  \n", m , npos_i[m+0], npos_i[m+1], npos_i[m+2]);
            pos_i[0] = npos_i[m+0];
            pos_i[1] = npos_i[m+1];
            pos_i[2] = npos_i[m+2];
            for (n = 0; n < j*3; n=n+3) {
                //printf("print_npos npos_j (%d)  %f %f %f  \n", n, npos_j[n+0], npos_j[n+1], npos_j[n+2]);
                pos_j[0] = npos_j[n+0];
                pos_j[1] = npos_j[n+1];
                pos_j[2] = npos_j[n+2];
                printf("delta_npos %d ",lat->d);
                if( lat->d < 3 ){
                    delta_pos_c(lat, pos_i,pos_j,d_r_ij);
                }
                else
                    {
                    delta_pos(lat, pos_i,pos_j,d_r_ij);
                        
                }
                npos_ij[o+0] = d_r_ij[0]; //npos_j[n+0] - npos_i[m+0];
                npos_ij[o+1] = d_r_ij[1]; //npos_j[n+1] - npos_i[m+1];
                npos_ij[o+2] = d_r_ij[2]; //npos_j[n+2] - npos_i[m+2];
                o = o + 3;
                nd_ij[p] = mag_pos(lat, d_r_ij,nd_ij[p]);
                p = p + 1;
            }
        }
    }
    
    
};