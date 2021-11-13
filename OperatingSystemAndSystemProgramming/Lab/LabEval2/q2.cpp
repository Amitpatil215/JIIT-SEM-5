#include <iostream>
using namespace std;

int main()
{

    int n, m, i, j, k;
    n = 5;
    m = 4;
    int alloc[5][4] = {{2, 0, 0, 1},
                       {3, 1, 2, 1},
                       {2, 1, 0, 3},
                       {1, 3, 1, 2},
                       {1, 4, 3, 2}};

    int max[5][4] = {{4, 2, 1, 2},
                     {5, 2, 5, 2},
                     {2, 3, 1, 6},
                     {1, 4, 2, 4},
                     {3, 6, 6, 5}};

    int avail[4] = {3, 3, 2, 1};
    int req[4] = {0, 0, 2, 0};

    int f[n], ans[n], ind = 0;
    for (k = 0; k < n; k++)
    {
        f[k] = 0;
    }
    int need[n][m];
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
            need[i][j] = max[i][j] - alloc[i][j];
    }
    cout << "Need Matrix\n"
         << endl;
    cout << "  "
         << " A B C D \n";
    for (i = 0; i < 5; i++)
    {
        cout << "P" << i << " ";
        for (j = 0; j < 4; j++)
        {
            cout << need[i][j] << " ";
        }
        cout << '\n';
    }

    int y = 0;
    for (k = 0; k < 5; k++)
    {
        for (i = 0; i < n; i++)
        {
            if (f[i] == 0)
            {

                int flag = 0;
                for (j = 0; j < m; j++)
                {
                    if (need[i][j] > avail[j])
                    {
                        flag = 1;
                        break;
                    }
                }

                if (flag == 0)
                {
                    ans[ind++] = i;
                    for (y = 0; y < m; y++)
                        avail[y] += alloc[i][y];
                    f[i] = 1;
                }
            }
        }
    }
    cout << endl;

    cout << "Following is the SAFE Sequence" << endl;
    for (i = 0; i < n - 1; i++)
        cout << " P" << ans[i] << " ->";
    cout << " P" << ans[n - 1] << endl;
    int fl = 0;
    for (i = 0; i < 4; i++)
    {
        if (req[i] > avail[i])
        {
            fl = 1;
            break;
        }
    }
    cout << endl;
    if (fl == 0)
    {
        cout << "Yes the process P4 gets the request immediately." << endl;
    }
    else
    {
        cout << "No, the process P4  not gets the request." << endl;
    }

    return (0);
}