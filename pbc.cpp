#include <stdio.h>
#include <iostream>

using namespace std;

typedef struct Lattice {
  int     d;
  float   basis[3][3];
} Lattice;


extern "C" {

  void print_basis(Lattice *lat) {
    int i,j;
    printf(" d = %d \n",lat->d);
    printf("\n");

    for (j = 0; j < lat->d; ++j) {
      for (i = 0; i < lat->d; ++i) {
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

