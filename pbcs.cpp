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
    float dr_ij(double ri_x,double ri_y,double ri_z){
        //= 1.12312;
        float sum_i = 0;
        std::cout << "Run dr_ij "  << std::endl;
        std::cout << "    dr_x  = "    <<  ri_x << std::endl;
        std::cout << "    dr_y  = "    <<  ri_y << std::endl;
        std::cout << "    dr_z  = "    <<  ri_z << std::endl;
        sum_i = ri_x + ri_y;
        std::cout << "    sum_i  = "    <<  sum_i << std::endl;
        return sum_i;
        
    }
    

};

extern "C" {
    
    Lattice* Lattice_new(){ return new Lattice(); }
    void Lattice_print_dim(Lattice* lattice){ lattice->print_dim(); }
    void Lattice_print_n(Lattice* lattice,int n){ lattice->print_n(n); }
    int Lattice_return_x(Lattice* lattice,int n){
        return lattice->return_x(n);
    }
    float Lattice_dr_ij(Lattice* lattice, double ri_x,double ri_y,double ri_z){return lattice->dr_ij(ri_x,ri_y,ri_z); }
    
}

