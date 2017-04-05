"""
CSC4800 Python App Programming
RE Regular Expression Testing
"""

import re


def testre(patt, s):
    print("'{}': ".format(s), end="")       # output the test string
    m = re.match(patt,s, flags=re.VERBOSE)  # perform the match
    if m is not None: print(m.group())      # output the results
    else: print("No Match")


def unittest_testre():
    print("unittest_testre")
    patt = '.+'
    print("Pattern: '{}'".format(patt))
    testre(patt, 'Abc')
    testre(patt, 'Abc  xyz')
    testre(patt, '123')
    testre(patt, '')
    print()


if __name__ == "__main__":
    unittest_testre()
