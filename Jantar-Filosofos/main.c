#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>
#include <pthread.h>
#include <unistd.h>
#define N 5
#define PENSAR 0
#define FOME 1
#define COMER 2
#define ESQUERDA (filosofo + 4) % N
#define DIREITA (filosofo + 1) % N

sem_t mutex;
sem_t S[N]; // estrutura do semáforo para os garfos

int estados[N];
int filosofos[N] = {0, 1, 2, 3, 4};
void *filosofo(void *);
void agarraGarfo(int);
void deixaGarfo(int);
void teste_condicoes(int);

void *filosofo(void *arg)
{
   int x = 0;

   while(x < 2)
   {
      int *i = arg;
      sleep(1);
      agarraGarfo(*i);
      sleep(1);
      deixaGarfo(*i);
	  x++;
   }
}

void agarraGarfo(int filosofo)
{
   sem_wait(&mutex);
   estados[filosofo] = FOME;
   printf("Filosofo %d está com fome.....\n", filosofo + 1);
   teste_condicoes(filosofo);
   sem_post(&mutex);
   sem_wait(&S[filosofo]);
   sleep(2);
}

void deixaGarfo(int filosofo)
{
   sem_wait(&mutex);
   estados[filosofo] = PENSAR;
   printf("Filosofo %d deixou os garfos %d e %d......\n", filosofo + 1, ESQUERDA + 1, DIREITA + 1);
   printf("Filosofo %d esta a pensar....\n", filosofo + 1);
   teste_condicoes(ESQUERDA);
   teste_condicoes(DIREITA);
   sem_post(&mutex);
}

void teste_condicoes(int filosofo)
{
   if(estados[filosofo] == FOME && estados[ESQUERDA] != COMER && estados[DIREITA] != COMER)
   {
      estados[filosofo] = COMER;
      sleep(2);
      printf("Filosofo %d agarrou os garfos %d e %d.....\n", filosofo + 1, ESQUERDA + 1, DIREITA + 1);
      printf("Filosofo %d está comendo.....\n", filosofo + 1);
      sem_post(&S[filosofo]);
   }
}

int main(void)
{
   pthread_t thread_id[N];
   sem_init(&mutex,0,1);

   for(int i = 0; i < N; i++) sem_init(&S[i],0,0);
   puts("Estado inicial.....");

   for(int i = 0; i < N; i++)
   {
      pthread_create(&thread_id[i], NULL, filosofo, &filosofos[i]);
      printf("Filosofo %d está pensando......\n", i + 1);
   }

   for(int i = 0; i < N; i++) pthread_join(thread_id[i],NULL);

   return 0;
}
