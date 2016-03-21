#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

typedef struct Lattice {
  int     d;
  int     Bravais;
  float     a;
  float     b;
  float     c;
  float     alpha;
  float     beta;
  float     gamma;
  float   basis[3][3];
  float   fractional[3][3];
} Lattice;


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

  double*  r_ij(Lattice *lat,double* r_i,double* r_j,double* r_ij){
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
    
    printf(" frac_ij  %g %g %g ",frac_ij[0],frac_ij[1],frac_ij[2]);


    frac_ij[0] = frac_ij[0] - round(frac_ij[0]);
    frac_ij[1] = frac_ij[1] - round(frac_ij[1]);
    frac_ij[2] = frac_ij[2] - round(frac_ij[2]);

    r_ij[0] = AA*frac_ij[0] + BA*frac_ij[1] + CA*frac_ij[2];
    r_ij[1] = AB*frac_ij[0] + BB*frac_ij[1] + CB*frac_ij[2];
    r_ij[2] = AC*frac_ij[0] + BC*frac_ij[1] + CC*frac_ij[2];
    return r_ij;
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

