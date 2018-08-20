"""
Isograms
7kyu

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

"""


def is_isogram(string):
   l = []
   for s in string.lower():
    if s in l:
     return False
    else:
     l.append(s)
   return True  
