import sys

def get_subMax(start, end):
  if start == end: # base condition
    return nums[start] ** 2
  
  mid = (start + end) // 2
  subMax = max(get_subMax(start, mid), get_subMax(mid + 1, end))
  
  left, right = mid, mid + 1
  subSum = sum(nums[left:right])
  min_value = min(nums[left:right])
  subMax = max(subMax, subSum * min_value)
  
  while left > start or right < end:
    if left > start and nums[left - 1] > min_value:
      subSum += nums[left - 1]
      left -= 1
    else:
      subSum += nums[right + 1]
      right += 1
    subMax = max(subMax, subSum * min_value)
  return subMax

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

get_subMax(0, n - 1)