#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define MEGASxMb 1024L
#include "kernel.h"

void *mem;

int main()
{
    mem = allocMem(MB * MEGASxMb); // alocou
    long i = 0;

    if(mem) 
    {
        puts("Alocou!!!");
        for(; i < MB*MEGASxMb - 1; i++)
        {
            ((char *) mem)[i] = 'a';
        }
        
        sleep(10);
        freeMem(mem);
    }

    return 0;
}