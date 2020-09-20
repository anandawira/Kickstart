test = int(input())
for _t in range(test):
    n = int(input())
    h = [int(s) for s in input().split()]
    
    c = 0
    for idx in range(1, n-1):
        if h[idx] > h[idx-1] and h[idx] > h[idx+1]:
            c += 1
    
    print("Case #{}: {}".format(_t+1, c))