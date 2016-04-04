#include <stdio.h>
#include <iostream>
#include <cmath>
#include "lattice.cpp"
#include "position.cpp"

using namespace std;


extern "C" {

  void print_basis(Lattice *lat) {
    int i,j;
    printf(" Dimensions = %d \n",lat->d);
    printf(" Bravais number = %d \n",lat->Bravais);
    printf(" a = %f \n",lat->a);
    printf(" b = %f \n",lat->b);
    printf(" c = %f \n",lat->c);
    printf(" alpha = %f \n",lat->alpha);
    printf(" beta = %f \n",lat->beta);
    printf(" gamma = %f \n",lat->gamma);
    printf("\n");

    for (i = 0; i < lat->d; ++i) {
      for (j = 0; j < lat->d; ++j) {
	printf("%g ", lat->basis[j][i]);
      }
      printf("\n");
    }
  }

  double*  calc_fractional(Lattice *lat,double* r,double* frac_r){
    // Set lattice vectors
    float AA;
    float AB;
    float AC;
    float BA;
    float BB;
    float BC;
    float CA;
    float CB;
    float CC;
    float X;
    float Y;
    float Z;
    int i;
    

    AA = lat->basis[0][0];
    AB = lat->basis[0][1];
    AC = lat->basis[0][2];
    BA = lat->basis[1][0];
    BB = lat->basis[1][1];
    BC = lat->basis[1][2];
    CA = lat->basis[2][0];
    CB = lat->basis[2][1];
    CC = lat->basis[2][2];

    for (i = 0; i < lat->d; ++i) {
        X = r[0];
        Y = r[1];
        Z = r[2];
	frac_r[0] = -((-BC*CB*X+BB*CC*X+BC*CA*Y-BA*CC*Y-BB*CA*Z+BA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
	frac_r[1] = -((AC*CB*X-AB*CC*X-AC*CA*Y+AA*CC*Y+AB*CA*Z-AA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
	frac_r[2] = -((-AC*BB*X+AB*BC*X+AC*BA*Y-AA*BC*Y-AB*BA*Z+AA*BB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
    }
    return frac_r;
  }

  double*  delta_r_ij(Lattice *lat,double* r_i,double* r_j,double* r_ij){
    // Set lattice vectors
    float frac_i[3];
    float frac_j[3];
    float frac_ij[3];

    float AA;
    float AB;
    float AC;
    float BA;
    float BB;
    float BC;
    float CA;
    float CB;
    float CC;
    float X;
    float Y;
    float Z;
    int i;
    

    AA = lat->basis[0][0];
    AB = lat->basis[0][1];
    AC = lat->basis[0][2];
    BA = lat->basis[1][0];
    BB = lat->basis[1][1];
    BC = lat->basis[1][2];
    CA = lat->basis[2][0];
    CB = lat->basis[2][1];
    CC = lat->basis[2][2];

    printf("\n in C++ r_ij r_i  %g %g %g ",r_i[0],r_i[1],r_i[2]);
    printf("\n in C++ r_ij r_j  %g %g %g ",r_j[0],r_j[1],r_j[2]);

    for (i = 0; i < lat->d; ++i) {
        X = r_i[0];
        Y = r_i[1];
        Z = r_i[2];
	frac_i[0] = -((-BC*CB*X+BB*CC*X+BC*CA*Y-BA*CC*Y-BB*CA*Z+BA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
	frac_i[1] = -((AC*CB*X-AB*CC*X-AC*CA*Y+AA*CC*Y+AB*CA*Z-AA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
	frac_i[2] = -((-AC*BB*X+AB*BC*X+AC*BA*Y-AA*BC*Y-AB*BA*Z+AA*BB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
        X = r_j[0];
        Y = r_j[1];
        Z = r_j[2];
	frac_j[0] = -((-BC*CB*X+BB*CC*X+BC*CA*Y-BA*CC*Y-BB*CA*Z+BA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
	frac_j[1] = -((AC*CB*X-AB*CC*X-AC*CA*Y+AA*CC*Y+AB*CA*Z-AA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
	frac_j[2] = -((-AC*BB*X+AB*BC*X+AC*BA*Y-AA*BC*Y-AB*BA*Z+AA*BB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
    }

    frac_ij[0] = frac_j[0] - frac_i[0];
    frac_ij[1] = frac_j[1] - frac_i[1];
    frac_ij[2] = frac_j[2] - frac_i[2];
    
    printf("\n frac_ij  %g %g %g ",frac_ij[0],frac_ij[1],frac_ij[2]);


    frac_ij[0] = frac_ij[0] - round(frac_ij[0]);
    frac_ij[1] = frac_ij[1] - round(frac_ij[1]);
    frac_ij[2] = frac_ij[2] - round(frac_ij[2]);

    printf("\n frac_ij 2 %g %g %g ",frac_ij[0],frac_ij[1],frac_ij[2]);

    r_ij[0] = AA*frac_ij[0] + BA*frac_ij[1] + CA*frac_ij[2];
    r_ij[1] = AB*frac_ij[0] + BB*frac_ij[1] + CB*frac_ij[2];
    r_ij[2] = AC*frac_ij[0] + BC*frac_ij[1] + CC*frac_ij[2];

    return r_ij;
  }

  double* pos_ij(Lattice *lat, double* npos_i, double* npos_j, int i, int j, double* pos_ij, double* dpos_ij){
    int n,m,pos_c,dpos_c;
    double dr_ij;
    double r_i[3],r_j[3],r_ij[3];

    pos_c = 0 ;
    dpos_c = 0 ;
    for (n = 0; n < i*3; n=n+3) {
      printf("r %f %f %f \n",  npos_i[i], npos_i[i+1], npos_i[i+2]);
      r_i[0] = npos_i[i];
      r_i[1] = npos_i[i+1];
      r_i[2] = npos_i[i+2];
      for (m = 0; m < j*3; m=m+3) {
	printf("r %f %f %f \n",  npos_j[i], npos_j[i+1], npos_j[i+2]);
	r_j[0] = npos_j[i];
	r_j[1] = npos_j[i+1];
	r_j[2] = npos_j[i+2];
	r_ij = delta_r_ij(lat,r_i,r_j,r_ij);
	pos_ij[pos_c] = r_ij[0];
	pos_ij[pos_c+1] = r_ij[1];
	pos_ij[pos_c+2] = r_ij[2];
	pos_c = pos_c + 3;
	dpos_ij[pos_c] = sqrt(r_ij[0]*r_ij[0] + r_ij[1]*r_ij[1] + r_ij[2]*r_ij[2]);
	dpos_c = dpos_c + 1;
      }
    }
    printf("\n");
    return pos_ij,dpos_ij;
        
   }

  double* set_r_array(Lattice *lat, double* npos_i, int n){
    int i;

    cout << " n = " << n << endl;
    cout << " in set_r_array  sizeof((npos_i))  = "<< sizeof((npos_i))   << endl;
    cout << " in set_r_array  sizeof((npos_i[0]))  = "<< sizeof((npos_i[0]))   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[0]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[1]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[2]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[3]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[4]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[5]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[6]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[7]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[8]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[9]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[10]   << endl;
    cout << " in set_r_array  npos_i[0]   = "<< npos_i[11]   << endl;

    for (i = 0; i < n*3; i=i+3) {
      cout << " i = " << i << endl;
      //cout << " in set_r_array ri = "<< npos_i[0][0] << endl;
      printf("r %f %f %f \n",  npos_i[i], npos_i[i+1], npos_i[i+2]);
    }
    printf("\n");
    return npos_i;
        
   }
            
  void print_fractional(Lattice *lat) {
    int i,j;
    for (i = 0; i < lat->d; ++i) {
      for (j = 0; j < lat->d; ++j) {
	printf("%g ", lat->basis[j][i]);
      }
      printf("\n");
    }
  }

  void print_r(double* ri){
    cout << " in pring_r ri = "<< ri[0] << " "<< ri[1] << " "<< ri[2] << endl;
  }

  double* return_r(double* ri){
    cout << " in return_r ri = "<< ri[0] << " "<< ri[1] << " "<< ri[2] << endl;
    return ri;
        
  }


  double* delta_r(Lattice *lat,double* ri,double* rj){
    
    cout << " in delta_r ri = "<< ri[0] << " "<< ri[1] << " "<< ri[2] << endl;
    cout << " in delta_r rj = "<< rj[0] << " "<< rj[1] << " "<< rj[2] << endl;
    return rj;
        
   }
    

}

