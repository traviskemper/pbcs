//
//  wrapper.c
//  pbc
//
//  Created by Kemper, Travis on 3/4/16.
//  Copyright (c) 2016 Kemper, Travis. All rights reserved.
//

#include <stdio.h>
#include "pbc.cpp"


extern "C" {
    
    pbc* PBC_new(){ return new PBC() ;  }
    void PBC_print_Bravais(pbc* pbc){ pbc->print_Bravais(); }
}