def third_max_usingpointer(nums):
  first = second = third = float('-inf')
  for num in nums:
    if num > first:
      third = second
      second = first
      first = num
    elif second < num < first:
      third = second
      second = num
    elif third < num < second:
      third = num
  return third if third != float('-inf') else first

def third_max_using_copy(arr):
  copy_arr = arr.copy()
  copy_arr.sort(reverse = True)
  max_count = 1
  third_max = copy_arr[0]
  for i in range(1,len(copy_arr)):
    if copy_arr[i] != copy_arr[i-1]:
      max_count += 1
      if max_count == 3:
        return copy_arr[i]
      elif max_count < 3:
        third_max = copy_arr[i]
  return third_max


  
