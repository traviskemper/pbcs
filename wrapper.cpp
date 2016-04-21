#include "pbc.cpp"

extern "C" {

  void print_basis(Lattice* lat){
    PBC *pbc = new PBC() ;
    pbc->print_basis(lat);
  }

  void delta_npos(Lattice* lat,double* npos_i,int n_i,double* npos_j,int n_j,double* npos_ij,double* nd_ij){
    PBC *pbc = new PBC() ;
    return pbc->delta_npos(lat,npos_i,n_i,npos_j,n_j,npos_ij,nd_ij);
  }
}

