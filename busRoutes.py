test = int(input())
for _t in range(test):
    n, d = [int(s) for s in input().split()]
    x = [int(s) for s in input().split()]
    x.reverse()
    
    s = d
    for r in x:
        if not s%r==0:
            s = (s//r)*r
    
    print("Case #{}: {}".format(_t+1, s))