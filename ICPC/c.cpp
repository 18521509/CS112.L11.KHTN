#include <bits/stdc++.h>
using namespace std;
#define MAX int(2e5)

int sum_digits(int s)
{
    int res = 0;
    while (s!=0)
    {
        res += s%10;
        s/=10;
    }
    return res;
}
int main()
{
    bool F[MAX];
    int Primes[20000];
    int i, c = 0,j;
    for (int i = 0;i<MAX; i++)
        F[i] = true;

    for (i = 2; i < MAX ;i++)
    {
        if (F[i])
        {
            for (j = 2; i*j < MAX;j++)
            F[i*j] = false;
            Primes[c++] = i;
        }
    }
    int m,n, pos = 0;
    c=0;
    cin>>m>>n;
    while (Primes[pos] < m)
        ++pos;
    /*
    for (i = pos;i<n+pos;i++)
        cout<<Primes[i]<<" ";
    cout<<endl; */
    for (i = pos;i<n+pos;i++)
    {
        if (sum_digits(Primes[i])%10==0)
            ++c;
    }
    cout<<c;
    return 0;
}
