#include <iostream>


class Lattice{
    public:
    
    Lattice(){
    }
    
    void print_dim(){
        std::cout << "Hello dim = ??"   << std::endl;
        
    }
    
    void print_n(int n){
        std::cout << "Run print_n"   << std::endl;
        std::cout << n   << std::endl;
    }
    
    int return_x(int n){
        int x = 12;
        
        // std::cout << "Run print_n"   << std::endl;
        //std::cout << n   << std::endl;
        return x;
    }
    

};

extern "C" {
    
    Lattice* Lattice_new(){ return new Lattice(); }
    void Lattice_print_dim(Lattice* lattice){ lattice->print_dim(); }
    void Lattice_print_n(Lattice* lattice,int n){ lattice->print_n(n); }
    int Lattice_return_x(Lattice* lattice,int n){
        return lattice->return_x(n);
    }
    
}

