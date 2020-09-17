import collections

def input_list() :
  return list(map(lambda x: int(x), input().split()))

def solve() :
  n = int(input())
  nums = input_list()

  return str('result')

def print_result(result, idx) :
  print("Case #{}: {}".format(idx+1, result))

if __name__ == "__main__":
  n = int(input())
    
  for i in range(0, n) :
    result = solve()
    print_result(result, i)