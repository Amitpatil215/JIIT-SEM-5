// it is exicutable file

#include <stdio.h>
#include <unistd.h>

int main()
{
    char *args[] = {"./q3exac", NULL};
    execvp(args[0], args);
    printf("%s", args[0]);
    printf("I'm  executing cause  command told me to do so");
    return 0;
}

/* 
gcc q3.c - o q3exec

for running
./q3exac

 */