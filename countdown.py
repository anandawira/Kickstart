import time

test = int(input())
for _t in range(test):
    n, k = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    
    cd = list(range(k, 0, -1))

    c = 0

    idx = [i for i, e in enumerate(a) if e == k]
    for i in idx:
        if cd == a[i:i+k]:
            c += 1
    # for i in range(n-k+1):
    #     if a[i] == k and cd == a[i:i+k]:
    #         c += 1
            

    print("Case #{}: {}".format(_t+1, c))