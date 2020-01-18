'''
Merge sort algorithm

@Owwino27
'''

from sys import exit
from get_array_args import getArrayArgs


def mergeSort(nums):
  #Create the initial group by separating all element into single-element lists
  groups = [[x] for x in nums]

  while (True):

    if ( len(groups) == 1):
      # When only one element is in the groups list, then sorting is done and the single element is the sorted list
      break

    tmp = [] # Holds temporary results from a single iteration of sorting

    for i in range(0, len(groups), 2): # step over 2 elements, this acts to group elements into two for each sort iteration

      # if the iteration variable is the same as the length of the groups, then this is an odd-numbered list
      # therefore, add this final element into the temp sort list since it wont have a partner list for comparison
      if ( len(groups) == i+1):
        tmp.append(groups[i])
        continue

      # extract the individual groups
      # the index variable stores the position of the next element to sort in each group

      g1      = groups[i]
      lenG1   = len(g1)
      g1Index = 0

      g2      = groups[i+1]
      lenG2   = len(g2)
      g2Index = 0

      # if both groups have only a single element, then compare the elements directly and add them to the list
      if ((lenG1 == 1 ) & (lenG2 == 1)):
        if ( g1[0] > g2[0]):
          tmp.append([g2[0], g1[0]])
        else:
          tmp.append([g1[0], g2[0]])
        continue

      mergeList = [] #holds results as the elements from the two groups are merged in sorted order

      while ((lenG1 > g1Index ) | (lenG2 > g2Index )): #while the any group still has an unsorted element...

        if ( lenG1 == g1Index): # Group 1 is already done, add all elements in group2 in order
          mergeList.extend(g2[g2Index:])
          break
        
        elif( lenG2 == g2Index ): # Group 2 is already done, add all elements in group1 in order
          mergeList.extend(g1[g1Index:])
          break

        elif ( g1[g1Index] > g2[g2Index]):
          mergeList.append(g2[g2Index])
          g2Index += 1
        else:
          mergeList.append(g1[g1Index])
          g1Index += 1

      tmp.append(mergeList) 

    groups = tmp
  
  return groups[0]

if __name__ == "__main__":
  nums = getArrayArgs()
  if ( len(nums) == 0):
    print('No numbers entered for sorting')
    exit(0)

  print(mergeSort(nums))
