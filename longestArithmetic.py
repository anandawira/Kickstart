from itertools import groupby

_n = int(input())
for _t in range(_n):
    n = int(input())
    a = [int(s) for s in input().split()]
    
    dif = [a[i]-a[i+1] for i, num in enumerate(a[:-1])]
    count = [len(list(gr))+1 for k, gr in groupby(dif)]
    print("Case #{}: {}".format(_t+1, max(count)))