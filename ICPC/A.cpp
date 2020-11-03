#include <bits/stdc++.h>
using namespace std;
int solve(int n, int k)
{
    if (n*(n+1)/2 <= k)
        return n;
    if (k < 2)
        return  k;
    int left = 0, right = n, mid;
    while (right > left + 1)
    {
        mid = int(left+right)/2;
        if ( mid*(mid+1) <= k*2 && (mid+1)*(mid+2) >k *2 )
            return mid;
        else if (mid*(mid+1)/2 < k)
            left = mid;
        else
            right = mid;
    }
    return mid;
}
int main()
{
    int t, n,k;
    vector<int> res;
    cin>>t;
    for (int i = 0;i<t;i++)
    {
        cin>>n>>k;
        res.push_back(solve(n,k));
    }
    for (int i = 0; i<res.size();i++)
        cout<<res[i]<<endl;
    return 0;
}
