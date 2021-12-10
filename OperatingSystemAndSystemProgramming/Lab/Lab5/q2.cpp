#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <string.h>

#define MAX_NUM 1
sem_t sem1, sem2, sem3, sem4;
int cuur = 0;

// Decleration of globle String
char globalString[10] = "";

void printFunction(int i)
{
    printf("Thread %d is executing\n", i);
}

void *f1(void *p)
{
    printf("%s", (char *)p);
    for (int i = 1; i <= MAX_NUM; i++)
    {
        sem_wait(&sem1);
        printFunction(1);
        printf("Modiifed global string to -> f1\n");
        sem_post(&sem2);
    }
}

void *f2(void *p)
{
    for (int i = 1; i <= MAX_NUM; i++)
    {
        sem_wait(&sem2);
        printFunction(2);
        // printf("%s", strncat);
        printf("Modiifed global string to -> f2\n");
        sem_post(&sem3);
    }
}

void *f3(void *p)
{
    for (int i = 1; i <= MAX_NUM; i++)
    {
        sem_wait(&sem3);
        printFunction(3);
        printf("Modiifed global string to -> f3\n");
        // strcnt()
        sem_post(&sem4);
    }
}

void *f4(void *p)
{
    for (int i = 1; i <= MAX_NUM; i++)
    {
        sem_wait(&sem4);
        printFunction(4);
        char f4string[] = "T4";
        printf("Modiifed global string to -> f4\n");
        p = &f4string;
        sem_post(&sem1);
    }
}
int main()
{
    pthread_t p1, p2, p3, p4;
    sem_init(&sem1, 0, 0);
    sem_init(&sem2, 0, 0);
    sem_init(&sem3, 0, 0);
    sem_init(&sem4, 0, 1);

    pthread_create(&p1, NULL, f1, globalString);
    pthread_create(&p2, NULL, f2, globalString);
    pthread_create(&p3, NULL, f3, globalString);
    pthread_create(&p4, NULL, f4, globalString);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);
    pthread_join(p4, NULL);

    return 0;
}