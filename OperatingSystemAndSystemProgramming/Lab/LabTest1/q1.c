#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

struct args
{
    int N;
};

// Function For finding Prime numbers upto N
void *findprimeNoUptoN(void *input)
{

    int low = 0, high = ((struct args *)input)->N, i, flag;

    while (low < high)
    {
        flag = 0;

        if (low <= 1)
        {
            ++low;
            continue;
        }

        for (i = 2; i <= low / 2; ++i)
        {

            if (low % i == 0)
            {
                flag = 1;
                break;
            }
        }

        if (flag == 0)
            printf("%d ", low);

        ++low;
    }
}

// Function For finding Fabonacci numbers upto N
void *findFabonacciNoUptoN(void *input)
{
    int sum = 0, n = ((struct args *)input)->N;
    int a = 0;
    int b = 1;

    while (sum <= n)
    {
        printf("%d ", sum);
        a = b;
        b = sum;
        sum = a + b;
    }
}
int main()
{
    int N;
    printf("Enter Number N\n");
    scanf("%d", &N);

    struct args *Argument = (struct args *)malloc(sizeof(struct args));
    Argument->N = N;

    printf("Print Prime numbers till %d\n",N);

    pthread_t tid;
    pthread_create(&tid, NULL, findprimeNoUptoN, (void *)Argument);
    pthread_join(tid, NULL);
    printf("\nPrint Fabonacci upto %d\n",N);

    pthread_t tid_1;
    pthread_create(&tid_1, NULL, findFabonacciNoUptoN, (void *)Argument);
    pthread_join(tid_1, NULL);
    return 0;
}
