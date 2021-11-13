#include <bits/stdc++.h>
using namespace std;
int main()
{
    int p[3];
    for (int i = 0; i < 3; i++)
    {
        cout << "Enter Execution time for process " << i << ": ";
        cin >> p[i];
    }
    int ib1[3];
    int cpub[3];
    int ib2[3];
    for (int i = 0; i < 3; i++)
    {
        ib1[i] = p[i] / 5;
    }
    for (int i = 0; i < 3; i++)
    {
        cpub[i] = 3 * p[i] / 5;
    }
    for (int i = 0; i < 3; i++)
    {
        ib2[i] = p[i] / 5;
    }
    cout << "I/O in begining of processes :" << endl;
    for (int i = 0; i < 3; i++)
    {
        cout << "Process " << i << ": " << ib1[i] << endl;
    }
    cout << "CPU burst in begining of processes :" << endl;
    for (int i = 0; i < 3; i++)
    {
        cout << "Process " << i << ": " << cpub[i] << endl;
    }
    cout << "I/O in end of processes :" << endl;
    for (int i = 0; i < 3; i++)
    {
        cout << "Process " << i << ": " << ib2[i] << endl;
    }
    int et[3];
    et[0] = 18 - 2;
    et[1] = 22 - 7;
    et[2] = 29 - 12;
    int tat[3];
    for (int i = 0; i < 3; i++)
    {
        tat[i] = et[i] - 0;
    }
    int wt[3];
    for (int i = 0; i < 3; i++)
    {
        wt[i] = tat[i] - cpub[i];
    }
    int avgtat, avgwt;
    avgtat = (tat[0] + tat[1] + tat[2]) / 3;
    avgwt = (wt[0] + wt[1] + wt[2]) / 3;
    for (int i = 0; i < 3; i++)
    {
        cout << "Turnaround Time for process " << i << ": " << tat[i] << endl;
        cout << "Waiting Time for process " << i << ": " << wt[i] << endl;
    }

    cout << "Average Turnaround Time: " << avgtat << endl;
    cout << "Average Waiting Time: " << avgwt << endl;
}