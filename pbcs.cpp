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

class Foo{
    public:
    
    
        void bar(){
            std::cout << "Hello" << std::endl;
        }
        void print_dim(){
            std::cout << "Hello asd" << std::endl;

	}

};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
    void Foo_print_dim(Foo* foo){ foo->print_dim(); }

    Lattice* Lattice_new(){ return new Lattice(); }
    void Lattice_print_dim(Lattice* lattice){ lattice->print_dim(); }
}

