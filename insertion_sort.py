'''
Insertion sort alogorithm

@Owwino27
'''

from sys import exit
from get_array_args import getArrayArgs

nums = getArrayArgs()
if ( len(nums) == 0):
  print('No numbers entered for sorting')
  exit(0)

startIndex = 1
currIndex = 1
count = 0

while( True ):

  count += 1
  print('Current list ', nums)

  if ( currIndex == 0):
    currIndex = startIndex

  if ( nums[currIndex] < nums[currIndex - 1]):

    smaller = nums[currIndex]
    nums[currIndex] = nums[currIndex - 1]
    nums[currIndex - 1] = smaller

    currIndex -= 1
    continue

  else:
    startIndex += 1
    currIndex = startIndex

    if ( startIndex == len(nums)):
      print('Start index ', startIndex)
      print('Number of elements: ', len(nums))
      break
    else:
      continue

print('Final sorted list ', nums)
print('Total iterations ', count)