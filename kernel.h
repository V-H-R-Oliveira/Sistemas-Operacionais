#include <stdlib.h>
#define MB (1024 * 1024)

// Prioridade

#define HIGH_P 0
#define MED_P 1
#define LOW_P 2

// estados

#define READY 0
#define RUNNING 1
#define BLOCKED 2
#define FINISH 3

void *allocMem(size_t size); 
void freeMem(void *mem);

struct Processo
{
    unsigned int pid;
    char * nome;
    int prioridade;
    unsigned int dep_pid; // depedência
};