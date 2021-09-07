t = int(input())

for _ in range(t):
    n = int(input())
    arr = map(int, input().split())
    org = range(n+1)
    pos = range(n+1)
    cnt = [0]*(n + 1)
    ans = 0
    invalid = 0
    
    for i in range(n - 1, -1, -1):
    
            if invalid:
                break
            
            # Get position where arr[i] should have been if no one bribed after this point
            
            oldp = pos[arr[i]]
            
            # Get the position where arr[i] currently is.
            
            newp = i + 1
            
            # oldp != newp indicates that even after this point, bribes took place
            # counting the number of furthter bribes that took place to bring arr[i] to i
            
            while oldp != newp:
                
                ans = ans + 1
                
                # arr[i] is at the right of org[oldp + 1] in the given array
                # that means org[oldp + 1] bribed arr[i] at some point
                # so increasing its count by 1
                
                cnt[org[oldp + 1]] += 1
                
                
                if cnt[org[oldp + 1]] > 2:
                    invalid = 1
                    break
                    
                # updating the original array to match the array after this bribe took place
                
                org[oldp], org[oldp+1] = org[oldp+1], org[oldp]
                
                
                # update the positions also due to the change 
                # caused by bribe that took place so far
                
                pos[org[oldp]] = oldp
                pos[org[oldp + 1]] = oldp + 1
                
                oldp = oldp + 1
                
    if invalid:
        ans = "Too chaotic"
        
    print(ans)