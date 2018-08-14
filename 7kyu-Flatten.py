"""
Flatten
7kyu

Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]
"""


def flatten(lst):
   flattenedList = []
   for i in lst:
    if type(i) == list:
     for ii in i:
      flattenedList.append(ii)
    else:
     flattenedList.append(i)
   return flattenedList  
     