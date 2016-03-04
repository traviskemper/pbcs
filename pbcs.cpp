#include <iostream>



class Lattice{
    public:
    
    
    Lattice(){
    }
    
    void print_dim(){
      int dim = 3 ;
        std::cout << "Hello dim = "  << dim  << std::endl;
        
    }
    
    void print_n(int n){
        std::cout << "Run print_n"   << std::endl;
        std::cout << &n   << std::endl;
        std::cout << n   << std::endl;
    }
    
    int return_x(int n){
        int x = 12;
        
        // std::cout << "Run print_n"   << std::endl;
        //std::cout << n   << std::endl;
        return n;
    }

    int return_y(int n){
      int y;
      y = n + 100;
      std::cout << "y = " << y   << std::endl;
      return y;
    }
    
    double sum_r(double ri_x,double ri_y,double ri_z){
        double sum_i = 0;
        std::cout << "Run dr_ij "  << std::endl;
        std::cout << "    dr_x  = "    <<  ri_x << std::endl;
        std::cout << "    dr_y  = "    <<  ri_y << std::endl;
        std::cout << "    dr_z  = "    <<  ri_z << std::endl;
        sum_i = ri_x + ri_y + ri_z;
        std::cout << "    sum_i  = "    <<  sum_i << std::endl;
        return sum_i;
        
    }
    
    double* dr_ij(double* ri){
        ri[0] = 33.337;
        std::cout << " in dr_ij ri = "<< ri[0] << " "<< ri[1] << " "<< ri[2] << std::endl;
        return ri;
    }
    


};

extern "C" {
    
    Lattice* Lattice_new(){ return new Lattice(); }
    void Lattice_print_dim(Lattice* lattice){ lattice->print_dim(); }
    void Lattice_print_n(Lattice* lattice,int n){ lattice->print_n(n); }
    int Lattice_return_x(Lattice* lattice,int n){
        return lattice->return_x(n);
    }
    int Lattice_return_y(Lattice* lattice,int n){
         return lattice->return_y(n);
    }
    double Lattice_sum_r(Lattice* lattice, double ri_x,double ri_y,double ri_z){
      return lattice->sum_r(ri_x,ri_y,ri_z);
    }
    double* Lattice_dr_ij(Lattice* lattice,double* ri){
         return lattice->dr_ij(ri);
    }
    
}

