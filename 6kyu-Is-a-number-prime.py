"""
Is a number prime?
6kyu

Define a function isPrime/is_prime() that takes one integer argument 
and returns true/True or false/False depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 
that has no positive divisors other than 1 and itself.

Example
bool isPrime(5) = return true
"""


def is_prime(num):
  if num <= 1:
   return False
  else: 
   for n in range(2,num):
    if num%n == 0:
     return False
  return True  