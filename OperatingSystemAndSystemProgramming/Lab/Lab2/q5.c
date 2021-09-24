#include <stdio.h>
#include <unistd.h>

int main()
{
    int pipefds[2];
    int returnstatus;
    int pid;

    char writemessage[2][20] = {"Hi", "Hello"};
    char readmessage[20];

    returnstatus = pipe(pipefds);
    if (returnstatus == -1)
    {
        printf("Unable to create pipe");
        return 1;
    }

    pid = fork();

    // child process
    if (pid == 0)
    {
        read(pipefds[0], readmessage, sizeof(readmessage));
        printf(" Child process from pipe message 1 %s \n", readmessage);

        read(pipefds[0], readmessage, sizeof(readmessage));
        printf(" Child process from pipe message 2 %s \n", readmessage);
    }
    else
    {
        printf("writing msg 1 to pipe %s \n", writemessage[0]);
        write(pipefds[1], writemessage[0], sizeof(writemessage[0]));

        printf("writing msg 2 to pipe %s \n", writemessage[1]);
        write(pipefds[1], writemessage[1], sizeof(writemessage[1]));
    }

    return 0;
}

/* 
 writing msg 1 to pipe Hi 
 writing msg 2 to pipe Hello 
 Child process from pipe message 1 Hi 
 Child process from pipe message 2 Hello 
 */