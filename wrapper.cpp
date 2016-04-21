#include "pbc.cpp"

extern "C" {
  void call_pbc(){
    PBC *pbc = new PBC() ;
    pbc->call_pbc2();
  }
  void pass_lat(Lattice* lat){
    PBC *pbc = new PBC() ;
    pbc->pass_lat2(lat);
  }
}

