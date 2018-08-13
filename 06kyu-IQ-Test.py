"""
IQ Test
6kyu

Bob is preparing to pass IQ test. The most frequent task in this test is
to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. 
Help Bob — to check his answers, he needs a program that among the given numbers 
finds one that is different in evenness, and return a position of this number.
! Keep in mind that your task is to help Bob solve a real IQ test, 
which means indexes of the elements start from 1 (not 0)

"""

def iq_test(numbers):
 listOfNumbers = map(int, numbers.split())
 countE = 0
 countO = 0
 ind = 0
 for n in listOfNumbers:
  if n%2 == 0:
   countE = countE + 1 
  else:
   countO = countO + 1
  if countE == 1:
   for i in range(len(listOfNumbers)):
    if listOfNumbers[i]%2 == 0:
     ind = i+1
  else:   
   for i in range(len(listOfNumbers)):
    if listOfNumbers[i]%2 != 0:
     ind = i+1
 return ind     