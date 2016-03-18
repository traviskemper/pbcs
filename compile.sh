# g++ -c -fPIC test.cpp -o test.o
# g++ -shared  -o libtest.so  test.o
# python test.py 

# g++ -c -fPIC class2.cpp -o class1.o
# g++ -shared  -o libpbc.so  class1.o
# python class1.py 

g++ -c -fPIC pbc.cpp -o pbc.o
g++ -shared  -o libpbc.so  pbc.o

python test_pbc.py 