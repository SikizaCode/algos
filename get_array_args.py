'''
Convert command line arguments to integers and return the list

@Owwino27
'''
from sys import argv

def getArrayArgs():
  return [ int(x) for x in argv[1:]]