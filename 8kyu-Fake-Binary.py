"""
Fake Binary
8kyu

Given a string of digits, you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string.
"""


def fake_bin(x):
    r = ''
    for c in x:
     r = r + '0' if int(c)<5 else r + '1'
    return r 