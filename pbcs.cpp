#include <iostream>

class Foo{
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
        void print_dim(){
            std::cout << "Hello asd" << std::endl;

	    // int n_dim = 3;

	  // std::cout << "n_dim " << n_dim << endl;

	  // return n_dim;

	}

};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
    void Foo_print_dim(Foo* foo){ foo->print_dim(); }
}

