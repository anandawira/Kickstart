import math
import numpy as np

def binary_search(diffs, k):
    first = 1
    max_d = np.max(diffs)
    last = max_d
    while first<=last:
        mid = (first+last)//2
        if requiredK(diffs, mid) < k:
            last = mid - 1
            max_d = mid
        elif requiredK(diffs, mid) > k:
            first = mid +1
        else:
            max_d = mid
            break
    return max_d
    
def requiredK(diff , op):
    result = [math.ceil(d/op)-1 for d in diff]
    return sum(result)

test = int(input())
for _t in range(test):
    n, k = [int(s) for s in input().split()]
    m = [int(s) for s in input().split()]
    
    diffs = np.diff(m)
    result = binary_search(diffs, k)
    
    while result!=1 and requiredK(diffs, result-1) <=k:
        result -= 1
    
    print("Case #{}: {}".format(_t+1, result))