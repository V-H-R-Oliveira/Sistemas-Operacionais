#include "kernel.h"

void *allocMem(size_t size)
{
    return malloc(size);
} 

void freeMem(void *mem)
{
    return free(mem);
}

