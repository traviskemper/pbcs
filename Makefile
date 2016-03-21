CC=g++
CFLAGS=-c -fPIC

all: pbc.o libpbc.so

pbc.o: pbc.cpp
	$(CC) $(CFLAGS) pbc.cpp -o pbc.o

libpbc.so: pbc.o
	$(CC) -shared  -o libpbc.so  pbc.o

tests:
	python tests.py

example:
	python example.py

clean:
	rm -rf libpbc.so  pbc.o

