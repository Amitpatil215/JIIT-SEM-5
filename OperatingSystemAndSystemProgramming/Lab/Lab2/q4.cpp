#include <stdio.h>
#include <unistd.h>

int main()
{
    int pipefds[2]; // count of pipe file descriptiors
    int returnstatus;

    char writemessages[2][20] = {"Hi", "There"};
    char readmessage[20];

    returnstatus = pipe(pipefds);

    if (returnstatus == -1)
    {
        printf("Unable to create pipe");
        return 0;
    }

    printf("Writing to pipe message %s \n", writemessages[0]);
    write(pipefds[1], writemessages[0], sizeof(writemessages[0]));
    read(pipefds[0], readmessage, sizeof(readmessage));
    printf("%s", readmessage);

    printf("\n");

    printf("Writing to pipe message %s \n", writemessages[1]);
    write(pipefds[1], writemessages[1], sizeof(writemessages[1]));
    read(pipefds[0], readmessage, sizeof(readmessage));
    printf("%s", readmessage);
    return 0;
}

/* 
Writing to pipe message Hi 
Hi
Writing to pipe message There 

 */