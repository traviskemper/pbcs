
typedef struct Lattice {
  int     d;
  int     Bravais;
  float     a;
  float     b;
  float     c;
  float     alpha;
  float     beta;
  float     gamma;
  float   basis[3][3];
  float   fractional[3][3];
} Lattice;
