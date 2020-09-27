import numpy as np

test = int(input())
for _t in range(test):
    n, x = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    
    result = [[] for i in range((max(a)//x)+1)]
    
    for i in range(n):
        result[(a[i]-1)//x] += [i+1]
    result = np.array(result)
    
    totalResult = np.concatenate(result)
    
    totalResult = ' '.join(str(r) for r in totalResult)
    
    print("Case #{}: {}".format(_t+1, totalResult))