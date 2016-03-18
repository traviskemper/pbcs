g++ -c -fPIC pbcs.cpp -o pbcs.o
g++ -shared  -o libpbcs.so  pbcs.o


python test.py 

