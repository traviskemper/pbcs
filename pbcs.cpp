#include <iostream>


class Lattice{
    public:

    int dim;
    int ri;
    int rj;

    Lattice(){
        dim = 3;
    }
    
    void print_dim(){
        std::cout << "Hello n = " << std::endl;
        
    }

};

extern "C" {

    Lattice* Lattice_new(){ return new Lattice(); }
    void Lattice_print_dim(Lattice* lattice){ lattice->print_dim(); }
}

