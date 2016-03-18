#include <stdio.h>

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

  void delta_r(Lattice *lat,double* ri) {
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



}

