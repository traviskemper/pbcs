

#include <iostream>
#include <vector>

class Lattice{
    public:

    int dim;
    float basis  [3][3];
    
  // std::vector<float> rij;

    Lattice(){
        dim = 3;
	basis[0][0] = 10.0 ;
	basis[1][1] = 10.0 ;
	basis[2][2] = 10.0 ;
    }
    
    void print_dim(){
      std::cout << "\n dimensions = "<< dim << std::endl;
    }
  
    void print_basis(){
      std::cout << " basis 1 = "<< basis[0][0] << " "<< basis[0][1] << " "<< basis[0][2] << " " << std::endl;
      std::cout << " basis 2 = "<< basis[1][0] << " "<< basis[1][1] << " "<< basis[1][2] << " " << std::endl;
      std::cout << " basis 3 = "<< basis[2][0] << " "<< basis[2][1] << " "<< basis[2][2] << " " << std::endl;
    }  
    
    void set_basis( float basis_i[][3] ){
      int n;
      int m;
      for (n=0;n<dim;n++){
	for (m=0;m<dim;m++){
	  basis[n][m] = basis_i[n][m];
	}
      }
    }

    std::vector<float>  dr(  std::vector<float> ri,  std::vector<float> rj ){

      int n;
      std::vector<float> rij (3);

      for (n=0;n<dim;n++){
	rij[n] = ri[n] - rj[n];
      }
      return rij;
    }


    std::vector<float>  realfractional(  std::vector<float> ri ){
      
      //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      //  Calculate fractional coordinates from mathmatica 
      //  J -> -(-BC CB X + BB CC X + BC CA Y - BA CC Y - BB CA Z + 
      //       BA CB Z)/(AC BB CA - AB BC CA - AC BA CB + AA BC CB + 
      //       AB BA CC - AA BB CC), 
      //  L -> -(AC CB X - AB CC X - AC CA Y + AA CC Y + AB CA Z - 
      //       AA CB Z)/(AC BB CA - AB BC CA - AC BA CB + AA BC CB + 
      //       AB BA CC - AA BB CC), 
      //  M -> -(-AC BB X + AB BC X + AC BA Y - AA BC Y - AB BA Z + 
      //       AA BB Z)/(AC BB CA - AB BC CA - AC BA CB + AA BC CB + 
      //       AB BA CC - AA BB CC)}}

      std::vector<float> f_r (3);

      //     Set lattice vectors
      float AA = basis[0][0]; //(1,1)
      float AB = basis[0][1]; //(1,2)
      float AC = basis[0][2]; //(1,3)
      float BA = basis[1][0]; //(2,1)
      float BB = basis[1][1]; //(2,2)
      float BC = basis[1][2]; //(2,3)
      float CA = basis[2][0]; //(3,1)
      float CB = basis[2][1]; //(3,2)
      float CC = basis[2][2]; //(3,3)


      float X = ri[0] ;
      float Y = ri[1] ;
      float Z = ri[2] ;

      f_r[0] = -((-BC*CB*X+BB*CC*X+BC*CA*Y-BA*CC*Y-BB*CA*Z+BA*CB*Z)/ (AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC)) ;
      f_r[1] =-((AC*CB*X-AB*CC*X-AC*CA*Y+AA*CC*Y+AB*CA*Z-AA*CB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));
      f_r[2] =-((-AC*BB*X+AB*BC*X+AC*BA*Y-AA*BC*Y-AB*BA*Z+AA*BB*Z)/(AC*BB*CA-AB*BC*CA-AC*BA*CB+AA*BC*CB+AB*BA*CC-AA*BB*CC));

      return f_r;
    }

        
};


int main(int argc, char** argv) {

  int n;
  int m;
  
  float basis_i  [3][3];
  float basis_j  [3][3];

  std::vector<float> ri (3);
  std::vector<float> rj (3);
  std::vector<float> rij (3);

  for (n=0;n<3;n++){
    ri[n] = 0.0 ;
    for (m=0;m<3;m++){
      basis_i[n][m] = 0.0;
    }
  }
  
  printf("\n new system ");
  Lattice *lattice = new Lattice() ;
  
  lattice->print_dim();
  lattice->print_basis();

  basis_i[0][0] = 100.0 ;
  basis_i[1][1] = 100.0 ;
  basis_i[2][2] = 100.0 ;

  //basis_i = lattice->get_basis();
  lattice->set_basis(basis_i);
  lattice->print_basis();
  
  ri[0] = 2.0;
  ri[1] = 4.0;
  ri[2] = 0.50;
  std::cout << " ri = "<< ri[0] << " "<< ri[1] << " "<< ri[2] << std::endl;
  rj[0] = -2.0;
  rj[1] = -4.0;
  rj[2] = -0.50;
  std::cout << " rj = "<< rj[0] << " "<< rj[1] << " "<< rj[2] << std::endl;
  //basis_j = lattice->get_basis();
  //basis_j = lattice->get_basis();
  //n = 0;
  //rij[n] = lattice->dr_n(ri[n],rj[n]);
  rij = lattice->dr(ri,rj);
  std::cout << " rij = "<< rij[0] << " "<< rij[1] << " "<< rij[2] << std::endl;
  printf("\n setting fractional  ");
  rij = lattice->realfractional(rij);
  std::cout << " rij = "<< rij[0] << " "<< rij[1] << " "<< rij[2] << std::endl;
  

  return 0;
}
