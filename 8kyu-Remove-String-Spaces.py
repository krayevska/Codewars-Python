"""
Remove String Spaces
8kyu
by A.Partridge
Simple, remove the spaces from the string, then return the resultant string.
"""

def no_space(x):
 return ("".join([y for y in x if y is not " "]))