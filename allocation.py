_n = int(input())
for _t in range(_n):
    n, b = [int(s) for s in input().split()]
    a = [int(s) for s in input().split()]
    a.sort()
    c = 0
    for i, p in enumerate(a):
        if b < p:
            break
        b -= p
        c += 1

    print("Case #{}: {}".format(_t+1, c))