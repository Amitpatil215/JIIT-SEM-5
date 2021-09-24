#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{
    pid_t cpid;
    int stat;
    if (fork() == 0) // on success fork return 0 otherwise -1
        exit(10); // exit status code set to 10
    else
        cpid = wait(&stat);
    printf("Parent pid = %d\n", getppid());
    printf("Child pid = %d\n", cpid);

    if (WIFEXITED(stat))
        printf("Exit status: %d\n", WEXITSTATUS(stat));

    return 0;
}

/* 
Parent pid = 6652
Child pid = 16666
Exit status: 10
 */