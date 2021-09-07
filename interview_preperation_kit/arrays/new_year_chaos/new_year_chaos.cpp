#include <iostream>
#include <vector>
using namespace std;

void minimumBribes(vector<int> A) 
{
    int n = A.size();
    int cnt = 0;
    for(int i = n - 1; i >= 0; i--)
    {
        if(A[i] != (i + 1))
        {
            if(((i - 1) >= 0) && A[i - 1] == (i + 1))
            {
                cnt++;
                swap(A[i], A[i-1]);
            }
            else if(((i - 2) >= 0) && A[i - 2] == (i + 1))
            {
                cnt += 2;
                A[i - 2] = A[i - 1];
                A[i - 1] = A[i];
                A[i] = i + 1;
            }
            else
            {
                printf("Too chaotic\n");
                return;
            }
        }      
    }
    printf("%d\n",cnt);
    return;
}