import time

test = int(input())
for _t in range(test):
    n, k = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    
    cd = list(range(k, 0, -1))

    c = 0

    # start = time.time()
    # for i in range(n-k+1):
    #     if a[i] == k and cd == a[i:i+k]:
    #         c += 1
    # print(str(time.time()-start))
    

    c = 0

    start = time.time()
    for i in range(n-k+1):
        if a[i] == k and cd == a[i:i+k]:
            c += 1
    print(str(time.time()-start))     

    print("Case #{}: {}".format(_t+1, c))