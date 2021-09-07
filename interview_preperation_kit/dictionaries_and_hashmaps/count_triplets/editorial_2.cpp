#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;


map<long, vector<long> >m;
long solve(vector<long> A, long r) {

    int n=A.size();
    
    //hashed list of indices for every value in the array
    for(int i=0;i<n;++i)
        m[A[i]].push_back(i);
    
    long c=0,x;
    for(int i=1;i<n-1;++i)
    {
    	//if A[i] is not divisible be r then no need to further proceed
        if(A[i]%r)
            continue;
        
        //Count of elements occur before A[i] and has a value of A[i]/r
        long less = upper_bound(m[A[i]/r].begin(),m[A[i]/r].end(),i-1)-m[A[i]/r].begin();
        
        //Count of elements occur after A[i] and has a value of A[i]*r
        long high = m[A[i]*r].end() - lower_bound(m[A[i]*r].begin(),m[A[i]*r].end(),i+1);
        
        //add the count of total possible combinations of both type of elements describe above
        c+=(high*less);
    }
    return c;

}