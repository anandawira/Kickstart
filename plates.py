from itertools import product

def get_possibilities(n, k, p):
    return [x for x in product(range(0,k+1), repeat=n) if sum(x)==p]

def get_max_point(l, p):
    max_point = 0
    for possibility in p:
        x = []
        for y in [point[:possibility[idx]] for idx, point in enumerate(l)]:
            x.extend(y)
        if sum(x)>max_point:
            max_point = sum(x)
    return max_point

test = int(input())
for _t in range(test):
    n, k, p = [int(s) for s in input().split()]
    nums = []
    for i in range(n):
        nums.append([int(s) for s in input().split()])
    
    possibilities = get_possibilities(n, k, p)
    highest = get_max_point(nums, possibilities)
    print("Case #{}: {}".format(_t+1, highest))