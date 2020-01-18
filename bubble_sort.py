'''
Bubble sort algorithm in python

@Owwino27
'''
import sys
from get_array_args import getArrayArgs

nums = getArrayArgs()
print(nums)

if ( len(nums) == 0 ):
  print('No number passed for sorting')
  sys.exit(0)

for iteration in range(1, len(nums)):
  print('Iteration ', iteration)
  for x in range(len(nums) - iteration):
    if ( nums[x] > nums[x+1]):
      bigger = nums[x]
      nums[x] = nums[x+1]
      nums[x+1] = bigger
  print('Current list ', nums)

print('Final sorted list ',nums)