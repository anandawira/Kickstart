def input_list() :
  return list(map(lambda x: int(x), input().split()))

def solve() :
  n = int(input())
  nums = input_list()

  record_day_count =0

  for i in range(n):
    current_number = nums[i]
    
    if (i == n-1) or current_number > nums[i+1]:
        if all(b < current_number for b in nums[:i]):
            record_day_count += 1

  return str(record_day_count)

def print_result(result, idx) :
  print("Case #{}: {}".format(idx+1, result))

if __name__ == "__main__":
  n = int(input())
    
  for i in range(0, n) :
    result = solve()
    print_result(result, i)