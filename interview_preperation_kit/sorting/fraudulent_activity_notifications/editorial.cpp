#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <cassert>
using namespace std;
#define SZ(x) ((int)(x.size()))
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)


typedef long long ll;
const int INF = 1e9;

const int N = 2e5;
const int V = 200;

int a[N];

int cnt[V+1];

int main()
{
    ios_base::sync_with_stdio(0);
    int n, d;
    cin >> n >> d;
    assert(n >= 1 && n <= N);
    assert(d >= 1 && d <= n);
    FOR(i, n) cin >> a[i];
    FOR(i, n) assert(a[i] >= 0 && a[i] <= V);
    int res = 0;

    FOR(i, d) cnt[a[i]]++;
    REP(i, d, n-1)
    {
        //SOLVE HERE
        int acc = 0;
        int low_median = -1, high_median = -1;
        REP(v, 0, V)
        {
            acc += cnt[v];
            if(low_median == -1 && acc >= int(floor((d+1)/2.0)))
            {
                low_median = v;
            }
            if(high_median == -1 && acc >= int(ceil((d+1)/2.0)))
            {
                high_median = v;
            }
        }
        assert(acc == d);
        int double_median = low_median + high_median;
        //cout << low_median << " " << high_median << " -> " << median << endl;
        if(a[i] >= double_median)
        {
            res++;
        }
        cnt[a[i-d]]--;
        cnt[a[i]]++;
    }
    cout << res << endl;
    return 0;
}