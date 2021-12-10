#include <stdio.h>
struct ProcessControlBlock
{
    int pid, wait, burst, turnaround, arrival;
};

void pline(int x)
{
    for (int i = 0; i < x; i++)
    {
        printf("-");
    }
    printf("\n");
}

void main()
{
    int i, num, j;
    int w_total = 0; //waiting total
    int t_total = 0; //turnaround total
    float w_avg = 0.0, t_avg = 0.0;
    float sum = 0.0;
    struct ProcessControlBlock p[10], temp;
    printf("SJF Algorithms\n");
    // taking the process data input
    printf("Enter the total number of Processes: ");
    scanf("%d", &num);
    for (i = 0; i < num; i++)
    {
        printf("Enter the process id, arrival time and burst time for process %d: \n", i + 1);
        scanf("%d %d %d", &p[i].pid, &p[i].arrival, &p[i].burst);
    }
    // sorting of processes according to burst time
    for (i = 0; i < num - 1; i++)
    {
        for (j = 0; j < num - i - 1; j++)
        {
            if (p[j].burst > p[j + 1].burst)
            {
                temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
    // calculate the turnaround time and waiting time of each process
    for (i = 0; i < num; i++)
    {
        p[i].wait = sum;
        sum = sum + p[i].burst;
        p[i].turnaround = sum;
    }
    // draw lines
    pline(44);
    printf("PID\tArrival\tBurst\tWaiting\tTurnaround\n");
    pline(44);

    // print all the processes
    for (i = 0; i < num; i++)
    {
        printf("%d\t%d\t%d\t%d\t%d\n", p[i].pid, p[i].arrival, p[i].burst, p[i].wait, p[i].turnaround);
        // sum of all the turnaround time of processes
        t_total += p[i].turnaround;
        // total waiting time
        w_total += p[i].wait;
    }

    pline(44);
    w_avg = w_total / (float)num;
    t_avg = t_total / (float)num;

    printf("\nTotal Turnaround time: %d", t_total);
    printf("\nAverage Turnaround time: %.3f", t_avg);
    printf("\nTotal Waiting time: %d", w_total);
    printf("\nAverage Waiting time: %.3f", w_avg);
}